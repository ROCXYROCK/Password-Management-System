import os,json
from sre_constants import CATEGORY_WORD


current_file = os.path.dirname(os.path.realpath(__file__))

def f1():
    with open(current_file+"/../Data/Data.json","r") as file:
        load = file.read()
        Data = json.loads(load)
        return Data

Data = f1()
print(Data)
class Sup_User():
    def __init__(self,Username,Password,Status,last_login,last_changed):
        self.Username = Username
        self.Password = Password
        self.Status = Status
        self.last_login = last_login
        self.last_changed = last_changed

    def login(self):
        pass
    def sign_up(self):
        #creat a new user
        def set_username(self):
            #enter username one time, if this doesn't exist, then pass
            pass
        def set_password(self):
            #enter password 2 times if its same then pass
            pass

    def change_password(self):
        #add password to password_hash list
        pass
    def generate_password(self):
        #generate password according to policy
        pass

class User(Sup_User):
    def show_apps():
        pass


class Admin(Sup_User):
    pass
    
#hier kommen noch funktionen, da ich die Daten hier behandeln möchte und nicht im Hauptfile, dann falls
#daten irgendwo gespeichert werden, dann wird eine Funktion set_Data aufgerufen. gelesen wird eine Funktion 
#get_Data