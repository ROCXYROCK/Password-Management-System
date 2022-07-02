"""
Module: Classes.py
Discription: Classes will be created in this module, to help other modules to create objects of this classes.
Author: Abdulhamid Hijli
Date: 30.06.2022
"""
import requests
import secrets
from typing import Union, Tuple
from datetime import datetime
from dateutil.relativedelta import relativedelta
from Packages.Exceptions import PasswordIsPwnedError
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from Packages.Encryption import hash_to_sha1, hash_to_bcrypt, password_hash_check


class Time:
    def time_now() -> str:
        return str(datetime.utcnow())

    def expiration_update(time_str: str) -> str:

        # convert string into datetime object
        time = datetime.fromisoformat(time_str)

        # add to the datetime object 3 months
        time = time + relativedelta(months=3)

        return str(time)


class Policy:
    def __init__(self, minlength: int, maxlength: int,
                 punctuation: int, numeric: int,
                 lower: int, upper: int, lastchange: str) -> None:

        self.__minlength: int = minlength
        self.__maxlength: int = maxlength
        self.__punctuation: int = punctuation
        self.__numeric: int = numeric
        self.__lower: int = lower
        self.__upper: int = upper
        self.__lastchange: str = lastchange

    def get_lastchange(self) -> str:
        return self.__lastchange

    def get_minlength(self) -> int:
        return self.__minlength

    def get_maxlength(self) -> int:
        return self.__maxlength

    def get_punctuation(self) -> int:
        return self.__punctuation

    def get_numeric(self) -> int:
        return self.__numeric

    def get_upper(self) -> int:
        return self.__upper

    def get_lower(self) -> int:
        return self.__lower

    def set_minlength(self, minlength: int) -> bool:
        try:
            self.__minlength = minlength
            return True
        except TypeError:
            return False

    def set_maxlength(self, maxlength: int) -> bool:
        try:
            self.__maxlength = maxlength
            return True
        except TypeError:
            return False

    def set_punctuation(self, punctuation: int) -> bool:
        try:
            self.__punctuation = punctuation
            return True

        except TypeError:
            return False

    def set_numeric(self, numeric: int) -> bool:
        try:
            self.__numeric = numeric
            return True

        except TypeError:
            return False

    def set_upper(self, upper: int) -> bool:
        try:
            self.__upper = upper
            return True

        except TypeError:
            return False

    def set_lower(self, lower: int) -> bool:
        try:
            self.__lower = lower
            return True

        except TypeError:
            return False

    def set_lastchange(self, time_str: str) -> bool:
        try:
            self.__lastchange = time_str
            return True

        except TypeError:
            return False

    def get_policy(self) -> dict:
        return {"minlength": self.__minlength, "maxlength": self.__maxlength,
                "upper": self.__upper, "lower": self.__lower,
                "punctuation": self.__punctuation, "numeric": self.__numeric,
                "lastchange": self.__lastchange}

    def isupper(self, text: str) -> bool:
        """checks if the password contains enough upper cases"""
        counter = 0

        for i in text:
            if i.isupper():
                counter += 1

        if counter >= self.__upper:
            return True

        return False

    def islower(self, text: str) -> bool:
        """checks if the password conatains enough lower cases"""
        counter = 0

        for i in text:
            if i.islower():
                counter += 1

        if counter >= self.__lower:
            return True

        return False

    def isnumeric(self, text: str) -> bool:
        """checks if the password has enough numerical characters"""
        counter = 0

        for i in text:
            if i.isnumeric():
                counter += 1

        if counter >= self.__numeric:
            return True

        return False

    def ispunctuation(self, text: str) -> bool:
        """checks if the password has enough special characters"""
        counter = 0
        list_of_non = ["\"", "'", ":", ";", "\\"]

        # check chars of string
        for i in text:
            if i in punctuation:
                counter += 1

            # check if any char of the string is part of the list_of_non
            if i in list_of_non:
                return False

        # check if count match with minimum count of punctuation
        if counter < self.__punctuation:
            return False

        return True

    def length(self, text: str) -> bool:
        """checks if the lenght of the given password is equal to the required length or not"""

        # checks if text has the minimum required length
        if len(text) < self.__minlength:
            return False

        # checks if text length is not greater than maximum allowed length
        if len(text) > self.__maxlength:
            return False

        return True

    def policy_text(self, text: str) -> bool:

        # check if text has enough lower letters
        if not self.islower(text=text):
            return False

        # check if text has enough upper letters
        if not self.isupper(text=text):
            return False

        # check if text has enough numerical characters
        if not self.isnumeric(text=text):
            return False

        # check if text has enough punctuation characters
        if not self.ispunctuation(text=text):
            return False

        # check if text has enough length
        if not self.length(text=text):
            return False
        return True

    def check_policy(self) -> bool:

        # check if minlength is not greater than maxlength
        if self.__minlength >= self.__maxlength:
            return False

        # sum of policy's possible minimum rules
        sum_of = self.__lower + self.__numeric + self.__punctuation + self.__upper

        # check if these rules are not greater than minlength
        if sum_of > self.__minlength:
            return False

        return True


