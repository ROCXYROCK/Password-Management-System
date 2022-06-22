import sys,os,json,unittest

file = os.path.dirname(os.path.realpath(__file__))+"/../../"

sys.path.append(file)

from Application import app

with open(file + "Unittest/data/login_users.json","r") as f:
    data = json.loads(f.read())
    f.close()


admin = data["admin"]
user1 = data["user1"]
user2 = data["user2"]
user3 = data["user3"]
user4 = data["user4"]
user5 = data["user5"]
user6 = data["user6"]
user7 = data["user7"]
user8 = data["user8"]
user9 = data["user9"]
user10 = data["user10"]

policy_user = data["policy_user"]
invalid_user = data["invalid_user"]


login_admin = {"username":"Amino1","password":"h]XN^3+R8"}



    
class loginTest(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.header = {"Content-Type":"application/json"}
    
    def test_login_user2(self):    
        response = self.app.get('/login',headers=self.header,data=json.dumps(user2))
        self.assertEqual(200,response.status_code)
    
    def test_login_user1(self):
        response = self.app.get('/login',headers=self.header,data=json.dumps(user1))
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.data,b"user doesn't exist!")
        
    def test_Value_Error(self):
        response = self.app.get('/login',headers=self.header,data=json.dumps(invalid_user))
        self.assertEqual(400,response.status_code)
        self.assertEqual(b"invalid values!",response.data)
    
    def test_wronge_method(self):
        response = self.app.post('/login',headers=self.header,data=login_admin)
        self.assertEqual(405,response.status_code)
        
        
