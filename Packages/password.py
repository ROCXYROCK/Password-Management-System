"""
Author: Abdulhamid Hijli
Project: password-management-system
Date: 15.05.2022
Discription:
This Module is created to handle password problems. It checks the password according to the password policy and checks 
if the password is pwned. For that it interact with the API of the Haveibeenpwned.com to check the password. The password policy
will be read from the Policy.json file in the Data folder and checks what is required for a secure password
"""
import requests,json,string,os
from Encryption import SHA1

Policy_File = os.path.dirname(os.path.realpath(__file__))

#open the policy.json file
with open(Policy_File+"/../Data/Policy.json","r") as File:
    Req = json.loads(File.read())
    File.close()
#checking if enough uppercases.
def isupper(password:str):
    """
    This is a sub-function of the function policy(), it checks if the password contains enough upper cases. If the password contains
    enough uppercases the function will returns True, else it will return False.
    """
    counter = 0
    for i in password:
        if i.isupper():
            counter +=1
    if counter >= Req["upper"]:
        return True
    return False

#checking if enough lowercases.
def islower(password:str):
    """
    This is a sub-function of the function policy(), it checks if the password conatains enough lower cases. The function returns 
    True, if there are enough lower cases, else it returns False.
    """
    counter = 0
    for i in password:
        if i.islower():
            counter += 1
    if counter >= Req["lower"]:
        return True
    return False

#checking if enough numerics.
def isnumeric(password:str):
    """
    This is a sub-fuction of the function policy(), it checks if the password has enough numerical characters. If there are enough,
    the function will return True, else False.
    """
    counter = 0
    for i in password:
        if i.isnumeric():
            counter += 1
    if counter >= Req["numeric"]:
        return True
    return False

# checking if enough punctuation.
def ispunctuation(password:str):
    """
    This is a sub-function of the function policy(), it checks if the password has enough special characters. 
    There is a counter which count every special characters. If there are enough special characters the function will returns True,
    else the function will returns False.
    """
    counter = 0
    for i in password:
        if i in string.punctuation:
            counter += 1
    if counter >= Req["punctuation"]:
        return True
    return False

# checking if required lenght.
def length(password:str):
    """
    This is a sub-function of the function policy(). it checks if the lenght of the given password is equal to the required length 
    or not. If the length is enough the fuction will returns True, else it will returns False.
    """
    if len(password) >= Req["length"]:
        return True
    return False


def pwned(password:str):
    """
    This is a function of this module which checks password if it's pwned or not. It communicates with the haveibeenpwned.com through
    the HIBP API, it recieve per HTTP Request a list of hashed passwords which have the same first 5 characters of the given password.
    The script search in this list for the hash of the given password, if this is in the list, the system will return False.
    """
    #hashing password
    hashed = SHA1(password).upper()
    
    #send request
    pwned_list = requests.get("https://api.pwnedpasswords.com/range/"+hashed[:5]).text

    #creating list of pwned hashes
    pwned_list = pwned_list.split(":")
    
    #cleaning list items
    for i in range(1,len(pwned_list)-1):
        cleaned_index = pwned_list[i].index("\n")+1
        pwned_list[i] = pwned_list[i].lstrip(pwned_list[i][:cleaned_index])
    pwned_list.pop()

    #looking if password in the pwned list
    if hashed[5:] in pwned_list:
        return False
    return True


# checking if password is containing the required cases.
def policy(password):
    """
    This function checks the password according to the policy, if the password conatain all required cases. The function has
    sub-functions to make the code more readable und easy to understand. The function returns True, if the password is containing
    all required cases, else it returns False.
    """
    
    a = False
    if islower(password):
        a = True

    b = False
    if isupper(password):
        b = True
    
    c = False
    if isnumeric(password):
        c = True
    
    d = False
    if ispunctuation(password):
        d = True
    
    e = False
    if length(password):
        e = True
    
    if a and b and c and d and e:
        return True
    return False

# check function which will be called by another modules
def check(password):
    """
    This function is the main function of this module. this function will be requested from the other modules to check
    password validation. If the password is not pwned and contain the policy requirement, the function returns True, 
    else it returns False.
    """
    #check if password is valid
    if policy(password) and pwned(password):
        return True
    return False
