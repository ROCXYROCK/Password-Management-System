import bcrypt
import hashlib


#hash password with sha-1 algorithm
def SHA1(password:str): 
    """
    This function uses the sha-1 hashing algorithm to hash the password. It will be used to communicate with the HIBP-API to check if a password is pwned or not.

    Args:
        password (str): The password will only be accepted if it's a string, this will be then hashed

    Returns:
        str: hashed password as hex chars
    """
    password = password.encode() 
    hash = hashlib.new('sha1') 
    
    #hash it and return it
    hash.update(password)
    return hash.hexdigest() 


#hash password with bcrypt algorithm 
def hash_psw(password:str):
    """
    this function is responsible for hashing password using a secure hash method. This method is slow, that can prevent a brute force attack, because it takes long time to be hashed

    Args:
        password (str): the password will be accepted as a string which will be hashed with the bcrypt method. 
        The password will go in 12 rounds  

    Returns:
        str: hash
    """
    password = password.encode()
    salt = bcrypt.gensalt(12)
    
    #hash it and return it
    hashed = bcrypt.hashpw(password,salt)
    return hashed.decode() 


#check if password belong to hash
def PSW_Check(password:str, hashed:str):
    
    """
    This function is used to check if a password belong to hash. The hash should be encrypted with the bcrypt algorithm and the password will be in plaintext

    Args:
    password (str): The password is plain text which should be a string.
    hashed (str): The hash should by an encrypted text using the 
    
    Returns:
        _type_: _description_
    """
    
    password = password.encode()
    hash = hashed.encode()
    
    #return checked password    
    return bcrypt.checkpw(password,hash)

