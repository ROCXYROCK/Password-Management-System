import requests
import hashlib
import string


def Check_pwned(password:str):
    """
    This is the main function of this module and checks password if it's pwned or not. It communicates with the haveibeenpwned.com through
    the HIBP API, it recieve per HTTP Request a list of hashed passwords which have the same first 5 characters of the given password.
    The script search in this list for the hash of the given password, if this is in the list, the system will return True.
    """
    pwned_list = requests.get("https://api.pwnedpasswords.com/range/"+hashed(password)[:5]).text

    pwned_list = pwned_list.split(":")
    for i in range(1,len(pwned_list)-1):
        cleaning_hash = pwned_list[i].index("\n")+1
        pwned_list[i] = pwned_list[i].lstrip(pwned_list[i][:cleaning_hash])

    pwned_list.pop() # the last item is not in need, so i can remove it

    def hashed(password:str):
        password = password.encode()
        hashed = hashlib.sha1(password).hexdigest()
        hashed = hashed.upper()
        return hashed
    
    if hashed(password)[5:] in pwned_list:
        return False
    return True


Policy_File = os.path.dirname(os.path.realpath(__file__))+"/Data/Policy.json"

#open the policy.json file
with open(Policy_File,"r") as File:
    Req = json.loads(File.read())

def isupper(password:str):
    counter = 0
    for i in password:
        if i.isupper():
            counter +=1
    if counter >= Req["upper"]:
        return True
    return False

def islower(password:str):
    counter = 0
    for i in password:
        if i.islower():
            counter += 1
    if counter >= Req["lower"]:
        return True
    return False

def isnumeric(password:str):
    counter = 0
    for i in password:
        if i.isnumeric():
            counter += 1
    if counter >= Req["numeric"]:
        return True
    return False

def ispunctuation(password:str):
    counter = 0
    for i in password:
        if i == string.punctuation():
            counter += 1
    if counter >= Req["punctuation"]:
        return True
    return False

def length(password:str):
    if len(password) >= Req["length"]:
        return True
    return False


def PSW_Policy(password):
    a = False
    if islower(password):
        a = True

    b = False
    if isupper(password):
        b = True
    
    c = False
    if isnumeric(password):
        c = True
    
    d = False
    if ispunctuation(password):
        d = True
    
    e = False
    if length(password):
        e = True
    
    if a and b and c and d and e:
        return True
    return False