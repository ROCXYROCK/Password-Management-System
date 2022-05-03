import jwt

username = "alo amk"
password= "hahaha"
user={
    "username": username,
    "password": password
}

encoded = jwt.encode(user,"hallowelt")
print(encoded)

decoded = jwt.decode(encoded.decode('ascii'),"hallowelt")
print(decoded)

def Json_load():
    pass


def Json_upload():
    pass