class Test_generate_password(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.header = {"Content-Type":"application/json"}
    
    def test_standard_user2(self):
        response = self.app.get('/generate-password',headers=self.header,data=json.dumps({**user2,**{"length":15}}))
        self.assertEqual(200,response.status_code)
    
    def test_disabled_user(self):
        response = self.app.get('/generate-password',headers=self.header,data=json.dumps({**user1,**{"length":15}}))
        self.assertEqual(response.data,b"invalid username or password!")
        self.assertEqual(response.status_code,401)
    
    def test_policy_trigger(self):
        response = self.app.get('/generate-password',headers=self.header,data=json.dumps({**user2,**{"length":10000000}}))
        self.assertEqual(response.data,b"length doesn't match!")
        self.assertEqual(response.status_code,400)
    
    def test_invalid_Type(self):
        response = self.app.get('/generate-password',headers=self.header,data=json.dumps({**user2,**{"length":"10"}}))
        self.assertEqual(response.data,b"invalid values!")
        self.assertEqual(response.status_code,400)

class Test_edit_password(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.header = {"Content-Type":"application/json"}
    
    def test_standard_user2(self):
        response = self.app.put("/edit-password",headers=self.header,data=json.dumps({**user7,**{"new":"Au4gL50$g4$&BUtz/"}}))
        self.assertEqual(response.data,b"successfully edited!")
        self.assertEqual(response.status_code,200)

    def test_disabled_user(self):
        response = self.app.put("/edit-password",headers=self.header,data=json.dumps({**user1,**{"new":"Au4gL50$g4$&BUtz/"}}))
        self.assertEqual(response.data,b"username or password invalid!")
        self.assertEqual(response.status_code,401)
        
    def test_invalid_user(self):
        response = self.app.put("/edit-password",headers=self.header,data=json.dumps({**invalid_user,**{"new":"Au4gL50$g4$&BUtz/"}}))
        self.assertEqual(response.data,b"invalid values!")
        self.assertEqual(response.status_code,400)
        
    def test_policy_user(self):
        response = self.app.put("/edit-password",headers=self.header,data=json.dumps({**policy_user,**{"new":"Au4gL50$g4$&BUtz/"}}))
        self.assertEqual(response.data,b"username or password invalid!")
        self.assertEqual(response.status_code,401)
        
    def test_policy_trigger_password(self):
        response = self.app.put("/edit-password",headers=self.header,data=json.dumps({**user2,**{"new":"Au"}}))
        self.assertEqual(response.data,b"new password is invalid!")
        self.assertEqual(response.status_code,400)
        
        
#____________________________________________________________________________
class Test_edit_username(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app.test_client()
        self.header = {"Content-Type":"application/json"}
    
    def test_standard_user2(self):
        response = self.app.put("/edit-username",headers=self.header,data=json.dumps({**user6,**{"new":"AH4§s&b7jn"}}))
        self.assertEqual(response.data,b"successfully edited!")
        self.assertEqual(response.status_code,200)
        
    def test_invalid_user(self):
        response = self.app.put("/edit-username",headers=self.header,data=json.dumps({**invalid_user,**{"new":"AH4§s&b7jn"}}))
        self.assertEqual(response.data,b"invalid values!")
        self.assertEqual(response.status_code,400)
        
    def test_disabled_user(self):
        response = self.app.put("/edit-username",headers=self.header,data=json.dumps({**user1,**{"new":"AH4&b7jn"}}))
        self.assertEqual(response.data,b"not authorized to edit the username!")
        self.assertEqual(response.status_code,401)
    
    def test_policy_user(self):
        response = self.app.put("/edit-username",headers=self.header,data=json.dumps({**policy_user,**{"new":"AH4&b7jn"}}))
        self.assertEqual(response.data,b"not authorized to edit the username!")
        self.assertEqual(response.status_code,401)
        
    def test_policy_trigger_username(self):
        response = self.app.put("/edit-username",headers=self.header,data=json.dumps({**user2,**{"new":"Ag"}}))
        self.assertEqual(response.data,b"username doesn't match with policy!")
        self.assertEqual(response.status_code,400)
        

class Test_admin_enable_user(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app.test_client()
        self.header = {"Content-Type":"application/json"}
    
    def test_standard_user2(self):
        response = self.app.put("/admin/enable-user",headers=self.header,data=json.dumps({**user2,**{"user":user4["username"]}}))
        self.assertEqual(response.data,b"user already enabled!")
        self.assertEqual(response.status_code,200)
    
    def test_admin_change_disabled_admin(self):
        response = self.app.put("/admin/enable-user",headers=self.header,data=json.dumps({**user2,**{"user":user5["username"]}}))
        self.assertEqual(response.data,b"not allowed to enable/disable!")
        self.assertEqual(response.status_code,403)
        
    def test_master_change_disabled_admin(self):
        response = self.app.put("/admin/enable-user",headers=self.header,data=json.dumps({**admin,**{"user":user5["username"]}}))
        self.assertEqual(response.data,b"status changed successfully!")
        self.assertEqual(response.status_code,200)
    
    def test_invalid_user_change_admin(self):
        response = self.app.put("/admin/enable-user",headers=self.header,data=json.dumps({**invalid_user,**{"user":user1["username"]}}))
        self.assertEqual(response.data,b"invalid values!")
        self.assertEqual(response.status_code,400)
    
    def test_user_enable_another(self):
        response = self.app.put("/admin/enable-user",headers=self.header,data=json.dumps({**user3,**{"user":user1["username"]}}))
        self.assertEqual(response.data,b"failed to login,try the path '/login'!")
        self.assertEqual(response.status_code,401)
        
        
        
class Test_disable_user(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app.test_client()
        self.header = {"Content-Type":"application/json"}
        
    def test_admin_change_enabled_admin(self):
        response = self.app.put("/admin/disable-user",headers=self.header,data=json.dumps({**user2,**{"user":user5["username"]}}))
        self.assertEqual(response.data,b"not allowed to enable/disable!")
        self.assertEqual(response.status_code,403)
        
    def test_master_change_enabled_admin(self):
        response = self.app.put("/admin/disable-user",headers=self.header,data=json.dumps({**admin,**{"user":user10["username"]}}))
        self.assertEqual(response.data,b"status changed successfully!")
        self.assertEqual(response.status_code,200)
    
    def test_user_already_disabled(self):
        response = self.app.put("/admin/disable-user",headers=self.header,data=json.dumps({**user2,**{"user":user9["username"]}}))
        self.assertEqual(response.data,b"user already disabled!")
        self.assertEqual(response.status_code,200)
    
    def test_invalid_user_change_admin(self):
        response = self.app.put("/admin/disable-user",headers=self.header,data=json.dumps({**invalid_user,**{"user":user1["username"]}}))
        self.assertEqual(response.data,b"invalid values!")
        self.assertEqual(response.status_code,400)
    
    def test_user_disable_another(self):
        response = self.app.put("/admin/disable-user",headers=self.header,data=json.dumps({**user3,**{"user":user4["username"]}}))
        self.assertEqual(response.data,b"failed to login,try the path '/login'!")
        self.assertEqual(response.status_code,401)
        
        
        
class Test_delete_user(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app.test_client()
        self.header = {"Content-Type":"application/json"}
    
    def test_master_delete_admin(self):
        response = self.app.delete("/admin/delete-user",headers=self.header,data=json.dumps({**admin,**{"user":user8["username"]}}))
        self.assertEqual(response.data,b"user deleted successfully!")
        self.assertEqual(response.status_code,200)
    
    def test_user_already_deleted(self):
        response = self.app.delete("/admin/delete-user",headers=self.header,data=json.dumps({**user2,**{"user":"fdgse"}}))
        self.assertEqual(response.data,b"user doesn't exist!")
        self.assertEqual(response.status_code,200)
    
    def test_invalid_user_delete_admin(self):
        response = self.app.delete("/admin/delete-user",headers=self.header,data=json.dumps({**invalid_user,**{"user":user1["username"]}}))
        self.assertEqual(response.data,b"invalid values!")
        self.assertEqual(response.status_code,400)
    
    def test_user_delete_another(self):
        response = self.app.delete("/admin/delete-user",headers=self.header,data=json.dumps({**user3,**{"user":user2["username"]}}))
        self.assertEqual(response.data,b"failed to login,try the path '/login'!")
        self.assertEqual(response.status_code,401)
    
    
class admin_reset_user_password(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app.test_client()
        self.header = {"Content-Type":"application/json"}
    
    def test_admin_resetting_master(self):
        response = self.app.put("/admin/reset-user",headers=self.header,data=json.dumps({**user2,**{"user":login_admin["username"]}}))
        self.assertEqual(response.status_code,403)
        self.assertEqual(response.data,b"not allowed to reset!")
    
    def test_standard_user2(self):
        response = self.app.put("/admin/reset-user",headers=self.header,data=json.dumps({**admin,**{"user":user9["username"]}}))
        self.assertEqual(response.status_code,200)
    
    def test_invalid_user_resetting_admin(self):
        response = self.app.put("/admin/reset-user",headers=self.header,data=json.dumps({**invalid_user,**{"user":user2["username"]}}))
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.data,b"invalid values!")
        
        
class admin_set_password_policy(unittest.TestCase):
    valid_policy = {"minlength":7,"maxlength":60,"upper":1,"lower":2,"punctuation":1,"numeric":1}
    invalid_policy = {"minlength":7,"maxlength":"60","upper":1,"lower":2,"punctuation":1,"numeric":1}
    logical_wrong_policy = {"minlength":7,"maxlength":5,"upper":1,"lower":2,"punctuation":1,"numeric":1}
    logical_wrong_policy2 = {"minlength":7,"maxlength":60,"upper":1,"lower":2,"punctuation":1,"numeric":5}
    
    def setUp(self) -> None:
        self.app = app.test_client()
        self.header = {"Content-Type":"application/json"}
        
    def test_master_setting_standard_policy(self):
        response = self.app.put("/admin/set-password-policy",headers=self.header,data=json.dumps({**admin,**self.valid_policy}))
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data,b"policy successfully updated!")
        
    def test_master_setting_invalid_policy(self):
        response = self.app.put("/admin/set-password-policy",headers=self.header,data=json.dumps({**admin,**self.invalid_policy}))
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.data,b"invalid values!")
        
    def test_master_setting_logical_wrong_policy1(self):
        response = self.app.put("/admin/set-password-policy",headers=self.header,data=json.dumps({**admin,**self.logical_wrong_policy}))
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.data,b"failed to set password policy, read documentation!")

    def test_master_setting_logical_wrong_policy2(self):
        response = self.app.put("/admin/set-password-policy",headers=self.header,data=json.dumps({**admin,**self.logical_wrong_policy2}))
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.data,b"failed to set password policy, read documentation!")



class admin_set_username_policy(unittest.TestCase):
    valid_policy = {"minlength":4,"maxlength":20,"upper":1,"lower":2,"punctuation":0,"numeric":1}
    invalid_policy = {"minlength":4,"maxlength":"60","upper":1,"lower":2,"punctuation":1,"numeric":1}
    logical_wrong_policy = {"minlength":4,"maxlength":2,"upper":1,"lower":2,"punctuation":1,"numeric":1}
    logical_wrong_policy2 = {"minlength":4,"maxlength":60,"upper":1,"lower":2,"punctuation":1,"numeric":5}
    
    def setUp(self) -> None:
        self.app = app.test_client()
        self.header = {"Content-Type":"application/json"}
        
    
    def test_master_setting_standard_policy(self):
        response = self.app.put("/admin/set-username-policy",headers=self.header,data=json.dumps({**admin,**self.valid_policy}))
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data,b"policy successfully updated!")
        
    def test_master_setting_invalid_policy(self):
        response = self.app.put("/admin/set-username-policy",headers=self.header,data=json.dumps({**admin,**self.invalid_policy}))
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.data,b"invalid values!")
        
    def test_master_setting_logical_wrong_policy1(self):
        response = self.app.put("/admin/set-username-policy",headers=self.header,data=json.dumps({**admin,**self.logical_wrong_policy}))
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.data,b"failed to set username policy, read documentation!")

    def test_master_setting_logical_wrong_policy2(self):
        response = self.app.put("/admin/set-username-policy",headers=self.header,data=json.dumps({**admin,**self.logical_wrong_policy2}))
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.data,b"failed to set username policy, read documentation!")
    


