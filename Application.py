import sys,os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/Packages")

from flask import Flask,make_response,request
import Help


app = Flask(__name__)

@app.route("/signup",methods=["POST"])
def register():
    try:
        data = request.get_json()
    
        admin_username = data.get("admin_username")
        admin_password = data.get("admin_password")
        username = data.get("username")
        password = data.get("password")
        status = data.get("status")
        admin  = data.get("admin")
        
        list_of_str = [admin_username,admin_password,username,password]
        list_of_bool = [status,admin]
        
        for i in list_of_str:
            if not isinstance(i,str):
                return make_response("invalid values",400)
        
        for i in list_of_bool:
            if not isinstance(i,bool):
                return make_response("invalid values",400)
        
        response = Help.admin_signup_user(admin={"username":admin_username,"password":admin_password},
                                          user={"username":username,"password":password,"enabled":status,"admin":admin})
        response = response.split(":")
        
        return make_response(response[0],response[1])
    except:
        return make_response("read the cheatsheet!",400)
        
    

@app.route("/login",methods=["GET"])
def login():
    try:
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        if not isinstance(username,str) or not isinstance(password,str):
            raise ValueError

        check = Help.user_login(user={"username":username,"password":password})

        if not check:
            return make_response("user doesn't exist",401)
        
        if check == "change":
            return make_response("outdated! go to '/editpassword'",403)

        if check == True:
            return make_response("authenticated",202)

    except ValueError:
        return make_response("invalid values",400)
    except:
        return make_response("read the cheatsheet!",400)
    
@app.route("/generate-password",methods=["GET"])
def user_generate_password():
    try:
        data = request.get_json()
        
        username = data.get("username")
        password = data.get("password")
        length = data.get("length")
        
        if not isinstance(username,str) or not isinstance(password,str) or not isinstance(length,int):
            return make_response("invalid values", 400)
        
        response = Help.user_generate_password(user={"username":username,"password":password},length=length)
        
        response = response.split(":")
        return make_response(response[0],response[1])
        
    except:
        return make_response("read the cheatsheet!",400)

@app.route("/edit-password",methods=["PUT"])
def edit_password():
    try:
        data = request.get_json()
        
        username = data.get("username")
        password = data.get("password")
        new_password = data.get("new")
        
        list_of_str = [username,password,new_password]
        
        for i in list_of_str:
            if not isinstance(i,str):
                return make_response("invalid values",400)
        
        response = Help.edit_password(
            user={"username":username,"password":password,"newpassword":new_password})
        response = response.split(":")
        
        return make_response(response[0],response[1])
    except:
        return make_response("read the cheatsheet!",400)

@app.route("/admin/enable-user",methods=["PUT"])
def enable_user():
    try:
        data = request.get_json()
        
        username = data.get("username")
        password =  data.get("password")
        user = data.get("user")
        
        list_of_str = [username,password,user]
        for i in list_of_str:
            if not isinstance(i,str):
                return make_response("invalid values",400)
        
        response = Help.admin_enable_disable_user(admin={"username":username,"password":password},
                                                  username=user,state=True)
        response = response.split(":")
        return make_response(response[0],response[1])
           
    except:
        return make_response("read the cheatsheet!",400)


@app.route("/admin/disable-user",methods=["PUT"])
def disable_user():
    try:
        data = request.get_json()
        
        username = data.get("username")
        password =  data.get("password")
        user = data.get("user")
        
        list_of_str = [username,password,user]
        for i in list_of_str:
            if not isinstance(i,str):
                return make_response("invalid values",400)
        
        response = Help.admin_enable_disable_user(admin={"username":username,"password":password},
                                                  username=user,state=False)
        response = response.split(":")
        return make_response(response[0],response[1])
           
    except:
        return make_response("read the cheatsheet!",400)

@app.route("/admin/delete-user",methods=["DELETE"])
def delete_user():
    try:
        data = request.get_json()
        
        username = data.get("username")
        password = data.get("password")
        user = data.get("user")
        
        list_of_str = [username,password,user]
        for i in list_of_str:
            if not isinstance(i,str):
                return make_response("invalid values",400)
        
        response = Help.admin_delete_user(admin={"username":username,"password":password},
                                          username=user)
        
        response = response.split(":")
        return make_response(response[0],response[1])
    except:
        return make_response("bad request!",400)

    
    
