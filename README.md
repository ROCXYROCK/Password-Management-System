Password Management System
==========================

##### Setup:

###### 

* install python3 on your pc.
* open the command line and go to the password-management-system directory.
* write "pip install flask" to install the flask library
* write "pip install -r Requirements.txt" to install needed libraries to run the API
* write "python3 Application.py" to run the application.
* write "python3 Unittest/Unittest.py" to run the 78 unit tests.

##### Rules:

###### 

* passwords not allowed to contain this characters " ' ; : \ this characters cause bugs
* password allowed to contain this punctuations !#$%&()*+,-./&lt;=&gt;?@\[\]^_`{|}~
* only english letters and punctuations are allowed
* username policy:
    
    |     |     |
    | --- | --- |
    | **minimum length** | 4   |
    | **maximum length** | 15  |
    | **minimum count of upper cases** | 1   |
    | **minimum count of lower cases** | 1   |
    | **minimum count of numerical characters** | 1   |
    | **minimum count of punctuations** | 0   |
    
* password policy:
    
    |     |     |
    | --- | --- |
    | **minimum length** | 8   |
    | **maximum length** | 60  |
    | **minimum count of upper cases** | 1   |
    | **minimum count of lower cases** | 1   |
    | **minimum count of numerical characters** | 2   |
    | **minimum count of punctuations** | 1   |
    

\-\-\-

#### Predefined Master:

###### This user is a default user which exist at the beginning of the program and can be used to execute all functions that need master permission. If anything went wrong with reading files, the system will be resetted and it exists only this master:

* username: Amino1
* password: h\]XN^3+R8s

| Functions/user level | Master |     |     | Admin |     |     | User |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| login | ✔️  |     |     | ✔️  |     |     | ✔️  |     |     |
| generate password | ✔️  |     |     | ✔️  |     |     | ✔️  |     |     |
| edit password | ✔️  |     |     | ✔️  |     |     | ✔️  |     |     |
| edit username | ✔️  |     |     | ✔️  |     |     | ✔️  |     |     |
| set username policy | ✔️  |     |     | ✔️  |     |     | ❌   |     |     |
| set password policy | ✔️  |     |     | ✔️  |     |     | ❌   |     |     |
| get user count | ✔️  |     |     | ✔️  |     |     | ❌   |     |     |
|     | Master | Admin | User | Master | Admin | User | Master | Admin | User |
| get data | ✔️  | ✔️  | ✔️  | ✔️  | ✔️  | ✔️  | ❌   | ❌   | ❌   |
| get login history | ✔️  | ✔️  | ✔️  | ✔️  | ✔️  | ✔️  | ❌   | ❌   | ❌   |
| get change history | ✔️  | ✔️  | ✔️  | ✔️  | ✔️  | ✔️  | ❌   | ❌   | ❌   |
| sign up | ❌   | ✔️  | ✔️  | ❌   | ✔️  | ✔️  | ❌   | ❌   | ❌   |
| enable | ❌   | ✔️  | ✔️  | ❌   | ❌   | ✔️  | ❌   | ❌   | ❌   |
| disable | ❌   | ✔️  | ✔️  | ❌   | ❌   | ✔️  | ❌   | ❌   | ❌   |
| delete | ❌   | ✔️  | ✔️  | ❌   | ❌   | ✔️  | ❌   | ❌   | ❌   |
| reset | ❌   | ✔️  | ✔️  | ❌   | ❌   | ✔️  | ❌   | ❌   | ❌   |

\-\-\-

Cheat Sheet:
------------

#### Possible Responses:

| Error | **Response** | Discription | Code |
| --- | --- | --- | --- |
| TypeError | "invalid values!" | user enter not supported type. | 400 |
| AttributeError | "wrong header!" | user enter not supported header. | 400 |
| FileNotFoundError | "files missed!, all data reset. Check for the original data on the cheat sheet" | Problem raised while reading files. | 500 |
| ClassCreationError | "failed to build an object, check the input!" | Problem raised while creating object | 500 |
| UserDoesNotExistError | "user is not in the database, please enter an existing user!" | User disabled or not found in the database! | 401 |
| UserisNotAdminError | "user has no admin privileges!" | User is not admin. | 405 |
| AdminIsNotMasterError | "admin has no master privileges!" | Admin is not master. | 405 |
| ChangeYourUsernameError | "username doesn't match with policy, change it!" | Username doesn't have required characters. | 403 |
| ChangeYourPasswordError | "password is not valid any more, change it!" | Password doesn't have required characters or is pwned. | 403 |
| UserExistsAlreadyError | "User exists already, try with another one!" | Sign up or editing username with already existing username. | 400 |
| AccountError | "go to login to check your account!" | User is trying to execute admin functions or his username/password should be changed. | 403 |
| LengthError | "length doesn't match policy!" | User is trying to generate password with invalid length. | 403 |
| PasswordUsedBeforeError | "password used before!" | User is trying to edit his password with an already used password. | 406 |
| AdminHimSelfError | "you cannot execute it on yourself!" | Admin is trying to enable,disable,delete or reset himself. | 403 |
| PasswordPolicyError | "password policy is not valid, try again!" | Admin is trying to enter logical invalid policy values. | 400 |
| UsernamePolicyError | "username policy is not valid, try again!" | Admin is trying to enter logical invalid policy values. | 400 |

#### **Login**

| **Login** | http://127.0.0.1:1337/login |
| --- | --- |
| **Description** | every user can get access to the system(user,admin,master) |
| **Method** | GET |
| **Header** | Content-Type:application/json |
| **Body** | {  <br>"username": str  <br>"password": str  <br>} |
| **Response** | user authenticated! |

  

#### **Sign up**

