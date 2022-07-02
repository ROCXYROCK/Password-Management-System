from Packages import File
from Packages import Encryption
from typing import Union
from Packages.Classes import User, Admin, Password, Username, Policy
from Packages.Exceptions import AccountError, ChangeYourUsernameError, ChangeYourPasswordError, UserExistsAlreadyError
from Packages.Exceptions import UserisNotAdminError, AdminIsNotMasterError, ClassCreationError, UserDoesNotExistError
from Packages.Exceptions import AdminHimSelfError, LengthError, PasswordPolicyError, PasswordUsedBeforeError, UsernamePolicyError


def create_policy_instance(data: dict) -> Union[Policy, bool]:
    """This function creates a policy object, which can be used to create
    username or password policy.

    Args:
        data (dict): policy dictionary containing needed keys to create policy object.

    Returns:
        Policy: created policy object.
        False: creating object went wrong.

    Raises:
        AttributeError: will be raised, if methods of other var types are used.
        TypeError: will be raised, if data type of objects in an operation is inappropriate.
    """
    try:
        return Policy(minlength=data["minlength"], maxlength=data["maxlength"], punctuation=data["punctuation"], numeric=data["numeric"],
                      lower=data["lower"], upper=data["upper"], lastchange=data["lastchange"])

    except TypeError:
        return False

    except AttributeError:
        return False


def create_password_instance(password: str) -> Union[Password, bool]:
    """This function creates a password object, which can be used to create
    an user object.

    Args:
        password (str): plain text, which will be saved as an attribute of the object password.

    Returns:
        Password: created password object.
        False: creating object went wrong.

    Raises:
        AttributeError: will be raised, if methods of other var types are used.
        TypeError: will be raised, if data type of objects in an operation is inappropriate.
    """
    try:
        data = File.get_policy_file()
        if not data:
            return False

        policy = create_policy_instance(data=data["password"])
        if not policy:
            return False

        return Password(plain=password, policy=policy)

    except TypeError:
        return False
    except AttributeError:
        return False


def create_username_instance(username: str) -> Union[Username, bool]:
    """This function creates a username object, which can be used to create
    an user object.

    Args:
        username (str): text, which will be saved as an attribute of the object username.

    Returns:
        Username: created username object.
        False: creating object went wrong.

    Raises:
        AttributeError: will be raised, if methods of other var types are used.
        TypeError: will be raised, if data type of objects in an operation is inappropriate.
        ClassCreationError: will be raised, if problems happend while object creation.
        FileNotFoundError: will be raised, if reading file failed.
    """
    try:
        data = File.get_policy_file()

        # check reading policy file
        if not data:
            raise FileNotFoundError

        policy = create_policy_instance(data=data["username"])

        # check creating policy object
        if not policy:
            raise ClassCreationError

        return Username(username=username, policy=policy)

    except FileNotFoundError:
        return False

    except ClassCreationError:
        return False

    except TypeError:
        return False

    except AttributeError:
        return False


def create_user_instance(user: dict) -> Union[User, Admin, bool]:
    """This function creates a user or admin object, which can be used to 
    register the user in the data storage, because this function doesn't check
    if user is in database.

    Args:
        user (dict): data, to create an user object.

    Returns:
        User: created user object.
        Admin: created admin object.
        False: creating object went wrong.

    Raises:
        AttributeError: will be raised, if methods of other var types are used.
        TypeError: will be raised, if data type of objects in an operation is inappropriate.
        ClassCreationError: will be raised, if problems happend while object creation.
    """
    # create password instance
    password = create_password_instance(password=user["password"])
    if not password:
        raise ClassCreationError

    # create username instance
    username = create_username_instance(username=user["username"])
    if not username:
        raise ClassCreationError

    try:

        # if admin == False -> user
        if not user["admin"]:
            return User(username=username, password=password,
                        hashed=user["hash"], enabled=user["enabled"],
                        lastchange=user["lastchange"], expiration=user["expiration"],
                        lastlogin=user["lastlogin"], admin=user["admin"])

        # else return admin object
        return Admin(username=username, password=password,
                     hashed=user["hash"], enabled=user["enabled"],
                     lastchange=user["lastchange"], expiration=user["expiration"],
                     lastlogin=user["lastlogin"], admin=user["admin"])

    except TypeError:
        return False

    except AttributeError:
        return False

    except ClassCreationError:
        return False


