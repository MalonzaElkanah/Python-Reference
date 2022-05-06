'''
			Flask-CORS
'''
# A Flask extension for handling Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible.

'''
			Installation
'''
$ pip install -U flask-cors


# In the simplest case, initialize the Flask-Cors extension with default arguments in order to allow CORS
# for all domains on all routes.
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"

'''
		Resource specific CORS
'''
# Alternatively, you can specify CORS options on a resource and origin level of granularity by passing
# a dictionary as the resources option, mapping paths to a set of options.

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/api/v1/users")
def list_users():
  return "user example"

'''
		Route specific CORS via decorator
'''
# This extension also exposes a simple decorator to decorate flask routes with. Simply add @cross_origin()
# below a call to Flask’s @app.route(..) to allow CORS on a given route. 
@app.route("/")
@cross_origin()
def helloWorld():
  return "Hello, cross-origin-world!"



# REF: https://flask-cors.corydolphin.com/en/latest/api.html