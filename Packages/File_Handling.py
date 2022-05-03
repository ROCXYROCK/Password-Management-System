"""
Package: File Handling\n
Author: Abdulhamid Hijli\n
Date: 03.Mai.2022\n
Descrpition:
This package is responsible to encrypt and decrypt the user data, prepare it to print out and store it. Every user get his Data except the ID encrypted with his uniqe secret key which will be built by putting the password hash, %&% and the username together.
This should save the other users data to get pwned by programm usage. Then all the users file data will be encrypted by the same key, this fixed key is 64 byte long and is a mix of alphanumerical and special characters. 
"""
import jwt,json,os


encryption_key = "jb2783rnapu31ubf2ipNFK2H0C)$NAOA$KASBP)AB§"

def File_decryption():
    """
    The Data file will be called and read then the data will be decrypted by using the fixed 64 byte secret key with the JSON Web token to send the data to the function it called by.
    The Data will be formatted from json to python dictionary and then returned.
    """
    with open(os.path.dirname(os.path.realpath(__file__))+"/Data/stored.json","r") as File:
        Data_encrypted = File.read()
    
    decoded_file = jwt.decode(Data_encrypted.decode('ascii'),encryption_key)
    Data = json.loads(decoded_file)
    return Data


def Read_Data(level:str,user_id:int,secret_key:str):
    """
    This function should be called by another module and get the user ID and the user level (admin/user) and the secret key of his passwordhash and %&% and username will be sent be function.
    it will decrypt the data after decrypting the file by calling the 'File_decryption' function and preparing the specified user Data to return it to the function it called by.
    """
    
    Data = File_decryption()
    
    for i in range(len(Data[level])): # here i look if the user exists in the db
        if Data[level][i]["id"] == user_id:
            user_data_encrypted = Data[level][i]["data"]
            break

    decoded_data = jwt.decode(user_data_encrypted.decode('ascii'),secret_key)
    return decoded_data


def File_encryption(Data:dict):##encrypt user

    """
    This Function File_encryption use a fixed secret key to encrypt the file data with the 'JSON Web Token'. 
    All the file data will be encrypted and secure. If the operation is successfully done, it will return True.
    """
    File_Data = jwt.encode(Data,encryption_key)

    with open(os.path.dirname(os.path.realpath(__file__))+"/Data/stored.json","w") as File:
        File.write(File_Data)
    
    return True

def Write_Data(Data:dict,level:str,id:int):
    """
    This Function should encrypt the user data except his id. 
    it's carried out by user uniqe secret key(password hash and %&% and the username). 
    JSON Web Token is the encryption medium. After the encryption of the Data there will be written by calling another function.
    """
    user_index = 0
    for i in range(len(Data[level])):
        if Data[level][i]["id"]:
            user_index = i
            break

    to_encrypt = Data[level][user_index]["data"]
    secret_key = to_encrypt["password"]+"%&%"+to_encrypt["username"]

    Data[level][id]["data"] = jwt.encode(to_encrypt,secret_key)

    File_encryption(Data)
    return True