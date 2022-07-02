"""
Module: File.py
Discription: This module helps to interact with the data files, so it has general functions which can be used of other modules.
Author: Abdulhamid Hijli
Date: 30.06.2022
"""
import json
import pathlib
from os import fspath
from typing import Union

# get the path of the Data directory
file = pathlib.Path(__file__).parent.parent.joinpath("Data")

data_file = fspath(file.joinpath("Data.json"))
key_file = fspath(file.joinpath("secret.json"))
policy_file = fspath(file.joinpath("Policy.json"))
history_file = fspath(file.joinpath("history.json"))


def read_file(file: str) -> Union[dict, bool]:
    """This function is a general function to write json data in files.

    Args:
        file (str): file, where data should stored in.
        data (dict): data, which should be stored in the file.

    Returns:
        read: data, which are successfully read.
        False: writing file went wrong.

    Raises:
        AttributeError: will be raised, if methods of other types are used.
        FileNotFoundError: will be raised when file doesn't exists at this place.
    """
    try:
        with open(file, "r", encoding='UTF-8') as f:
            read = f.read()

        return read

    except AttributeError:
        return False
    except FileNotFoundError:
        return False


def write_file(file: str, data: dict) -> Union[dict, bool]:
    """This function is a general function to write json data in files.

    Args:
        file (str): file, where data should stored in.
        data (dict): data, which should be stored in the file.

    Returns:
        True: file is stored successfully.
        False: writing file went wrong.

    Raises:
        AttributeError: will be raised, if methods of other types are used.
    """
    try:
        with open(file, "w", encoding='UTF-8') as f:
            json.dump(data, f, indent=2)

        return True

    except AttributeError:
        return False


def filenotfoundwriter() -> bool:
    """This function will be called, if files are empty or raising a NotFileFoundError

    Returns:
        True: All files already written
        False: Files couldn't be wrought
    """
    data = {"Amino1": {"hash": "$2b$12$e.pj8zLRRX1exJFPTnRBoOwXfK0eVXLbJqd3B8mwMTUpgrh37EbgW",
            "enabled": True,
                       "admin": True,
                       "expiration": "2022-09-21 00:59:00.268556",
                       "lastlogin": "2022-06-30 16:32:10.458613",
                       "lastchange": "2022-06-16 15:30:54.359203"}}

    policy = {
        "password": {
            "minlength": 8,
            "maxlength": 60,
            "upper": 1,
            "lower": 1,
            "punctuation": 1,
            "numeric": 2,
            "lastchange": "2022-06-17 23:02:31.468827"
        },
        "username": {
            "minlength": 4,
            "maxlength": 15,
            "upper": 1,
            "lower": 1,
            "punctuation": 0,
            "numeric": 1,
            "lastchange": "2022-06-17 22:47:02.195846"
        }
    }

    history = {
        "password": {
            "Amino1": [
                "$2b$12$bZklyhqIvlBxDhW/Mw8wQuLoJihOsuRjN/0TSwmRPvpCVZjz7wPcu",
                "$2b$12$j0qdeJtDARVzq0Go2h7z3.6vxDbNU5pDcRwARMOhmbvqDIa6F96a6"]},
        "login": {
            "Amino1": [
                "2022-06-30 15:46:10.091938",
                "2022-06-30 15:46:17.866905",
                "2022-06-30 15:47:00.505671",
                "2022-06-30 15:48:48.050426",
                "2022-06-30 15:51:34.097386",
                "2022-06-30 15:51:59.604746",
                "2022-06-30 15:52:39.113701"]},
            "change": {
                "Amino1": [
                    "2022-06-11 17:14:35.321194",
                    "2022-06-11 17:14:35.321194",
                    "2022-06-16 15:25:17.779154"]}}

    key = {"key": "Amino1"}

    if not write_file(file=data_file, data=data):
        return False

    if not write_file(file=key_file, data=key):
        return False

    if not write_file(file=policy_file, data=policy):
        return False

    if not write_file(file=history_file, data=history):
        return False


def get_data_file() -> Union[dict, bool]:
    """This function returns the data file converted into Dictionary.

    Returns:
        data: data file converted in dictionary for treatment.
        False: something went wrong.

    Raises:
        AttributeError: will be raised, if methods of other types are used.
        FileNotFoundError: will be raised when file doesn't exists at this place.
    """
    try:
        data = read_file(data_file)

        # check if file able to read
        if not data:
            raise FileNotFoundError

        # convert json to dict
        data = json.loads(data)
        return data

    except AttributeError:
        return False

    except FileNotFoundError:
        if not filenotfoundwriter():
            return False
        return get_data_file()