def instance_create_useroradmin(username: str, password: str) -> Union[User, Admin, bool]:
    """This function creates a user or admin object, which can be used to 
    login user, because this function does check if user exists in database.

    Args:
        username (str): user's username.
        password (str): user's password.

    Returns:
        User: created user object.
        Admin: created admin object.
        False: creating object went wrong.
    """

    file_data = File.get_data_file()

    if not file_data:
        return False

    if username not in file_data:
        return False

    data = file_data[username]
    data["username"] = username
    data["password"] = password

    return create_user_instance(user=data)


def check_master_admin(data: str) -> bool:
    """This function checks if the user is the master admin of the application.

    Args:
        data(str): username which should be checked.

    Returns:
        True: admin is a master.
        False: admin is not a master.

    Raises:
        FileNotFoundError: will be raised, if reading file failed.
    """

    # get the key file data
    key_data = File.get_key_file()
    if not key_data:
        raise FileNotFoundError

    # check how is the master
    key = key_data["key"]

    # check if user is master
    if key != data:
        return False

    return True


def user_login(data: dict) -> Union[str, bool]:
    """This function checks if user is allowed to get access into the system. 

    Args:
        data(dict): data, to create an user object.

    Returns:
        "change username": username doesn't match with the policy.
        "change password": password is leaked or doesn't match with policy.
        True: user get access to the system. 
        False: user is not allowed to get access to the system. 

    Raises:
        AttributeError: will be raised, if methods of other var types are used.
        TypeError: will be raised, if data type of objects in an operation is inappropriate.
    """
    try:
        user = instance_create_useroradmin(username=data["username"],
                                           password=data["password"])

        # check creating user object
        if not user:
            raise UserDoesNotExistError

        # check if user is allowed to get access
        login = user.login_user()
        if not login:
            raise UserDoesNotExistError

        # check updating data file
        if not File.update_user_data(user=user.get_user()):
            return FileNotFoundError

        # check updating last login history
        if not File.update_history_with_type(
                username=user.get_username().get_username(),
                data=user.get_lastlogin(),
                data_type="login"):

            return False

        return login

    except TypeError:
        return False

    except AttributeError:
        return False


def login_user(data: dict) -> str:
    """This function communicate with the application file and 
    checks if user can get access to the system.

    Args:
        data(dict): user data containing the username and the password.

    Returns:
        "user authenticated!": user allowed to get access.
        "invalid values!": entered values types doesn't match with the required types.
        "wrong header!": header of request doesn't match with the required header.
        "Failed to build an object, check the input!": class user cannot be created.
        "User is not in the database, please enter an existing user!": user doesn't exist.
        "Username doesn't match with policy, change it!": username doesn't match with
        the username policy, it should be changed.
        "Password is not valid any more, change it!": password is either leaked or doesn't match
        with password policy, it should be changed.
        "files missed!": something went wrong while saving the data.

    Raises:
        AttributeError: will be raised if methods of other var types are used.
        TypeError: will be raised when data type of objects in an operation is inappropriate.
        ClassCreationError: will be raised when problems happen while object creation.
        FileNotFoundError: will be raised when file is not in the storage. 
        UserDoesNotExistError: will be raised when user is not found in the database.
        ChangeYourUsernameError: will be raised when username doesn't match with policy.
        ChangeYourPasswordError: will be raised when password is either leaked or not matching policy.
    """
    user = instance_create_useroradmin(
        username=data["username"],
        password=data["password"])

    if not user:
        raise ClassCreationError

    # call object method login_user
    login = user.login_user()
    if not login:
        raise UserDoesNotExistError

    # check if username is not matching with policy
    if login == "change username":
        raise ChangeYourUsernameError

    # check if password is outdated or pwned
    if login == "change password":
        raise ChangeYourPasswordError

    # check if user data successfully updated
    if not File.update_user_data(user=user.get_user()):
        raise FileNotFoundError

    # check if user login history successfully updated
    if not File.update_history_with_type(
            username=user.get_username().get_username(),
            data=user.get_lastlogin(), data_type="login"):
        raise FileNotFoundError

    return "user authenticated!:200"


