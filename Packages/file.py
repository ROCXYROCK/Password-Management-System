from email.policy import Policy
from importlib.resources import read_binary
from operator import index
import os,json
from unittest import expectedFailure

from flask import make_response


current_file = os.path.dirname(os.path.realpath(__file__))

Data_File = "/../Data/Data.json"
History_File = "/../Data/history.json"
Applications_File = "/../Data/Applications.json"
Policy_File = "/../Data/Policy.json"

def read_file(file:str):
    
    f = open(current_file+file,"r")
    Read = f.read()
    f.close()
    return Read

def write_file(file:str,Data):
    f = open(current_file+file,"w")
    json.dump(Data,f,indent=2)
    f.close()


def set_user(user:dict):
    
        try:
            #read the data from the file
            Read = read_file(Data_File)
            Data =json.loads(Read)

            #add the user to the data
            Data.update(user)
    
            #write the data to the file
            write_file(Data_File,Data)
            return True
        except:
            return False

def get_user(username:str):
    
    try:
        # read data 
        Read = read_file(Data_File)
        Data = json.loads(Read)
                        
        if username in Data.keys():
            return Data[username]
    except:
        return False

def check_enabled(username):
    try:
        Read = read_file(Data_File)
        Data = json.loads(Read)
        
        if Data[username]["enabled"] == True:
            return True
        return False
    except:
        return False

def check_admin(username):
    try:
        Read = read_file(Data_File)
        Data = json.loads(Read)
        
        if Data[username]["admin"] == True:
            return True
        return False
    except:
        return False

def check_user_type(user:dict,content:list):
    try:
        for i in content: 
            if i not in user:
                return False
            if not type(user[i]) == str:
                return False
        return True
    except:
        return False
    
    
def reset_password(username,new_hash):
    try:
        Read = read_file(Data_File)
        Data = json.loads(Read)
        
        Data[username]["password"] = new_hash
        
        write_file(Data_File,Data)
        return True
    except:
        return False

def edit_lastchange(username,editto):
    try:
        Read = read_file(Data_File)
        Data = json.loads(Read)
        
        Data[username]["last_changed"] = editto
        
        write_file(Data_File,Data)
        return True
    except:
        return False
    
    
    

def set_history(username:str,hash:str):
    try:
        Read = read_file(History_File)
        Data =json.loads(Read)
        
        history = Data[username]
        history.append(hash)
        
        Data[username] = (history)
        write_file(History_File,Data)
        return True
    except:
        Read = read_file(History_File)
        Data =json.loads(Read)
        
        history = []
        history.append(hash)
        
        Data[username] = history
        write_file(History_File,Data)
        return True


def get_history(username:str):
    try:
        Read = read_file(History_File)
        Data =json.loads(Read)
        
        return Data[username]
    except:
        return False




def set_policy(policy:dict):
    try:
        Read = read_file(Policy_File)
        Data = json.loads(Read)
        
        Data = policy
        
        write_file(Policy_File,Data)
        return True
    except:
        return False

def edit_policy(k:list,v:list):
    try:
        Read = read_file(Policy_File)
        Data = json.loads(Read)

        for index,i in enumerate(k):
            if i not in Data.keys():
                return False
            
            Data[i]=v[index]
        write_file(Policy_File,Data)
        return True
    
    except:
        return False


def check_policy(policy:dict,content:list):
    try:
        for i in policy.keys():
            if not i in content:
                return False
        
        return True
    except:
        return False


def check_policy_file(policy:dict):
    try: 
        Read = read_file(Policy_File)
        Data = json.loads(Read)
        
        for i in policy.keys():
            if i not in Data.keys():
                return False
        return True
    
    except:
        return False
        
        
def check_policy_type(policy:dict,content:list):
    try:
        for i in content:
            if type(policy[i]) != int:
                return False
        
        return True
    except:
        return False






# class Sup_User():
#     def __init__(self,Username,Password,Status,last_login,last_changed):
#         self.Username = Username
#         self.Password = Password
#         self.Status = Status
#         self.last_login = last_login
#         self.last_changed = last_changed

#     def login(self):
#         pass
#     def sign_up(self):
#         #creat a new user
#         def set_username(self):
#             #enter username one time, if this doesn't exist, then pass
#             pass
#         def set_password(self):
#             #enter password 2 times if its same then pass
#             pass

#     def change_password(self):
#         #add password to password_hash list
#         pass
#     def generate_password(self):
#         #generate password according to policy
#         pass

# class User(Sup_User):
#     def show_apps():
#         pass


# class Admin(Sup_User):
#     pass
    
#hier kommen noch funktionen, da ich die Daten hier behandeln möchte und nicht im Hauptfile, dann falls
#daten irgendwo gespeichert werden, dann wird eine Funktion set_Data aufgerufen. gelesen wird eine Funktion 
#get_Data