<body>
<h1>Password Management System</h1>

<h5>Setup:</h5>
<h6>
<ul style="list-style-type:circle;">
<li>install python3 on your pc.</li>
<li>open the command line and go to the password-management-system directory.</li>
<li> write "python3 Application.py" to run the application.</li>
<li> write "python3 Unittest/Unittest.py" to run the 78 unit tests.</li>
</ul>
</h6>

<h5>Rules:</h5>
<h6>
<ul style="list-style-type:circle;">
<li>passwords not allowed to contain this characters " ' ; : \ this characters cause bugs</li>
<li>password allowed to contain this punctuations !#$%&()*+,-./<=>?@[]^_`{|}~</li>
<li>username policy:
<ul>
<table>
<tbody>
<tr>
<td><b>minimum length</b></td>
<td>4</td>
</tr>
<tr>
<td><b>maximum length</b></td>
<td>15</td>
</tr>
<tr>
<td><b>minimum count of upper cases</b></td>
<td>1</td>
</tr>
<tr>
<td><b>minimum count of lower cases</b></td>
<td>1</td>
</tr>
<tr>
<td><b>minimum count of numerical characters</b></td>
<td>1</td>
</tr>
<tr>
<td><b>minimum count of punctuations</b></td>
<td>0</td>
</tr>
</tbody>
</table>
</ul>
</li>
<li>password policy:
<ul>
<table>
<tbody>
<tr>
<td><b>minimum length</b></td>
<td>8</td>
</tr>
<tr>
<td><b>maximum length</b></td>
<td>60</td>
</tr>
<tr>
<td><b>minimum count of upper cases</b></td>
<td>1</td>
</tr>
<tr>
<td><b>minimum count of lower cases</b></td>
<td>1</td>
</tr>
<tr>
<td><b>minimum count of numerical characters</b></td>
<td>2</td>
</tr>
<tr>
<td><b>minimum count of punctuations</b></td>
<td>1</td>
</tr>
</tbody>
</table>
</ul>
</li>
</h6>


<!-- <h6>if you want to use the system, please check which permissions you have.</h6> -->

<h4>Predefined Master: <h6>This user is a default user which exist at the beginning of the program and can be used to execute all functions that need master permission. If anything went wrong with reading files, the system will be resetted and it exists only this master:
<ul>
<li>username: Amino1</li>
<li>password: h]XN^3+R8s</li>
</ul>
</h6>
</h4>


<table>
<tbody>
<tr style="height: 18px;">
<th style="text-align: center;">Functions/user level</th>
<th style="text-align: center;"colspan="3">Master</th>
<th style="text-align: center;"colspan="3">Admin</th>
<th style="text-align: center;"colspan="3">User</th>
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

<h2>Cheat Sheet:</h2>