def user_generate_password(data: dict, length: int) -> str:
    """This function communicate with the application file and 
    generate a secure password for the user.

    Args:
        data(dict): user data containing the username and the password.
        length(int): password length that should be generated.

    Returns:
        str: generated password.
        "Failed to build an object, check the input!": class user cannot be created.
        "invalid values!": entered values types doesn't match with the required types.
        "wrong header!": header of request doesn't match with the required header.
        "User is not in the database, please enter an existing user!": user doesn't exist.
        "length doesn't match policy!": entered length doesn't match with the policy.
        "files missed!": something went wrong while saving the data.

    Raises:
        AttributeError: will be raised if methods of other var types are used.
        TypeError: will be raised when data type of objects in an operation is inappropriate.
        ClassCreationError: will be raised when problems happen while object creation.
        FileNotFoundError: will be raised when file is not in the storage. 
        UserDoesNotExistError: will be raised when user is not found in the database.
        LengthError: will be raised if the entered length doesn't match with the policy.
    """
    login = user_login(data=data)

    # check if user is allowed to do that
    if not login:
        raise UserDoesNotExistError

    user = instance_create_useroradmin(
        username=data["username"], password=data["password"])

    # check creating user object
    if not user:
        raise ClassCreationError

    password = create_password_instance(password="")
    generated = user.generate_password(length=length, password=password)

    # check if given password length is matching policy
    if not generated:
        raise LengthError

    return generated + ":200"


def edit_password(data: dict) -> str:
    """This function communicate with the application file and 
    allows to users to edit their passwords.

    Args:
        data(dict): user data containing the username, password and the new password.

    Returns:
        "successfully edited!": user's password is successfully edited.
        "invalid values!": entered values types doesn't match with the required types.
        "wrong header!": header of request doesn't match with the required header.
        "Failed to build an object, check the input!": class user cannot be created.
        "User is not in the database, please enter an existing user!": user doesn't exist.
        "Password is not valid any more, change it!": new password is either leaked or doesn't match
        with password policy, it should be changed.
        "password used before!": password is in the user password history.
        "files missed!": something went wrong while saving the data.

    Raises:
        AttributeError: will be raised if methods of other var types are used.
        TypeError: will be raised when data type of objects in an operation is inappropriate.
        ClassCreationError: will be raised when problems happen while object creation.
        FileNotFoundError: will be raised when file is not in the storage. 
        UserDoesNotExistError: will be raised when user is not found in the database.
        PasswordUsedBeforeError: will be raised when password will be found in the user's password history.
        ChangeYourPasswordError: will be raised when password is either leaked or not matching policy.
    """
    new_password = data["newpassword"]

    # delete the key newpassword of the dict data
    data.pop("newpassword")

    login = user_login(data=data)

    # check if user allowed to do that
    if not login:
        raise UserDoesNotExistError

    user = instance_create_useroradmin(
        username=data["username"], password=data["password"])

    # check creating user object
    if not user:
        raise ClassCreationError

    old_hash = user.get_hash()

    # check setting user's new password
    if not user.get_password().set_password(plain=new_password):
        raise ChangeYourPasswordError

    # check editing password
    if not user.edit_password():
        raise ChangeYourPasswordError

    history = File.get_history_file()

    # check getting history file
    if not history:
        raise FileNotFoundError

    password_history = history["password"][user.get_username().get_username()]

    # check if password history list exists
    if password_history:

        # check every entry of the history if password match with it
        for i in password_history:
            if Encryption.password_hash_check(password=new_password, hashed=i):
                raise PasswordUsedBeforeError

    # check updating user data to save the new hash
    if not File.update_user_data(user=user.get_user()):
        raise FileNotFoundError

    # check updating password history
    if not File.update_history_with_type(username=user.get_username().get_username(), data=old_hash, data_type="password"):
        raise FileNotFoundError

    # check updating password change history
    if not File.update_history_with_type(username=user.get_username().get_username(), data=user.get_lastchange(), data_type="change"):
        raise FileNotFoundError

    return "successfully edited!:200"


