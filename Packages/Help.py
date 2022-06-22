import File,Encryption
from Classes import User,Admin,Password,Username,Policy

def create_policy_instance(data:dict):
    try:
        return Policy(minlength=data["minlength"],maxlength=data["maxlength"],punctuation=data["punctuation"],numeric=data["numeric"],
                  lower=data["lower"],upper=data["upper"],lastchange=data["lastchange"])
    except:
        return False
    
def create_password_instance(password:str):
    try:
        data = File.get_policy_file()
        if not data:
            return False
        
        policy = create_policy_instance(data=data["password"])
        if not policy:
            return False
         
        return Password(plain=password,policy=policy)
    except:
        return False
    
def create_username_instance(username:str):
    try:
        data = File.get_policy_file()
        if not data:
            return False
        
        policy = create_policy_instance(data=data["username"])
        if not policy:
            return False
        
        return Username(username=username,policy=policy)
    except:
        return False
    
def create_user_instance(user:dict):
    
           
    password = create_password_instance(password=user["password"])
    if not password:
        return False
       
    username = create_username_instance(username=user["username"])
    if not username:
        return False
    try:
        if not user["admin"]:
            return User(username=username,password=password,hash=user["hash"],enabled=user["enabled"],
                        lastchange=user["lastchange"],expiration=user["expiration"],
                        lastlogin=user["lastlogin"],admin=user["admin"])
        
        return Admin(username=username,password=password,hash=user["hash"],enabled=user["enabled"],
                        lastchange=user["lastchange"],expiration=user["expiration"],
                        lastlogin=user["lastlogin"],admin=user["admin"])
    except:
        return False



def instance_create_useroradmin(username:str,password:str):
    file_data = File.get_data_file()
    
    if not file_data:
        return False
    
    if username not in file_data:
        return False
    
    data = file_data[username]
    data["username"]=username
    data["password"]=password
    
    return create_user_instance(user=data)


def check_master_admin(data:str):
    
    key_data = File.get_key_file()
    if not key_data:
        return False
    key = key_data["key"]
    
    if key == data:
        return True 
    return False

def user_login(data:dict) -> bool:
    try:
        user = instance_create_useroradmin(username=data["username"],password=data["password"])
        if not user:
            return False
        
        if not user.get_enabled():
            return False
        
        login = user.login_user()
        if not login:
            return False
        
        if not File.update_user_data(user=user.get_user()):
            return False
        
        if not File.update_history_with_type(username=user.get_username().get_username(),data=user.get_lastlogin(),data_type="login"):
            return False
        
        return login
    except:
        return False
    
def login_user(data:dict):
    user = instance_create_useroradmin(username=data["username"],password=data["password"])
    if not user:
        return "couldn't create object!:500"
    
    if not user.get_enabled():
        return "user doesn't exist!:400"
    
    login = user.login_user()
    if not login:
        return "invalid password or username!:400"
    
    if login == "change":
        return "outdated password or username, change it!:403"
    
    if not File.update_user_data(user=user.get_user()):
        return "couldn't update user data!:500"
    
    if not File.update_history_with_type(username=user.get_username().get_username(),data=user.get_lastlogin(),data_type="login"):
        return "couldn't update history data!:500"
    
    return "user authenticated!:200"

def user_generate_password(data:dict,length:int) -> str:
    
    login = user_login(data=data)
    if not login:
        return "invalid username or password!:401"
    
    user = instance_create_useroradmin(username=data["username"],password=data["password"])
    if not user:
        return "class conflict:500"
    
    password = create_password_instance(password="")
    
    generated = user.generate_password(length=length,password=password)
    if not generated:
        return "length doesn't match!:400"
    
    return generated + ":200"

def edit_password(data:dict) -> str:
    new_password = data["newpassword"]
    data.pop("newpassword")    
    
    login = user_login(data=data)
    if not login:
        return "username or password invalid!:401"
    
    user = instance_create_useroradmin(username=data["username"],password=data["password"])
    if not user:
        return "class conflict:500"
        
    old_hash = user.get_hash()    
    if not user.get_password().set_password(plain=new_password):
        return "couldn't set the newpassword:500"
    
    if not user.edit_password():
        return "new password is invalid!:400"
    
    history = File.get_history_file()
    if not history:
        return "couldn't get history!:500"
    
    password_history = history["password"][user.get_username().get_username()]
    if password_history:
        for i in password_history:
            if Encryption.password_hash_check(password=new_password,hashed=i):
                return "password used before!:406"
    
    if not File.update_user_data(user=user.get_user()):
        return "failed to update user:500" 
    
    if not File.update_history_with_type(username=user.get_username().get_username(),data=old_hash,data_type="password"):
        return "couldn't update password history:500"
    
    if not File.update_history_with_type(username=user.get_username().get_username(),data=user.get_lastchange(),data_type="change"):
        return "couldn't update change history:500"
    
    return "successfully edited!:200"

