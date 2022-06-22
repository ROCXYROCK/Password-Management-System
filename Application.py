import sys,os

sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/Packages")

from flask import Flask,make_response,request
import Help


app = Flask(__name__)

@app.route("/signup",methods=["POST"])
def signup():
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
                raise TypeError
        
        for i in list_of_bool:
            if not isinstance(i,bool):
                raise TypeError
        
        response = Help.admin_signup_user(admin={"username":admin_username,"password":admin_password},
                                          user_data={"username":username,"password":password,"enabled":status,"admin":admin})
        response = response.split(":")
        
        return make_response(response[0],response[1])
        
    except TypeError:
        return make_response("invalid values!",400)
    
    except:
        return make_response("read the documentation!",400)
        
        
    

@app.route("/login",methods=["GET"])
def login():
    try:
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        if not isinstance(username,str) or not isinstance(password,str):
            raise TypeError

        response = Help.login_user(data={"username":username,"password":password})
        response = response.split(":")
        
        return make_response(response[0],response[1])
        
    except TypeError:
        return make_response("invalid values!",400)
    except:
        return make_response("read the documentation!",400)
    
    
    
@app.route("/generate-password",methods=["GET"])
def user_generate_password():
    try:
        data = request.get_json()
        
        username = data.get("username")
        password = data.get("password")
        length = data.get("length")
        
        if not isinstance(username,str) or not isinstance(password,str) or not isinstance(length,int):
            raise TypeError
        
        response = Help.user_generate_password(
            data={"username":username,"password":password},
            length=length)
        
        response = response.split(":")
        return make_response(response[0],response[1])
    
    except TypeError:
        return make_response("invalid values!", 400)
    
    except:
        return make_response("read the documentation!",400)



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
                raise TypeError
        
        response = Help.edit_password(data={"username":username,"password":password,"newpassword":new_password})
        response = response.split(":")
        
        return make_response(response[0],response[1])
    
    except TypeError:
        return make_response("invalid values!", 400)
    
    except:
        return make_response("read the documentation!",400)
    
   
    
@app.route("/edit-username",methods=["PUT"])
def edit_useranme():
    try:
        data = request.get_json()
        
        username = data.get("username")
        password = data.get("password")
        new_username = data.get("new")
        
        list_of_str = [username,password,new_username]
        
        for i in list_of_str:
            if not isinstance(i,str):
                raise TypeError  
        
        response = Help.user_edit_username(data={"username":username,"password":password,"newusername":new_username})
        response = response.split(":")
        
        return make_response(response[0],response[1])
    
    except TypeError:
        return make_response("invalid values!", 400)
    
    except:
        return make_response("read the documentation!",400)  



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
                raise TypeError
        
        response = Help.admin_enable_disable_user(admin={"username":username,"password":password},
                                                  username=user,state=True)
        response = response.split(":")
        return make_response(response[0],response[1])
    
    except TypeError:
        return make_response("invalid values!", 400)       
    
    except:
        return make_response("read the documentation!",400)




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
                raise TypeError
        
        response = Help.admin_enable_disable_user(admin={"username":username,"password":password},
                                                  username=user,state=False)
        response = response.split(":")
        return make_response(response[0],response[1])
           
    except TypeError:
        return make_response("invalid values!", 400)
           
    except:
        return make_response("read the documentation!",400)



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
                raise TypeError
        
        response = Help.admin_delete_user(admin={"username":username,"password":password},
                                          username=user)
        
        response = response.split(":")
        return make_response(response[0],response[1])
    
    except TypeError:
        return make_response("invalid values!", 400)
    
    except:
        return make_response("read the documentation!",400)

    
    
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
                raise TypeError
        
        response = Help.admin_reset_user_password(admin={"username":username,"password":password},username=user)
        response = response.split(":")
    
        return make_response(response[0],response[1])
    
    except TypeError:
        return make_response("invalid values!", 400)
    
    except:
        return make_response("read the documentation!",400)
        