| **Sign up** | http://127.0.0.1:1337/signup |
| --- | --- |
| **Description** | Admin and master can register admin and user |
| **Method** | POST |
| **Header** | Content-Type:application/json |
| **Body** | {  <br>"admin_username": str  <br>"admin_password": str  <br>"username": str  <br>"password": str  <br>"status": bool  <br>"admin": bool  <br>} |
| **Response** | created successfully! |

  

#### **Generate Password**

| **Generate password** | http://127.0.0.1:1337/generate-password |
| --- | --- |
| **Description** | every user can get generated password after logging in |
| **Method** | GET |
| **Header** | Content-Type:application/json |
| **Body** | {  <br>"username": str  <br>"password": str  <br>"length": int  <br>} |
| **Response** | str: generated password |

  

#### **Edit Password**

| **Edit password** | http://127.0.0.1:1337/edit-password |
| --- | --- |
| **Description** | every user can get change his password after logging in |
| **Method** | PUT |
| **Header** | Content-Type:application/json |
| **Body** | {  <br>"username": str  <br>"password": str  <br>"new": str  <br>} |
| **Response** | successfully edited! |

  

#### **Edit Username**

| **Edit username** | http://127.0.0.1:1337/edit-username |
| --- | --- |
| **Description** | every user can get change his username after logging in |
| **Method** | PUT |
| **Header** | Content-Type:application/json |
| **Body** | {  <br>"username": str  <br>"password": str  <br>"new": str  <br>} |
| **Response** | successfully edited! |

  

#### **Enable User**

| **enable user** | http://127.0.0.1:1337/admin/enable-user |
| --- | --- |
| **Description** | Master admin can enable admins and users. Admin can enable users. User has no permission to excute this function. No admin is allowed to excute this function on himself. |
| **Method** | PUT |
| **Header** | Content-Type:application/json |
| **Body** | {  <br>"username": str  <br>"password": str  <br>"user": str  <br>} |
| **Response** | status changed successfully! |

  

#### **Disable User**

| **Disable user** | http://127.0.0.1:1337/admin/disable-user |
| --- | --- |
| **Description** | Master admin can disable admins and users. Admin can disable users. User has no permission to excute this function. No admin is allowed to excute this function on himself. |
| **Method** | PUT |
| **Header** | Content-Type:application/json |
| **Body** | {  <br>"username": str  <br>"password": str  <br>"user": str  <br>} |
| **Response** | status changed successfully! |

  

#### **Delete User**

| **Delete user** | http://127.0.0.1:1337/admin/delete-user |
| --- | --- |
| **Description** | Master admin can delete admins and users. Admin can delete users. User has no permission to excute this function. No admin is allowed to excute this function on himself. |
| **Method** | DELETE |
| **Header** | Content-Type:application/json |
| **Body** | {  <br>"username": str  <br>"password": str  <br>"user": str  <br>} |
| **Response** | user deleted successfully! |

  

#### **Reset User**

| **Reset user** | http://127.0.0.1:1337/admin/reset-user |
| --- | --- |
| **Description** | Master admin can reset admins and users. Admin can reset users. User has no permission to excute this function. No admin is allowed to excute this function on himself. |
| **Method** | PUT |
| **Header** | Content-Type:application/json |
| **Body** | {  <br>"username": str  <br>"password": str  <br>"user": str  <br>} |
| **Response** | str: new password |

  

#### **Set Password Policy**

| **Set password policy** | http://127.0.0.1:1337/admin/set-password-policy |
| --- | --- |
| **Description** | Admin can set password policy. |
| **Method** | PUT |
| **Header** | Content-Type:application/json |
| **Body** | {  <br>"username": str  <br>"password": str  <br>"minlength": int  <br>"maxlength": int  <br>"upper": int  <br>"lower": int  <br>"numeric": int  <br>"punctuation": int  <br>} |
| **Response** | policy successfully updated! |

  

#### **Set Username Policy**

| **Set username policy** | http://127.0.0.1:1337/admin/set-username-policy |
| --- | --- |
| **Description** | Admin can set username policy. |
| **Method** | PUT |
| **Header** | Content-Type:application/json |
| **Body** | {  <br>"username": str  <br>"password": str  <br>"minlength": int  <br>"maxlength": int  <br>"upper": int  <br>"lower": int  <br>"numeric": int  <br>"punctuation": int  <br>} |
| **Response** | policy successfully updated! |

  

#### **Get User Data**

| **Get user data** | http://127.0.0.1:1337/admin/get-user-data |
| --- | --- |
| **Description** | Admin can get every user data. |
| **Method** | GET |
| **Header** | Content-Type:application/json |
| **Body** | {  <br>"username": str  <br>"password": str  <br>"user": str  <br>} |
| **Response** | dict: user data |

  

#### **Get User Count**

| **Get user count** | http://127.0.0.1:1337/admin/get-user-count |
| --- | --- |
| **Description** | Admin can get user count. |
| **Method** | GET |
| **Header** | Content-Type:application/json |
| **Body** | {  <br>"username": str  <br>"password": str  <br>} |
| **Response** | int : user count |

  

#### **Get Login History**

| **Get login history** | http://127.0.0.1:1337/admin/get-login-history |
| --- | --- |
| **Description** | Admin can get user login history. |
| **Method** | GET |
| **Header** | Content-Type:application/json |
| **Body** | {  <br>"username": str  <br>"password": str  <br>"user": str  <br>} |
| **Response** | list: user login history |

  

#### **Get Password Change History**

| **Get password change history** | http://127.0.0.1:1337/admin/get-change-history |
| --- | --- |
| **Description** | Admin can get user password change history. |
| **Method** | GET |
| **Header** | Content-Type:application/json |
| **Body** | {  <br>"username": str  <br>"password": str  <br>"user": str  <br>} |
| **Response** | list: user password change history |
