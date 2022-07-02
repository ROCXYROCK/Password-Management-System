import json
import pathlib
import unittest
from Packages.Encryption import hash_to_sha1, hash_to_bcrypt, password_hash_check

# get the path of the encryption test file
file = pathlib.Path(__file__).parent.parent.joinpath("data")
encryption_file = file.joinpath("encryption.json").__fspath__()

# read the encryption test file
with open(encryption_file, "r") as f:
    data = json.loads(f.read())
    f.close()

# _______________________________________encryption test file__________________________________
password = data["password"]
invalid_password = data["invalid_password"]
valid_bcrypt = data["valid_bcrypt"]
invalid_bcrypt = data["invalid_bcrypt"]
valid_sha1 = data["valid_sha1"]
invalid_sha1 = data["invalid_sha1"]

# ________________________________________test classes____________________________________________


class VerifyBcryptTest(unittest.TestCase):
    def test_valid_password_valid_bcrypt(self):
        response = password_hash_check(password=password, hashed=valid_bcrypt)
        self.assertTrue(response)

    def test_invalid_password_valid_bcrypt(self):
        response = password_hash_check(
            password=invalid_password, hashed=valid_bcrypt)
        self.assertFalse(response)

    def test_valid_password_invalid_bcrypt(self):
        response = password_hash_check(
            password=password, hashed=invalid_bcrypt)
        self.assertFalse(response)

    def test_int_password_valid_bcrypt(self):
        response = password_hash_check(password=2, hashed=valid_bcrypt)
        self.assertFalse(response)
        self.assertRaises(TypeError, response)

    def test_raise_password_size_error(self):
        response = password_hash_check(
            password=(4999*"g"), hashed=valid_bcrypt)
        self.assertFalse(response)


class HashToBcrypt(unittest.TestCase):
    def test_valid_hashing(self):
        response = hash_to_bcrypt(password=password)
        self.assertTrue(response)

    def test_raise_password_size_error(self):
        response = hash_to_bcrypt(password=4999*"g")
        self.assertFalse(response)

    def test_raising_type_error(self):
        response = hash_to_bcrypt(password=2)
        self.assertRaises(TypeError, response)
        self.assertFalse(response)


class HashToSha1(unittest.TestCase):
    def test_valid_hashing(self):
        response = hash_to_sha1(password=password)
        self.assertEqual(response, valid_sha1)

    def test_invalid_hashing(self):
        response = hash_to_sha1(password=invalid_password)
        self.assertNotEqual(response, valid_sha1)

    def test_raising_type_error(self):
        response = hash_to_sha1(password=2)
        self.assertRaises(TypeError, response)
        self.assertFalse(response)


if __name__ == "__main__":
    unittest.main()
