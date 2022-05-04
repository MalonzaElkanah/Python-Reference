'''
		1.	flask-sqlalchemy
'''

# Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy to your application. 
# It aims to simplify using SQLAlchemy with Flask by providing useful defaults and extra helpers
# that make it easier to accomplish common tasks.


'''
		2. Installation
'''
$ pip install -U Flask-SQLAlchemy


'''
		3. A Minimal Application¶
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# To create the initial database, just import the db object from an interactive Python shell and
# run the SQLAlchemy.create_all() method to create the tables and database:
>>> from yourapplication import db
>>> db.create_all()

# Now to create some users
>>> from yourapplication import User
>>> admin = User(username='admin', email='admin@example.com')
>>> guest = User(username='guest', email='guest@example.com')

# But they are not yet in the database, so let’s make sure they are:
>>> db.session.add(admin)
>>> db.session.add(guest)
>>> db.session.commit()

# Accessing the data in database is easy as a pie:
>>> User.query.all()
[<User u'admin'>, <User u'guest'>]
>>> User.query.filter_by(username='admin').first()
<User u'admin'>


'''
			# Simple Relationships
'''
from datetime import datetime


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
        nullable=False)
    category = db.relationship('Category',
        backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name


# First let’s create some objects
>>> py = Category(name='Python')
>>> Post(title='Hello Python!', body='Python is pretty cool', category=py)
>>> p = Post(title='Snakes', body='Ssssssss')
>>> py.posts.append(p)
>>> db.session.add(py)
# Accessing them will load them from the database since the relationship is lazy-loaded
>>> py.posts
[<Post 'Hello Python!'>, <Post 'Snakes'>]

# If you wanted a single query to load all categories and their posts, you could do it like this:
>>> from sqlalchemy.orm import joinedload
>>> query = Category.query.options(joinedload('posts'))
>>> for category in query:
...     print category, category.posts
<Category u'Python'> [<Post u'Hello Python!'>, <Post u'Snakes'>]

# If you want to get a query object for that relationship, you can do so using with_parent().
# Let’s exclude that post about Snakes for example:
>>> Post.query.with_parent(py).filter(Post.title != 'Snakes').all()
[<Post 'Hello Python!'>]



# The types of the column are the first argument to Column. 
# You can either provide them directly or call them to further specify them (like providing a length).
# The following types are the most common:
TYPE_OF_COLUMN = '''

Integer 		- 	an integer

String(size) 	-	a string with a maximum length (optional in some databases, e.g. PostgreSQL)

Text			-	some longer unicode text

DateTime		-	date and time expressed as Python datetime object.

Float 			-	stores floating point values

Boolean			- 	stores a boolean value

PickleType		- 	stores a pickled Python object

LargeBinary		-	stores large arbitrary binary data

'''


'''
			Many-to-Many Relationships
'''

# If you want to use many-to-many relationships you will need to define a helper table that is used for
# the relationship. For this helper table it is strongly recommended to not use a model but an actual table

tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True)
)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship('Tag', secondary=tags, lazy='subquery',
        backref=db.backref('pages', lazy=True))

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)