class Test_admin_get_user_data(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app.test_client()
        self.header = {"Content-Type":"application/json"}
    
    def test_get_standard(self):
        response = self.app.get("/admin/get-user-data",headers=self.header,data=json.dumps({**admin,**{"user":user2["username"]}}))
        self.assertEqual(response.status_code,200)
    
    def test_invalid_user_get_admin(self):
        response = self.app.get("/admin/get-user-data",headers=self.header,data=json.dumps({**invalid_user,**{"user":user2["username"]}}))
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.data,b"invalid values!")
    
    def test_policy_trigger_user_get_admin(self):
        response = self.app.get("/admin/get-user-data",headers=self.header,data=json.dumps({**policy_user,**{"user":user2["username"]}}))
        self.assertEqual(response.status_code,401)
        self.assertEqual(response.data,b"failed to login,try the path '/login'!")
    
    
class Test_admin_get_user_count(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app.test_client()
        self.header = {"Content-Type":"application/json"}
    
    def test_get_standard(self):
        response = self.app.get("/admin/get-user-count",headers=self.header,data=json.dumps(admin))
        self.assertEqual(response.status_code,200)
        
    def test_invalid_user_get_admin(self):
        response = self.app.get("/admin/get-user-count",headers=self.header,data=json.dumps(invalid_user))
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.data,b"invalid values!")
    
    def test_policy_trigger_user_get_admin(self):
        response = self.app.get("/admin/get-user-count",headers=self.header,data=json.dumps(policy_user))
        self.assertEqual(response.status_code,401)
        self.assertEqual(response.data,b"failed to login,try the path '/login'!")

        