Possible Responses:
<table>
<tbody>
<tr>
<th style="color: #33cc66">Error</td>
<th style="color: #33cc66"><b>Response</b></td>
<th style="color: #33cc66">Discription</td>
<th style="color: #33cc66">Code</td>
</tr>
<tr>
<td>TypeError</td>
<td>"invalid values!"</td>
<td>user enter not supported type.</td>
<td>400</td>
</tr>
<tr>
<td>AttributeError</td>
<td>"wrong header!"</td>
<td>user enter not supported header.</td>
<td>400</td>
</tr>
<tr>
<td>FileNotFoundError</td>
<td>"files missed!, all data resetted. Check for the original data on the cheat sheet"</td>
<td>Problem arised while reading files.</td>
<td>500</td>
</tr>
<tr>
<td>ClassCreationError</td>
<td>"Failed to build an object, check the input!"</td>
<td>Problem arised while creating object</td>
<td>500</td>
</tr>
<tr>
<td>UserDoesNotExistError</td>
<td>"User is not in the database, please enter an existing user!"</td>
<td>User disabled or not found in the database!</td>
<td>401</td>
</tr>
<tr>
<td>UserisNotAdminError</td>
<td>"User has no admin privileges!"</td>
<td>User is not admin.</td>
<td>405</td>
</tr>
<tr>
<td>AdminIsNotMasterError</td>
<td>"Admin has no master privileges!"</td>
<td>Admin is not master.</td>
<td>405</td>
</tr>
<tr>
<td>ChangeYourUsernameError</td>
<td>"Username doesn't match with policy, change it!"</td>
<td>Username doesn't have required charcters.</td>
<td>403</td>
</tr>
<tr>
<td>ChangeYourPasswordError</td>
<td>"Password is not valid any more, change it!"</td>
<td>Password doesn't have required characters or is pwned.</td>
<td>403</td>
</tr>
<tr>
<td>UserExistsAlreadyError</td>
<td>"User exists already, try with another one!"</td>
<td>Sign up or editing username with already existing username.</td>
<td>400</td>
</tr>
<tr>
<td>AccountError</td>
<td>"go to login to check your account!"</td>
<td>User is trying to excute admin functions or his username/password should be changed.</td>
<td>403</td>
</tr>
<tr>
<td>LengthError</td>
<td>"length doesn't match policy!"</td>
<td>User is trying to generate password with invalid length.</td>
<td>403</td>
</tr>
<tr>
<td>PasswordUsedBeforeError</td>
<td>"password used before!"</td>
<td>User is trying to edit his password with a already used password.</td>
<td>406</td>
</tr>
<tr>
<td>AdminHimSelfError</td>
<td>"you cannot excute it on yourself!"</td>
<td>Admin is trying to enable,disable,delete or reset himself.</td>
<td>403</td>
</tr>
<tr>
<td>PasswordPolicyError</td>
<td>"password policy is not valid, try again!"</td>
<td>Admin is trying to enter logical invalid policy values.</td>
<td>400</td>
</tr>
<tr>
<td>UsernamePolicyError</td>
<td>"username policy is not valid, try again!"</td>
<td>Admin is trying to enter logical invalid policy values.</td>
<td>400</td>
</tr>
</tbody>
</table>

<h4><b>Login</b></h4>

<table>
<tbody>
<tr>
<th style="color: #33cc66"><b>Login</b></td>
<th style="color: #33cc66">http://127.0.0.1:1337/login</td>
</tr>
<tr>
<td style="color: #006600"><b>Description</b></td>
<td>every user can get access to the system(user,admin,master)</td>
</tr>
<tr>
<td style="color: #006600"><b>Method</b></td>
<td>GET</td>
</tr>
<tr>
<td style="color: #006600"><b>Header</b></td>
<td>Content-Type:application/json</td>
</tr>
<tr>
<td style="color: #006600"><b>Body</b></td>
<td>
<p>{<br>"username": str<br>"password": str<br>}</p>
</td>
</tr>
<tr>
<td style="color: #006600"><b>Response</b></td>
<td>
<p>user authenticated!</p>
</td>
</tr>
</tbody>
</table>

<br>
<h4><b>Sign up</b></h4>

<table>
<tbody>
<tr>
<th style="color: #33cc66"><b>Sign up</b></td>
<th style="color: #33cc66">http://127.0.0.1:1337/signup</td>
</tr>
<tr>
<td style="color: #006600"><b>Description</b></td>
<td>Admin and master can register admin and user</td>
</tr>
<tr>
<td style="color: #006600"><b>Method</b></td>
<td>POST</td>
</tr>
<tr>
<td style="color: #006600"><b>Header</b></td>
<td>Content-Type:application/json</td>
</tr>
<tr>
<td style="color: #006600"><b>Body</b></td>
<td>
<p>{<br>"admin_username": str<br>"admin_password": str<br>"username": str<br>"password": str<br>"status": bool<br>"admin": bool<br>}</p>
</td>
</tr>
<tr>
<td style="color: #006600"><b>Response</b></td>
<td>
<p>created successfully!</p>
</td>
</tr>
</tbody>
</table>

<br>
<h4><b>Generate Password</b></h4>