def user_edit_username(data: dict):
    """This function communicate with the application file and 
    allow to users to change their usernames.

    Args:
        data(dict): user data containing the username, password and new username.

    Returns:
        "successfully edited!": new username is saved.
        "invalid values!": entered values types doesn't match with the required types.
        "wrong header!": header of request doesn't match with the required header.
        "Failed to build an object, check the input!": class user cannot be created.
        "User is not in the database, please enter an existing user!": user doesn't exist.
        "Username doesn't match with policy, change it!": username doesn't match with
        the username policy, it should be changed.
        "User exists already, try with another one!": another user has this username.
        "files missed!": something went wrong while saving the data.

    Raises:
        AttributeError: will be raised if methods of other var types are used.
        TypeError: will be raised when data type of objects in an operation is inappropriate.
        ClassCreationError: will be raised when problems happen while object creation.
        FileNotFoundError: will be raised when file is not in the storage. 
        UserExistsAlreadyError: will be raised if username is already in the database.
        UserDoesNotExistError: will be raised when user is not found in the database.
        ChangeYourUsernameError: will be raised when username doesn't match with policy.
    """
    login = user_login(data=data)

    # check if user has permission to get access
    if not login:
        raise UserDoesNotExistError

    user = instance_create_useroradmin(
        username=data["username"], password=data["password"])

    file_data = File.get_data_file()

    # check if username is existing
    if data["newusername"] in file_data:
        raise UserExistsAlreadyError

    # check setting new username
    if not user.get_username().set_username(username=data["newusername"]):
        raise ClassCreationError

    # check editing username
    if not user.edit_username():
        raise ChangeYourUsernameError

    # check if master is changing his username
    if check_master_admin(data=data["username"]) and user.get_admin_status() and user.get_enabled():

        # check updating master username
        if not File.update_key(key=user.get_username().get_username()):
            raise FileNotFoundError

    # check updating data file
    if not File.update_user_data(user=user.get_user()):
        raise FileNotFoundError

    return "successfully edited!:200"


def admin_login(admin: dict) -> bool:
    """This function communicate with the application file and 
    checks if user is an admin can get access to the system.

    Args:
        data(dict): user data containing the username and the password.

    Returns:
        True: user is admin.
        False: user is not admin
        "invalid values!": entered values types doesn't match with the required types.
        "wrong header!": header of request doesn't match with the required header.
        "User is not in the database, please enter an existing user!": user doesn't exist.
        "files missed!": something went wrong while saving the data.
    Raises:
        AttributeError: will be raised if methods of other var types are used.
        TypeError: will be raised when data type of objects in an operation is inappropriate.
        ClassCreationError: will be raised when problems happen while object creation.
        FileNotFoundError: will be raised when file is not in the storage. 
        UserDoesNotExistError: will be raised when user is not found in the database.
    """
    login = user_login(data=admin)
    if not login:
        return False

    if login == "change username":
        return False

    if login == "change password":
        return False

    user = instance_create_useroradmin(
        username=admin["username"],
        password=admin["password"])

    if not user:
        return False

    if not isinstance(user, Admin):
        return False

    if not user.get_admin_status():
        return False

    return True


