from flask import Flask, make_response,request, redirect, url_for,session# to set session id for 30 min.
from Packages import file,password,Encryption
import pathlib,datetime


# session["user"]=user with this u make a session for a user which u can delete after logging out, u need for it a secret key because all the data of session is saved on the server
# return redirect (url_for("path like 'logout'")) with this u direct the user to another path. 
#os.path.dirname(os.path.realpath(__file__))# it gives you the current file path


App = Flask(__name__)
App.secret_key="aaaaaaaaaa"


@App.route("/register",methods=["POST"])
def register():
    Data_input = request.get_json()
    
    username = Data_input.get("username","")
    pw = Data_input.get("password","")
    hashed = Encryption.SHA1(pw).upper()
    secure_pw_hash = Encryption.hash_psw(pw)
    status = Data_input.get("status",False)
    admin  = Data_input.get("admin",False)
    last_log = str(datetime.datetime.utcnow())
    last_change = str(datetime.datetime.utcnow())
    
    #look if user exists
    if file.get_user(username):
        return  make_response("user exists already!",405)
    
    user = {username:{"password":secure_pw_hash,"enabled":status,"admin":admin,"last_log":last_log,"last_changed":last_change}}
    
    # if password doesn't match policy or is pwned
    if not password.check(pw,hashed):
        return make_response("password invalid!",406)
    
    #if user is registered
    if file.set_user(user):
        return redirect(url_for("login"),201)
    return make_response("bad request!",400)

@App.route("/login",methods=["GET"])
def login():
    
    Data_input = request.get_json()
    username = Data_input.get("username","")
    pw = Data_input.get("password","")
    pw_sha1 = Encryption.SHA1(pw).upper()
    
    user = file.get_user(username)
    if user != False:
        user_hash = user["password"]
        if Encryption.PSW_Check(pw,user_hash) and password.pwned(pw_sha1):
            return make_response("accepted!",202)
    return make_response("unauthorized!",401)

if __name__=="__main__":
    App.run(debug=True,port=1337)

