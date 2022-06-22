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
    

class Policy:    
    def __init__(self,minlength:int,maxlength:int,punctuation:int,numeric:int,lower:int,upper:int,lastchange:str) -> None:
        self.__minlength : int = minlength
        self.__maxlength : int = maxlength
        self.__punctuation : int = punctuation
        self.__numeric : int = numeric
        self.__lower : int  = lower
        self.__upper : int = upper
        self.__lastchange : str = lastchange
        
    def get_lastchange(self) -> str:
        return self.__lastchange
    
    def get_minlength(self) -> int:
        return self.__minlength
    
    def get_maxlength(self) -> int:
        return self.__maxlength
    
    def get_punctuation(self) -> int:
        return self.__punctuation    
    
    def get_numeric(self) -> int:
        return self.__numeric
    
    def get_upper(self) -> int:
        return self.__upper
    
    def get_lower(self) -> int:
        return self.__lower
    
    def set_minlength(self,minlength:int) -> bool:
        try:
            self.__minlength = minlength
            return True 
        except:
            return False
    
    def set_maxlength(self,maxlength:int) -> bool:
        try:
            self.__maxlength = maxlength
            return True 
        except:
            return False
    
    def set_punctuation(self,punctuation:int) -> bool:
        try:
            self.__punctuation = punctuation
            return True 
        except:
            return False

    def set_numeric(self,numeric:int) -> bool:
        try:
            self.__numeric = numeric
            return True 
        except:
            return False
    
    def set_upper(self,upper:int) -> bool:
        try:
            self.__upper = upper
            return True 
        except:
            return False
    
    def set_lower(self,lower:int) -> bool:
        try:
            self.__lower = lower
            return True 
        except:
            return False
    
    def set_lastchange(self,time_str:str) -> bool:
        try:
            self.__lastchange = time_str
            return True
        except:
            return False
    
    def get_policy(self) -> dict:
        return {"minlength":self.__minlength,"maxlength":self.__maxlength,"upper":self.__upper,"lower":self.__lower,"punctuation":self.__punctuation,"numeric":self.__numeric,"lastchange":self.__lastchange}

    def isupper(self,text:str) -> bool:
        """checks if the password contains enough upper cases"""
        counter = 0
        
        for i in text:
            if i.isupper():
                counter +=1
        
        if counter >= self.__upper:
            return True
        
        return False
        
    def islower(self,text:str) -> bool:
        """checks if the password conatains enough lower cases"""
        counter = 0
        
        for i in text:
            if i.islower():
                counter += 1
        
        if counter >= self.__lower:
            return True
        
        return False
    def isnumeric(self,text:str) -> bool:
        """checks if the password has enough numerical characters"""
        counter = 0
        
        for i in text:
            if i.isnumeric():
                counter += 1
                
        if counter >= self.__numeric:
            return True
        
        return False
    
    def ispunctuation(self,text:str) -> bool:
        """checks if the password has enough special characters"""
        counter = 0
        list_of_non = ["\"","'",":",";","\\"]
        
        for i in text:
            if i in string.punctuation :
                counter += 1
            
            if i in list_of_non:
                return False
        
        if counter < self.__punctuation:
            return False
        
        return True
    
    def length(self,text:str) -> bool:
        """checks if the lenght of the given password is equal to the required length or not"""
        if text.__len__() < self.__minlength:
            return False
        
        if text.__len__() > self.__maxlength:
            return False
        
        return True
    
    
    def policy_text(self,text:str) -> bool:
        """
        This function checks the password according to the policy, if the password conatain all required cases. The function has
        sub-functions to make the code more readable und easy to understand. The function returns True, if the password is containing
        all required cases, else it returns False.
        """
        if not self.islower(text=text):
            return False

        if not self.isupper(text=text):
            return False
        
        if not self.isnumeric(text=text):
            return False
        
        if not self.ispunctuation(text=text):
            return False
        
        if not self.length(text=text):
            return False
        return True
    
    
    def check_policy(self):
        if self.__minlength >= self.__maxlength:
            return False
        
        sum_of = self.__lower + self.__numeric + self.__punctuation + self.__upper
        if sum_of > self.__minlength:
            return False
        return True

