                    # Flask-Migrate

'''
Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic. 
The database operations are made available through the Flask command-line interface.

'''

'''
                    # Installation
'''
pip install Flask-Migrate


'''
                    # Initializing Flask Migrate
'''
# Flask-Migrate exposes one class called Migrate. This class contains all the functionality of the extension.
from flask_migrate import Migrate
migrate = Migrate(app, db)
# The two arguments to Migrate are the application instance and the Flask-SQLAlchemy database instance. 



# Example- An application that handles database migrations through Flask-Migrate
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

# As is standard for all Flask extensions, Flask-Migrate can be initialized using the init_app method as well

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
     """Application-factory pattern"""
     ...
     ...
     db.init_app(app)
     migrate.init_app(app, db)
     ...
     ...
     return app

# After the extension is initialized, a db group will be added to the command-line options with several sub-commands. 


$ flask db init 	# create a migration repository. This will add a migrations folder to your application.

$ flask db migrate -m "Initial migration." # You can then generate an initial migration

$ flask db upgrade	# Then you can apply the migration to the database
# each time the database models change repeat the migrate and upgrade commands.

$ flask db --help   # To see all the commands that are available

$ flask db list-templates # Shows a list of available database repository templates.

$ flask db downgrade <revision> # Downgrades the database. If revision isn’t given then -1 is assumed.


$ flask db current  # Shows the current revision of the database.

$ flask db history  # Shows the list of migrations. If a range isn’t given then the entire history is shown.

flask db show <revision>    # Show the revision denoted by the given symbol.

flask db merge <revisions>  # Merge two revisions together. Creates a new revision file.




'''
Multiple Database Support
'''
# To create a multiple database migration repository, add the --multidb argument to the init command, 
# the migration repository will be set up to track migrations on your main database, 
# and on any additional databases defined in the SQLALCHEMY_BINDS configuration option
$ flask db init --multidb




# REFERENCE: https://flask-migrate.readthedocs.io/en/latest/ 