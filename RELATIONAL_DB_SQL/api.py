import os
from flask import Flask, request, Response, jsonify, abort
from functools import wraps
from flask_sqlalchemy import SQLAlchemy

# dummy users

USERS = [
    (0, 'Joe','Bloggs',
        'joe@bloggs.com', 'student',  True),
    (1, 'Ben', 'Bitdiddle',
        'ben@cuny.edu', 'student',  True),
    (2, 'Alissa P','Hacker',
         'missalissa@cuny.edu', 'professor',  True)
]
'''
USERS = {
    {'id': 0, 'first': 'Joe', 'last': 'Bloggs',
        'email': 'joe@bloggs.com', 'role': 'student', 'active': True},
    {'id': 1, 'first': 'Ben', 'last': 'Bitdiddle',
        'email': 'ben@cuny.edu', 'role': 'student', 'active': True},
    {'id': 2, 'first': 'Alissa P', 'last': 'Hacker',
        'email': 'missalissa@cuny.edu', 'role': 'professor', 'active': True},
}'''

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

def init_db():
    # create a global variable __db__ that you can use from route handlers
    global __db__
    
    # use in-memory database for debugging
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    __db__ = SQLAlchemy(app)
    engine = __db__.engine
    
    # put your database initialization statements here
    create_table_stmt = """create table MyDataBase(
      id integer primary key,
      first text not null,
      last text not null,
      email text not null,
      role text ,
      active boolean 
    );
    """
    # create the users table
    engine.execute(create_table_stmt)
    
    # insert each item from USERS list into the users table
    
    insert_statement = """
    insert into MyDataBase ('id', 'first', 'last',
        'email', 'role', 'active')
      values(?, ?, ?, ?, ?, ?)
    """

    for u in USERS:
        print(f"inserting {u}")
        # insert into db; note unpacking of tuple (*u)
        engine.execute(insert_statement, *u)


if __name__ == 'api':
    # save database handle in module-level global
    init_db()
    app.run(debug=True)


# Problem 1
@app.route("/users", methods=["GET"])
def get_users():
    u = __db__.engine.execute('select * from MyDataBase')
    users = [dict(user) for user in u]
    return jsonify(users)


# Problem 2
@app.route("/users/<int:post_id>", methods=["GET"])
def users_get_member(post_id):
    u = __db__.engine.execute(f'select * from MyDataBase WHERE id = {post_id}')
    target = u.fetchone()
    if target: #Check for whether target is empty if have invalid id.
        return jsonify(dict(target))
    return Response(None,404)

# Your code here...
# E.g.,
# @app.route("/users", methods=["GET"])

# Problem 3
@app.route("/users", methods=["POST"])
def add_user():
    new_user = request.get_json() #input from client to server
    myArray = [] #use list-array since each row is a tuple
    if 'first' in new_user.keys():
        myArray.append(new_user['first'])
        myArray.append(new_user['last'])
        myArray.append(new_user['email'])
        
        add_statement = """
            insert into MyDataBase ('first', 'last', 'email')
             values(?, ?, ?)
        """
        
        __db__.engine.execute(add_statement,myArray)
        
        response = Response(None, 201)
        return response
        
    return Response(None, 422)

# Problem 4
@app.route("/users/<int:post_id>", methods=["PUT","PATCH"])
def update_user(post_id):# client provides post_id
    
    myDict = request.get_json()#returns dictionary

#     update_statement = f"""
#        UPDATE MyDataBase 
#        SET first = {myDict['first']}, last = {myDict['last']}, email = {myDict['email']}, 
#        role = {myDict['role']}, active = {myDict['active']}
#     """
    update_statement = f"""
       UPDATE MyDataBase 
       SET first = ?
       WHERE id = {post_id}
    """
    engineRP = __db__.engine.execute(update_statement,myDict['first'])#THIS IS THE DISPATCHER TO THE SERVER
    u = __db__.engine.execute(f'select * from MyDataBase WHERE id = {post_id}')
    target = u.fetchone()
    if target: #Check for whether target is empty if have invalid id.
        return jsonify(dict(target))
    return Response(None,404)

    #response = Response(None, 200)
    #return jsonify(dict(engineRP.fetchone())) #returns to client
# Problem 5

@app.route("/users/<int:post_id>/deactivate", methods=["POST"])
def deactivate_user(post_id): 

    update_statement = f"""
       UPDATE MyDataBase 
       SET active = ?
       WHERE id = {post_id}
    """
    engineRP = __db__.engine.execute(update_statement,[False])#THIS IS THE DISPATCHER TO THE SERVER
    u = __db__.engine.execute(f'select * from MyDataBase WHERE id = {post_id}')
    target = u.fetchone()
    if target: #Check for whether target is empty if have invalid id.
        return jsonify(dict(target))
    return Response(None,404)
     
    
    
'''


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
@app.route("/users/<int:post_id>", methods=["PUT","PATCH"])
def update_user(post_id):  
    for dictionary in USERS:      
        if post_id == dictionary['id']:
            user = request.get_json()
            dictionary['first'] = user['first']
            response = Response(None, 200)
            return jsonify(dictionary)
        
    response = Response(None, 404)
    return response
    
# Problem 5

@app.route("/users/<int:post_id>/deactivate", methods=["POST"])
def deactivate_user(post_id): 
    for dictionary in USERS:    
        if post_id == dictionary['id']:
            dictionary['active']=False
            response = Response(None, 200)
            return jsonify(dictionary)
    response = Response(None, 404)
    return response
'''