class Username:
    def __init__(self, username: str, policy: Policy) -> None:
        self.__username: str = username
        self.__policy: Policy = policy

    def get_username(self) -> str:
        return self.__username

    def get_policy(self) -> Policy:
        """It returns a Policy bject"""
        return self.__policy

    def policy_username(self) -> bool:
        """check if username is matching with username policy"""

        resault = self.__policy.policy_text(text=self.__username)

        if not resault:
            return False

        return True

    def set_username(self, username: str) -> bool:
        try:
            self.__username = username
            return True
        except TypeError:
            return False


class Password:

    def __init__(self, plain: str, policy: Policy) -> None:
        self.__policy: Policy = policy
        self.__plain: str = plain

    def get_length(self) -> int:
        return len(self.__plain)

    def get_password(self) -> str:
        return self.__plain

    def get_policy(self) -> Policy:
        return self.__policy

    def set_password(self, plain: str) -> bool:
        try:
            self.__plain = plain
            return True

        except TypeError:
            return False

    def pwned(self) -> bool:
        try:
            # hash the self.__plain to sha1 with upper cases
            hashed = hash_to_sha1(password=self.__plain).upper()

            # send reqest to HIBP
            pwned_list = requests.get(
                url="https://api.pwnedpasswords.com/range/"+hashed[:5])

            # check if response is valid
            if pwned_list.status_code != 200:
                raise TypeError

            # convert recieved text to list
            pwned = pwned_list.text.split("\n")

            # pop the last item of the list
            pwned.pop()

            # check if hash is in the list
            for i in pwned:
                tmp = i.split(":")[0]

                if hashed[5:] == tmp:
                    raise PasswordIsPwnedError

            return True

        except TypeError:
            return False

        except PasswordIsPwnedError:
            return False

    def check(self) -> bool:

        # check if password is not pwned and matching with password policy
        if self.__policy.policy_text(text=self.__plain) and self.pwned():
            return True

        return False

    def generate(self, length: int) -> str:
        chars = ascii_lowercase+ascii_uppercase+digits+punctuation

        # set the password to the attribute __plain
        self.__plain = "".join(secrets.choice(chars) for _ in range(length))

        # check the attribute __plain, if it's not pwned and matching policy
        if self.check():
            return self.__plain

        # if not recall the same method
        return self.generate(length=length)


