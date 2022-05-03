"""
Project: Password-Management-System/password-pwned-check\n
Author: Abdulhamid Hijli\n
Date: 02.Mai.2022\n
Discription: This is a part of my 'Password Management System' project. This script checks if a password is pwned(leaked) or not. 
This Module can be integrated in any System which can pass a password to check. If password is pwned it will return True, if not it will return False
"""

import requests
import hashlib

def Check_pwned(password:str):
    """
    This is the main function of this module and checks password if it's pwned or not. It communicates with the haveibeenpwned.com through
    the HIBP API, it recieve per HTTP Request a list of hashed passwords which have the same first 5 characters of the given password.
    The script search in this list for the hash of the given password, if this is in the list, the system will return True.
    """
    pwned_list = requests.get("https://api.pwnedpasswords.com/range/"+hashed(password)[:5]).text

    pwned_list = pwned_list.split(":")
    for i in range(1,len(pwned_list)-1):
        cleaning_hash = pwned_list[i].index("\n")+1
        pwned_list[i] = pwned_list[i].lstrip(pwned_list[i][:cleaning_hash])

    pwned_list.pop() # the last item is not in need, so i can remove it

    def hashed(password:str):
        password = password.encode()
        hashed = hashlib.sha1(password).hexdigest()
        hashed = hashed.upper()
        return hashed
    
    if hashed(password)[5:] in pwned_list:
        return True
    return False
    

