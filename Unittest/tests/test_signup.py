import json
import pathlib
import unittest
from Application import app

file = pathlib.Path(__file__).parent.parent.joinpath("data")
signup_file = file.joinpath("signup.json").__fspath__()


with open(signup_file, "r") as f:
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

############test preparation#############
app = app.test_client()
header = {"Content-Type": "application/json"}

#############responses###################
CREATED = b"created successfully!"

# ______________________________________test class_____________________________________________


class SignupTest(unittest.TestCase):

    def setUp(self):
        self.path = "/signup"

    def test_create_user1(self):
        response = app.post(self.path, headers=header,
                            data=json.dumps({**admin, **user1}))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, CREATED)

    def test_create_user2(self):
        response = app.post(self.path, headers=header,
                            data=json.dumps({**admin, **user2}))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, CREATED)

    def test_create_user3(self):
        response = app.post(self.path, headers=header,
                            data=json.dumps({**admin, **user3}))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, CREATED)

    def test_create_user4(self):
        response = app.post(self.path, headers=header,
                            data=json.dumps({**admin, **user4}))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, CREATED)

    def test_create_user5(self):
        response = app.post(self.path, headers=header,
                            data=json.dumps({**admin, **user5}))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, CREATED)

    def test_create_user6(self):
        response = app.post(self.path, headers=header,
                            data=json.dumps({**admin, **user6}))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, CREATED)

    def test_create_user7(self):
        response = app.post(self.path, headers=header,
                            data=json.dumps({**admin, **user7}))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, CREATED)

    def test_create_user8(self):
        response = app.post(self.path, headers=header,
                            data=json.dumps({**admin, **user8}))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, CREATED)

    def test_create_user9(self):
        response = app.post(self.path, headers=header,
                            data=json.dumps({**admin, **user9}))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, CREATED)

    def test_create_user10(self):
        response = app.post(self.path, headers=header,
                            data=json.dumps({**admin, **user10}))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, CREATED)

    def test_create_invalid_user(self):
        response = app.post(self.path, headers=header,
                            data=json.dumps({**{"admin_username": invalid_user["username"],
                                                "admin_password": invalid_user["password"]}, **user1}))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, b"invalid values!")

    def test_create_policy_trigger_user(self):
        response = app.post(self.path, headers=header,
                            data=json.dumps({**admin, **policy_user}))
        self.assertEqual(
            response.data, b"invalid password or username, read documentation!")


if __name__ == "__main__":
    unittest.main()