class User:
    def __init__(self,
                 username: Username, password: Password,
                 hashed: str, enabled: bool,
                 lastchange: str, expiration: str,
                 lastlogin: str, admin: bool) -> None:

        self.__username: Username = username
        self.__password: Password = password
        self.__hash: str = hashed
        self.__lastchange: str = lastchange
        self.__lastlogin: str = lastlogin
        self.__expiration: str = expiration
        self.__enabled: bool = enabled
        self.__admin: bool = admin

    def get_user(self) -> dict:
        return {"username": self.__username.get_username(),
                "hash": self.__hash, "enabled": self.__enabled,
                "admin": self.__admin, "expiration": self.__expiration,
                "lastlogin": self.__lastlogin, "lastchange": self.__lastchange}

    def get_password(self) -> Password:
        return self.__password

    def get_hash(self) -> str:
        return self.__hash

    def get_username(self) -> Username:
        return self.__username

    def get_expiration(self) -> str:
        return self.__expiration

    def get_lastlogin(self) -> str:
        return self.__lastlogin

    def get_lastchange(self) -> str:
        return self.__lastchange

    def get_enabled(self) -> bool:
        return self.__enabled

    def get_admin_status(self) -> bool:
        return self.__admin

    def set_enabled(self, status: bool) -> bool:
        try:
            self.__enabled = status
            return True

        except TypeError:
            return False

    def set_hash(self, hashed: str) -> bool:
        try:
            self.__hash = hashed
            return True

        except TypeError:
            return False

    def set_expiration(self, expiration: str) -> bool:
        try:
            self.__expiration = expiration
            return True

        except TypeError:
            return False

    def set_lastchange(self, lastchange: str) -> bool:
        try:
            self.__lastchange = lastchange
            return True

        except TypeError:
            return False

    def set_lastlogin(self, lastlogin: str) -> bool:
        try:
            self.__lastlogin = lastlogin
            return True

        except TypeError:
            return False

    def login_user(self) -> Union[str, bool]:

        # check if the password match with the hash
        if not password_hash_check(password=self.__password.get_password(), hashed=self.get_hash()):
            return False

        # chcek if user is enabled
        if not self.get_enabled():
            return False

        # set new lastlogin
        if not self.set_lastlogin(lastlogin=Time.time_now()):
            return False

        # check if password is pwned
        if not self.__password.pwned():
            return "change password"

        # chcek if password policy has changed
        password_policy = self.__password.get_policy()
        if self.get_lastchange() < password_policy.get_lastchange():

            # check for policy, if no matching then change the expiration time
            if not password_policy.policy_text(text=self.__password.get_password()):
                self.set_expiration(expiration=Time.time_now())

        # check if username policy has changed, check for policy
        if not self.get_username().policy_username():
            return "change username"

        # check if password is expired
        if self.get_expiration() < Time.time_now():
            return "change password"

        return True

    def generate_password(self, length: int, password: Password) -> Union[str, bool]:

        policy = password.get_policy()

        # checks if from user inputted length is doesn't match with policy lengths
        if length < policy.get_minlength() or length > policy.get_maxlength():
            return False

        return password.generate(length=length)

    def edit_password(self):

        password = self.get_password()
        hashed = hash_to_bcrypt(password=password.get_password())

        # checks if password is not pwned and matching with password policy
        if not password.check():
            return False

        # checks if hashing function went well
        if not hashed:
            return False

        # overriting the old hash of the object
        if not self.set_hash(hashed=hashed):
            return False

        # overwriting the lastchange date to now
        if not self.set_lastchange(lastchange=Time.time_now()):
            return False

        # overwriting the expiration date and adding 3 months to the lastchange date
        if not self.set_expiration(expiration=Time.expiration_update(self.get_lastchange())):
            return False

        return True

    def edit_username(self):
        try:
            username = self.get_username()

            # check if username match with username policy
            if not username.policy_username():
                return False

            return True

        except TypeError:
            return False