<table>
<tbody>
<tr>
<th style="color: #33cc66"><b>Generate password</b></td>
<th style="color: #33cc66">http://127.0.0.1:1337/generate-password</td>
</tr>
<tr>
<td style="color: #006600"><b>Description</b></td>
<td>every user can get generated password after logging in</td>
</tr>
<tr>
<td style="color: #006600"><b>Method</b></td>
<td>GET</td>
</tr>
<tr>
<td style="color: #006600"><b>Header</b></td>
<td>Content-Type:application/json</td>
</tr>
<tr>
<td style="color: #006600"><b>Body</b></td>
<td>
<p>{<br>"username": str<br>"password": str<br>"length": int<br>}</p>
</td>
</tr>
<tr>
<td style="color: #006600"><b>Response</b></td>
<td>
<p>str: generated password</p>
</td>
</tr>
</tbody>
</table>

<br>
<h4><b>Edit Password</b></h4>


<table>
<tbody>
<tr>
<th style="color: #33cc66"><b>Edit password</b></td>
<th style="color: #33cc66">http://127.0.0.1:1337/edit-password</td>
</tr>
<tr>
<td style="color: #006600"><b>Description</b></td>
<td>every user can get change his password after logging in</td>
</tr>
<tr>
<td style="color: #006600"><b>Method</b></td>
<td>PUT</td>
</tr>
<tr>
<td style="color: #006600"><b>Header</b></td>
<td>Content-Type:application/json</td>
</tr>
<tr>
<td style="color: #006600"><b>Body</b></td>
<td>
<p>{<br>"username": str<br>"password": str<br>"new": str<br>}</p>
</td>
</tr>
<tr>
<td style="color: #006600"><b>Response</b></td>
<td>
<p>successfully edited!</p>
</td>
</tr>
</tbody>
</table>

<br>
<h4><b>Edit Username</b></h4>

<table>
<tbody>
<tr>
<th style="color: #33cc66"><b>Edit username</b></td>
<th style="color: #33cc66">http://127.0.0.1:1337/edit-username</td>
</tr>
<tr>
<td style="color: #006600"><b>Description</b></td>
<td>every user can get change his username after logging in</td>
</tr>
<tr>
<td style="color: #006600"><b>Method</b></td>
<td>PUT</td>
</tr>
<tr>
<td style="color: #006600"><b>Header</b></td>
<td>Content-Type:application/json</td>
</tr>
<tr>
<td style="color: #006600"><b>Body</b></td>
<td>
<p>{<br>"username": str<br>"password": str<br>"new": str<br>}</p>
</td>
</tr>
<tr>
<td style="color: #006600"><b>Response</b></td>
<td>
<p>successfully edited!</p>
</td>
</tr>
</tbody>
</table>

<br>
<h4><b>Enable User</b></h4>

<table>
<tbody>
<tr>
<th style="color: #33cc66"><b>enable user</b></td>
<th style="color: #33cc66">http://127.0.0.1:1337/admin/enable-user</td>
</tr>
<tr>
<td style="color: #006600"><b>Description</b></td>
<td>Master admin can enable admins and users. Admin can enable users. User has no permission to excute this function. No admin is allowed to excute this function on himself.</td>
</tr>
<tr>
<td style="color: #006600"><b>Method</b></td>
<td>PUT</td>
</tr>
<tr>
<td style="color: #006600"><b>Header</b></td>
<td>Content-Type:application/json</td>
</tr>
<tr>
<td style="color: #006600"><b>Body</b></td>
<td>
<p>{<br>"username": str<br>"password": str<br>"user": str<br>}</p>
</td>
</tr>
<tr>
<td style="color: #006600"><b>Response</b></td>
<td>
<p>status changed successfully!</p>
</td>
</tr>
</tbody>
</table>

<br>
<h4><b>Disable User</b></h4>

<table>
<tbody>
<tr>
<th style="color: #33cc66"><b>Disable user</b></td>
<th style="color: #33cc66">http://127.0.0.1:1337/admin/disable-user</td>
</tr>
<tr>
<td style="color: #006600"><b>Description</b></td>
<td>Master admin can disable admins and users. Admin can disable users. User has no permission to excute this function. No admin is allowed to excute this function on himself.</td>
</tr>
<tr>
<td style="color: #006600"><b>Method</b></td>
<td>PUT</td>
</tr>
<tr>
<td style="color: #006600"><b>Header</b></td>
<td>Content-Type:application/json</td>
</tr>
<tr>
<td style="color: #006600"><b>Body</b></td>
<td>
<p>{<br>"username": str<br>"password": str<br>"user": str<br>}</p>
</td>
</tr>
<tr>
<td style="color: #006600"><b>Response</b></td>
<td>
<p>status changed successfully!</p>
</td>
</tr>
</tbody>
</table>

