# Password-Management_System

Access Control System with some Password Management System's Functions

API Cheatsheet:

create user:

curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:1337/register -d '{"username":"amin","password":"AHasdin§$5SDs","status":true,"admin":false}'



login:

curl -X GET -H 'Content-Type: application/json' http://127.0.0.1:1337/login -d '{"username":"amin","password":"AHasdin§$5SDs"}'




generate password:

curl -X GET -H "Content-Type: application/json" http://127.0.0.1:1337/generator -d '{"length":15}'



change_user_status:

curl -X PUT -H 'Content-Type: application/json' http://127.0.0.1:1337/admin/user-status -d '{"username":"amin","password":"AHasdin§$5SDs","user":"addmin","status":true}'



change password: 

curl -X PUT -H 'Content-Type: application/json' http://127.0.0.1:1337/user/editpassword -d '{"username":"admino","password":"ha!$&sdASD345","newpassword":"hasb§$&23WES"}'
__________
jsonify:
jsonify(username="iwas",password="haha",id="1222") -> {"username":"iwas","password":"haha","id":"1222"}