from flask import Flask, request, jsonify, url_for
import json
import os

#os.path.dirname(os.path.realpath(__file__))# it gives you the current file path

App = Flask(__name__)

@App.route("/register/user",methods=["PUT"])
def register():
    InputData = json.loads(request.data)
    #open file and read data

    with open(os.path.dirname(os.path.realpath(__file__))+"/Data/stored.json","r") as File:
        Reader = File.read()
    Reader = json.loads(Reader)
    print(Reader["Users"])

    if not Reader:
        Data["Users"].append(InputData)
    else:
        Data = Reader
        Data["Users"].append(InputData)
        print(Data["Users"])
    
    
    return jsonify(Data)



if __name__=="__main__":
    App.run(debug=True,port=1337)

