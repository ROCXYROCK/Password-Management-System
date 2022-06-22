import sys,os,json,unittest

file = os.path.dirname(os.path.realpath(__file__))+"/../../"
sys.path.append(file)

from Application import app
with open(file + "Unittest/data/signup_users.json","r") as f:
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

print({**admin,**user1})
class SignupTest(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.header = {"Content-Type":"application/json"}
        
    def test_create_user1(self):
        response = self.app.post("/signup",headers=self.header,data=json.dumps({**admin,**user1}))
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.data,b"created successfully!")
        
        
    def test_create_user2(self):
        response = self.app.post("/signup",headers=self.header,data=json.dumps({**admin,**user2}))
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.data,b"created successfully!")
        
        
    def test_create_user3(self):
        response = self.app.post("/signup",headers=self.header,data=json.dumps({**admin,**user3}))
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.data,b"created successfully!")
        
    
    def test_create_user4(self):
        response = self.app.post("/signup",headers=self.header,data=json.dumps({**admin,**user4}))
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.data,b"created successfully!")
        
    def test_create_user5(self):
        response = self.app.post("/signup",headers=self.header,data=json.dumps({**admin,**user5}))
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.data,b"created successfully!")
    
    def test_create_user6(self):
        response = self.app.post("/signup",headers=self.header,data=json.dumps({**admin,**user6}))
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.data,b"created successfully!")
        
    def test_create_user7(self):
        response = self.app.post("/signup",headers=self.header,data=json.dumps({**admin,**user7}))
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.data,b"created successfully!")
    
    def test_create_user8(self):
        response = self.app.post("/signup",headers=self.header,data=json.dumps({**admin,**user8}))
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.data,b"created successfully!")
    
    def test_create_user9(self):
        response = self.app.post("/signup",headers=self.header,data=json.dumps({**admin,**user9}))
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.data,b"created successfully!")
    
    def test_create_user10(self):
        response = self.app.post("/signup",headers=self.header,data=json.dumps({**admin,**user10}))
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.data,b"created successfully!")
    
    def test_create_invalid_user(self):
        response = self.app.post("/signup",headers=self.header,
                                data=json.dumps({**{"admin_username":invalid_user["username"],
                                                    "admin_password":invalid_user["password"]},**user1}))
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.data,b"invalid values!")
    
    
    def test_create_policy_user(self):
        response = self.app.post("/signup",headers=self.header,data=json.dumps({**admin,**policy_user}))
        self.assertEqual(response.data,b"invalid password or username, read documentation!")
        
if __name__=="__main__":
    unittest.main()