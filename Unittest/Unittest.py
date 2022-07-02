# https://dev.to/paurakhsharma/flask-rest-api-part-6-testing-rest-apis-4lla
import unittest
import json
import sys
import pathlib

# adding the /passowrd-management-system to the python path
pms = pathlib.Path(__file__).parent.parent.__fspath__()
sys.path.append(pms)

# the password-management-system folder should be added to path before calling this modules
import tests.test_app as app
import tests.test_signup as signup
import tests.test_encryption as encryption

#############################application files###########################
file = pathlib.Path(__file__).parent.parent
data_file = file.joinpath("Data", "Data.json").__fspath__()
secret_file = file.joinpath("Data", "secret.json").__fspath__()
history_file = file.joinpath("Data", "history.json").__fspath__()
policy_file = file.joinpath("Data", "Policy.json").__fspath__()


# reading application files
def read_data():
    with open(data_file, "r") as f:
        data = json.loads(f.read())

    with open(secret_file, "r") as f:
        secret = json.loads(f.read())

    with open(policy_file, "r") as f:
        policy = json.loads(f.read())

    with open(history_file, "r") as f:
        history = json.loads(f.read())

    return data, secret, policy, history

# writing data in application files


def write_data(data, secret, policy, history):
    with open(data_file, "w") as f:
        json.dump(data, f, indent=2)

    with open(secret_file, "w") as f:
        json.dump(secret, f, indent=2)

    with open(policy_file, "w") as f:
        json.dump(policy, f, indent=2)

    with open(history_file, "w") as f:
        json.dump(history, f, indent=2)


def run_tests():
    # load signup test file and run it
    suite = unittest.TestLoader().loadTestsFromModule(signup)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # load app test file and run it
    suite = unittest.TestLoader().loadTestsFromModule(app)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # load encryption test file and run it
    suite = unittest.TestLoader().loadTestsFromModule(encryption)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    # read data
    data, secret, policy, history = read_data()
    # run tests
    run_tests()
    # write the read data again
    write_data(data=data, secret=secret, policy=policy, history=history)
