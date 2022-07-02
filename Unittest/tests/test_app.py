import pathlib
import json
import unittest
from Application import app

###################login test file path#####################
file = pathlib.Path(__file__).parent.parent.joinpath("data")
login_file = file.joinpath("login.json").__fspath__()

##################get login test data########################
with open(login_file, "r") as f:
    data = json.loads(f.read())
    f.close()


################## divide data into variables#################
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
login_admin = {"username": "Amino1", "password": "h]XN^3+R8"}


###############testing app variables###############
app = app.test_client()
header = {"Content-Type": "application/json"}

################responses################
USER_DOESNT_EXIST = b"User is not in the database, please enter an existing user!"
INVALID_VALUES = b"invalid values!"
NO_MASTER_PRIVELEGES = b'Admin has no master privileges!'
GO_TO_LOGIN = b'go to login to check your account!'


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.path = '/login'

    def test_login_user2(self):
        response = app.get(self.path, headers=header, data=json.dumps(user2))
        self.assertEqual(200, response.status_code)

    def test_login_user1(self):
        response = app.get(self.path, headers=header, data=json.dumps(user1))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(USER_DOESNT_EXIST, response.data)

    def test_Type_Error(self):
        response = app.get(self.path, headers=header,
                           data=json.dumps(invalid_user))
        self.assertEqual(400, response.status_code)
        self.assertEqual(INVALID_VALUES, response.data)

    def test_wronge_method(self):
        response = app.post(self.path, headers=header, data=login_admin)
        self.assertEqual(405, response.status_code)


class TestGeneratePassword(unittest.TestCase):

    def setUp(self):
        self.path = '/generate-password'

    def test_standard_user2(self):
        response = app.get(self.path, headers=header,
                           data=json.dumps({**user2, **{"length": 15}}))
        self.assertEqual(response.status_code, 200)

    def test_disabled_user(self):
        response = app.get(self.path, headers=header,
                           data=json.dumps({**user1, **{"length": 15}}))
        self.assertEqual(response.data, USER_DOESNT_EXIST)
        self.assertEqual(response.status_code, 401)

    def test_policy_trigger(self):
        response = app.get(self.path, headers=header, data=json.dumps(
            {**user2, **{"length": 10000000}}))
        self.assertEqual(response.data, b"length doesn't match policy!")
        self.assertEqual(response.status_code, 403)

    def test_invalid_Type(self):
        response = app.get(self.path, headers=header,
                           data=json.dumps({**user2, **{"length": "10"}}))
        self.assertEqual(response.data, INVALID_VALUES)
        self.assertEqual(response.status_code, 400)


class TestEditPassword(unittest.TestCase):
    def setUp(self):
        self.path = "/edit-password"

    def test_standard_user2(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**user7, **{"new": "Au4gL50$g4$&BUtz/"}}))
        self.assertEqual(response.data, b"successfully edited!")
        self.assertEqual(response.status_code, 200)

    def test_disabled_user(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**user1, **{"new": "Au4gL50$g4$BUtz/"}}))
        self.assertEqual(response.data, USER_DOESNT_EXIST)
        self.assertEqual(response.status_code, 401)

    def test_invalid_user(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**invalid_user, **{"new": "Au4gL504$&BUtz/"}}))
        self.assertEqual(response.data, INVALID_VALUES)
        self.assertEqual(response.status_code, 400)

    def test_policy_user(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**policy_user, **{"new": "Au4gL50$g4$&BUtz/"}}))
        self.assertEqual(response.data, USER_DOESNT_EXIST)
        self.assertEqual(response.status_code, 401)

    def test_policy_trigger_password(self):
        response = app.put(self.path, headers=header,
                           data=json.dumps({**user2, **{"new": "Au"}}))
        self.assertEqual(
            response.data, b'Password is not valid any more, change it!')
        self.assertEqual(response.status_code, 403)


# ____________________________________________________________________________
class TestEditUsername(unittest.TestCase):
    def setUp(self) -> None:
        self.path = "/edit-username"

    def test_standard_user2(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**user6, **{"new": "AH4§s&b7jn"}}))
        self.assertEqual(response.data, b"successfully edited!")
        self.assertEqual(response.status_code, 200)

    def test_invalid_user(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**invalid_user, **{"new": "AH4§s&b7jn"}}))
        self.assertEqual(response.data, INVALID_VALUES)
        self.assertEqual(response.status_code, 400)

    def test_disabled_user(self):
        response = app.put(self.path, headers=header,
                           data=json.dumps({**user1, **{"new": "AH4&b7jn"}}))
        self.assertEqual(response.data, USER_DOESNT_EXIST)
        self.assertEqual(response.status_code, 401)

    def test_policy_user(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**policy_user, **{"new": "AH4&b7jn"}}))
        self.assertEqual(response.data, USER_DOESNT_EXIST)
        self.assertEqual(response.status_code, 401)

    def test_policy_trigger_username(self):
        response = app.put(self.path, headers=header,
                           data=json.dumps({**user2, **{"new": "Ag"}}))
        self.assertEqual(
            response.data, b"Username doesn't match with policy, change it!")
        self.assertEqual(response.status_code, 403)