def user_edit_username(data:dict):
    
    login = user_login(data=data)
    if not login or login == "change":
        return "not authorized to edit the username!:401"
    
    user = instance_create_useroradmin(username=data["username"],password=data["password"])
    
    file_data = File.get_data_file()
    if data["newusername"] in file_data:
        return "user already exists!:400"
    
    if not user.get_username().set_username(username=data["newusername"]):
        return "couldn't set username!:500"
    
    if not user.edit_username():
        return "username doesn't match with policy!:400"
    
    if check_master_admin(data=data["username"]) and user.get_admin_status() and user.get_enabled():
        if not File.update_key(key=user.get_username().get_username()):
            return "couldn't update key!:500"
    
    if not File.update_user_data(user=user.get_user()):
        return "couldn't update data file!:500"
    return "successfully edited!:200"
    

def admin_login(admin:dict) -> bool:
    
    login = user_login(data=admin) 
    if not login or login == "change":
        return False
    
    user = instance_create_useroradmin(username=admin["username"],password=admin["password"])
    if not user:
        return False
    
    if not isinstance(user,Admin):
        return False
    
    if not user.get_admin_status():
        return False
    
    return True

def admin_enable_disable_user(admin:dict,username:str,state:bool) -> str:
    login = admin_login(admin=admin) 
    if not login:
        return "failed to login,try the path '/login'!:401"

    user_admin = instance_create_useroradmin(username=admin["username"],password=admin["password"])
    user = instance_create_useroradmin(username=username,password="")
    if not user_admin or not user:
        return "user doesn't exist!:200"
    
    if isinstance(user,Admin):
        if not check_master_admin(data=user_admin.get_username().get_username()):
            return "not allowed to enable/disable!:403"
    
    if not state:
        if not user.get_enabled():
            return "user already disabled!:200"
        data = user_admin.disable_user(user_x=user)
    
    if state:
        if user.get_enabled():
            return "user already enabled!:200"
        data = user_admin.enable_user(user_x=user)
    
    if not File.update_user_data(user=data):
        return "failed to update user!:500"
    return "status changed successfully!:200"

def admin_delete_user(admin:dict,username:str) -> str:
    login = admin_login(admin=admin) 
    if not login:
        return "failed to login,try the path '/login'!:401"

    user_admin = instance_create_useroradmin(username=admin["username"],password=admin["password"])
    user = instance_create_useroradmin(username=username,password="")
            
    if not user_admin or not user:
        return "user doesn't exist!:200"
    
    if isinstance(user,Admin):
        if not check_master_admin(data=user_admin.get_username().get_username()):
            return "not allowed to delete!:403"
    
    data = File.get_data_file()
    history = File.get_history_file()
    
    if not data: 
        return "couldn't get user data!:500"
    if not history:
        return "couldn't get user history!:500"
    
    user_data,user_history = user_admin.delete_user(user_x=user,data=data,history=history)
    
    if not File.update_data(data=user_data):
        return "couldn't update data!:500"
    
    if not File.update_history(history=user_history):
        return "couldn't update history!:500"
    
    return "user deleted successfully!:200"

def admin_reset_user_password(admin:dict,username:str) -> str:
    login = admin_login(admin=admin) 
    if not login:
        return "failed to login,try the path '/login'!:401"

    user_admin = instance_create_useroradmin(username=admin["username"],password=admin["password"])
    user = instance_create_useroradmin(username=username,password="")
    
    if not user_admin or not user:
        return "user doesn't exist:200"
    
    if isinstance(user,Admin):
        if not check_master_admin(data=user_admin.get_username().get_username()):
            return "not allowed to reset!:403"
    
    new_password =user_admin.reset_password(user_x=user)
    if not new_password:
        return "failed to generate password!:500"
    
    if not File.update_user_data(user=user.get_user()):
        return "Failed to update data!:500"
    
    if not File.update_history_with_type(username=user.get_username().get_username(),data=user.get_hash(),data_type="password"):
        return "Failed to update history!:500"
    
    if not File.update_history_with_type(username=user.get_username().get_username(),data=user.get_lastchange(),data_type="change"):
        return "Failed to update history!:500"
    
    return new_password + ":200"
    