class Admin(User):

    def enable_user(self, user: User) -> Union[dict, bool]:

        # setting user enabled to True
        if not user.set_enabled(status=True):
            return False

        return user.get_user()

    def disable_user(self, user: User) -> Union[dict, bool]:

        # setting user enabled to False
        if not user.set_enabled(status=False):
            return False

        return user.get_user()

    def delete_user(self, user: User, data: dict, history: dict) -> Tuple[dict, dict]:

        # deleteing user from the data dictionary
        data.pop(user.get_username().get_username())

        # deleting user from the histories
        history["login"].pop(user.get_username().get_username())
        history["change"].pop(user.get_username().get_username())
        history["password"].pop(user.get_username().get_username())

        return data, history

    def reset_password(self, user: User) -> Union[str, bool]:

        password = user.get_password()
        policy = password.get_policy()

        # generate valid password with the min. length
        if not password.generate(length=policy.get_minlength()):
            return False

        # create a hash
        hashed = hash_to_bcrypt(password=password.get_password())
        if not hashed:
            return False

        # set the created hash
        if not user.set_hash(hashed=hashed):
            return False

        # set password lastchange date to now
        if not user.set_lastchange(lastchange=Time.time_now()):
            return False

        # set password expiration to 3 months after lastchange
        if not user.set_expiration(expiration=user.get_lastchange()):
            return False

        # return the new password
        return password.get_password()

    def get_password_policy(self) -> dict:
        policy = self.get_password().get_policy()
        return policy.get_policy()

    def get_username_policy(self) -> dict:
        policy = self.get_username().get_policy()
        return policy.get_policy()

    def set_password_policy(self, data: dict) -> Union[dict, bool]:
        policy = self.get_password().get_policy()

        # sets the lower min count
        if not policy.set_lower(lower=data["lower"]):
            return False

        # sets the upper min count
        if not policy.set_upper(upper=data["upper"]):
            return False

        # sets the min length
        if not policy.set_minlength(minlength=data["minlength"]):
            return False

        # sets the max length
        if not policy.set_maxlength(maxlength=data["maxlength"]):
            return False

        # sets the punctuation min count
        if not policy.set_punctuation(punctuation=data["punctuation"]):
            return False

        # sets the numeric min count
        if not policy.set_numeric(numeric=data["numeric"]):
            return False

        # checks if policy is valid
        if not policy.check_policy():
            return False

        # sets lastchange date on now
        if not policy.set_lastchange(time_str=Time.time_now()):
            return False

        return policy.get_policy()

    def set_username_policy(self, data: dict) -> Union[str, bool]:
        policy = self.get_username().get_policy()

        # sets the lower min count
        if not policy.set_lower(lower=data["lower"]):
            return False

        # sets the upper min count
        if not policy.set_upper(upper=data["upper"]):
            return False

        # sets the min length
        if not policy.set_minlength(minlength=data["minlength"]):
            return False

        # sets the max length
        if not policy.set_maxlength(maxlength=data["maxlength"]):
            return False

        # sets the punctuation min count
        if not policy.set_punctuation(punctuation=data["punctuation"]):
            return False

        # sets the numeric min count
        if not policy.set_numeric(numeric=data["numeric"]):
            return False

        # checks if policy is valid
        if not policy.check_policy():
            return False

        # sets lastchange date to now
        if not policy.set_lastchange(time_str=Time.time_now()):
            return False

        return policy.get_policy()

    def get_user_data(self, user: User) -> dict:
        return user.get_user()

    def get_user_count(self, data: dict) -> int:
        return len(data)

    def signup(self, user: User) -> bool:

        # set lastchange
        if not user.set_lastchange(lastchange=Time.time_now()):
            return False

        # set expiration date to 3 months after lastchange
        if not user.set_expiration(expiration=Time.expiration_update(user.get_lastchange())):
            return False

        # set lastlogin date to now
        if not user.set_lastlogin(lastlogin=Time.time_now()):
            return False

        # check password with password policy and pwned
        password = user.get_password()
        if not password.check():
            return False

        username = user.get_username()

        # check username with username policy
        if not username.policy_username():
            return False

        # check that username is not in password
        if username.get_username() in password.get_password():
            return False

        # check that password is not in username
        if password.get_password() in username.get_username():
            return False

        # create hash of the password
        password_hash = hash_to_bcrypt(password=password.get_password())

        # check if creating hash went well
        if not password_hash:
            return False

        # set that hash
        if not user.set_hash(hashed=password_hash):
            return False

        return user

    def get_user_login_history(self, history: dict, user: User) -> list:

        # returns login history of username
        return history["login"][user.get_username().get_username()]

    def get_user_change_history(self, history: dict, user: User) -> list:

        # returns change history of username
        return history["change"][user.get_username().get_username()]
