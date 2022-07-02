from Packages import Help
from flask import Flask, make_response, request
from Packages.Exceptions import ChangeYourUsernameError, ChangeYourPasswordError, UserExistsAlreadyError, AccountError
from Packages.Exceptions import UserisNotAdminError, AdminIsNotMasterError, ClassCreationError, UserDoesNotExistError
from Packages.Exceptions import AdminHimSelfError, LengthError, PasswordPolicyError, PasswordUsedBeforeError, UsernamePolicyError

app = Flask(__name__)


@app.route("/signup", methods=["POST"])
def signup():

    data = request.get_json()

    admin_username = data.get("admin_username")
    admin_password = data.get("admin_password")
    username = data.get("username")
    password = data.get("password")
    status = data.get("status")
    admin = data.get("admin")

    list_of_str = [admin_username, admin_password, username, password]
    list_of_bool = [status, admin]

    for i in list_of_str:
        if not isinstance(i, str):
            raise TypeError

    for i in list_of_bool:
        if not isinstance(i, bool):
            raise TypeError

    response = Help.admin_signup_user(admin={"username": admin_username,
                                             "password": admin_password},
                                      user_data={"username": username,
                                                 "password": password,
                                                 "enabled": status,
                                                 "admin": admin})

    response = response.split(":")

    return make_response(response[0], response[1])


@app.route("/login", methods=["GET"])
def login():

    data = request.get_json()

    # get input
    username = data.get("username")
    password = data.get("password")

    # check if items are strings
    if not isinstance(username, str) or not isinstance(password, str):
        raise TypeError

    response = Help.login_user(
        data={"username": username,
              "password": password})

    response = response.split(":")

    return make_response(response[0], response[1])


@app.route("/generate-password", methods=["GET"])
def user_generate_password():

    data = request.get_json()

    # get input
    username = data.get("username")
    password = data.get("password")
    length = data.get("length")

    # check if items are strings
    if not isinstance(username, str) or not isinstance(password, str):
        raise TypeError

    # check if item is integer
    if not isinstance(length, int):
        raise TypeError

    response = Help.user_generate_password(
        data={"username": username,
              "password": password},
        length=length)

    response = response.split(":")

    return make_response(response[0], response[1])


@app.route("/edit-password", methods=["PUT"])
def edit_password():

    data = request.get_json()

    # get input
    username = data.get("username")
    password = data.get("password")
    new_password = data.get("new")

    # check if list items are strings
    list_of_str = [username, password, new_password]
    for i in list_of_str:
        if not isinstance(i, str):
            raise TypeError

    response = Help.edit_password(
        data={"username": username,
              "password": password,
              "newpassword": new_password})

    response = response.split(":")

    return make_response(response[0], response[1])


@app.route("/edit-username", methods=["PUT"])
def edit_useranme():

    data = request.get_json()

    # get input
    username = data.get("username")
    password = data.get("password")
    new_username = data.get("new")

    # check if list items are strings
    list_of_str = [username, password, new_username]
    for i in list_of_str:
        if not isinstance(i, str):
            raise TypeError

    response = Help.user_edit_username(
        data={"username": username,
              "password": password,
              "newusername": new_username})

    response = response.split(":")

    return make_response(response[0], response[1])


@app.route("/admin/enable-user", methods=["PUT"])
def enable_user():

    data = request.get_json()

    # read data as input
    username = data.get("username")
    password = data.get("password")
    user = data.get("user")

    # check if all data are strings
    list_of_str = [username, password, user]
    for i in list_of_str:
        if not isinstance(i, str):
            raise TypeError

    response = Help.admin_enable_disable_user(admin={"username": username,
                                                     "password": password},
                                              username=user,
                                              state=True)

    response = response.split(":")

    return make_response(response[0], response[1])


