from typing import Union
from passlib.hash import bcrypt as b
from passlib.exc import PasswordSizeError
import hashlib


def hash_to_sha1(password: str) -> Union[str, bool]:
    """
    This function uses the sha-1 hashing algorithm to hash the password. 

    Args:
        password (str): The password will only be accepted if it's a string, this will be then hashed

    Returns:
        hashed: hashed password as hex characters.
        False: password hashing went wrong.

    Errors:
        TypeError: will be raised, if passord is not a string.
    """
    try:
        # check if password is string
        if not isinstance(password, str):
            raise TypeError

        # convert password to byte and choose sha1 as hash algorithm
        password = password.encode()
        hashed = hashlib.new('sha1')

        # hash it and return it
        hashed.update(password)
        return hashed.hexdigest()

    except TypeError:
        return False


def hash_to_bcrypt(password: str) -> Union[str, bool]:
    """This function hash password securly using bcrypt algorithm to secure hashing. 

    Args:
        password (str): string, which should be compared if this belong to hash 

    Returns:
        hashed: bcrypt hash of the entered password
        False: password doesn't belong to the hash

    Errors:
        PasswordSizeError: will be raised if password is longer than 4096 characters
    """
    try:
        # check if password is string
        if not isinstance(password, str):
            raise TypeError

        # hash it and return it
        hashed = b.hash(password.encode(), rounds=14)
        return hashed

    except TypeError:
        return False

    except PasswordSizeError:
        return False


def password_hash_check(password: str, hashed: str) -> bool:
    """This function verify if password belong to hash using bcrypt algorithm to secure hashing. 

    Args:
        password (str): string, which should be compared if this belong to hash 
        hashed (str): string, which should be comapred if this hash match with the password

    Returns:
        True: password belongs to the hash
        False: password doesn't belong to the hash

    Errors:
        PasswordSizeError: will be raised if password is longer than 4096 characters
    """
    try:
        # check if passowrd is string
        if not isinstance(password, str):
            raise TypeError

        # check if hash is string
        if not isinstance(hashed, str):
            raise TypeError

        # convert password and hash to byte string
        byte_password = password.encode()
        byte_hash = hashed.encode()

        # return checked password
        return b.verify(byte_password, byte_hash)

    except TypeError:
        return False

    except PasswordSizeError:
        return False
