from flask import Flask, make_response,request, redirect, url_for
import File

app = Flask(__name__)

# @App.route("/register",methods=["POST"])
# def register():
#     Data_input = request.get_json()
    
#     username = Data_input.get("username","")
#     pw = Data_input.get("password","")
#     status = Data_input.get("status",False)
#     admin  = Data_input.get("admin",False)


@app.route("/login",methods=["GET"])
def login():
    try:
        Data = request.get_json()

        username = Data.get("username")
        password = Data.get("password")

        if type(password) != str or type(username) != str:#instances
            raise ValueError

        check = File.login({"username":username,"password":password})

        if not check:
            return make_response("user doesn't exist",401)
        
        if check == "change":
            return make_response("outdated, change it!",403)

        if check == True:
            return make_response("authenticated",202)

    except ValueError:
        return make_response("invalid Values",400)
    except:
        return make_response("bad request!",400)
    
    
# @App.route("/generator",methods=["GET"])
# def generate_password():
#     try:  
#         Data = request.get_json()
#         length = int(Data.get("length"))
        
#         a = True
#         while a:
#             pw = generator.generate(length)
#             hashed = Encryption.SHA1(pw).upper()
            
#             if password.check(pw,hashed):
#                 a = False  
#         return make_response(pw,201) 
#     except:
#         return make_response("JSON structure is required!",400)

# @App.route("/admin/user-status",methods=["PUT"])
# def status_user():
#     try:
#         Data = request.get_json()
#         username = Data.get("username")
#         pw = Data.get("password")
#         user_to_change = Data.get("user")
#         status = Data.get("status")
        
#         user = flogin(username,pw)
#         if user:
#             userdata = file.get_user(user_to_change)
#             if userdata:
#                 userdata["enabled"] = status
#                 try:
#                     file.set_user({user_to_change:userdata})
#                     return make_response("status changed!")
#                 except:
#                     return make_response("something went wrong!",409)        
#             return make_response("user doesn't exists in Database!",404)
#     except:
#         return make_response("check your reqest!",400)

# @App.route("/user/editpassword",methods=["PUT"])
# def edit_pw():
#     try:
#         Data = request.get_json()
#         username = Data.get("username")
#         pw = Data.get("password")
#         new_pw = Data.get("newpassword")
#         hashed = Encryption.SHA1(new_pw).upper()
#         secure_pw_hash = Encryption.hash_psw(new_pw)
        
#         user = flogin(username,pw)
#         if not user:
#             return make_response("username or password invalid!",401)
#         if password.check(new_pw,hashed):
#             user["password"] = secure_pw_hash
#             file.set_user({username:user})
#             return make_response("password edited!",202)
#     except:
#         return make_response("JSON Structure is required!",400)

# #check types for every parameter you get and create a class user
# @App.route("/admin/set-policy",methods=["POST"])
# def set_policy():
#     try:
#         Data = request.get_json()
#         username = Data.get("username")
#         pw = Data.get("password")
#         policy = Data.get("policy")
#         req = ["length","upper","lower","punctuation","numeric"]
        
#         if not file.check_user_type({"username":username,"password":pw},["username","password"]):
#             return make_response("user values need to be str")
        
#         if not (flogin(username,pw) and file.check_admin(username) and file.check_enabled(username)):
#             return make_response("not authorized!",401)
        
#         if not file.check_policy(policy,req): 
#             return make_response("invalid requirements",400)
        
#         if not file.check_policy_type(policy,req):
#             return make_response("values needs to be int",400)
        
#         policy["lastchange"] = str(datetime.datetime.utcnow())
        
#         if not file.set_policy(policy):
#             return make_response("failed setting policy!",404)
        
#         return make_response("successfuly created!",201)    
        
#     except:
#         return make_response("JSON required!",400)


# @App.route("/admin/edit-policy",methods=["PUT"])
# def edit_policy():
#     try:
#         Data = request.get_json()
#         username = Data.get("username")
#         pw = Data.get("password")
#         policy = Data.get("policy")
        
        
#         if not file.check_user_type({"username":username,"password":password},["username","password"]):
#             return make_response("invalid userdata!",400)
        
#         if not file.check_policy_type(policy,policy.keys()):
#             return make_response("invalid policy type!")
        
#         if not (flogin(username,pw) and file.check_admin(username) and file.check_enabled(username)):
#             return make_response("invalid user!",401)
        
#         if not file.check_policy_file(policy):
#             return make_response("invalid Policy",404)
        
#         if not file.edit_policy(policy.keys(),policy.values()):
#             return make_response("couldn't write policy in file",404)
        
#         return make_response("successfuly edited!",200)
#     except:
#         make_response("JSON required!",400)

# #look like the first if, if u can übergeben data and the list, instead to give the whole dict written. 
# #user should not take any password from history
# #if user have an insecure password he should change it
# @App.route("/admin/reset")
# def reset_pw():
#     try:
#         Data = request.get_json()
#         username = Data.get("username")
#         pw = Data.get("password")
#         to_change_user = Data.get("user")
#         new_pw = generator.generate(10)
#         new_hash = Encryption.hash_psw(new_pw) 
        
        
#         if not file.check_user_type(Data,["username","password","user"]):
#             return make_response("invalid data type!",400)
        
#         if not (flogin(username,pw) and file.check_admin(username) and file.check_enabled(username)):
#             return make_response("invalid user!",401)
        
#         if not file.get_user(to_change_user):
#             return make_response("user dosn't exist!")
        
#         if not file.reset_password(to_change_user,new_hash):
#             return make_response("cannot reset password!",404)
        
#         if not file.edit_lastchange(to_change_user,"r"):
#             return make_response (f"cannot force to change! {new_pw}",401)
        
#         return make_response(f"password: {new_pw} | successfully resetted!",200)
        
#     except:
#         return make_response("JSON required!",400)
    
    
    


if __name__=="__main__":
    app.run(debug=True,port=1337)

