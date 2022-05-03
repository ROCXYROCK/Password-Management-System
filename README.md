# Password-Management_System

Access Control System with some Password Management System's Functions

1. The Data will be stored in this format: 
{
"Users":
[
    {"id":"","username":"","hashed":["first psw","second","third"],"last_login":"", "last_change":""}
    ,...,{}
],
"Admins":
[{"id":"","username":"","hashed":["first psw","second","third"],"last_login":"","last_change":""},...,{}]
}

GET: Fordert die angegebene Ressource vom Server an. GET weist keine Nebeneffekte auf.
POST: Daten übergeben / Ressource anlegen (also wie ein CREATE).
PUT: Die angegebene Ressource wird angelegt (also wie ein UPDATE). Wenn die Ressource bereits existiert, wird sie geändert.
DELETE: Die angegebene Daten werden gelöscht

__________
jsonify:
jsonify(username="iwas",password="haha",id="1222") -> {"username":"iwas","password":"haha","id":"1222"}