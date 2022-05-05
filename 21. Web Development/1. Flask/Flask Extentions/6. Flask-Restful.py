'''
		1. Flask-RESTful
'''


# Installation
pip install flask-restful


# A Minimal API
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)

'''
			# Resourceful Routing
'''
# The main building block provided by Flask-RESTful are resources. 
# Resources are built on top of Flask pluggable views, 
# giving you easy access to multiple HTTP methods just by defining methods on your resource. 

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)

# Flask-RESTful understands multiple kinds of return values from view methods
class Todo1(Resource):
    def get(self):
        # Default to 200 OK
        return {'task': 'Hello world'}

class Todo2(Resource):
    def get(self):
        # Set the response code to 201
        return {'task': 'Hello world'}, 201

class Todo3(Resource):
    def get(self):
        # Set the response code to 201 and return custom headers
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}



'''
		Endpoints
'''
# You can pass multiple URLs to the add_resource() method on the Api object.
# Each one will be routed to your Resource
api.add_resource(HelloWorld,
    '/',
    '/hello')

# You can also match parts of the path as variables to your resource methods.
api.add_resource(Todo,
    '/todo/<int:todo_id>', endpoint='todo_ep')


'''
		Argument Parsing
'''
# Flask-RESTful has built-in support for request data validation using a library similar to argparse.
from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help='Rate to charge for this resource')
args = parser.parse_args()

# If an argument fails to pass validation, Flask-RESTful will respond with a 400 Bad Request and
# a response highlighting the error.
$ curl -d 'rate=foo' http://127.0.0.1:5000/todos
{'status': 400, 'message': 'foo cannot be converted to int'}

# Calling parse_args with strict=True ensures that an error is thrown if the request
# includes arguments your parser does not define.
args = parser.parse_args(strict=True)



'''
			Data Formatting
'''
# Flask-RESTful provides the fields module and the marshal_with() decorator to describe the structure of your response.
from flask_restful import fields, marshal_with

resource_fields = {
    'task':   fields.String,
    'uri':    fields.Url('todo_ep')
}

class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task

        # This field will not be sent in the response
        self.status = 'active'

class Todo(Resource):
    @marshal_with(resource_fields)
    def get(self, **kwargs):
        return TodoDao(todo_id='my_todo', task='Remember the milk')


'''
			Full Example
'''
# Save this example in api.py

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
'''
Example usage
'''

# GET the list
$ curl http://localhost:5000/todos
{"todo1": {"task": "build an API"}, "todo3": {"task": "profit!"}, "todo2": {"task": "?????"}}

GET a single task

$ curl http://localhost:5000/todos/todo3
{"task": "profit!"}

# DELETE a task
$ curl http://localhost:5000/todos/todo2 -X DELETE -v

> DELETE /todos/todo2 HTTP/1.1
> User-Agent: curl/7.19.7 (universal-apple-darwin10.0) libcurl/7.19.7 OpenSSL/0.9.8l zlib/1.2.3
> Host: localhost:5000
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 204 NO CONTENT
< Content-Type: application/json
< Content-Length: 0
< Server: Werkzeug/0.8.3 Python/2.7.2
< Date: Mon, 01 Oct 2012 22:10:32 GMT

# Add a new task
$ curl http://localhost:5000/todos -d "task=something new" -X POST -v

> POST /todos HTTP/1.1
> User-Agent: curl/7.19.7 (universal-apple-darwin10.0) libcurl/7.19.7 OpenSSL/0.9.8l zlib/1.2.3
> Host: localhost:5000
> Accept: */*
> Content-Length: 18
> Content-Type: application/x-www-form-urlencoded
>
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 25
< Server: Werkzeug/0.8.3 Python/2.7.2
< Date: Mon, 01 Oct 2012 22:12:58 GMT
<
* Closing connection #0
{"task": "something new"}

# Update a task
$ curl http://localhost:5000/todos/todo3 -d "task=something different" -X PUT -v

> PUT /todos/todo3 HTTP/1.1
> Host: localhost:5000
> Accept: */*
> Content-Length: 20
> Content-Type: application/x-www-form-urlencoded
>
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 27
< Server: Werkzeug/0.8.3 Python/2.7.3
< Date: Mon, 01 Oct 2012 22:13:00 GMT
<
* Closing connection #0
{"task": "something different"}


'''
		Project Structure
'''
# we’ll describe Project Structure that scales pretty well with larger apps and maintains a nice level organization.
# The basic idea is to split your app into three main parts:
	# the routes,
	# the resources, and
	# any common infrastructure.

Directory_Structure = '''

myapi/
    __init__.py
    app.py          # this file contains your app and routes
    resources/
        __init__.py
        foo.py      # contains logic for /Foo
        bar.py      # contains logic for /Bar
    common/
        __init__.py
        util.py     # just some common infrastructure

'''
# The common directory would probably just contain a set of helper functions to fulfill common needs across your application.
# It could also contain, for example, any custom input/output types your resources need to get the job done.


# In the resource files, you just have your resource objects. So here’s what foo.py might look like:
from flask_restful import Resource

class Foo(Resource):
    def get(self):
        pass
    def post(self):
        pass

# The key to this setup lies in app.py:

from flask import Flask
from flask_restful import Api
from myapi.resources.foo import Foo
from myapi.resources.bar import Bar
from myapi.resources.baz import Baz

app = Flask(__name__)
api = Api(app)

api.add_resource(Foo, '/Foo', '/Foo/<string:id>')
api.add_resource(Bar, '/Bar', '/Bar/<string:id>')
api.add_resource(Baz, '/Baz', '/Baz/<string:id>')

# As you can imagine with a particularly large or complex API, this file ends up being very valuable
# as a comprehensive list of all the routes and resources in your API. You would also use this file to
# set up any config values (before_request(), after_request()). Basically, this file configures your entire API.

# The things in the common directory are just things you’d want to support your resource modules.