def admin_enable_disable_user(admin: dict, username: str, state: bool):
    """This function communicate with the application file and 
    allow admin to enable/disable users and master to enable/disable users or admins.

    Args:
        admin(dict): user data containing the username and the password.
        username(str): username of user that should be enabled/disabled.
        state(bool): False for disabling, True is for enabling.

    Returns:
        "status changed successfully!": user could change the status of another user.
        "go to login to check your account!": user is not an admin, doesn't exist or if user is disabled!
        "you cannot excute it on yourself!": admin cannot disable himself. enable him self doesnot work if he is disabled.
        "Admin has not master privileges!": admin is not allowed to enable or disable another admin.
        "User has not admin privileges!": user is not allowed to excute this function.
        "user already enabled!": admin is trying to enable an already enabled user.
        "user already disabled!": admin is trying to disable an already disabled user.
        "invalid values!": entered values types doesn't match with the required types.
        "wrong header!": header of request doesn't match with the required header.
        "User is not in the database, please enter an existing user!": user doesn't exist.
        "files missed!": something went wrong while saving the data.
    Raises:
        AttributeError: will be raised if methods of other var types are used.
        TypeError: will be raised when data type of objects in an operation is inappropriate.
        ClassCreationError: will be raised when problems happen while object creation.
        FileNotFoundError: will be raised when file is not in the storage. 
        UserDoesNotExistError: will be raised when user is not found in the database.
        AdminHimSelfError: will be raised when admin tries to disable himself.
        AccountError: will be raised if user has expired password, not existing user or not admin.
        AdminIsNotMasterError: will be raised when admin tries to enable/disable other admins.
        UserisNotAdminError: will be raised when user tries to excute admin functions.
    """
    login = admin_login(admin=admin)

    # check if user is admin
    if not login:
        raise AccountError

    # create user or admin objects
    user_admin = instance_create_useroradmin(
        username=admin["username"], password=admin["password"])

    user = instance_create_useroradmin(username=username, password="")

    # check creating admin object
    if not user_admin:
        raise UserisNotAdminError

    # check creating user object
    if not user:
        raise UserDoesNotExistError

    # check if user is allowed to enable/disable the other user
    if isinstance(user, Admin):
        if not check_master_admin(data=user_admin.get_username().get_username()):
            raise AdminIsNotMasterError

    # check that user doesn't enable/disable hisself
    if user_admin.get_username().get_username() == user.get_username().get_username():
        raise AdminHimSelfError

    # check if user want to disable
    if not state:
        if not user.get_enabled():
            return "user already disabled!:200"
        data = user_admin.disable_user(user=user)

    # check if user want to enable
    if state:
        if user.get_enabled():
            return "user already enabled!:200"
        data = user_admin.enable_user(user=user)

    # update data
    if not File.update_user_data(user=data):
        raise FileNotFoundError

    return "status changed successfully!:200"


def admin_delete_user(admin: dict, username: str) -> str:
    """This function communicate with the application file and 
    allow admin to delete users and master to delete users or admins.

    Args:
        admin(dict): user data containing the username and the password.
        username(str): username of user that should be deleted.

    Returns:
        "user deleted successfully!": user could delete the other user.
        "go to login to check your account!": user is not an admin, doesnot exist or if user is disabled.
        "you cannot excute it on yourself!": admin cannot delete himself.
        "Admin has not master privileges!": admin is not allowed to delete another admin.
        "User has not admin privileges!": user is not allowed to excute this function.
        "invalid values!": entered values types doesnot match with the required types.
        "wrong header!": header of request doesnot match with the required header.
        "User is not in the database, please enter an existing user!": user doesnot exist.
        "files missed!": something went wrong while saving the data.
    Raises:
        AttributeError: will be raised if methods of other var types are used.
        TypeError: will be raised when data type of objects in an operation is inappropriate.
        ClassCreationError: will be raised when problems happen while object creation.
        FileNotFoundError: will be raised when file is not in the storage. 
        UserDoesNotExistError: will be raised when user is not found in the database.
        AdminHimSelfError: will be raised when admin tries to disable himself.
        AccountError: will be raised if user has expired password, not existing user or not admin.
        AdminIsNotMasterError: will be raised when admin tries to enable/disable other admins.
        UserisNotAdminError: will be raised when user tries to excute admin functions.
    """
    login = admin_login(admin=admin)

    # check if user is admin
    if not login:
        raise AccountError

    user_admin = instance_create_useroradmin(
        username=admin["username"],
        password=admin["password"])

    user = instance_create_useroradmin(username=username,
                                       password="")

    # check creating admin object
    if not user_admin:
        raise UserisNotAdminError

    # check creating user object
    if not user:
        raise UserDoesNotExistError

    # check if the user is admin
    if isinstance(user, Admin):

        # check if the admin is master
        if not check_master_admin(data=user_admin.get_username().get_username()):
            raise AdminIsNotMasterError

    # check if user trying to delete hisself
    if user_admin.get_username().get_username() == user.get_username().get_username():
        raise AdminHimSelfError

    data = File.get_data_file()
    history = File.get_history_file()

    # check getting data file
    if not data:
        raise FileNotFoundError

    # check getting history file
    if not history:
        raise FileNotFoundError

    user_data, user_history = user_admin.delete_user(
        user=user,
        data=data,
        history=history)

    # check updating data file
    if not File.update_data(data=user_data):
        raise FileNotFoundError

    # check updating history file
    if not File.update_history(history=user_history):
        raise FileNotFoundError

    return "user deleted successfully!:200"