@app.route("/admin/reset-user",methods=["PUT"])
def reset_password():
    try:
        data = request.get_json()
        
        username = data.get("username")
        password = data.get("password")
        user = data.get("user")
        
        list_of_str = [username,password,user]
        for i in list_of_str:
            if not isinstance(i,str):
                return make_response("invalid values",400)
        
        response = Help.admin_reset_user_password(admin={"username":username,"password":password},username=user)
        response = response.split(":")
    
        return make_response(response[0],response[1])
    except:
        return make_response("read the cheatsheet!",400)
        

@app.route("/admin/set-policy",methods=["PUT"])
def set_policy():
    try:
        data = request.get_json()
        
        username = data.get("username")
        password = data.get("password")
        length = data.get("length")
        max_length = data.get("maxlength")
        upper = data.get("upper")
        lower = data.get("lower")
        numeric = data.get("numeric")
        punctuation = data.get("punctuation")
        
        list_of_str = [username,password]
        list_of_int = [upper,lower,punctuation,numeric,max_length,length]
        
        for i in list_of_str:
            if not isinstance(i,str):
                return make_response("invalid values!",400)
        
        for i in list_of_int:
            if not isinstance(i,int):
                return make_response("invalid values!",400)
        
        response = Help.admin_set_policy(
            admin={"username":username,"password":password},
            policy={"length":length,"maxlength":max_length,"upper":upper,"lower":lower,"punctuation":punctuation,"numeric":numeric})

        response = response.split(":")
        return make_response(response[0],response[1])
    except:
        return make_response("read the cheatsheet!",400)


@app.route("/admin/get-user-data",methods=["GET"])
def get_user_data():
    try:
        data = request.get_json()
        
        username = data.get("username")
        password = data.get("password")
        user = data.get("user")
        
        list_of_str = [username,password,user]
        for i in list_of_str:
            if not isinstance(i,str):
                return make_response("invalid values",400)
        
        response = Help.admin_get_user_data(admin={"username":username,"password":password},
                                            username=username)
        response = response.split(":")
        return make_response(response[0],response[1])

    except:
        return make_response("read the cheatsheet!",400)


@app.route("/admin/get-user-count",methods=["GET"])
def get_user_count():
    try:
        data = request.get_json()
        
        username = data.get("username")
        password = data.get("password")
        
        list_of_str = [username,password]
        for i in list_of_str:
            if not isinstance(i,str):
                return make_response("invalid values",400)
        
        response = Help.admin_get_user_count(admin={"username":username,"password":password})
        response = response.split(":")
        return make_response(response[0],response[1])

    except:
        return make_response("read the cheatsheet!",400)



@app.route("/admin/get-user-login-history",methods=["GET"])
def get_user_login_history():
    try:
        data = request.get_json()
        
        username = data.get("username")
        password = data.get("password")
        user = data.get("user")
        
        list_of_str = [username,password,user]
        for i in list_of_str:
            if not isinstance(i,str):
                return make_response("invalid values",400)
        
        response = Help.admin_get_user_loginorchange_history(
            admin={"username":username,"password":password},
            username=user,type=True)
        response = response.split(";")
        return make_response(response[0],response[1])

    except:
        return make_response("read the cheatsheet!",400)

@app.route("/admin/get-user-change-history")
def get_user_change_history():
    try:
        data = request.get_json()
        
        username = data.get("username")
        password = data.get("password")
        user = data.get("user")
        
        list_of_str = [username,password,user]
        for i in list_of_str:
            if not isinstance(i,str):
                return make_response("invalid values",400)
        
        response = Help.admin_get_user_loginorchange_history(
            admin={"username":username,"password":password},
            username=user,type=False)
        response = response.split(";")
        return make_response(response[0],response[1])

    except:
        return make_response("read the cheatsheet!",400)
        
if __name__=="__main__":
    app.run(port=1337,debug=True)

#write hints to the user when he signup