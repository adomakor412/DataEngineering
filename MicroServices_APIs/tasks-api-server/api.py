import os
from flask import Flask, request, Response, jsonify
from functools import wraps


# Custom error handler. Raise this exception
# to return a status_code, message, and body
class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


print(__name__)

app = Flask(__name__)

# set the default error handler
@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == '__main__':
    app.run(debug=True)

# dummy users
USERS = [
    {'id': 0, 'first': 'Joe', 'last': 'Bloggs',
        'email': 'joe@bloggs.com', 'role': 'student', 'active': True},
    {'id': 1, 'first': 'Ben', 'last': 'Bitdiddle',
        'email': 'ben@cuny.edu', 'role': 'student', 'active': True},
    {'id': 2, 'first': 'Alissa P', 'last': 'Hacker',
        'email': 'missalissa@cuny.edu', 'role': 'professor', 'active': True},
]

# Your code here...
# E.g.,
# @app.route("/users", methods=["GET"])

# Problem 1

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(USERS)

    
# Problem 2
@app.route("/users/<int:post_id>", methods=["GET"])
def profile(post_id):
    for user in USERS:
        if post_id == user['id']:
            return jsonify(user)
    return Response(None,404)
# Problem 3
@app.route("/users", methods=["POST"])
def add_user():
    new_user = request.get_json()
    myDict = {}
    if 'first' in new_user.keys():
        myDict['first'] = new_user['first']
        myDict['last'] = new_user['last']
        myDict['email'] = new_user['email']
        
        #user role true
        #myDict['role'] = new_user['role']
        #myDict['status'] = new_user['status']
        
        #print('/n/n/n This is Running /n/n/n')
        
        #new user TRUE
        myDict['id'] = len(USERS)      
        
        #response
        USERS.append(myDict)
        response = Response(None, 201)
        
        return response
        
    else:
        response = Response(None, 422)
        return response
    
# Problem 4
@app.route("/users/<id>", methods=["PUT"])
def update_user():
    user = request.get_json()
    post_id = user['id']
    print(user)
    for dictionary in USERS:      
        if post_id == dictionary['id']:
            dictionary['first'] = user['first']
            dictionary['last'] = user['last']
            dictionary['email'] = user['email']
            dictionary['role'] = user['role']
            dictionary['active'] = user['active']

            #response
            response = Response(None, 200)
            return response
        
    response = Response(None, 404)
    return response
    
# Problem 5
