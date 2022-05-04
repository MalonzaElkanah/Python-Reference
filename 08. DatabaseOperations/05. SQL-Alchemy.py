
'''
The SQLAlchemy SQL Toolkit and Object Relational Mapper is a comprehensive set of tools 
for working with databases and Python.
'''

#  SQLAlchemy divided into two major section
		# 1. the Object Relational Mapper (ORM) and 
		# 2. the Core.


# 1. Core - This is the foundational architecture for SQLAlchemy as a “database toolkit”. 
			# The library provides tools for managing connectivity to a database, 
			# interacting with database queries and results, and programmatic construction of SQL statements.


# 2. ORM - 	It extends the Core-level SQL Expression Language to allow SQL queries to be composed and 
			# invoked in terms of user-defined objects.
			# This provides an additional configuration layer allowing user-defined Python classes to be mapped 
			# to database tables and other constructs, as well as an object persistence mechanism known as the Session. 




'''
			# Installing SQL Alchemy
'''
$ pip install SQLAlchemy

# Checking the Installed SQLAlchemy Version
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
2.0.0


'''
			Establishing Connectivity - the Engine
'''
# The start of any SQLAlchemy application is an object called the Engine. This object acts as a central source
# of connections to a particular database, providing both a factory as well as a holding space 
# called a connection pool for these database connections.

>>> from sqlalchemy import create_engine
>>> engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

# 1. The "sqlite+pysqlite:///:memory:" String url contains three parts:
		# 1.1 sqlite 	- we are connecting to sqlite databse
		# 1.2 pysqlite 	- In this part we are mentioning the DBA we are using. Example pysqlite for sqlite3 lib
		# 1.3 /:memory: - Location of database. Example this is an IN-memory DB. 

# 2. create_engine.echo - instruct the Engine to log all of the SQL it emits to a Python logger that will write to standard out.  


'''
			Getting a Connection
'''
# The purpose of the Engine object is to provide a unit of connectivity to the database called the Connection.
# Working with the Core directly, the Connection object is how all interaction with the database is done.
>>> from sqlalchemy import text
>>> with engine.connect() as conn:
...     result = conn.execute(text("select 'hello world'"))
...     print(result.all())


'''
			Committing Changes
'''
# The transaction is not committed automatically; To commit data we normally need to call Connection.commit()
>>> with engine.connect() as conn:
...     conn.execute(text("CREATE TABLE some_table (x int, y int)"))
...     conn.execute(
...         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
...         [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
...     )
...     conn.commit()


# There is also another style of committing data, we use the Engine.begin() method to acquire the connection. 
# This method will both manage the scope of the Connection and also enclose everything inside of a transaction 
# with COMMIT at the end, assuming a successful block, or ROLLBACK in case of exception raise. 
>>> with engine.begin() as conn:
...     conn.execute(
...         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
...         [{"x": 6, "y": 8}, {"x": 9, "y": 10}]
...     )


'''
			Fetching Rows
'''
>>> with engine.connect() as conn:
...     result = conn.execute(text("SELECT x, y FROM some_table"))
...     for row in result:
...         print(f"x: {row.x}  y: {row.y}")


'''
			Parameters
'''
>>> with engine.connect() as conn:
...     result = conn.execute(
...         text("SELECT x, y FROM some_table WHERE y > :y"),
...         {"y": 2}
...     )
...     for row in result:
...        print(f"x: {row.x}  y: {row.y}")

#  INSERT multiple rows into the database at once
>>> with engine.connect() as conn:
...     conn.execute(
...         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
...         [{"x": 11, "y": 12}, {"x": 13, "y": 14}]
...     )
...     conn.commit()

# Bundling Parameters with a Statement
>>> stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=6)
>>> with engine.connect() as conn:
...     result = conn.execute(stmt)
...     for row in result:
...        print(f"x: {row.x}  y: {row.y}")



'''
			Executing with an ORM Session
'''
# The fundamental transactional / database interactive object when using the ORM is called the Session.
>>> from sqlalchemy.orm import Session

>>> stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=6)
>>> with Session(engine) as session:
...     result = session.execute(stmt)
...     for row in result:
...        print(f"x: {row.x}  y: {row.y}")

# Commits as you go
with Session(engine) as session:
...     result = session.execute(
...         text("UPDATE some_table SET y=:y WHERE x=:x"),
...         [{"x": 9, "y":11}, {"x": 13, "y": 15}]
...     )
...     session.commit()




'''
			Working with Database Metadata
'''
# The most common foundational objects for database metadata in SQLAlchemy are known as 
		# 1. MetaData, 
		# 2. Table, and
		# 3. Column
# 1. MetaData object -  a Python dictionary that stores a series of Table objects keyed to their string name. 

# 2. Table - represents a database table and assigns itself to a MetaData collection.

# 3. Column	- represents a column in a database table, and assigns itself to a Table object. 
			# The Column usually includes a string name and a type object. 
