import requests,string
from datetime import datetime
from random import shuffle,sample
from dateutil.relativedelta import relativedelta
from Encryption import hash_to_sha1,hash_to_bcrypt,password_hash_check


class Time:
    def time_now() -> str:
        return str(datetime.utcnow())

    def expiration_update(time_str:str) -> str:
        time = datetime.fromisoformat(time_str)
        time = time + relativedelta(months=3)
        return str(time)
    
class Password:
    def __init__(self,length:int,maxlength:int,punctuation:int,numeric:int,lower:int,upper:int,lastchange:str) -> None:
        self.__length : int = length
        self.__maxlength : int = maxlength
        self.__punctuation : int = punctuation
        self.__numeric : int = numeric
        self.__lower : int  = lower
        self.__upper : int = upper
        self.__lastchange : str = lastchange
    
    def set_lastchange(self,time_str:str) -> bool:
        try:
            self.__lastchange = time_str
            return True
        except:
            return False
    
    def get_length(self) -> int:
        return self.__length
    
    def get_lastchange(self) -> str:
        return self.__lastchange
    
    def get_policy(self) -> dict:
        return {"length":self.__length,"upper":self.__upper,"lower":self.__lower,"punctuation":self.__punctuation,"numeric":self.__numeric,"lastchange":self.__lastchange}
    
    def pwned(self,password:str) -> bool:
        
        hashed  = hash_to_sha1(password = password).upper()
        pwned_list = requests.get(url="https://api.pwnedpasswords.com/range/"+hashed[:5]).text

        
        pwned_list = pwned_list.split("\n")
        pwned_list.pop()
        
        for i in range(pwned_list.__len__()):
            tmp = pwned_list[i].split(":")[0]
            
            if hashed[5:] == tmp:
                return False
    
        return True
    
    def isupper(self,password:str) -> bool:
        """
        This is a sub-function of the function policy(), it checks if the password contains enough upper cases. If the password contains
        enough uppercases the function will returns True, else it will return False.
        """
        counter = 0
        for i in password:
            if i.isupper():
                counter +=1
        if counter >= self.__upper:
            return True
        return False
    
    def islower(self,password:str) -> bool:
        """
        This is a sub-function of the function policy(), it checks if the password conatains enough lower cases. The function returns 
        True, if there are enough lower cases, else it returns False.
        """
        counter = 0
        for i in password:
            if i.islower():
                counter += 1
        if counter >= self.__lower:
            return True
        return False
    
    def isnumeric(self,password:str) -> bool:
        """
        This is a sub-fuction of the function policy(), it checks if the password has enough numerical characters. If there are enough,
        the function will return True, else False.
        """
        counter = 0
        for i in password:
            if i.isnumeric():
                counter += 1
        if counter >= self.__numeric:
            return True
        return False
    
    def ispunctuation(self,password:str) -> bool:
        """
        This is a sub-function of the function policy(), it checks if the password has enough special characters. 
        There is a counter which count every special characters. If there are enough special characters the function will returns True,
        else the function will returns False.
        """
        counter = 0
        for i in password:
            if i in string.punctuation :
                counter += 1
            if i =="\"" or i =="'":
                return False
        
        if counter < self.__punctuation:
            return False
        
        return True
    
    def length(self,password:str) -> bool:
        """
        This is a sub-function of the function policy(). it checks if the lenght of the given password is equal to the required length 
        or not. If the length is enough the fuction will returns True, else it will returns False.
        """
        if password.__len__() < self.__length:
            return False
        
        if password.__len__() > self.__maxlength:
            return False
        return True

    def policy(self,password:str) -> bool:
        """
        This function checks the password according to the policy, if the password conatain all required cases. The function has
        sub-functions to make the code more readable und easy to understand. The function returns True, if the password is containing
        all required cases, else it returns False.
        """
        if not self.islower(password = password):
            return False

        if not self.isupper(password = password):
            return False
        
        if not self.isnumeric(password = password):
            return False
        
        if not self.ispunctuation(password = password):
            return False
        
        if not self.length(password = password):
            return False
        return True
    
    def check_policy(self):
        sum_of = self.__lower + self.__numeric + self.__punctuation + self.__upper
        if sum_of > self.__length:
            return False
        return True
    
    def check(self,password:str) -> bool:
        """
        This function is the main function of this module. this function will be requested from the other modules to check
        password validation. If the password is not pwned and contain the policy requirement, the function returns True, 
        else it returns False.
        """
        #check if password is valid
        if self.policy(password = password) and self.pwned(password = password):
            return True
        return False
    
    def generate(self,length:int) -> str:
        """
        This is a function to generate a secure password, it gets the length and returns the password as a string. The password will be 
        generated according to the password policy.
        """
        if length < self.__length or length > self.__maxlength:
            return False
        #set a list of all possible characters
        all = list(string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation)
        
        shuffle(all)
        shuffle(all)

        temp = sample(all,length) 
        password = "".join(temp)
        
        if self.check(password = password):
            return password
        
        return self.generate(length = length)
    
    