class Test_get_user_login_history(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app.test_client()
        self.header = {"Content-Type":"application/json"}
    
    def test_get_standard(self):
        response = self.app.get("/admin/get-user-login-history",headers=self.header,data=json.dumps({**admin,**{"user":user2["username"]}}))
        self.assertEqual(response.status_code,200)
    
    def test_invalid_user_get_admin(self):
        response = self.app.get("/admin/get-user-login-history",headers=self.header,data=json.dumps({**invalid_user,**{"user":user2["username"]}}))
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.data,b"invalid values!")
    
    def test_policy_trigger_user_get_admin(self):
        response = self.app.get("/admin/get-user-login-history",headers=self.header,data=json.dumps({**policy_user,**{"user":user2["username"]}}))
        self.assertEqual(response.status_code,401)
        self.assertEqual(response.data,b"failed to login,try the path '/login'!")
    

class Test_get_user_change_history(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app.test_client()
        self.header = {"Content-Type":"application/json"}
    
    def test_get_standard(self):
        response = self.app.get("/admin/get-user-change-history",headers=self.header,data=json.dumps({**admin,**{"user":user2["username"]}}))
        self.assertEqual(response.status_code,200)

    def test_invalid_user_get_admin(self):
        response = self.app.get("/admin/get-user-change-history",headers=self.header,data=json.dumps({**invalid_user,**{"user":user2["username"]}}))
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.data,b"invalid values!")
    
    def test_policy_trigger_user_get_admin(self):
        response = self.app.get("/admin/get-user-change-history",headers=self.header,data=json.dumps({**policy_user,**{"user":user2["username"]}}))
        self.assertEqual(response.status_code,401)
        self.assertEqual(response.data,b"failed to login,try the path '/login'!")
    

if __name__=="__main__":
    unittest.main()

    