@app.route("/admin/disable-user", methods=["PUT"])
def disable_user():

    data = request.get_json()

    # get input
    username = data.get("username")
    password = data.get("password")
    user = data.get("user")

    # check if list items are strings
    list_of_str = [username, password, user]
    for i in list_of_str:
        if not isinstance(i, str):
            raise TypeError

    response = Help.admin_enable_disable_user(admin={"username": username,
                                                     "password": password},
                                              username=user,
                                              state=False)

    response = response.split(":")

    return make_response(response[0], response[1])


@app.route("/admin/delete-user", methods=["DELETE"])
def delete_user():

    data = request.get_json()

    # get input
    username = data.get("username")
    password = data.get("password")
    user = data.get("user")

    # check if list items are strings
    list_of_str = [username, password, user]
    for i in list_of_str:
        if not isinstance(i, str):
            raise TypeError

    response = Help.admin_delete_user(admin={"username": username,
                                             "password": password},
                                      username=user)

    response = response.split(":")

    return make_response(response[0], response[1])


@app.route("/admin/reset-user", methods=["PUT"])
def reset_password():

    data = request.get_json()

    # get input
    username = data.get("username")
    password = data.get("password")
    user = data.get("user")

    # check if input are strings
    list_of_str = [username, password, user]
    for i in list_of_str:
        if not isinstance(i, str):
            raise TypeError

    response = Help.admin_reset_user_password(
        admin={"username": username,
               "password": password},
        username=user)

    response = response.split(":")

    return make_response(response[0], response[1])


@app.route("/admin/set-password-policy", methods=["PUT"])
def set_password_policy():

    data = request.get_json()

    # get user data
    username = data.get("username")
    password = data.get("password")

    # get policy data
    minlength = data.get("minlength")
    maxlength = data.get("maxlength")
    upper = data.get("upper")
    lower = data.get("lower")
    numeric = data.get("numeric")
    punctuation = data.get("punctuation")

    list_of_str = [username, password]
    list_of_int = [upper, lower, punctuation,
                   numeric, maxlength, minlength]

    # check if list items are strings
    for i in list_of_str:
        if not isinstance(i, str):
            raise TypeError

    # check if list items are integers
    for i in list_of_int:
        if not isinstance(i, int):
            raise TypeError

    response = Help.admin_set_policy(
        admin={"username": username,
               "password": password},
        policy={"minlength": minlength,
                "maxlength": maxlength,
                "upper": upper,
                "lower": lower,
                "punctuation": punctuation,
                "numeric": numeric},
        policy_type=False)

    response = response.split(":")

    return make_response(response[0], response[1])


@app.route("/admin/set-username-policy", methods=["PUT"])
def set_username_policy():

    data = request.get_json()

    # login data
    username = data.get("username")
    password = data.get("password")

    # policy data
    minlength = data.get("minlength")
    max_length = data.get("maxlength")
    upper = data.get("upper")
    lower = data.get("lower")
    numeric = data.get("numeric")
    punctuation = data.get("punctuation")

    list_of_str = [username, password]
    list_of_int = [upper, lower, punctuation,
                   numeric, max_length, minlength]

    # check if items are strings
    for i in list_of_str:
        if not isinstance(i, str):
            raise TypeError

    # check if items are integers
    for i in list_of_int:
        if not isinstance(i, int):
            raise TypeError

    response = Help.admin_set_policy(
        admin={"username": username,
               "password": password},
        policy={"minlength": minlength,
                "maxlength": max_length,
                "upper": upper,
                "lower": lower,
                "punctuation": punctuation,
                "numeric": numeric},
        policy_type=True)

    response = response.split(":")

    return make_response(response[0], response[1])


@app.route("/admin/get-user-data", methods=["GET"])
def get_user_data():

    data = request.get_json()

    # get input
    username = data.get("username")
    password = data.get("password")
    user = data.get("user")

    # check if list items are strings
    list_of_str = [username, password, user]
    for i in list_of_str:
        if not isinstance(i, str):
            raise TypeError

    response = Help.admin_get_user_data(
        admin={"username": username,
               "password": password},
        username=username)

    response = response.split(";")
    return make_response(response[0], response[1])