@app.route("/admin/set-password-policy",methods=["PUT"])
def set_password_policy():
    try:
        data = request.get_json()
        
        username = data.get("username")
        password = data.get("password")
        
        minlength = data.get("minlength")
        maxlength = data.get("maxlength")
        upper = data.get("upper")
        lower = data.get("lower")
        numeric = data.get("numeric")
        punctuation = data.get("punctuation")
        
        list_of_str = [username,password]
        list_of_int = [upper,lower,punctuation,numeric,maxlength,minlength]
        
        for i in list_of_str:
            if not isinstance(i,str):
                raise TypeError
        
        for i in list_of_int:
            if not isinstance(i,int):
                raise TypeError
        
        response = Help.admin_set_policy(
            admin={"username":username,"password":password},
            policy={"minlength":minlength,"maxlength":maxlength,"upper":upper,"lower":lower,"punctuation":punctuation,"numeric":numeric},
            policy_type=False)

        response = response.split(":")
        return make_response(response[0],response[1])
    
    except TypeError:
        return make_response("invalid values!", 400)
    
    except:
        return make_response("read the documentation!",400)



@app.route("/admin/set-username-policy",methods=["PUT"])
def set_username_policy():
    try:
        data = request.get_json()
        
        username = data.get("username")
        password = data.get("password")
        
        minlength = data.get("minlength")
        max_length = data.get("maxlength")
        upper = data.get("upper")
        lower = data.get("lower")
        numeric = data.get("numeric")
        punctuation = data.get("punctuation")
        
        list_of_str = [username,password]
        list_of_int = [upper,lower,punctuation,numeric,max_length,minlength]
        
        for i in list_of_str:
            if not isinstance(i,str):
                raise TypeError
        
        for i in list_of_int:
            if not isinstance(i,int):
                raise TypeError
        
        response = Help.admin_set_policy(
            admin={"username":username,"password":password},
            policy={"minlength":minlength,"maxlength":max_length,"upper":upper,"lower":lower,"punctuation":punctuation,"numeric":numeric},
            policy_type=True)

        response = response.split(":")
        return make_response(response[0],response[1])
    
    except TypeError:
        return make_response("invalid values!", 400)
    
    except:
        return make_response("read the documentation!",400)



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
                raise TypeError
        
        response = Help.admin_get_user_data(admin={"username":username,"password":password},
                                            username=username)
        response = response.split(";")
        return make_response(response[0],response[1])

    except TypeError:
        return make_response("invalid values!", 400)
    
    except:
        return make_response("read the documentation!",400)



@app.route("/admin/get-user-count",methods=["GET"])
def get_user_count():
    try:
        data = request.get_json()
        
        username = data.get("username")
        password = data.get("password")
        
        list_of_str = [username,password]
        for i in list_of_str:
            if not isinstance(i,str):
                raise TypeError
        
        response = Help.admin_get_user_count(admin={"username":username,"password":password})
        response = response.split(":")
        return make_response(response[0],response[1])

    except TypeError:
        return make_response("invalid values!", 400)
    
    except:
        return make_response("read the documentation!",400)



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
                raise TypeError
        
        response = Help.admin_get_user_loginorchange_history(
            admin={"username":username,"password":password},
            username=user,type=True)
        response = response.split(";")
        return make_response(response[0],response[1])

    except TypeError:
        return make_response("invalid values!", 400)
    
    except:
        return make_response("read the documentation!",400)



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
                raise TypeError
        
        response = Help.admin_get_user_loginorchange_history(
            admin={"username":username,"password":password},
            username=user,type=False)
        response = response.split(";")
        return make_response(response[0],response[1])

    except TypeError:
        return make_response("invalid values!", 400)
    
    except:
        return make_response("read the documentation!",400)
    
    
if __name__=="__main__":
    app.run(port=1337,debug=True)



