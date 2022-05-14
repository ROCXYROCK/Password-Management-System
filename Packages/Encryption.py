import bcrypt
import hashlib

def SHA1(password:str): 

    password = password.encode() 
    hash = hashlib.new('sha1') 
    hash.update(password)
    return hash.hexdigest() 

def hash_psw(password:str):

    password = password.encode()
    salt = bcrypt.gensalt(12)
    hashed = bcrypt.hashpw(password,salt)
    return hashed.decode() 

def PSW_Check(password: str, encrypted : str):
    
    password = password.encode()
    hash = encrypted.encode()
    
    return bcrypt.checkpw(password,hash)

hashed = hash_psw("haha")