class TestAdminEnableUser(unittest.TestCase):
    def setUp(self) -> None:
        self.path = "/admin/enable-user"

    def test_standard_user2(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**user2, **{"user": user4["username"]}}))
        self.assertEqual(response.data, b"user already enabled!")
        self.assertEqual(response.status_code, 200)

    def test_admin_change_disabled_admin(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**user2, **{"user": user5["username"]}}))
        self.assertEqual(response.data, NO_MASTER_PRIVELEGES)
        self.assertEqual(response.status_code, 405)

    def test_master_change_disabled_admin(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**admin, **{"user": user5["username"]}}))
        self.assertEqual(response.data, b"status changed successfully!")
        self.assertEqual(response.status_code, 200)

    def test_invalid_user_change_admin(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**invalid_user, **{"user": user1["username"]}}))
        self.assertEqual(response.data, INVALID_VALUES)
        self.assertEqual(response.status_code, 400)

    def test_user_enable_another(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**user3, **{"user": user1["username"]}}))
        self.assertEqual(response.data, GO_TO_LOGIN)
        self.assertEqual(response.status_code, 403)


class TestAdminDisableUser(unittest.TestCase):
    def setUp(self) -> None:
        self.path = "/admin/disable-user"

    def test_admin_change_enabled_admin(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**user2, **{"user": user5["username"]}}))
        self.assertEqual(response.data, NO_MASTER_PRIVELEGES)
        self.assertEqual(response.status_code, 405)

    def test_master_change_enabled_admin(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**admin, **{"user": user10["username"]}}))
        self.assertEqual(response.data, b"status changed successfully!")
        self.assertEqual(response.status_code, 200)

    def test_user_already_disabled(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**user2, **{"user": user9["username"]}}))
        self.assertEqual(response.data, b"user already disabled!")
        self.assertEqual(response.status_code, 200)

    def test_invalid_user_change_admin(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**invalid_user, **{"user": user1["username"]}}))
        self.assertEqual(response.data, INVALID_VALUES)
        self.assertEqual(response.status_code, 400)

    def test_user_disable_another(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**user3, **{"user": user4["username"]}}))
        self.assertEqual(response.data, GO_TO_LOGIN)
        self.assertEqual(response.status_code, 403)


class TestAdminDeleteUser(unittest.TestCase):
    def setUp(self) -> None:
        self.path = "/admin/delete-user"

    def test_master_delete_admin(self):
        response = app.delete(self.path, headers=header, data=json.dumps(
            {**admin, **{"user": user8["username"]}}))
        self.assertEqual(response.data, b"user deleted successfully!")
        self.assertEqual(response.status_code, 200)

    def test__delete_already_deleted_user(self):
        response = app.delete(self.path, headers=header,
                              data=json.dumps({**user2, **{"user": "fdgse"}}))
        self.assertEqual(response.data, USER_DOESNT_EXIST)
        self.assertEqual(response.status_code, 401)

    def test_invalid_user_delete_admin(self):
        response = app.delete(self.path, headers=header, data=json.dumps(
            {**invalid_user, **{"user": user1["username"]}}))
        self.assertEqual(response.data, INVALID_VALUES)
        self.assertEqual(response.status_code, 400)

    def test_user_delete_another(self):
        response = app.delete(self.path, headers=header, data=json.dumps(
            {**user3, **{"user": user2["username"]}}))
        self.assertEqual(response.data, GO_TO_LOGIN)
        self.assertEqual(response.status_code, 403)


class AdminResetUserPassword(unittest.TestCase):
    def setUp(self) -> None:
        self.path = "/admin/reset-user"

    def test_admin_resetting_master(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**user2, **{"user": login_admin["username"]}}))
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.data, NO_MASTER_PRIVELEGES)

    def test_standard_user2(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**admin, **{"user": user9["username"]}}))
        self.assertEqual(response.status_code, 200)

    def test_invalid_user_resetting_admin(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**invalid_user, **{"user": user2["username"]}}))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, INVALID_VALUES)


class AdminSetPasswordPolicy(unittest.TestCase):

    def setUp(self):
        self.valid_policy = {"minlength": 7, "maxlength": 60,
                             "upper": 1, "lower": 2, "punctuation": 1, "numeric": 1}
        self.invalid_policy = {"minlength": 7, "maxlength": "60",
                               "upper": 1, "lower": 2, "punctuation": 1, "numeric": 1}
        self.logical_wrong_policy = {"minlength": 7, "maxlength": 5,
                                     "upper": 1, "lower": 2, "punctuation": 1, "numeric": 1}
        self.logical_wrong_policy2 = {
            "minlength": 7, "maxlength": 60, "upper": 1, "lower": 2, "punctuation": 1, "numeric": 5}
        self.path = "/admin/set-password-policy"

    def test_master_setting_standard_policy(self):
        response = app.put(self.path, headers=header,
                           data=json.dumps({**admin, **self.valid_policy}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"policy successfully updated!")

    def test_master_setting_invalid_policy(self):
        response = app.put(self.path, headers=header,
                           data=json.dumps({**admin, **self.invalid_policy}))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, INVALID_VALUES)

    def test_master_setting_logical_wrong_policy1(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**admin, **self.logical_wrong_policy}))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data, b'password policy is not valid, try again!')

    def test_master_setting_logical_wrong_policy2(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**admin, **self.logical_wrong_policy2}))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data, b'password policy is not valid, try again!')


