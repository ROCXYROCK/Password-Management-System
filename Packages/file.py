import os,json


current_file = os.path.dirname(os.path.realpath(__file__))

Data_File = "/../Data/Data.json"
History_File = "/../Data/history.json"
Applications_File = "/../Data/Applications.json"

def read_file(file:str):
    
    f = open(current_file+file,"r")
    Read = f.read()
    f.close()
    return Read

def write_file(file:str,Data):
    f = open(current_file+file,"w")
    json.dump(Data,f,indent=2)
    f.close()


def get_user(username:str):
    try:
        # read data 
        Read = read_file(Data_File)
        Data = json.loads(Read)
                        
        if username in Data.keys():
            return Data[username]
    except:
        return False



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



# def set_history(username,hash)









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