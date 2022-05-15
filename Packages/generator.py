"""
Author: Abdulhamid Hijli
Project: password-management-system
Date: 15.05.2022
Description:
The Module generator has a function generate, which generates a secure and not pwned password to use it by resetting the password
and by calling the generate function. The module will be called and returns a secure password to the user.   
"""

from string import ascii_lowercase,ascii_uppercase,digits,punctuation
from random import shuffle,sample
from password import check

def generate(length:int):

    """
    This is a function to generate a secure password, it gets the length and returns the password as a string. The password will be 
    generated according to the password policy.
    """

    #set a list of all possible characters
    all = list(ascii_lowercase+ascii_uppercase+digits+punctuation)
    
    # shuffle the list twice
    shuffle(all)
    shuffle(all)

    #choice length characters of the list randomly
    temp = sample(all,length)
    
    #convert the choice to string
    password = "".join(temp)
    
    #if the generated password doesn't equal the policies then generate another one.
    if not check(password):
        generate(length)
    return password

    