def get_policy_file() -> Union[dict, bool]:
    """This function returns policy file converted into dictionary.

    Returns:
        data: policy file converted in dictionary for treatment.
        False: something went wrong.

    Raises:
        AttributeError: will be raised, if methods of other types are used.
        FileNotFoundError: will be raised when file doesn't exists at this place.
    """
    try:
        data = read_file(policy_file)

        if not data:
            raise FileNotFoundError

        # convert json in dict
        data = json.loads(data)
        return data

    except AttributeError:
        return False

    except FileNotFoundError:
        if not filenotfoundwriter():
            return False
        return get_policy_file()


def get_history_file() -> Union[dict, bool]:
    """This function returns history file converted into dictionary.

    Returns:
        data: history file converted in dictionary for treatment.
        False: something went wrong.

    Raises:
        AttributeError: will be raised, if methods of other types are used.
        FileNotFoundError: will be raised when file doesn't exists at this place.
    """
    try:
        data = read_file(history_file)

        if not data:
            raise FileNotFoundError

        data = json.loads(data)
        return data

    except AttributeError:
        return False

    except FileNotFoundError:
        if not filenotfoundwriter():
            return False
        return get_history_file()


def get_key_file() -> Union[dict, bool]:
    """This function returns the secret file converted in dict.

    Returns:
        data: data file converted in dictionary for treatment.
        False: something went wrong.

    Raises:
        AttributeError: will be raised, if methods of other types are used.
        FileNotFoundError: will be raised when file doesn't exists at this place.
    """
    try:
        data = read_file(key_file)

        # checks if file is empty
        if not data:
            raise FileNotFoundError

        data = json.loads(data)
        return data
    except AttributeError:
        return False

    except FileNotFoundError:
        if not filenotfoundwriter():
            return False
        return get_key_file()


def update_data(data: dict) -> bool:
    """This function write the data in the data file.

    Args:
        data (dict): data where every user is saving it.

    Returns:
        True: data updated successfully.
        False: something went wrong.

    Raises:
        AttributeError: will be raised, if methods of other types are used.
    """
    try:
        write_file(file=data_file, data=data)
        return True

    except AttributeError:
        return False


def update_policy(policy: dict) -> bool:
    """This function write the ploicy data in the policy file.

    Args:
        policy (dict): policy data

    Returns:
        True: policy updated successfully
        False: something went wrong

    Raises:
        AttributeError: will be raised, if methods of other types are used
    """
    try:
        write_file(file=policy_file, data=policy)
        return True

    except AttributeError:
        return False


def update_history(history: dict) -> bool:
    """This function saves the history data after reading this.

    Args:
        history (dict): history data which should be saved

    Returns:
        True: history updated successfully
        False: something went wrong

    Raises:
        AttributeError: will be raised, if methods of other types are used
    """
    try:
        write_file(file=history_file, data=history)
        return True

    except AttributeError:
        return False


def update_history_with_type(username: str, data: str, data_type: str) -> bool:
    """This function updates single lists of the history,
       it upadates this with calling the history_update function.
       The lists of each user should contain just 15 items,
       which will be checked with help of this funtion.

    Args:
        username (str): which existing user should it be
        data (str): data which sould be stored in the list of this user
        data_type (str): which history should it be: "login","password" or "change"

    Returns:
        True: history updated successfully
        False: something went wrong

    Raises:
        AttributeError: will be raised, if methods of other types are used
    """
    try:
        history = get_history_file()

        if not history:
            return False

        # check if username is in the history
        if username not in history[data_type]:
            history[data_type][username] = []

        # adding the given data by the calling function
        data_list: list = history[data_type][username]

        # add data to data_list
        data_list.append(data)

        # set list length in length
        length = len(data_list)

        # checks if length is more than 15, then it removes the first entry of the list
        if length > 15:
            for _ in range(length-15):
                data_list.pop(0)

        # data will added after handling to the history var and try to store data again
        history[data_type][username] = data_list

        # checks if updating history went well
        if not update_history(history=history):
            return False

        return True

    except AttributeError:
        return False


def update_user_data(user: dict) -> bool:
    """This function adds or updates user data into the data file.

    Args:
        user (dict): needed user data to save it in the Data.json

    Returns:
        True: data updated successfully
        False: something went wrong

    Raises:
        AttributeError: will be raised, if methods of other types are used
    """
    try:
        data = get_data_file()

        # check if data creating went well
        if not data:
            return False

        username = user["username"]

        # remove the item username
        user.pop("username")

        # adding user data to data
        data[username] = user

        # check if file wrought successfully
        if not write_file(file=data_file, data=data):
            return False

        return True

    except AttributeError:
        return False


def update_key(key: str) -> bool:
    """This function updates the name of the master admin

    Args:
        key (str): username of the master admin

    Returns:
        True: secret file updated successfully
        False: something went wrong

    Raises:
        AttributeError: will be raised, if methods of other types are used
    """
    try:
        data = get_key_file()

        # check if data exists
        if not data:
            return False

        data["key"] = key

        write_file(file=key_file, data=data)
        return True

    except AttributeError:
        return False