class AdminSetUsernamePolicy(unittest.TestCase):

    def setUp(self) -> None:
        self.valid_policy = {"minlength": 4, "maxlength": 20,
                             "upper": 1, "lower": 2, "punctuation": 0, "numeric": 1}
        self.invalid_policy = {"minlength": 4, "maxlength": "60",
                               "upper": 1, "lower": 2, "punctuation": 1, "numeric": 1}
        self.logical_wrong_policy = {"minlength": 4, "maxlength": 2,
                                     "upper": 1, "lower": 2, "punctuation": 1, "numeric": 1}
        self.logical_wrong_policy2 = {
            "minlength": 4, "maxlength": 60, "upper": 1, "lower": 2, "punctuation": 1, "numeric": 5}
        self.path = "/admin/set-username-policy"

    def test_master_setting_standard_policy(self):
        response = app.put(self.path, headers=header,
                           data=json.dumps({**admin, **self.valid_policy}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"policy successfully updated!")

    def test_master_setting_invalid_policy(self):
        response = app.put(self.path, headers=header,
                           data=json.dumps({**admin, **self.invalid_policy}))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, INVALID_VALUES)

    def test_master_setting_logical_wrong_policy1(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**admin, **self.logical_wrong_policy}))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data, b'username policy is not valid, try again!')

    def test_master_setting_logical_wrong_policy2(self):
        response = app.put(self.path, headers=header, data=json.dumps(
            {**admin, **self.logical_wrong_policy2}))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data, b'username policy is not valid, try again!')


class TestAdminGetUserData(unittest.TestCase):
    def setUp(self) -> None:
        self.path = "/admin/get-user-data"

    def test_get_standard(self):
        response = app.get(self.path, headers=header, data=json.dumps(
            {**admin, **{"user": user2["username"]}}))
        self.assertEqual(response.status_code, 200)

    def test_invalid_user_get_admin(self):
        response = app.get(self.path, headers=header, data=json.dumps(
            {**invalid_user, **{"user": user2["username"]}}))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, INVALID_VALUES)

    def test_policy_trigger_user_get_admin(self):
        response = app.get(self.path, headers=header, data=json.dumps(
            {**policy_user, **{"user": user2["username"]}}))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, USER_DOESNT_EXIST)


class TestAdminGetUserCount(unittest.TestCase):
    def setUp(self) -> None:
        self.path = "/admin/get-user-count"

    def test_get_standard(self):
        response = app.get(self.path, headers=header, data=json.dumps(admin))
        self.assertEqual(response.status_code, 200)

    def test_invalid_user_get_admin(self):
        response = app.get(self.path, headers=header,
                           data=json.dumps(invalid_user))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, INVALID_VALUES)

    def test_policy_trigger_user_get_admin(self):
        response = app.get(self.path, headers=header,
                           data=json.dumps(policy_user))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, USER_DOESNT_EXIST)


class TestGetUserLoginHistory(unittest.TestCase):
    def setUp(self) -> None:
        self.path = "/admin/get-login-history"

    def test_get_standard(self):
        response = app.get(self.path, headers=header, data=json.dumps(
            {**admin, **{"user": user2["username"]}}))
        self.assertEqual(response.status_code, 200)

    def test_invalid_user_get_admin(self):
        response = app.get(self.path, headers=header, data=json.dumps(
            {**invalid_user, **{"user": user2["username"]}}))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, INVALID_VALUES)

    def test_policy_trigger_user_get_admin(self):
        response = app.get(self.path, headers=header, data=json.dumps(
            {**policy_user, **{"user": user2["username"]}}))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, USER_DOESNT_EXIST)


class TestGetUserChangeHistory(unittest.TestCase):

    def setUp(self) -> None:
        self.path = "/admin/get-change-history"

    def test_get_standard(self):
        response = app.get(self.path, headers=header, data=json.dumps(
            {**admin, **{"user": user2["username"]}}))
        self.assertEqual(response.status_code, 200)

    def test_invalid_user_get_admin(self):
        response = app.get(self.path, headers=header, data=json.dumps(
            {**invalid_user, **{"user": user2["username"]}}))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, INVALID_VALUES)

    def test_policy_trigger_user_get_admin(self):
        response = app.get(self.path, headers=header, data=json.dumps(
            {**policy_user, **{"user": user2["username"]}}))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, USER_DOESNT_EXIST)


if __name__ == "__main__":
    unittest.main()
