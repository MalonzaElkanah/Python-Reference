# Install Flask
# pip install flask



# A minimal Flask application looks something like this:
'''
    First we imported the Flask class. An instance of this class will be our WSGI application.
'''
from flask import Flask

'''
	Next we create an instance of this class. 
	The first argument is the name of the application’s module or package. 
	__name__ is a convenient shortcut for this that is appropriate for most cases. 
	This is needed so that Flask knows where to look for resources such as templates and static files.

'''
app = Flask(__name__)

'''
	We then use the route() decorator to tell Flask what URL should trigger our function.

    The function returns the message we want to display in the user’s browser. 
    The default content type is HTML, so HTML in the string will be rendered by the browser.

'''
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


'''
	You can add variable sections to a URL by marking sections with <variable_name>. 
	Your function then receives the <variable_name> as a keyword argument. 
'''
from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


'''
	Optionally, you can use a converter to specify the type of the argument like <converter:variable_name>.
					Converter types:
'''
# string - (default) accepts any text without a slash
# int - accepts positive integers
# float - accepts positive floating point values
# path - like string but also accepts slashes
# uuid - accepts UUID strings
from markupsafe import escape

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


'''
	URL Building

	To build a URL to a specific function, use the url_for() function. 
	It accepts the name of the function as its first argument and any number of keyword arguments, 
	each corresponding to a variable part of the URL rule. 
	Unknown variable parts are appended to the URL as query parameters.
'''

'''
	We use the test_request_context() method to try out url_for(). 
	test_request_context() tells Flask to behave as though it’s handling a request 
	even while we use a Python shell.
'''

from flask import url_for

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index')) 						# /
    print(url_for('login')) 	 					# /login
    print(url_for('login', next='/'))				# /login?next=/
    print(url_for('profile', username='John Doe'))	# /user/John%20Doe



'''
	HTTP Methods

	By default, a route only answers to GET requests. 
	You can use the methods argument of the route() decorator to handle different HTTP methods.
'''
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


'''
	Static Files

	usually where the CSS and JavaScript files are coming from. 
	Create a folder called static in your package or next to your module and it will be available 
	at /static on the application.

	To generate URLs for static files, use the special 'static' endpoint name:
'''
url_for('static', filename='style.css') # The file has to be stored on the filesystem as static/style.css.



'''
	Rendering Templates

	To render a template you can use the render_template() method, 
	provide the name of the template and the variables you want to pass to the template engine as 
	keyword arguments.
'''
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

'''
	Flask will look for templates in the templates folder. 
	So if your application is a module, this folder is next to that module, 
	if it’s a package it’s actually inside your package
'''


'''
	For templates you can use the full power of Jinja2 templates.
'''

html = """
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
"""

'''
	Inside templates you also have access to the 
	config, 
	request, 
	session and 
	g 

	1 objects as well as the 
	url_for() and 
	get_flashed_messages() 
	functions.
'''



'''
				The Request Object¶
'''

from flask import request

'''
1.	The current request method is available by using the method attribute. 
	To access form data (data transmitted in a POST or PUT request) you can use the form attribute. 
'''
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


'''
2.	To access parameters submitted in the URL (?key=value) you can use the args attribute:

'''
searchword = request.args.get('key', '')


'''
	File Uploads

	set the enctype="multipart/form-data" attribute on your HTML form, for browser to transmit your files.

	You can access those files by looking at the files attribute on the request object. 
	Each uploaded file is stored in that dictionary. 
	It has a save() method that allows you to store that file on the filesystem of the server. 
'''
from flask import request
from werkzeug.utils import secure_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(f"/var/www/uploads/{secure_filename(file.filename)}")


'''
	Cookies

	To access cookies you can use the cookies attribute. 
	To set cookies you can use the set_cookie method of response objects. 
	The cookies attribute of request objects is a dictionary with all the cookies the client transmits. 
	If you want to use sessions, do not use the cookies directly but instead use the Sessions in Flask 
	that add some security on top of cookies for you.
'''

# Reading cookies:

from flask import request

@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.

# Storing cookies:

from flask import make_response

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp


'''
	Redirects and Errors

	To redirect a user to another endpoint, use the redirect() function; 
	to abort a request early with an error code, use the abort() function:
'''

from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()


'''
	If you want to customize the error page, you can use the errorhandler() decorator.
	404 after the render_template() call. This tells Flask that the status code of that 
	page should be 404 which means not found. 
	By default 200 is assumed which translates to: all went well.
'''
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


'''
					Responses

	The return value from a view function is automatically converted into a response object for you.
	If you want to get hold of the resulting response object inside the view 
	you can use the make_response() function.
'''
from flask import make_response

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp


'''
	APIs with JSON

	JSON a response format when writing an API. If you return a dict from a view, 
	it will be converted to a JSON response.
'''
@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }


'''
	to create JSON responses for types other than dict, use the jsonify() function, 
	which will serialize any supported JSON data type.
'''
from flask import jsonify

@app.route("/users")
def users_api():
    users = get_all_users()
    return jsonify([user.to_json() for user in users])


'''
	Sessions

	Session allows you to store information specific to a user from one request to the next. 
	This is implemented on top of cookies for you and signs the cookies cryptographically. 
	What this means is that the user could look at the contents of your cookie but not modify it, 
	unless they know the secret key used for signing.

	In order to use sessions you have to set a secret key. 
'''
from flask import session

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


'''
	Logging
'''
app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')