class Username:
    def __init__(self,username:str,policy:Policy) -> None:
        self.__username : str = username
        self.__policy : Policy = policy
    
    def get_username(self) -> str:
        return self.__username
    
    def get_policy(self) -> Policy:# maybe no need 
        return self.__policy
    
    def policy_username(self):
        resault = self.__policy.policy_text(text=self.__username)
        if not resault:
            return False
        return True
    
    def set_username(self,username:str) -> bool:
        try:
            self.__username = username
            return True
        except:
            return False



class Password:
    
    def __init__(self,plain:str,policy:Policy) -> None:
        self.__policy : Policy = policy 
        self.__plain : str = plain
    
    def get_length(self) -> int:
        return self.plain.__len__()
    
    def get_password(self) -> str:
        return self.__plain
    
    def get_policy(self) -> Policy:
        return self.__policy
    
    def set_password(self,plain:str):
        try:
            self.__plain = plain
            return True
        except:
            return False
    
    def pwned(self) -> bool:
        hashed  = hash_to_sha1(password = self.__plain).upper()
        pwned_list = requests.get(url="https://api.pwnedpasswords.com/range/"+hashed[:5]).text

        
        pwned_list = pwned_list.split("\n")
        pwned_list.pop()
        
        for i in range(pwned_list.__len__()):
            tmp = pwned_list[i].split(":")[0]
            
            if hashed[5:] == tmp:
                return False
    
        return True
    
    def check(self) -> bool:
        """
        This function is the main function of this module. this function will be requested from the other modules to check
        password validation. If the password is not pwned and contain the policy requirement, the function returns True, 
        else it returns False.
        """
        #check if password is valid
        if self.__policy.policy_text(text = self.__plain) and self.pwned():
            return True
        return False
    
    def generate(self,length:int) -> str:
        """
        This is a function to generate a secure password, it gets the length and returns the password as a string. The password will be 
        generated according to the password policy.
        """
        #set a list of all possible characters
        all = list(string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation)
        
        shuffle(all)
        shuffle(all)

        temp = sample(all,length) 
        self.__plain = "".join(temp)
        
        if self.check():
            return self.__plain
        
        return self.generate(length = length)
    
        
class User:
    def __init__(self,username:str,password:str,hash:str,enabled:bool,lastchange:str, expiration:str,lastlogin:str,admin:bool) -> None:
        self.__username : Username = username
        self.__password : Password = password
        self.__hash : str = hash
        self.__lastchange : str = lastchange
        self.__lastlogin : str = lastlogin
        self.__expiration : str = expiration
        self.__enabled : bool = enabled
        self.__admin : bool = admin
    
    def get_user(self) -> dict:
        return {"username":self.__username.get_username(),"hash":self.__hash,
                "enabled":self.__enabled,"admin":self.__admin,"expiration":self.__expiration,
                "lastlogin":self.__lastlogin,"lastchange":self.__lastchange}
    
    def get_password(self) -> Password:
        return self.__password
    
    def get_hash(self) -> str:
        return self.__hash
    
    def get_username(self) -> Username:
        return self.__username
    
    def get_expiration(self) -> str:
        return self.__expiration
    
    def get_lastlogin(self) -> str:
        return self.__lastlogin
    
    def get_lastchange(self) -> str:
        return self.__lastchange
    
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
    
    def set_hash(self,hash:str) -> bool:
        try:
            self.__hash = hash
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
            self.__lastchange = lastchange
            return True
        except:
            return False
        
    def set_lastlogin(self,lastlogin:str) -> bool:
        try:
            self.__lastlogin = lastlogin
            return True
        except:
            return False
    
    def login_user(self) -> bool:
             
        if not password_hash_check(password = self.__password.get_password(),hashed = self.get_hash()):
            return False
        
        if not self.get_enabled():
            return False

        self.set_lastlogin(lastlogin=Time.time_now()) 
        if not self.__password.pwned():
            return "change"
        
        if not self.get_username().policy_username():
            return "change"
        
        policy = self.__password.get_policy()
        if self.get_lastchange() < policy.get_lastchange():
            if not policy.policy_text(text=self.__password.get_password()):
                self.set_expiration(expiration=Time.time_now()) 
        
        if self.get_expiration() < Time.time_now():
            return "change"
        return True
    
    def generate_password(self,length:int,password:Password) -> str:
        
        policy = password.get_policy()
        if length < policy.get_minlength() or length > policy.get_maxlength():
            return False
        
        return password.generate(length=length)
    
    def edit_password(self) -> bool:
        password = self.get_password()
        hashed = hash_to_bcrypt(password=password.get_password())
        
        if not password.check():
            return False
        if not hashed:
            return False
        
        self.__hash = hashed
        self.__lastchanged = Time.time_now()
        self.__expiration = Time.expiration_update(self.__lastchanged)
        
        return True
    
    def edit_username(self):
        try:
            username = self.get_username()
            if not username.policy_username():
                return False
        
            return True
        except:
            return False


