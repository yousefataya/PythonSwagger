from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from api import create_app
from api.db import db
from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields

from flask_jwt_extended import get_jwt_identity

from api.entities.services import get_user_by_id, update_user
from api.core import validate_json_body

bp = Blueprint('user', __name__, url_prefix='/users')

from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, get_jwt_claims
)
# sets up the app
app = create_app()

manager = Manager(app)
migrate = Migrate(app, db)

# adds the python manage.py db init, db migrate, db upgrade commands
manager.add_command("db", MigrateCommand)


@manager.command
def runserver():
    app.run(debug=True, host="localhost", port=3001)


@manager.command
def runworker():
    app.run(debug=False)


@manager.command
def recreate_db():
    """
    Recreates a database. This should only be used once
    when there's a new database instance. This shouldn't be
    used when you migrate your database.
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


from flask import Flask
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='TodoMVC API',
    description='A simple TodoMVC API',
)

ns = api.namespace('todos', description='TODO operations')

todo = api.model('Todo', {
    'id': fields.Integer(readOnly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})

app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

class TodoDAO(object):
    def __init__(self):
        self.counter = 0
        self.todos = []

    def get(self, id):
        for todo in self.todos:
            if todo['id'] == id:
                return todo
        api.abort(404, "Todo {} doesn't exist".format(id))

    def create(self, data):
        todo = data
        todo['id'] = self.counter = self.counter + 1
        self.todos.append(todo)
        return todo

    def update(self, id, data):
        todo = self.get(id)
        todo.update(data)
        return todo

    def delete(self, id):
        todo = self.get(id)
        self.todos.remove(todo)


DAO = TodoDAO()
DAO.create({'task': 'Build an API'})
DAO.create({'task': '?????'})
DAO.create({'task': 'profit!'})


@ns.route('/')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @ns.doc('list_todos')
    @ns.marshal_list_with(todo)
    def get(self):
        '''List all tasks'''
        return DAO.todos

    @ns.doc('create_todo')
    @ns.expect(todo)
    @ns.marshal_with(todo, code=201)
    def post(self):
        '''Create a new task'''
        return DAO.create(api.payload), 201

ns_____________ = api.namespace('tokens', description='Tokens operations')

todo_____________ = api.model('Token', {
    'id': fields.Integer(readOnly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})

@ns_____________.route('/<int:id>')
@ns_____________.response(404, 'Todo not found')
@ns_____________.param('id', 'The task identifier')
class Todo(Resource):
    '''Show a single todo item and lets you delete them'''
    @ns_____________.doc('get_todo')
    @ns_____________.marshal_with(todo_____________)
    def get(self, id):
        '''Fetch a given resource'''
        return DAO.get(id)

    @ns_____________.doc('delete_todo')
    @ns_____________.response(204, 'Todo deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        DAO.delete(id)
        return '', 204

    @ns_____________.expect(todo_____________)
    @ns_____________.marshal_with(todo_____________)
    def put(self, id):
        '''Update a task given its identifier'''
        return DAO.update(id, api.payload)

    @jwt.user_claims_loader
    def add_claims_to_access_token(user):
        return {'roles': user.roles}

    @jwt.user_identity_loader
    def user_identity_lookup(user):
           return user.username


    @ns_____________.doc('login')
    @ns_____________.marshal_with(todo_____________)
    def login():
             username = request.json.get('username', None)
             password = request.json.get('password', None)
             if username != 'admin' or password != 'admin':
                return jsonify({"msg": "Bad username or password"}), 401

             user = UserTokenObject(username='admin', roles=['foo', 'bar'])

             access_token = create_access_token(identity=user)
             ret = {'access_token': access_token}
             return jsonify(ret), 200


    @ns_____________.doc('protected')
    @ns_____________.response(204, 'protected featuers')
    @jwt_required
    def protected():
       ret = {
        'current_identity': get_jwt_identity(),  # test
        'current_roles': get_jwt_claims()['roles']  # ['foo', 'bar']
             }
       return jsonify(ret), 200

    @ns_____________.doc('get_current_user')
    @ns_____________.response(204, 'get_current_user featuers')
    def get_current_user():
         user_id = get_jwt_identity()
         user = get_user_by_id(user_id)
         return jsonify(__serialize_user(user))

    @ns_____________.doc('update_current_user')
    @ns_____________.response(204, 'update_current_user featuers')
    def update_current_user():
         user_id = get_jwt_identity()
         data = request.get_json()

         user = get_user_by_id(user_id)

         user.email = data['email']
         user.first_name = data['firstName']
         user.last_name = data['lastName']
         user.login = data['userName']
         user.age = data['age']
         user.street = data['address']['street']
         user.city = data['address']['city']
         user.zip = data['address']['zipCode']

         update_user(user)

         return jsonify(__serialize_user(user))
# app = Flask(__name__)







# This is an example of a complex object that we could build
# a JWT from. In practice, this will likely be something
# like a SQLAlchemy instance.
@ns.route('/token')
@ns.response(404, 'Token not found')
class UserTokenObject(Resource):
    def __init__(self, username, roles):
        self.username = username
        self.roles = roles


# Create a function that will be called whenever create_access_token
# is used. It will take whatever object is passed into the
# create_access_token method, and lets us define what custom claims
# should be added to the access token.
    


def __serialize_user(user):
    return {
        'id': user.id,
        'email': user.email,
        'firstName': user.first_name,
        'lastName': user.last_name,
        'userName': user.login,
        'age': user.age,
        'address': {
            'street': user.street,
            'city': user.city,
            'zipCode': user.zip,
        }
    }

if __name__ == '__main__':
    app.run(debug=True)