# 4. Integer, String - these classes represent SQL datatypes and can be passed to a Column with or 
			# without necessarily being instantiated. 

# Declaring Metadata object
>>> from sqlalchemy import MetaData
>>> metadata_obj = MetaData()

# Once we have a MetaData object, we can declare some Table objects.
>>> from sqlalchemy import Table, Column, Integer, String
>>> user_table = Table(
...     "user_account",
...     metadata_obj,
...     Column('id', Integer, primary_key=True),
...     Column('name', String(30)),
...     Column('fullname', String)
... )
# Above, we want to give a length of “30” to the “name” column, so we instantiated String(30). 
# But for “id” and “fullname” we did not specify these, so we can send the class itself.

>>> user_table.c.name
Column('name', String(length=30), table=<user_account>)

>>> user_table.c.keys()
['id', 'name', 'fullname']

# Declaring Simple Constraints
	# - PrimaryKeyConstraint 
	# - ForeignKeyConstraint 

>>> user_table.primary_key
PrimaryKeyConstraint(Column('id', Integer(), table=<user_account>, primary_key=True, nullable=False))

>>> from sqlalchemy import ForeignKey
>>> address_table = Table(
...     "address",
...     metadata_obj,
...     Column('id', Integer, primary_key=True),
...     Column('user_id', ForeignKey('user_account.id'), nullable=False),
...     Column('email_address', String, nullable=False)
... )


# MetaData.create_all() - emit CREATE TABLE statements/DDL, to our database so that we can insert/query data from them. 
>>> metadata_obj.create_all(engine)

# MetaData.drop_all() - a method that will emit DROP statements in order to drop schema elements.



'''
			Defining Table Metadata with the ORM
'''
# When using the ORM, the process by which we declare Table metadata is usually combined with 
# the process of declaring mapped classes. The mapped class is any Python class we’d like to create,
# which will then have attributes on it that will be linked to the columns in a database table.  


# Setting up the Registry¶

# The MetaData collection object of ORM is known as the registry. 

>>> from sqlalchemy.orm import registry
>>> mapper_registry = registry()

# MetaData object that will store a collection of Table objects:
>>> mapper_registry.metadata
MetaData()

# We will declare Tables indirectly through directives applied to our mapped classes. 
# Each mapped class descends from a common base class known as the declarative base. 
# We get a new declarative base from the registry using the registry.generate_base() method:
>>> Base = mapper_registry.generate_base()

# The steps of creating the registry and “declarative base” classes can be combined into one step using 
# declarative_base() function.
from sqlalchemy.orm import declarative_base
Base = declarative_base()


# Declaring Mapped Classes
>>> from sqlalchemy.orm import relationship
>>> class User(Base):
...     __tablename__ = 'user_account'
...
...     id = Column(Integer, primary_key=True)
...     name = Column(String(30))
...     fullname = Column(String)
...
...     addresses = relationship("Address", back_populates="user")
...
...     def __repr__(self):
...        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

>>> class Address(Base):
...     __tablename__ = 'address'
...
...     id = Column(Integer, primary_key=True)
...     email_address = Column(String, nullable=False)
...     user_id = Column(Integer, ForeignKey('user_account.id'))
...
...     user = relationship("User", back_populates="addresses")
...
...     def __repr__(self):
...         return f"Address(id={self.id!r}, email_address={self.email_address!r})"


# We can see these Table objects from a declarative mapped class using the .__table__ attribute:

>>> User.__table__
Table('user_account', MetaData(),
    Column('id', Integer(), table=<user_account>, primary_key=True, nullable=False),
    Column('name', String(length=30), table=<user_account>),
    Column('fullname', String(), table=<user_account>), schema=None)



# emit CREATE statements given ORM registry
mapper_registry.metadata.create_all(engine)

# the identical MetaData object is also present on the declarative base
Base.metadata.create_all(engine)



'''
			Inserting Rows with Core
'''

'''
			Selecting Rows with Core or ORM
'''

'''
			Updating and Deleting Rows with Core
'''



'''
			Data Manipulation with the ORM
'''



'''
    		Inserting Rows with the ORM
'''
# Instances of Classes represent Rows
>>> squidward = User(name="squidward", fullname="Squidward Tentacles")
>>> krabs = User(name="ehkrabs", fullname="Eugene H. Krabs")
>>> squidward
User(id=None, name='squidward', fullname='Squidward Tentacles')

# Adding objects to a Session
>>> session = Session(engine)
>>> session.add(squidward)
>>> session.add(krabs)
# When we have pending objects, we can see this state by looking at a collection on the Session called Session.new:
>>> session.new
IdentitySet([User(id=None, name='squidward', fullname='Squidward Tentacles'), User(id=None, name='ehkrabs', fullname='Eugene H. Krabs')])

# Flushing -  emit SQL to the database to push out the current set of changes.
# The transaction remains open until we call any of the Session.commit(), Session.rollback(), or Session.close() methods of Session.
>>> session.flush()

