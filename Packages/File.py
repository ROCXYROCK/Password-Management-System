import os,json,datetime
import Encryption,Generator
from Password import policy,check,pwned
from Classes import User,Admin,Password

current_file = os.path.dirname(os.path.realpath(__file__))

data_file = "/../Data/Data.json"
history_file = "/../Data/history.json"
applications_file = "/../Data/Applications.json"
policy_file = "/../Data/Policy.json"


def time_now():
    return str(datetime.datetime.utcnow())

def read_file(file:str):    
    f = open(current_file+file,"r")
    Read = f.read()
    f.close()
    return Read

def write_file(file:str,Data):
    f = open(current_file+file,"w")
    json.dump(Data,f,indent=2)
    f.close()


data = json.loads(read_file(data_file))
policy = json.loads(read_file(policy_file))
history = json.loads(read_file(history_file))

def update_user_data(user:dict):
    try:
        username = user["username"]
        user.pop("username")
        data[username] = user
        
        write_file(data_file,data)
        return True
    except:
        return False

def update_login_history(username:str,Date:str):
    try:
        pass_list = history["login"][username]
        length = len(pass_list)
        
        if length > 15:
            for i in range(length-15):
                pass_list.pop(0)
        
        history["login"][username] = pass_list
        write_file(history_file,history)
        return True
    except:
        
        return False
        



def create_user_instance(username:str):
    return User(username,data[username]["password"],data[username]["enabled"],data[username]["last_changed"],data[username]["expiration"],data[username]["last_login"],data[username]["admin"])

def login(user:dict): 
    if user["username"] not in data:
        return False
    
    username = user["username"]
    
    User_X = create_user_instance(username)
    return User_X.login_user(user["password"])#lastlogin speichern und user updaten

# def generate_psw(user:dict,length:int):
    
#     if login(user) != True:
#         return False
    
#     User_X = create_user_instance(user["username"])
#     return User_X.generate_password(length)
    
    

#hier kommen noch funktionen, da ich die Daten hier behandeln möchte und nicht im Hauptfile, dann falls
#daten irgendwo gespeichert werden, dann wird eine Funktion set_Data aufgerufen. gelesen wird eine Funktion 
#get_Data