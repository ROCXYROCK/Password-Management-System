import os,json

current_file = os.path.dirname(os.path.realpath(__file__))

data_file = "/../Data/Data.json"
history_file = "/../Data/history.json"
key_file = "/../Data/secret.json"
policy_file = "/../Data/Policy.json"

def read_file(file:str):    
    f = open(current_file+file,"r")
    Read = f.read()
    f.close()
    return Read

def write_file(file:str,Data):
    f = open(current_file+file,"w")
    json.dump(Data,f,indent=2)
    f.close()


def get_data_file():# write some check if file data is corrupt, if yes then write a new function to create or to handle this problem
    try:
        data = read_file(data_file)
        
        if not data:
            return False
        
        data = json.loads(data)
        return data
    except:
        return False
    
def get_policy_file():
    try:
        data = read_file(policy_file)
        
        if not data:
            return False
        
        data = json.loads(data)
        return data
    except:
        return False

def get_history_file():
    try:
        data = read_file(history_file)
        
        if not data:
            return False
        
        data = json.loads(data)
        return data
    except:
        return False
    
def get_key_file():
    try:
        data = read_file(key_file)
        
        if not data:
            return False
        
        data = json.loads(data)
        return data
    except:
        return False

def update_data(data:dict):
    try:
        write_file(data_file,data)
        return True
    except:
        return False
    
def update_policy(policy:dict):
    try:
        write_file(policy_file,policy)
        return True
    except:
        return False
    
def update_history(history:dict):
    try:
        write_file(history_file,history)
        return True
    except:
        return False
    
def update_history_with_type(username:str,data:str,data_type:str):
    try:
        history = get_history_file()
        if not username in history[data_type]:
            history[data_type][username]=[]
        data_list:list = history[data_type][username]
        data_list.append(data)
        length = data_list.__len__()
        
        if length > 15:
            for i in range(length-15):
                data_list.pop(0)
        
        history[data_type][username] = data_list
        update_history(history=history)
        return True
    
    except:
        return False
    
def update_user_data(user:dict):
    try:
        data = get_data_file()
        if not data:
            return data
        
        username = user["username"]
        user.pop("username")
        data[username] = user
        
        write_file(data_file,data)
        return True
    except:
        return False
    
def update_key(key:str):
    try: 
        data = get_key_file()
        if not data:
            return data
    
        data["key"]=key
        write_file(key_file,data)
        return True
    except:
        return False