# Autogenerated primary key attributes
>>> squidward.id
4
>>> krabs.id
5

# Identity Map -  The identity map is an in-memory store that links all objects currently loaded in memory to their primary key identity.
>>> some_squidward = session.get(User, 4)
>>> some_squidward
User(id=4, name='squidward', fullname='Squidward Tentacles')
#  the some_squidward refers to the same object as that of squidward previously
>>> some_squidward is squidward
True

# Committing
>>> session.commit()
COMMIT


'''
    		Updating ORM Objects

'''
# Supposing we loaded the User object for the username sandy into a transaction
>>> sandy = session.execute(select(User).filter_by(name="sandy")).scalar_one()
>>> sandy
User(id=2, name='sandy', fullname='Sandy Cheeks')
# If we alter the attributes of this object, the Session tracks this change
>>> sandy.fullname = "Sandy Squirrel"
# The object appears in a collection called Session.dirty, indicating the object is “dirty”
>>> sandy in session.dirty
True
# flush occurs automatically before we emit any SELECT(autoflush).
# We can query directly for the User.fullname column from this row and we will get our updated value back
>>> sandy_fullname = session.execute(
...     select(User.fullname).where(User.id == 2)
... ).scalar_one()

>>> print(sandy_fullname)
Sandy Squirrel
>>> sandy in session.dirty
False

'''
        ORM-enabled UPDATE statements
'''
>>> session.execute(
...     update(User).
...     where(User.name == "sandy").
...     values(fullname="Sandy Squirrel Extraordinaire")
... )
>>> sandy.fullname
'Sandy Squirrel Extraordinaire'


'''
    Deleting ORM Objects
'''
>>> patrick = session.get(User, 3)
>>> session.delete(patrick)
>>> session.execute(select(User).where(User.name == "patrick")).first()
>>> patrick in session
False


'''
        ORM-enabled DELETE Statements
'''
>>> squidward = session.get(User, 4)
>>> session.execute(delete(User).where(User.name == "squidward"))
>>> squidward in session
False


'''
    Rolling Back
'''
>>> session.rollback()
ROLLBACK

>>> sandy.__dict__
{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x...>}

>>> sandy.fullname
'Sandy Cheeks'

# We may now observe that the full database row was also populated into the __dict__ of the sandy object:
>>> sandy.__dict__  
{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x...>,
 'id': 2, 'name': 'sandy', 'fullname': 'Sandy Cheeks'}

# For deleted objects, when we earlier noted that patrick was no longer in the session, that object’s identity is also restored
>>> patrick in session
True

# and of course the database data is present again as well:
>>> session.execute(select(User).where(User.name == 'patrick')).scalar_one() is patrick

'''
    Closing a Session
'''
>>> session.close()



'''
				Working with Related Objects
'''
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = 'user_account'

    # ... Column mappings

    addresses = relationship("Address", back_populates="user")


class Address(Base):
    __tablename__ = 'address'

    # ... Column mappings

    user = relationship("User", back_populates="addresses")



'''
		# Persisting and Loading Relationships
'''
>>> u1 = User(name='pkrabs', fullname='Pearl Krabs')
>>> u1.addresses
[]
# .Using the list.append() method we may add an Address object:
>>> a1 = Address(email_address="pearl.krabs@gmail.com")
>>> u1.addresses.append(a1)

# At this point, the u1.addresses collection as expected contains the new Address object:
>>> u1.addresses
[Address(id=None, email_address='pearl.krabs@gmail.com')]

>>> a1.user
User(id=None, name='pkrabs', fullname='Pearl Krabs')

>>> a2 = Address(email_address="pearl@aol.com", user=u1)
>>> u1.addresses
[Address(id=None, email_address='pearl.krabs@gmail.com'), Address(id=None, email_address='pearl@aol.com')]
# equivalent effect as a2 = Address(user=u1)
>>> a2.user = u1

'''
        # Cascading Objects into the Session
''' 
# We make use of the Session that’s still ongoing, and note that when we apply the Session.add() method
# to the lead User object, the related Address object also gets added to that same Session:
>>> session.add(u1)
>>> u1 in session
True
>>> a1 in session
True
>>> a2 in session
True    
>>> print(u1.id)
None
>>> print(a1.user_id)
None
session.commit()

# Loading Relationships
>>> u1.id
6
>>> u1.addresses
[Address(id=4, email_address='pearl.krabs@gmail.com'), Address(id=5, email_address='pearl@aol.com')]
>>> a1
Address(id=4, email_address='pearl.krabs@gmail.com')
>>> a2
Address(id=5, email_address='pearl@aol.com')

'''
       Using Relationships in Queries
 

        Using Relationships to Join
        Joining between Aliased targets
        Augmenting the ON Criteria
        EXISTS forms: has() / any()
        Common Relationship Operators
''' 

''''
    Loader Strategies
        Selectin Load
        Joined Load
        Explicit Join + Eager load
        Augmenting Loader Strategy Paths
        Raiseload

'''