@app.route("/admin/get-user-count", methods=["GET"])
def get_user_count():

    data = request.get_json()

    # get input
    username = data.get("username")
    password = data.get("password")

    # check if list items are strings
    list_of_str = [username, password]
    for i in list_of_str:
        if not isinstance(i, str):
            raise TypeError

    response = Help.admin_get_user_count(
        admin={"username": username,
               "password": password})

    response = response.split(":")

    return make_response(response[0], response[1])


@app.route("/admin/get-login-history", methods=["GET"])
def get_user_login_history():

    data = request.get_json()

    # get user input
    username = data.get("username")
    password = data.get("password")
    user = data.get("user")

    # check if list items are strings
    list_of_str = [username, password, user]
    for i in list_of_str:
        if not isinstance(i, str):
            raise TypeError

    response = Help.admin_get_user_loginorchange_history(
        admin={"username": username,
               "password": password},
        username=user,
        history_type=True)

    # split with ; because it returns data which include :
    response = response.split(";")

    return make_response(response[0], response[1])


@app.route("/admin/get-change-history", methods=["GET"])
def get_user_change_history():

    data = request.get_json()

    # get user input
    username = data.get("username")
    password = data.get("password")
    user = data.get("user")

    # check if items are strings
    list_of_str = [username, password, user]
    for i in list_of_str:
        if not isinstance(i, str):
            raise TypeError

    response = Help.admin_get_user_loginorchange_history(
        admin={"username": username,
               "password": password},
        username=user,
        history_type=False)

    # split with ; because it returns data which include :
    response = response.split(";")
    return make_response(response[0], response[1])

# _________________________________________________________________________________________________


@app.errorhandler(ClassCreationError)
def handling(e):
    e = str(e).split(":")
    return make_response(e[0], e[1])


@app.errorhandler(UserDoesNotExistError)
def handling(e):
    e = str(e).split(":")
    return make_response(e[0], e[1])


@app.errorhandler(UserisNotAdminError)
def handling(e):
    e = str(e).split(":")
    return make_response(e[0], e[1])


@app.errorhandler(AdminIsNotMasterError)
def handling(e):
    e = str(e).split(":")
    return make_response(e[0], e[1])


@app.errorhandler(ChangeYourPasswordError)
def handling(e):
    e = str(e).split(":")
    return make_response(e[0], e[1])


@app.errorhandler(ChangeYourUsernameError)
def handling(e):
    e = str(e).split(":")
    return make_response(e[0], e[1])


@app.errorhandler(UserExistsAlreadyError)
def handling(e):
    e = str(e).split(":")
    return make_response(e[0], e[1])


@app.errorhandler(AccountError)
def handling(e):
    e = str(e).split(":")
    return make_response(e[0], e[1])


@app.errorhandler(LengthError)
def handling(e):
    e = str(e).split(":")
    return make_response(e[0], e[1])


@app.errorhandler(PasswordUsedBeforeError)
def handling(e):
    e = str(e).split(":")
    return make_response(e[0], e[1])


@app.errorhandler(AdminHimSelfError)
def handling(e):
    e = str(e).split(":")
    return make_response(e[0], e[1])


@app.errorhandler(PasswordPolicyError)
def handling(e):
    e = str(e).split(":")
    return make_response(e[0], e[1])


@app.errorhandler(UsernamePolicyError)
def handling(e):
    e = str(e).split(":")
    return make_response(e[0], e[1])


@app.errorhandler(AttributeError)
def handling(e):
    return make_response("wrong header!", 400)


@app.errorhandler(TypeError)
def handling(e):
    return make_response("invalid values!", 400)


@app.errorhandler(FileNotFoundError)
def handling(e):
    return make_response("files missed!, all data resetted. Check for the original data on the cheat sheet", 500)


if __name__ == "__main__":
    app.run(port=1337, debug=True)