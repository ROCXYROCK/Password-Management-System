<head>
<style>
h1 {text-align: center;}
p {text-align: center;}
div {text-align: center;}
tr:hover {background-color: coral;}
table {position:relative;margin-left: 500px;align-items:right;margin-right: auto;}

</style>
</head>
<body>
<h1>Password-Management-System</h1>

<h4>System to manage user account</h4>


<table>
<tbody>
<tr style="height: 18px;">
<th style="height: 18px;">Functions/user level</th>
<th colspan="3">Master</th>
<th colspan="3">Admin</th>
<th colspan="3">User</th>
</tr>
<tr style="height: 18px;">
<td style="height: 18px;">login</td>
<td style="text-align: center;" colspan="3">✔️</td>
<td style="text-align: center;" colspan="3">✔️</td>
<td style="text-align: center;" colspan="3">✔️</td>
</tr>
<tr style="height: 18px;">
<td style="height: 18px;">generate password </td>
<td style="text-align: center;" colspan="3">✔️</td>
<td style="text-align: center;" colspan="3">✔️</td>
<td style="text-align: center;" colspan="3">✔️</td>
</tr>
<tr style="height: 18px;">
<td style="height: 18px;">edit password</td>
<td style="text-align: center;" colspan="3">✔️</td>
<td style="text-align: center;" colspan="3">✔️</td>
<td style="text-align: center;" colspan="3">✔️</td>
</tr>
<tr style="height: 18px;">
<td style="height: 18px;">edit username</td>
<td style="text-align: center;" colspan="3">✔️</td>
<td style="text-align: center;" colspan="3">✔️</td>
<td style="text-align: center;" colspan="3">✔️</td>
</tr>
<tr style="height: 18px;">
<td style="height: 18px;">set username policy</td>
<td style="text-align: center;" colspan="3">✔️</td>
<td style="text-align: center;" colspan="3">✔️</td>
<td style="text-align: center;" colspan="3">❌</td>
</tr>
<tr style="height: 18px;">
<td style=" height: 18px;">set password policy</td>
<td style=" text-align: center;" colspan="3">✔️</td>
<td style=" text-align: center;" colspan="3">✔️</td>
<td style=" text-align: center;" colspan="3">❌</td>
</tr>
<tr style="height: 18px;">
<td style="height: 18px;">get user count</td>
<td style="text-align: center;" colspan="3">✔️</td>
<td style="text-align: center;" colspan="3">✔️</td>
<td style="text-align: center;" colspan="3">❌</td>
</tr>
<tr style="height: 18px;">
<td style="height: 18px;">&nbsp;</td>
<td style="text-align: center;">Master</td>
<td style="text-align: center;">Admin</td>
<td style="height: 18px; text-align: center;">User</td>
<td style="text-align: center;">Master</td>
<td style="text-align: center;">Admin</td>
<td style="height: 18px; text-align: center;">User</td>
<td style="text-align: center;">Master</td>
<td style="text-align: center;">Admin</td>
<td style="height: 18px; text-align: center;">User</td>
</tr>
<tr>
<td>get data </td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">❌</td>
</tr>
<tr>
<td >sign up</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">❌</td>
</tr>
<tr style="height: 10px;">
<td style="height: 10px;">get login history </td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">✔️</td>
<td style="height: 10px; text-align: center;">✔️</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">✔️</td>
<td style="height: 10px; text-align: center;">✔️</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">❌</td>
<td style="height: 10px; text-align: center;">❌</td>
</tr>
<tr>
<td >get change history</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">❌</td>
</tr>
<tr>
<td >enable</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">❌</td>
</tr>
<tr>
<td >disable</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">❌</td>
</tr>
<tr>
<td >delete</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">❌</td>
</tr>
<tr>
<td >reset</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">✔️</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">❌</td>
<td style="text-align: center;">❌</td>
</tr>
</tbody>
</table>

___


</body>










API Cheatsheet:

create user:
curl -X POST -H "Content-Type:application/json" http://127.0.0.1:1337/signup -d'{"admin_username":"Amino1","admin_password":"h]XN^3+R8s","username":"ASu3w2","password":"h&5s§!/2S)JhGBV","status":true,"admin":true}'



login:
curl -X GET -H 'Content-Type: application/json' http://127.0.0.1:1337/login -d '{"username":"Amino1","password":"h]XN^3+R8s"}'

curl -X GET -H 'Content-Type: application/json' http://127.0.0.1:1337/login -d '{"username":"ASu3w2","password":"h]XN^3+R8s"}'

generate password:
curl -X GET -H 'Content-Type: application/json' http://127.0.0.1:1337/generate-password -d '{"username":"Amino1","password":"h]XN^3+R8s","length":20}'



edit password:
curl -X PUT -H 'Content-Type: application/json' http://127.0.0.1:1337/edit-password -d '{"username":"ASu3w2","password":"4{!@q1N9","new":"h]XN^3+R8s"}'



edit username:
curl -X PUT -H 'Content-Type: application/json' http://127.0.0.1:1337/edit-username -d '{"username":"Amino1","password":"h]XN^3+R8s","new":"loasd1§A"}'



enable user:
curl -X PUT -H 'Content-Type: application/json' http://127.0.0.1:1337/admin/enable-user -d '{"username":"Amino1","password":"h]XN^3+R8s","user":"ASu3w2"}'



disable user:
curl -X PUT -H 'Content-Type: application/json' http://127.0.0.1:1337/admin/disable-user -d '{"username":"amin","password":"h]XN^3+R8s","user":"abdul"}'



delete user:
curl -X DELETE -H 'Content-Type: application/json' http://127.0.0.1:1337/admin/delete-user -d '{"username":"Amino1","password":"h]XN^3+R8s","user":"ASu3w2"}'



reset user's password:
curl -X PUT -H 'Content-Type: application/json' http://127.0.0.1:1337/admin/reset-user -d '{"username":"Amino1","password":"h]XN^3+R8s","user":"ASu3w2"}'



set password policy:
curl -X PUT -H 'Content-Type: application/json' http://127.0.0.1:1337/admin/set-password-policy -d '{"username":"Amino1","password":"A+2-0n)051","minlength":8,"maxlength":60,"upper":1,"lower":1,"numeric":2,"punctuation":1}'



set username policy:
curl -X PUT -H 'Content-Type: application/json' http://127.0.0.1:1337/admin/set-username-policy -d '{"username":"Amino1","password":"A+2-0n)051","minlength":4,"maxlength":14,"upper":1,"lower":1,"numeric":3,"punctutation":1}'



get user data:
curl -X GET -H 'Content-Type: application/json' http://127.0.0.1:1337/admin/get-user-data -d '{"username":"Amino1","password":"A+2-0n)051","user":"Ap23"}'



get user count:
curl -X GET -H 'Content-Type: application/json' http://127.0.0.1:1337/admin/get-user-count -d '{"username":"Amino1","password":"h]XN^3+R8s"}'



get user login history:
curl -X GET -H 'Content-Type: application/json' http://127.0.0.1:1337/admin/get-user-login-history -d '{"username":"Amino1","password":"h]XN^3+R8s","user":"ASu3w2"}'



get user change history:
curl -X GET -H 'Content-Type: application/json' http://127.0.0.1:1337/admin/get-user-change-history -d '{"username":"Amino1","password":"A+2-0n)051","user":"Ap23"}'


sudo -u postgres -s
username: sonarqube
password: abc12345.
https://techexpert.tips/sonarqube/sonarqube-installation-ubuntu-linux/

talk about linting
talk about time class , behavior oriented class
overwriting the typeerror class
own error classes
writting files, with finally, try except, in try read the file in var, if except do anything then in finally write the data
working always with type hinting
using inharitance
documentation with google style of docstrings
make a done list at the end of the pms to show which requirments are done by the system, which are required by schaad