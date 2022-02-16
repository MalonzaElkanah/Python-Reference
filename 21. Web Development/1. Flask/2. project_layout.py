''' GENERAL PROJECT LAYOUT IN FLASK


/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in

'''


# flaskr/__init__.py 

''' serves double duty: it will contain the application factory, and it tells Python that 
the flaskr directory should be treated as a package.'''
''' application factory - Instead of creating a Flask instance globally, you will create it inside a function. 
This function is known as the application factory. Any configuration, registration, and other setup 
the application needs will happen inside the function, then the application will be returned. '''


# flaskr/db.py
'''The first thing to do when working with a database is to create a connection to it. 
Any queries and operations are performed using the connection (In this case it is tied to the request), 
which is closed after the work is finished.
'''



# flaskr/schema.sql
'''In SQLite, data is stored in tables and columns. 
These need to be created before you can store and retrieve data. 
'''



# flaskr/auth.py
'''An authentication blueprint. A Blueprint is a way to organize a group of related views and other code. 
Then the blueprint is registered with the application when it is available in the factory function.
'''



# flaskr/blog.py
''' blog view blueprint
'''


# flaskr/template/auth
''' auth view blueprint template
'''

# flaskr/template/blog
''' blog view blueprint template
'''

# flaskr/static/
''' Project static files location
'''

# flaskr/static/style.css
''' CSS file for the project
'''




# setup.py 
'''This file describes your project and the files that belong to it.
'''

# MANIFEST.in 
'''tell what this other data is.'''