def admin_reset_user_password(admin: dict, username: str) -> str:
    """This function communicate with the application file and 
    allow admin to reset users and master to reset users or admins. The password will be resetted but expired too,
    because the password has been showed as plain text to the user, so after resetting he should edit the password.

    Args:
        admin(dict): user data containing the username and the password.
        username(str): username of user that should be resetted.

    Returns:
        str: new password which has been generated by the system.
        "go to login to check your account!": user is not an admin, doesnot exist or if user is disabled.
        "you cannot excute it on yourself!": admin cannot reset himself.
        "Admin has not master privileges!": admin is not allowed to reset another admin.
        "User has not admin privileges!": user is not allowed to excute this function.
        "failed to generate password!": something went wrong, while generating new password.
        "invalid values!": entered values types does not match with the required types.
        "wrong header!": header of request does not match with the required header.
        "User is not in the database, please enter an existing user!": user does not exist.
        "files missed!": something went wrong while saving the data.
    Raises:
        AttributeError: will be raised if methods of other var types are used.
        TypeError: will be raised when data type of objects in an operation is inappropriate.
        ClassCreationError: will be raised when problems happen while object creation.
        FileNotFoundError: will be raised when file is not in the storage. 
        UserDoesNotExistError: will be raised when user is not found in the database.
        AdminHimSelfError: will be raised when admin tries to disable himself.
        AccountError: will be raised if user has expired password, not existing user or not admin.
        AdminIsNotMasterError: will be raised when admin tries to enable/disable other admins.
        UserisNotAdminError: will be raised when user tries to excute admin functions.
    """
    login = admin_login(admin=admin)

    # check if user is admin
    if not login:
        raise AccountError

    # create admin object
    user_admin = instance_create_useroradmin(
        username=admin["username"],
        password=admin["password"])

    # create user object
    user = instance_create_useroradmin(
        username=username,
        password="")

    # check if creating object failed
    if not user_admin:
        raise UserisNotAdminError

    # check if creating object failed
    if not user:
        raise UserDoesNotExistError

    # check if to resetted user is admin
    if isinstance(user, Admin):

        # check if admin is master
        if not check_master_admin(data=user_admin.get_username().get_username()):
            raise AdminIsNotMasterError

    # check if user is trying to reset himself
    if user_admin.get_username().get_username() == user.get_username().get_username():
        raise AdminHimSelfError

    new_password = user_admin.reset_password(user=user)

    # check resetting password
    if not new_password:
        return "failed to generate password!:500"

    # check overwriting user data
    if not File.update_user_data(user=user.get_user()):
        raise FileNotFoundError

    # check overwriting password history
    if not File.update_history_with_type(
            username=user.get_username().get_username(),
            data=user.get_hash(),
            data_type="password"):

        raise FileNotFoundError

    # check overwriting password change dates history
    if not File.update_history_with_type(
            username=user.get_username().get_username(),
            data=user.get_lastchange(),
            data_type="change"):

        raise FileNotFoundError

    return new_password + ":200"


def admin_set_policy(admin: dict, policy: dict, policy_type: bool) -> str:
    """This function communicate with the application file and 
    allow admins to set password and username policy which should not have any logical error. 

    Args:
        admin(dict): user data containing the username and the password.
        policy(str): policy data: minlength, maxlength, upper, lower, numeric, punctuation.
        policy_type(bool): False password policy, True username policy.

    Returns:
        "policy successfully updated!": policy accepted and already stored.
        "go to login to check your account!": user is not an admin, doesnot exist or if user is disabled.
        "User has not admin privileges!": user is not allowed to excute this function.
        "invalid values!": entered values types does not match with the required types.
        "wrong header!": header of request does not match with the required header.
        "User is not in the database, please enter an existing user!": user does not exist.
        "files missed!": something went wrong while saving the data.
    Raises:
        AttributeError: will be raised if methods of other var types are used.
        TypeError: will be raised when data type of objects in an operation is inappropriate.
        FileNotFoundError: will be raised when file is not in the storage. 
        UserDoesNotExistError: will be raised when user is not found in the database.
        AccountError: will be raised if user has expired password, not existing user or not admin.
        UserisNotAdminError: will be raised when user tries to excute admin functions.
    """
    login = admin_login(admin=admin)

    # check user is admin
    if not login:
        raise AccountError

    user_admin = instance_create_useroradmin(
        username=admin["username"], password=admin["password"])

    # check creating admin object
    if not user_admin:
        raise UserisNotAdminError

    policy_data = File.get_policy_file()

    # check getting policy file
    if not policy_data:
        raise FileNotFoundError

    # check if policy is password policy
    if not policy_type:
        data = user_admin.set_password_policy(data=policy)

        # check if creating password policy went well
        if not data:
            raise PasswordPolicyError

        policy_data["password"] = data

    # check if policy is username policy
    if policy_type:
        data = user_admin.set_username_policy(data=policy)

        # check if creating username policy went well
        if not data:
            raise UsernamePolicyError

        policy_data["username"] = data

    # check if updating policy file went well
    if not File.update_policy(policy=policy_data):
        raise FileNotFoundError

    return "policy successfully updated!:200"