def admin_set_policy(admin:dict,policy:dict,policy_type:bool) -> str:
    login = admin_login(admin=admin) 
    if not login:
        return "failed to login,try the path '/login'!:401"

    user_admin = instance_create_useroradmin(username=admin["username"],password=admin["password"])
    if not user_admin:
        return "failed class creation!:400"
    
    policy_data = File.get_policy_file()
    if not policy_data:
        policy_data = {}
        
    if not policy_type:
        data = user_admin.set_password_policy(data=policy)
    
        if not data:
            return "failed to set password policy, read documentation!:400"
        
        policy_data["password"] = data
    
    if policy_type:
        data = user_admin.set_username_policy(data=policy)
        
        if not data:
            return "failed to set username policy, read documentation!:400"
        
        policy_data["username"] = data
    
    if not File.update_policy(policy=policy_data):
        return "couldn't update policy!:500"
    
    return "policy successfully updated!:200"


def admin_get_user_data(admin:dict,username:str) -> str:
    login = admin_login(admin=admin) 
    if not login:
        return "failed to login,try the path '/login'!;401"

    user_admin = instance_create_useroradmin(username=admin["username"],password=admin["password"])
    if not user_admin:
        return "failed class creation!;400"
    
    user = instance_create_useroradmin(username=username,password="")
    if not user:
        return "this user doesn't exist!;400"
    
    file_data = File.get_data_file()
    if not file_data:
        return "couldn't get data!;500"

    data = user_admin.get_user_data(user=user)
    
    return str(data) + ";200"

def admin_get_user_count(admin:dict) -> str:
    login = admin_login(admin=admin) 
    if not login:
        return "failed to login,try the path '/login'!:401"

    user_admin = instance_create_useroradmin(username=admin["username"],password=admin["password"])
    if not user_admin:
        return "failed class creation!:400"

    data = File.get_data_file()
    if not data:
        return "couldn't get data!:500"
    
    count = user_admin.get_user_count(data=data)
    return str(count) + ":200"
    
def admin_get_user_loginorchange_history(admin:dict,username:str,type:bool) -> str:
    login = admin_login(admin=admin) 
    if not login:
        return "failed to login,try the path '/login'!;401"
    
    user_admin = instance_create_useroradmin(username=admin["username"],password=admin["password"])
    if not user_admin:
        return "failed class creation!;400"
    
    user_x = instance_create_useroradmin(username=username,password="")
    if not user_x:
        return "failed class creation!;400"
    
    history = File.get_history_file()
    if not history:
        return "couldn't get history!;500"
    
    if type:#True is login
        data = user_admin.get_user_login_history(history=history,user_x=user_x)
        
    if not type:#False is change
        data = user_admin.get_user_change_history(history=history,user_x=user_x)
        
    return str(data) + ";200"

def admin_signup_user(admin:dict,user_data:dict):
    
    login = admin_login(admin=admin) 
    if not login:
        return "failed to login,try the path '/login'!:401"
    
    user_admin = instance_create_useroradmin(username=admin["username"],password=admin["password"])
    if not user_admin:
        return "failed class creation!:400"
    
    user_data["lastchange"]=""
    user_data["lastlogin"]=""
    user_data["expiration"]=""
    user_data["hash"]=""
    
    user = create_user_instance(user=user_data)
    if not user:
        return "couldn't create user!:500"
    
    data_file = File.get_data_file()
    if user.get_username().get_username() in data_file:
        return "user exists already!:400"
    
    new_user = user_admin.signup(user=user)
    if not new_user:
        return "invalid password or username, read documentation!:400"
    
    if not File.update_user_data(new_user.get_user()):
        return "Failed to set user!:500"
   
    if not File.update_history_with_type(username=new_user.get_username().get_username(),data=new_user.get_lastlogin(),data_type="login"):
        return "Failed to update history!:500"
    
    if not File.update_history_with_type(username=new_user.get_username().get_username(),data=new_user.get_hash(),data_type="password"):
        return "Failed to update history!:500"
    
    if not File.update_history_with_type(username=new_user.get_username().get_username(),data=new_user.get_lastchange(),data_type="change"):
        return "Failed to update history!:500"
    
    return "created successfully!:201"
    
    
#think how your application is going to react if the files are not here