<br>
<h4><b>Delete User</b></h4>

<table>
<tbody>
<tr>
<th style="color: #33cc66"><b>Delete user</b></td>
<th style="color: #33cc66">http://127.0.0.1:1337/admin/delete-user</td>
</tr>
<tr>
<td style="color: #006600"><b>Description</b></td>
<td>Master admin can delete admins and users. Admin can delete users. User has no permission to excute this function. No admin is allowed to excute this function on himself.</td>
</tr>
<tr>
<td style="color: #006600"><b>Method</b></td>
<td>DELETE</td>
</tr>
<tr>
<td style="color: #006600"><b>Header</b></td>
<td>Content-Type:application/json</td>
</tr>
<tr>
<td style="color: #006600"><b>Body</b></td>
<td>
<p>{<br>"username": str<br>"password": str<br>"user": str<br>}</p>
</td>
</tr>
<tr>
<td style="color: #006600"><b>Response</b></td>
<td>
<p>user deleted successfully!</p>
</td>
</tr>
</tbody>
</table>

<br>
<h4><b>Reset User</b></h4>

<table>
<tbody>
<tr>
<th style="color: #33cc66"><b>Reset user</b></td>
<th style="color: #33cc66">http://127.0.0.1:1337/admin/reset-user</td>
</tr>
<tr>
<td style="color: #006600"><b>Description</b></td>
<td>Master admin can reset admins and users. Admin can reset users. User has no permission to excute this function. No admin is allowed to excute this function on himself.</td>
</tr>
<tr>
<td style="color: #006600"><b>Method</b></td>
<td>PUT</td>
</tr>
<tr>
<td style="color: #006600"><b>Header</b></td>
<td>Content-Type:application/json</td>
</tr>
<tr>
<td style="color: #006600"><b>Body</b></td>
<td>
<p>{<br>"username": str<br>"password": str<br>"user": str<br>}</p>
</td>
</tr>
<tr>
<td style="color: #006600"><b>Response</b></td>
<td>
<p>str: new password</p>
</td>
</tr>
</tbody>
</table>

<br>
<h4><b>Set Password Policy</b></h4>

<table>
<tbody>
<tr>
<th style="color: #33cc66"><b>Set password policy</b></td>
<th style="color: #33cc66">http://127.0.0.1:1337/admin/set-password-policy</td>
</tr>
<tr>
<td style="color: #006600"><b>Description</b></td>
<td>Admin can set password policy.</td>
</tr>
<tr>
<td style="color: #006600"><b>Method</b></td>
<td>PUT</td>
</tr>
<tr>
<td style="color: #006600"><b>Header</b></td>
<td>Content-Type:application/json</td>
</tr>
<tr>
<td style="color: #006600"><b>Body</b></td>
<td>
<p>{<br>"username": str<br>"password": str<br>"minlength": int<br>"maxlength": int<br>"upper": int<br>"lower": int<br>"numeric": int<br>"punctuation": int<br>}</p>
</td>
</tr>
<tr>
<td style="color: #006600"><b>Response</b></td>
<td>
<p>policy successfully updated!</p>
</td>
</tr>
</tbody>
</table>

<br>
<h4><b>Set Username Policy</b></h4>

<table>
<tbody>
<tr>
<th style="color: #33cc66"><b>Set username policy</b></td>
<th style="color: #33cc66">http://127.0.0.1:1337/admin/set-username-policy</td>
</tr>
<tr>
<td style="color: #006600"><b>Description</b></td>
<td>Admin can set username policy.</td>
</tr>
<tr>
<td style="color: #006600"><b>Method</b></td>
<td>PUT</td>
</tr>
<tr>
<td style="color: #006600"><b>Header</b></td>
<td>Content-Type:application/json</td>
</tr>
<tr>
<td style="color: #006600"><b>Body</b></td>
<td>
<p>{<br>"username": str<br>"password": str<br>"minlength": int<br>"maxlength": int<br>"upper": int<br>"lower": int<br>"numeric": int<br>"punctuation": int<br>}</p>
</td>
</tr>
<tr>
<td style="color: #006600"><b>Response</b></td>
<td>
<p>policy successfully updated!</p>
</td>
</tr>
</tbody>
</table>