def admin_get_user_data(admin: dict, username: str) -> str:
    """This function communicate with the application file and 
    allow admins to get user data of any existing user on the system.

    Args:
        admin(dict): user data containing the username and the password.
        username(str): username of user that his data should be returned.

    Returns:
        str: required user data.
        "go to login to check your account!": user is not an admin, doesnot exist or if user is disabled.
        "User has not admin privileges!": user is not allowed to excute this function.
        "invalid values!": entered values types does not match with the required types.
        "wrong header!": header of request does not match with the required header.
        "User is not in the database, please enter an existing user!": user does not exist.
        "files missed!": something went wrong while saving the data.
    Raises:
        AttributeError: will be raised if methods of other var types are used.
        TypeError: will be raised when data type of objects in an operation is inappropriate.
        FileNotFoundError: will be raised when file is not in the storage. 
        UserDoesNotExistError: will be raised when user is not found in the database.
        AccountError: will be raised if user has expired password, not existing user or not admin.
        UserisNotAdminError: will be raised when user tries to excute admin functions.
    """
    login = admin_login(admin=admin)

    # check if user is admin
    if not login:
        raise AccountError

    user_admin = instance_create_useroradmin(
        username=admin["username"], password=admin["password"])

    # check if creating admin object went well
    if not user_admin:
        raise UserisNotAdminError

    user = instance_create_useroradmin(username=username, password="")

    # check if creating user object went well
    if not user:
        raise UserDoesNotExistError

    file_data = File.get_data_file()

    # check if getting data file went well
    if not file_data:
        return FileNotFoundError

    data = user_admin.get_user_data(user=user)

    return str(data) + ";200"


def admin_get_user_count(admin: dict) -> str:
    """This function communicate with the application file and 
    allow admins to get user count of the existing users on the system.

    Args:
        admin(dict): user data containing the username and the password.

    Returns:
        str: user count.
        "go to login to check your account!": user is not an admin, doesnot exist or if user is disabled.
        "User has not admin privileges!": user is not allowed to excute this function.
        "invalid values!": entered values types does not match with the required types.
        "wrong header!": header of request does not match with the required header.
        "User is not in the database, please enter an existing user!": user does not exist.
        "files missed!": something went wrong while saving the data.
    Raises:
        AttributeError: will be raised if methods of other var types are used.
        TypeError: will be raised when data type of objects in an operation is inappropriate.
        FileNotFoundError: will be raised when file is not in the storage. 
        UserDoesNotExistError: will be raised when user is not found in the database.
        AccountError: will be raised if user has expired password, not existing user or not admin.
        UserisNotAdminError: will be raised when user tries to excute admin functions.
    """
    login = admin_login(admin=admin)

    # check if user is admin
    if not login:
        raise AccountError

    user_admin = instance_create_useroradmin(
        username=admin["username"], password=admin["password"])

    # check if admin object is created
    if not user_admin:
        raise UserisNotAdminError

    data = File.get_data_file()

    # check if reading data file went well
    if not data:
        raise FileNotFoundError

    count = user_admin.get_user_count(data=data)
    return str(count) + ":200"


