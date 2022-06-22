# Password-Management_System

Access-Control-System with some Password-Management-System Functions

API Cheatsheet:



create user:
curl -X POST -H "Content-Type:application/json" http://127.0.0.1:1337/signup -d'{"admin_username":"Amino1","admin_password":"A+2-0n)051","username":"Aüow2","password":"abcd23§!4qA","status":true,"admin":true}'



login:
curl -X GET -H 'Content-Type: application/json' http://127.0.0.1:1337/login -d '{"username":"Ap23","password":"abcd2§§!4qA"}'

curl -X GET -H 'Content-Type: application/json' http://127.0.0.1:1337/login -d '{"username":"Amino1","password":"h]XN^3+R8"}'


generate password:
curl -X GET -H 'Content-Type: application/json' http://127.0.0.1:1337/generate-password -d '{"username":"Amino1","password":"h]XN^3+R8","length":20}'

curl -X POST -H "Content-Type:application/json" http://127.0.0.1:1337/signup -d'{"admin_username": "Amino1", "admin_password": "h]XN^3+R8", "username": "ASfle31()§", "password": "sDeQ3§&!$124", "status": True, "admin": False}'

edit password:
curl -X PUT -H 'Content-Type: application/json' http://127.0.0.1:1337/edit-password -d '{"username":"Amino1","password":"h]XN^3+R8","new":"h]XN^3+R8s"}'



edit username:
curl -X PUT -H 'Content-Type: application/json' http://127.0.0.1:1337/edit-username -d '{"username":"amin","password":"A+2-0n)051","new":"loasd1§A"}'



enable user:
curl -X PUT -H 'Content-Type: application/json' http://127.0.0.1:1337/admin/enable-user -d '{"username":"Amino1","password":"h]XN^3+R8","user":"Ap23"}'



disable user:
curl -X PUT -H 'Content-Type: application/json' http://127.0.0.1:1337/admin/disable-user -d '{"username":"amin","password":"h]XN^3+R8","user":"abdul"}'



delete user:
curl -X DELETE -H 'Content-Type: application/json' http://127.0.0.1:1337/admin/delete-user -d '{"username":"amin","password":"A+2-0n)051","user":"abdul"}'



reset user's password:
curl -X PUT -H 'Content-Type: application/json' http://127.0.0.1:1337/admin/reset-user -d '{"username":"amin","password":"A+2-0n)051","user":"abdul"}'



set password policy:
curl -X PUT -H 'Content-Type: application/json' http://127.0.0.1:1337/admin/set-password-policy -d '{"username":"Amino1","password":"A+2-0n)051","minlength":8,"maxlength":60,"upper":1,"lower":1,"numeric":2,"punctuation":1}'



set username policy:
curl -X PUT -H 'Content-Type: application/json' http://127.0.0.1:1337/admin/set-username-policy -d '{"username":"Amino1","password":"A+2-0n)051","minlength":4,"maxlength":14,"upper":1,"lower":1,"numeric":3,"punctutation":1}'



get user data:
curl -X GET -H 'Content-Type: application/json' http://127.0.0.1:1337/admin/get-user-data -d '{"username":"Amino1","password":"A+2-0n)051","user":"Ap23"}'



get user count:
curl -X GET -H 'Content-Type: application/json' http://127.0.0.1:1337/admin/get-user-count -d '{"username":"Amino1","password":"A+2-0n)051"}'



get user login history:
curl -X GET -H 'Content-Type: application/json' http://127.0.0.1:1337/admin/get-user-login-history -d '{"username":"Amino1","password":"A+2-0n)051","user":"Ap23"}'



get user change history:
curl -X GET -H 'Content-Type: application/json' http://127.0.0.1:1337/admin/get-user-change-history -d '{"username":"Amino1","password":"A+2-0n)051","user":"Ap23"}'