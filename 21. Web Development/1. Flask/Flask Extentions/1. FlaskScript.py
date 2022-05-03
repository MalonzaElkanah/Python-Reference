'''
The Flask-Script extension provides support for writing external scripts in Flask. 
This includes running a development server, a customised Python shell, scripts to set up your database, 
cronjobs, and other command-line tasks that belong outside the web application itself.

Docs: https://flask-script.readthedocs.io/en/latest/

Flask-Script works in a similar way to Flask itself. 
You define and add commands that can be called from the command line to a Manager instance:
'''


'''Installing Flask-Script'''
pip install Flask-Script



'''Example 1'''

# manage.py

from flask_script import Manager

from myapp import app

manager = Manager(app)

@manager.command
def hello():
    print "hello"

if __name__ == "__main__":
    manager.run()

'''Once you define your script commands, you can then run them on the command line:

python manage.py hello
> hello
'''



'''Example 2'''
from flask_script import Manager

app = Flask(__name__)
# configure your app

manager = Manager(app)

if __name__ == "__main__":
    manager.run()




'''Example 3'''
from flask_script import Command

class Hello(Command):
    "prints hello world"

    def run(self):
        print "hello world"


from flask_script import Manager

manager = Manager(app)

manager.add_command('hello', Hello())

if __name__ == "__main__":
	manager.run()




# To get a list of available commands and their descriptions, just run with no command:
python manage.py

# To get help text for a particular command, This will print usage plus the docstring of the Command.
python manage.py runserver -?



'''
the @option decorator
'''
# belongs to Manager can be used when you want more sophisticated control over your commands:

@manager.option('-n', '--name', help='Your name')
def hello(name):
    print "hello", name




# If you want to restore the original meaning of -h, 
# set your manager’s help_args attribute to a list of argument strings you want to be considered helpful:
manager = Manager()
manager.help_args = ('-h', '-?', '--help')


# You can override this list in sub-commands and -managers, 
# so that manager -h prints help, while manager connect -h fubar.example.com connects to a remote host.

def talker(host='localhost'):
    pass
ccmd = ConnectCmd(talker)
ccmd.help_args = ('-?', '--help')
manager.add_command("connect", ccmd)
manager.run()



'''
Adding arguments to commands
'''
# 1. To facilitate this you use the option_list attribute of the Command class:
from flask_script import Command, Manager, Option

class Hello(Command):

    option_list = (
        Option('--name', '-n', dest='name'),
    )

    def run(self, name):
        print "hello %s" % name


# 2. Alternatively, you can define a get_options method for your Command class.
class Hello(Command):

    def __init__(self, default_name='Joe'):
        self.default_name=default_name

    def get_options(self):
        return [
            Option('-n', '--name', dest='name', default=self.default_name),
        ]

    def run(self, name):
        print "hello",  name


# 3. In @command decorator, the options are extracted automatically from your function arguments.
@manager.command
def hello(name):
    print "hello", name
# You then invoke this on the command line like so:
> python manage.py hello Joe


# 4. you can do optional arguments:
@manager.command
def hello(name="Fred")
    print "hello", name
# These can be called like so:
> python manage.py hello --name=Joe
> python manage.py hello -n Joe


# 5. For more sophisticated options it’s better to use the @option decorator:
@manager.option('-n', '--name', dest='name', default='joe')
def hello(name):
    print "hello", name

# You can add as many options as you want:
@manager.option('-n', '--name', dest='name', default='joe')
@manager.option('-u', '--url', dest='url', default=None)
def hello(name, url):
    if url is None:
        print "hello", name
    else:
        print "hello", name, "from", url
> python manage.py hello -n Joe -u reddit.com
> python manage.py hello --name=Joe --url=reddit.com




''' 
Adding options to the manager
'''
# Options can also be passed to the Manager instance. 
# This is allows you to set up options that are passed to the application rather than a single command. 

# In order to pass that config argument, use the add_option() method of your Manager instance. It takes the same arguments as Option:

manager.add_option('-c', '--config', dest='config', required=False)

# For example

@manager.command
def hello(name):
    uppercase = app.config.get('USE_UPPERCASE', False)
    if uppercase:
        name = name.upper()
    print "hello", name
# You can now run the following:
> python manage.py -c dev.cfg hello joe


# Below Example, will show an error message because the -c option does not belong to the hello command.
> python manage.py hello joe -c dev.cfg



'''
Getting user input
'''

# Flask-Script comes with a set of helper functions for grabbing user input from the command line. For example:

from flask_script import Manager, prompt_bool

from myapp import app
from myapp.models import db

manager = Manager(app)

@manager.command
def dropdb():
    if prompt_bool(
        "Are you sure you want to lose all your data"):
        db.drop_all()

# It then runs like this:
> python manage.py dropdb
# Are you sure you want to lose all your data ? [N]



'''
Default commands
'''
# 1. runserver  -  Flask-Script has a couple of ready commands you can add and customise: Server and Shell.