def admin_get_user_loginorchange_history(admin: dict, username: str, history_type: bool) -> str:
    """This function communicate with the application file and 
    allow admins to get user's password change or last login histories of any existing user on the system.

    Args:
        admin(dict): user data containing the username and the password.
        username(str): username of user that his history should be returned.
        history_type(bool): False is password change history, True is last login history.

    Returns:
        str: required user's history.
        "go to login to check your account!": user is not an admin, doesnot exist or if user is disabled.
        "User has not admin privileges!": user is not allowed to excute this function.
        "invalid values!": entered values types does not match with the required types.
        "wrong header!": header of request does not match with the required header.
        "User is not in the database, please enter an existing user!": user does not exist.
        "files missed!": something went wrong while saving the data.
    Raises:
        AttributeError: will be raised if methods of other var types are used.
        TypeError: will be raised when data type of objects in an operation is inappropriate.
        FileNotFoundError: will be raised when file is not in the storage. 
        UserDoesNotExistError: will be raised when user is not found in the database.
        AccountError: will be raised if user has expired password, not existing user or not admin.
        UserisNotAdminError: will be raised when user tries to excute admin functions.
    """
    login = admin_login(admin=admin)

    # check if user is admin
    if not login:
        return AccountError

    user_admin = instance_create_useroradmin(
        username=admin["username"], password=admin["password"])

    # check if admin object created
    if not user_admin:
        return UserisNotAdminError

    user = instance_create_useroradmin(username=username, password="")

    # check if creating user object went well
    if not user:
        return UserDoesNotExistError

    history = File.get_history_file()

    # check if updating history file went well
    if not history:
        return FileNotFoundError

    # True is login history
    if history_type:
        data = user_admin.get_user_login_history(history=history, user=user)

    # False is change history
    if not history_type:
        data = user_admin.get_user_change_history(history=history, user=user)

    return str(data) + ";200"


def admin_signup_user(admin: dict, user_data: dict) -> str:
    """This function communicate with the application file and 
        allow admins to register users to the system.

        Args:
            admin(dict): user data containing the username and the password.
            user_data(dict): user data that should be registered. 

        Returns:
            "created successfully!": user has been registered.
            "go to login to check your account!": user is not an admin, doesnot exist or if user is disabled.
            "User has not admin privileges!": user is not allowed to excute this function.
            "invalid password or username, read documentation!": username or password does not match with system requirements.
            "User exists already, try with another one!": username already exists.
            "invalid values!": entered values types does not match with the required types.
            "wrong header!": header of request does not match with the required header.
            "User is not in the database, please enter an existing user!": user does not exist.
            "files missed!": something went wrong while saving the data.
        Raises:
            AttributeError: will be raised if methods of other var types are used.
            TypeError: will be raised when data type of objects in an operation is inappropriate.
            FileNotFoundError: will be raised when file is not in the storage. 
            UserDoesNotExistError: will be raised when user is not found in the database.
            AccountError: will be raised if user has expired password, not existing user or not admin.
            UserisNotAdminError: will be raised when user tries to excute admin functions.
            UserExistsAlreadyError: will be raised when user's username is already given. 
    """
    login = admin_login(admin=admin)

    # check if user is admin
    if not login:
        raise UserisNotAdminError

    user_admin = instance_create_useroradmin(
        username=admin["username"], password=admin["password"])

    # check if user is admin
    if not user_admin:
        raise UserisNotAdminError

    user_data["lastchange"] = ""
    user_data["lastlogin"] = ""
    user_data["expiration"] = ""
    user_data["hash"] = ""

    user = create_user_instance(user=user_data)

    # check if creating user object went well
    if not user:
        raise UserDoesNotExistError

    data_file = File.get_data_file()

    # check if user exists already
    if user.get_username().get_username() in data_file:
        raise UserExistsAlreadyError

    new_user = user_admin.signup(user=user)

    # check if register user went well
    if not new_user:
        return "invalid password or username, read documentation!:400"

    # check if updating file went well
    if not File.update_user_data(new_user.get_user()):
        raise FileNotFoundError

    # check if updating login history went well
    if not File.update_history_with_type(username=new_user.get_username().get_username(), data=new_user.get_lastlogin(), data_type="login"):
        raise FileNotFoundError

    # check if updating password history went well
    if not File.update_history_with_type(username=new_user.get_username().get_username(), data=new_user.get_hash(), data_type="password"):
        raise FileNotFoundError

    # check if updating change history went well
    if not File.update_history_with_type(username=new_user.get_username().get_username(), data=new_user.get_lastchange(), data_type="change"):
        raise FileNotFoundError

    return "created successfully!:201"