class Admin(User):
    def enable_user(self,user_x:User) -> dict:
        user_x.set_enabled(status = True)
        return user_x.get_user()
    
    def disable_user(self,user_x:User) -> dict:
        user_x.set_enabled(status = False)
        return user_x.get_user()
    
     
    def delete_user(self,user_x:User,data:dict,history:dict) -> dict:
        data.pop(user_x.get_username().get_username())
        
        history["login"].pop(user_x.get_username().get_username())
        history["change"].pop(user_x.get_username().get_username())
        history["password"].pop(user_x.get_username().get_username())
        
        return data,history

    def reset_password(self,user_x:User) -> str:
       
        password = user_x.get_password()
        policy = password.get_policy()
        password.generate(length=policy.get_minlength())
        
        if not password.check():
            return False
        
        hashed = hash_to_bcrypt(password=password.get_password())
        if not hashed:
            return False
        
        if not user_x.set_hash(hash=hashed):
            return False
        
        if not user_x.set_lastchange(lastchange=Time.time_now()):
            return False
        
        if not user_x.set_expiration(expiration = Time.time_now()):
            return False
        
        return password.get_password()
    
    
    def get_password_policy(self) -> dict:
        policy = self.get_password().get_policy()
        return policy.get_policy()
    
    def get_username_policy(self) -> dict:
        policy = self.get_username().get_policy()
        return policy.get_policy()
    
    def set_password_policy(self,data:dict) -> dict:
        policy = self.get_password().get_policy()
        
        if not policy.set_lower(lower=data["lower"]):
            return False
        
        if not policy.set_upper(upper=data["upper"]):
            return False
        
        if not policy.set_minlength(minlength=data["minlength"]):
            return False
        
        if not policy.set_maxlength(maxlength=data["maxlength"]):
            return False
        
        if not policy.set_punctuation(punctuation=data["punctuation"]):
            return False
        
        if not policy.set_numeric(numeric=data["numeric"]):
            return False
        
        if not policy.check_policy():
            return False
        
        policy.set_lastchange(time_str = Time.time_now()) 
        return policy.get_policy()
    
    def set_username_policy(self,data:dict) -> dict:
        policy = self.get_username().get_policy()
        
        if not policy.set_lower(lower=data["lower"]):
            return False
        
        if not policy.set_upper(upper=data["upper"]):
            return False
        
        if not policy.set_minlength(minlength=data["minlength"]):
            return False
        
        if not policy.set_maxlength(maxlength=data["maxlength"]):
            return False
        
        if not policy.set_punctuation(punctuation=data["punctuation"]):
            return False
        
        if not policy.set_numeric(numeric=data["numeric"]):
            return False
        
        if not policy.check_policy():
            return False
        
        policy.set_lastchange(time_str = Time.time_now()) 
        return policy.get_policy()
        
    def get_user_data(self,user:User) -> dict: 
        return user.get_user()
        
    def get_user_count(self,data:dict) -> int:
        return data.__len__()

    def signup(self,user:User) -> User:

        if not user.set_lastchange(lastchange=Time.time_now()):
            return False
        if not user.set_expiration(expiration=Time.expiration_update(user.get_lastchange())):
            return False
        if not user.set_lastlogin(lastlogin = Time.time_now()):
            return False
        
        password = user.get_password()
        if not password.check():
            return False
        
        username = user.get_username()
        if not username.policy_username():
            return False
        
        if username.get_username() in password.get_password():
            return False
        
        password_hash = hash_to_bcrypt(password = password.get_password())
        user.set_hash(hash= password_hash) 
        return user
    
    def get_user_login_history(self,history:dict,user_x:User) -> list:
        return history["login"][user_x.get_username().get_username()]
    
    def get_user_change_history(self,history:dict,user_x:User) -> list:
        return history["change"][user_x.get_username().get_username()]