from flask_script import Server, Manager
from myapp import create_app

manager = Manager(create_app)
manager.add_command("runserver", Server())

if __name__ == "__main__":
    manager.run()

# and then run the command:
> python manage.py runserver

# The Server command has a number of command-line arguments - run python manage.py runserver -? for details on these. 
# You can redefine the defaults in the constructor:
server = Server(host="0.0.0.0", port=9000)



# 2. shell - The Shell command starts a Python shell. 

# You can pass in a make_context argument, which must be a callable returning a dict. 
# By default, this is just a dict returning the your Flask application instance:

from flask_script import Shell, Manager

from myapp import app
from myapp import models
from myapp.models import db

def _make_context():
    return dict(app=app, db=db, models=models)

manager = Manager(create_app)
manager.add_command("shell", Shell(make_context=_make_context))
# This is handy if you want to include a bunch of defaults in your shell to save typing lots of import statements.
# The Shell command will use IPython if it is installed, otherwise it defaults to the standard Python shell. 
# You can disable this behaviour in two ways: 
    # - by passing the use_ipython argument to the Shell constructor, or 
    # - passing the flag --no-ipython in the command line:
shell = Shell(use_ipython=False)

# There is also a shell decorator which you can use with a context function, This enables a shell command with the defaults enabled
@manager.shell
def make_shell_context():
    return dict(app=app, db=db, models=models)

> python manage.py shell

'''
The default commands shell and runserver are included by default, with the default options for these commands. 
If you wish to replace them with different commands simply override with add_command() or the decorators. 
If you pass with_default_commands=False to the Manager constructor these commands will not be loaded:'''
manager = Manager(app, with_default_commands=False)



'''
Sub-Managers
'''

# A Sub-Manager is an instance of Manager added as a command to another Manager. To create a submanager:
def sub_opts(app, **kwargs):
    pass
sub_manager = Manager(sub_opts)
manager = Manager(self.app)
manager.add_command("sub_manager", sub_manager)

# If you attach options to the sub_manager, the sub_opts procedure will receive their values.
# If sub_opts returns a value other than None, this value will replace the app value that’s passed on. 
# This way, you can implement a sub-manager which replaces the whole app. 
# One use case is to create a separate administrative application for improved security:
def gen_admin(app, **kwargs):
    from myweb.admin import MyAdminApp
    ## easiest but possibly incomplete way to copy your settings
    return MyAdminApp(config=app.config, **kwargs)
sub_manager = Manager(gen_admin)

manager = Manager(MyApp)
manager.add_command("admin", sub_manager)

> python manage.py runserver
[ starts your normal server ]
> python manage.py admin runserver
[ starts an administrative server ]

# You can cascade sub-managers, i.e. add one sub-manager to another. 
# A sub-manager does not get default commands added to itself (by default)


'''
Extension developers
'''
# Extension developers can easily create convenient sub-manager instance within their extensions to make 
# it easy for a user to consume all the available commands of an extension.

# Example how a database extension could provide (ex. database.py):

# database.py
manager = Manager(usage="Perform database operations")

@manager.command
def drop():
    "Drops database tables"
    if prompt_bool("Are you sure you want to lose all your data"):
        db.drop_all()


@manager.command
def create(default_data=True, sample_data=False):
    "Creates database tables from sqlalchemy models"
    db.create_all()
    populate(default_data, sample_data)


@manager.command
def recreate(default_data=True, sample_data=False):
    "Recreates database tables (same as issuing 'drop' and then 'create')"
    drop()
    create(default_data, sample_data)


@manager.command
def populate(default_data=False, sample_data=False):
    "Populate database with default data"
    from fixtures import dbfixture

    if default_data:
        from fixtures.default_data import all
        default_data = dbfixture.data(*all)
        default_data.setup()

    if sample_data:
        from fixtures.sample_data import all
        sample_data = dbfixture.data(*all)
        sample_data.setup()



# Then the user can register the sub-manager to their primary Manager (within manage.py):
manager = Manager(app)

from flask_database import manager as database_manager
manager.add_command("database", database_manager)


# The commands will then be available:

> python manage.py database

 Please provide a command:

 Perform database operations
  create    Creates database tables from sqlalchemy models
  drop      Drops database tables
  populate  Populate database with default data
  recreate  Recreates database tables (same as issuing 'drop' and then 'create')


'''
Error handling
'''
# In your command handler:

from flask_script.commands import InvalidCommand

[… if some command verification fails …]
class MyCommand(Command):
    def run(self, foo=None, bar=None):
        if foo and bar:
            raise InvalidCommand("Options foo and bar are incompatible")

# In your main loop:

try:
    MyManager().run()
except InvalidCommand as err:
    print(err, file=sys.stderr)
    sys.exit(1)





'''
The Manager runs the command inside a Flask test context. 
This means that you can access request-local proxies where appropriate, 
such as current_app, which may be used by extensions.

'''



