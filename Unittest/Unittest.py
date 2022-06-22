#https://dev.to/paurakhsharma/flask-rest-api-part-6-testing-rest-apis-4lla
import sys,os,json
import unittest

file = os.path.dirname(os.path.realpath(__file__))+"/../"
file1 = os.path.dirname(os.path.realpath(__file__))+"/tests/"
files_test = os.path.dirname(os.path.realpath(__file__))+"/data"

sys.path.append(file)
sys.path.append(file1)

import Test_Application,Test_Creating_users

def read_test_data():
    with open(files_test+"/Data.json","r") as f:
        data_file = json.loads(f.read())
        f.close()

    with open(files_test+"/secret.json","r") as f:
        secret_file = json.loads(f.read())
        f.close()
        
    with open(files_test+"/Policy.json","r") as f:
        policy_file = json.loads(f.read())
        f.close()

    with open(files_test+"/history.json","r") as f:
        history_file = json.loads(f.read())
        f.close()
        
    return data_file,secret_file,policy_file,history_file


def read_data():
    with open(file+"/Data/Data.json","r") as f:
        data_file = json.loads(f.read())
        f.close()

    with open(file+"/Data/secret.json","r") as f:
        secret_file = json.loads(f.read())
        f.close()
        
    with open(file+"/Data/Policy.json","r") as f:
        policy_file = json.loads(f.read())
        f.close()

    with open(file+"/Data/history.json","r") as f:
        history_file = json.loads(f.read())
        f.close()
        
    return data_file,secret_file,policy_file,history_file



def write_data(data_file,secret_file,policy_file,history_file):
    with open(file+"/Data/Data.json","w") as f:
        json.dump(data_file,f,indent=2)
        f.close()

    with open(file+"/Data/secret.json","w") as f:
        json.dump(secret_file,f,indent=2)
        f.close()
        
    with open(file+"/Data/Policy.json","w") as f:
        json.dump(policy_file,f,indent=2)
        f.close()

    with open(file+"/Data/history.json","w") as f:
        json.dump(history_file,f,indent=2)
        f.close()   
        
def run_tests():
    suite = unittest.TestLoader().loadTestsFromModule(Test_Creating_users)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
    suite = unittest.TestLoader().loadTestsFromModule(Test_Application)
    unittest.TextTestRunner(verbosity=2).run(suite)



if __name__=="__main__":
    
    data,secret,policy,history=read_data()
    
    run_tests()
    
    write_data(data_file=data,secret_file=secret,policy_file=policy,history_file=history)