<br>
<h4><b>Get User Data</b></h4>

<table>
<tbody>
<tr>
<th style="color: #33cc66"><b>Get user data</b></td>
<th style="color: #33cc66">http://127.0.0.1:1337/admin/get-user-data</td>
</tr>
<tr>
<td style="color: #006600"><b>Description</b></td>
<td>Admin can get every user data.</td>
</tr>
<tr>
<td style="color: #006600"><b>Method</b></td>
<td>GET</td>
</tr>
<tr>
<td style="color: #006600"><b>Header</b></td>
<td>Content-Type:application/json</td>
</tr>
<tr>
<td style="color: #006600"><b>Body</b></td>
<td>
<p>{<br>"username": str<br>"password": str<br>"user": str<br>}</p>
</td>
</tr>
<tr>
<td style="color: #006600"><b>Response</b></td>
<td>
<p>dict: user data</p>
</td>
</tr>
</tbody>
</table>

<br>
<h4><b>Get User Count</b></h4>

<table>
<tbody>
<tr>
<th style="color: #33cc66"><b>Get user count</b></td>
<th style="color: #33cc66">http://127.0.0.1:1337/admin/get-user-count</td>
</tr>
<tr>
<td style="color: #006600"><b>Description</b></td>
<td>Admin can get user count.</td>
</tr>
<tr>
<td style="color: #006600"><b>Method</b></td>
<td>GET</td>
</tr>
<tr>
<td style="color: #006600"><b>Header</b></td>
<td>Content-Type:application/json</td>
</tr>
<tr>
<td style="color: #006600"><b>Body</b></td>
<td>
<p>{<br>"username": str<br>"password": str<br>}</p>
</td>
</tr>
<tr>
<td style="color: #006600"><b>Response</b></td>
<td>
<p>int : user count</p>
</td>
</tr>
</tbody>
</table>

<br>
<h4><b>Get Login History</b></h4>

<table>
<tbody>
<tr>
<th style="color: #33cc66"><b>Get login history</b></td>
<th style="color: #33cc66">http://127.0.0.1:1337/admin/get-login-history</td>
</tr>
<tr>
<td style="color: #006600"><b>Description</b></td>
<td>Admin can get user login history.</td>
</tr>
<tr>
<td style="color: #006600"><b>Method</b></td>
<td>GET</td>
</tr>
<tr>
<td style="color: #006600"><b>Header</b></td>
<td>Content-Type:application/json</td>
</tr>
<tr>
<td style="color: #006600"><b>Body</b></td>
<td>
<p>{<br>"username": str<br>"password": str<br>"user": str<br>}</p>
</td>
</tr>
<tr>
<td style="color: #006600"><b>Response</b></td>
<td>
<p>list: user login history</p>
</td>
</tr>
</tbody>
</table>

<br>
<h4><b>Get Password Change History</b></h4>

<table>
<tbody>
<tr>
<th style="color: #33cc66"><b>Get password change history</b></td>
<th style="color: #33cc66">http://127.0.0.1:1337/admin/get-change-history</td>
</tr>
<tr>
<td style="color: #006600"><b>Description</b></td>
<td>Admin can get user password change history.</td>
</tr>
<tr>
<td style="color: #006600"><b>Method</b></td>
<td>GET</td>
</tr>
<tr>
<td style="color: #006600"><b>Header</b></td>
<td>Content-Type:application/json</td>
</tr>
<tr>
<td style="color: #006600"><b>Body</b></td>
<td>
<p>{<br>"username": str<br>"password": str<br>"user": str<br>}</p>
</td>
</tr>
<tr>
<td style="color: #006600"><b>Response</b></td>
<td>
<p>list: user password change history</p>
</td>
</tr>
</tbody>
</table>

</body>