class User:
    def __init__(self,username:str,password:str,enabled:bool,lastchanged:str, expiration:str,lastlogin:str,admin:bool) -> None:
        self.__username : str = username
        self.__password : str = password
        self.__lastchanged : str = lastchanged
        self.__lastlogin : str = lastlogin
        self.__expiration : str = expiration
        self.__enabled : bool = enabled
        self.__admin : bool = admin
    
    def get_user(self) -> dict:
        return {"username":self.__username,"password":self.__password,
                "enabled":self.__enabled,"admin":self.__admin,"expiration":self.__expiration,
                "last_login":self.__lastlogin,"last_changed":self.__lastchanged}
    
    def get_password(self) -> str:
        return self.__password
    
    def get_username(self) -> str:
        return self.__username
    
    def get_expiration(self) -> str:
        return self.__expiration
    
    def get_lastlogin(self) -> str:
        return self.__lastlogin
    
    def get_lastchanged(self) -> str:
        return self.__lastchanged
    
    def get_enabled(self) -> bool:
        return self.__enabled
    
    def get_admin_status(self) -> bool:
        return self.__admin
        
    def set_enabled(self,status:bool) -> bool:
        try:
            self.__enabled = status
            return True
        except:
            return False
    
    def set_password(self,password:str) -> bool:
        try:
            self.__password = password
            return True
        except:
            return False
        
    def set_expiration(self,expiration:str) -> bool:
        try:
            self.__expiration = expiration
            return True
        except:
            return False
    
    def set_lastchange(self,lastchange:str) -> bool:
        try:
            self.__lastchanged = lastchange
            return True
        except:
            return False
    
    
    def login_user(self,password:str,policy:dict) -> bool:
             
        if not password_hash_check(password = password,hashed = self.__password):
            return False
        
        if not self.__enabled:
            return False

        self.__lastlogin = Time.time_now()
        
        password_object = Password(length=policy["length"],punctuation=policy["punctuation"], maxlength=policy["maxlength"],
                            numeric=policy["numeric"],lower=policy["lower"],
                            upper=policy["upper"], lastchange=policy["lastchange"])
    
        if not password_object.pwned(password = password):
            return "change"
         
        if self.__lastchanged < password_object.get_lastchange():
            if not policy(password=password):
                self.__expiration = Time.time_now()
        
        if self.__expiration < Time.time_now():
            return "change"
        
        return True
    
    def generate_password(self,length:int,policy:dict) -> str:
        
        password = Password(length=policy["length"],punctuation=policy["punctuation"], maxlength=policy["maxlength"],
                            numeric=policy["numeric"],lower=policy["lower"],
                            upper=policy["upper"], lastchange=policy["lastchange"])

        if length < password.get_length():
            return False
        
        return password.generate(length=length)
    
    def edit_password(self,new_password:str,policy:dict) -> dict:
        
        password = Password(length=policy["length"],punctuation=policy["punctuation"], maxlength=policy["maxlength"],
                            numeric=policy["numeric"],lower=policy["lower"],
                            upper=policy["upper"], lastchange=policy["lastchange"])
        
        hashed = hash_to_bcrypt(password=new_password)
        
        if not password.check(password=new_password):
            return False
        if not hashed:
            return False
        
        self.__password = hashed
        self.__expiration = Time.expiration_update(self.__lastchanged)
        self.__lastchanged = Time.time_now()
        
        return True
    


class Admin(User):
    def enable_user(self,user_x:User):
        user_x.set_enabled(status = True)
        return user_x.get_user()
    
    def disable_user(self,user_x:User):
        user_x.set_enabled(status = False)
        return user_x.get_user()
    
     
    def delete_user(self,user_x:User,data:dict,history:dict):
        data.pop(user_x.get_username())
        history["login"].pop(user_x.get_username())
        history["change"].pop(user_x.get_username())
        history["password"].pop(user_x.get_username())
        
        return data,history

    def reset_password(self,user_x:User,policy:dict):
        password = Password(length=policy["length"],punctuation=policy["punctuation"], maxlength=policy["maxlength"],
                            numeric=policy["numeric"],lower=policy["lower"],
                            upper=policy["upper"], lastchange=policy["lastchange"])
        
        new_password = password.generate(length=password.get_length())
        if not password.check(password=new_password):
            return False
        
        hashed = hash_to_bcrypt(password=new_password)
        if not hashed:
            return False
        
        if not user_x.set_password(password = hashed):
            return False
        
        if not user_x.set_expiration(expiration = Time.time_now()):
            return False
        
        return new_password
    
    
    def get_policy(self,policy:Password) -> dict:
        return policy.get_policy()
    
    def set_policy(self,policy:dict) -> dict:
        password_policy = Password(length=policy["length"],punctuation=policy["punctuation"], maxlength=policy["maxlength"],
                                   numeric=policy["numeric"],upper=policy["upper"],
                                   lower=policy["lower"],lastchange=policy["lastchange"])
        if not password_policy.check_policy():
            return False
        password_policy.set_lastchange(time_str = Time.time_now()) 
        return password_policy.get_policy()
        
    def get_user_data(self,username:str,data:dict) -> dict:
        user_data = data[username]
        user = User(username = username, password = user_data["password"], enabled = user_data["enabled"],
                    admin = user_data["admin"], expiration = user_data["expiration"],
                    lastchanged = user_data["last_changed"], lastlogin = user_data["last_login"])
        
        return user.get_user()
        
    def get_user_count(self,data:dict) -> int:
        return data.__len__()

    def signup(self,user:dict,policy:dict) -> dict:
        user_object = User(username = user["username"], password = user["password"], enabled = user["enabled"],
                    admin = user["admin"], expiration = Time.expiration_update(Time.time_now()),
                    lastchanged = Time.time_now(), lastlogin = Time.time_now())
        
        password = Password(length = policy["length"], punctuation = policy["punctuation"], maxlength=policy["maxlength"],
                            numeric = policy["numeric"], upper = policy["upper"],
                            lower = policy["lower"], lastchange = policy["lastchange"])
        
        if not password.check(password = user_object.get_password()):
            return False
        
        password_hash = hash_to_bcrypt(password = user_object.get_password())
        user_object.set_password(password = password_hash) 
        return user_object
    
    def get_user_login_history(self,history:dict,user_x:User) -> list:
        return history["login"][user_x.get_username()]
    
    def get_user_change_history(self,history:dict,user_x:User) -> list:
        return history["change"][user_x.get_username()]