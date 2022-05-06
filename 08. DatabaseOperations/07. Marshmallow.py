'''
            marshmallow
'''
# marshmallow is an ORM/ODM/framework-agnostic library for converting complex datatypes,
# such as objects, to and from native Python datatypes.

# In short, marshmallow schemas can be used to:
    # 1. Validate input data.
    # 2. Deserialize input data to app-level objects.
    # 3. Serialize app-level objects to primitive Python types. 
        # The serialized objects can then be rendered to standard formats such as JSON for use in an HTTP API.


from datetime import date
from pprint import pprint

from marshmallow import Schema, fields


class ArtistSchema(Schema):
    name = fields.Str()


class AlbumSchema(Schema):
    title = fields.Str()
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema())


bowie = dict(name="David Bowie")
album = dict(artist=bowie, title="Hunky Dory", release_date=date(1971, 12, 17))

schema = AlbumSchema()
result = schema.dump(album)
pprint(result, indent=2)
# { 'artist': {'name': 'David Bowie'},
#   'release_date': '1971-12-17',
#   'title': 'Hunky Dory'}



'''
            Installtion
'''
$ pip install -U marshmallow


'''
            Quickstart - Declaring Schemas
'''
# Let’s start with a basic user “model”.
import datetime as dt


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return "<User(name={self.name!r})>".format(self=self)

# Create a schema by defining a class with variables mapping attribute names to Field objects.
from marshmallow import Schema, fields


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

# You can create a schema from a dictionary of fields using the from_dict method.
from marshmallow import Schema, fields

UserSchema = Schema.from_dict(
    {"name": fields.Str(), "email": fields.Email(), "created_at": fields.DateTime()}
)


'''
            Serializing Objects (“Dumping”)
'''
# Serialize objects by passing them to your schema’s dump method, which returns the formatted result.
from pprint import pprint

user = User(name="Monty", email="monty@python.org")
schema = UserSchema()
result = schema.dump(user)
pprint(result)
# {"name": "Monty",
#  "email": "monty@python.org",
#  "created_at": "2014-08-17T14:54:16.049594+00:00"}


# You can also serialize to a JSON-encoded string using dumps.
json_result = schema.dumps(user)
pprint(json_result)
# '{"name": "Monty", "email": "monty@python.org", "created_at": "2014-08-17T14:54:16.049594+00:00"}'


'''
            Filtering Output
'''
# You can specify which fields to output with the only parameter.
summary_schema = UserSchema(only=("name", "email"))
summary_schema.dump(user)
# {"name": "Monty", "email": "monty@python.org"}
# You can also exclude fields by passing in the exclude parameter.



'''
            Deserializing Objects (“Loading”)
'''
# The load method validates and deserializes an input dictionary to an application-level data structure.
# By default, load will return a dictionary of field names mapped to deserialized values 
# (or raise a ValidationError with a dictionary of validation errors, which we’ll revisit later).

from pprint import pprint

user_data = {
    "created_at": "2014-08-11T05:26:03.869245",
    "email": "ken@yahoo.com",
    "name": "Ken",
}
schema = UserSchema()
result = schema.load(user_data)
pprint(result)
# {'name': 'Ken',
#  'email': 'ken@yahoo.com',
#  'created_at': datetime.datetime(2014, 8, 11, 5, 26, 3, 869245)},


'''
        Deserializing to Objects
'''
# In order to deserialize to an object, define a method of your Schema and decorate it with post_load. 
# The method receives a dictionary of deserialized data.

from marshmallow import Schema, fields, post_load


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)

# Now, the load method return a User instance.
user_data = {"name": "Ronnie", "email": "ronnie@stones.com"}
schema = UserSchema()
result = schema.load(user_data)
print(result)  # => <User(name='Ronnie')>


'''
        Handling Collections of Objects
'''
# Set many=True when dealing with iterable collections of objects.

user1 = User(name="Mick", email="mick@stones.com")
user2 = User(name="Keith", email="keith@stones.com")
users = [user1, user2]
schema = UserSchema(many=True)
result = schema.dump(users)  # OR UserSchema().dump(users, many=True)
pprint(result)
# [{'name': u'Mick',
#   'email': u'mick@stones.com',
#   'created_at': '2014-08-17T14:58:57.600623+00:00'}
#  {'name': u'Keith',
#   'email': u'keith@stones.com',
#   'created_at': '2014-08-17T14:58:57.600623+00:00'}]


'''
            Validation
'''
# Schema.load() and Schema.loads() raises a ValidationError error when invalid data are passed in.
# You can access the dictionary of validation errors from the ValidationError.messages attribute.
# The data that were correctly deserialized are accessible in ValidationError.valid_data.
# Some fields, such as the Email and URL fields, have built-in validation.

from marshmallow import ValidationError

try:
    result = UserSchema().load({"name": "John", "email": "foo"})
except ValidationError as err:
    print(err.messages)  # => {"email": ['"foo" is not a valid email address.']}
    print(err.valid_data)  # => {"name": "John"}

# When validating a collection, the errors dictionary will be keyed on the indices of invalid items.

from pprint import pprint

from marshmallow import Schema, fields, ValidationError


class BandMemberSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email()


user_data = [
    {"email": "mick@stones.com", "name": "Mick"},
    {"email": "invalid", "name": "Invalid"},  # invalid email
    {"email": "keith@stones.com", "name": "Keith"},
    {"email": "charlie@stones.com"},  # missing "name"
]

try:
    BandMemberSchema(many=True).load(user_data)
except ValidationError as err:
    pprint(err.messages)
    # {1: {'email': ['Not a valid email address.']},
    #  3: {'name': ['Missing data for required field.']}}


# You can perform additional validation for a field by passing the validate argument.
# There are a number of built-in validators in the marshmallow.validate module.
from pprint import pprint

from marshmallow import Schema, fields, validate, ValidationError


class UserSchema(Schema):
    name = fields.Str(validate=validate.Length(min=1))
    permission = fields.Str(validate=validate.OneOf(["read", "write", "admin"]))
    age = fields.Int(validate=validate.Range(min=18, max=40))


in_data = {"name": "", "permission": "invalid", "age": 71}
try:
    UserSchema().load(in_data)
except ValidationError as err:
    pprint(err.messages)
    # {'age': ['Must be greater than or equal to 18 and less than or equal to 40.'],
    #  'name': ['Shorter than minimum length 1.'],
    #  'permission': ['Must be one of: read, write, admin.']}


# You may implement your own validators. A validator is a callable that accepts a single argument,
# the value to validate. If validation fails, the callable should raise a ValidationError with a useful
# error message or return False (for a generic error message).

from marshmallow import Schema, fields, ValidationError


def validate_quantity(n):
    if n < 0:
        raise ValidationError("Quantity must be greater than 0.")
    if n > 30:
        raise ValidationError("Quantity must not be greater than 30.")


class ItemSchema(Schema):
    quantity = fields.Integer(validate=validate_quantity)


in_data = {"quantity": 31}
try:
    result = ItemSchema().load(in_data)
except ValidationError as err:
    print(err.messages)  # => {'quantity': ['Quantity must not be greater than 30.']}

'''
            Field Validators as Methods
'''
# It is sometimes convenient to write validators as methods.
# Use the validates decorator to register field validator methods.
from marshmallow import fields, Schema, validates, ValidationError


class ItemSchema(Schema):
    quantity = fields.Integer()

    @validates("quantity")
    def validate_quantity(self, value):
        if value < 0:
            raise ValidationError("Quantity must be greater than 0.")
        if value > 30:
            raise ValidationError("Quantity must not be greater than 30.")



'''
        Required Fields
'''

# Make a field required by passing required=True.
# An error will be raised if the the value is missing from the input to Schema.load().

# To customize the error message for required fields, pass a dict with a required key as
# the error_messages argument for the field.

from pprint import pprint

from marshmallow import Schema, fields, ValidationError


class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True, error_messages={"required": "Age is required."})
    city = fields.String(
        required=True,
        error_messages={"required": {"message": "City required", "code": 400}},
    )
    email = fields.Email()


try:
    result = UserSchema().load({"email": "foo@bar.com"})
except ValidationError as err:
    pprint(err.messages)
    # {'age': ['Age is required.'],
    # 'city': {'code': 400, 'message': 'City required'},
    # 'name': ['Missing data for required field.']}


'''
            Partial Loading
'''
# When using the same schema in multiple places, you may only want to skip required validation by passing partial.
class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True)


result = UserSchema().load({"age": 42}, partial=("name",)) # OR UserSchema(partial=('name',)).load({'age': 42})
print(result)  # => {'age': 42}

# You can ignore missing fields entirely by setting partial=True.
class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True)


result = UserSchema().load({"age": 42}, partial=True)
# OR UserSchema(partial=True).load({'age': 42})
print(result)  # => {'age': 42}



'''
        Specifying Defaults
'''
# load_default specifies the default deserialization value for a field.
# Likewise, dump_default specifies the default serialization value.

class UserSchema(Schema):
    id = fields.UUID(load_default=uuid.uuid1)
    birthdate = fields.DateTime(dump_default=dt.datetime(2017, 9, 29))


UserSchema().load({})
# {'id': UUID('337d946c-32cd-11e8-b475-0022192ed31b')}
UserSchema().dump({})
# {'birthdate': '2017-09-29T00:00:00+00:00'}


'''
        Handling Unknown Fields
'''
# By default, load will raise a ValidationError if it encounters a key with no matching Field in the schema.
# This behavior can be modified with the unknown option, which accepts one of the following:

Unknown_Option='''
    RAISE (default):    raise a ValidationError if there are any unknown fields

    EXCLUDE:            exclude unknown fields

    INCLUDE:            accept and include the unknown fields
'''

# You can specify unknown in the class Meta of your Schema,
from marshmallow import Schema, INCLUDE


class UserSchema(Schema):
    class Meta:
        unknown = INCLUDE

# at instantiation time,
schema = UserSchema(unknown=INCLUDE)

# or when calling load.
UserSchema().load(data, unknown=INCLUDE)

'''
        Validation Without Deserialization
'''
# If you only need to validate input data (without deserializing to an object), you can use Schema.validate().

errors = UserSchema().validate({"name": "Ronnie", "email": "invalid-email"})
print(errors)  # {'email': ['Not a valid email address.']}
'''
        “Read-only” and “Write-only” Fields
'''
# dump_only and load_only parameters are conceptually equivalent to “read-only” and “write-only” fields
class UserSchema(Schema):
    name = fields.Str()
    # password is "write-only"
    password = fields.Str(load_only=True)
    # created_at is "read-only"
    created_at = fields.DateTime(dump_only=True)


'''
        Specifying Serialization/Deserialization Keys
'''
# Schemas will (de)serialize an input dictionary from/to an output dictionary whose keys are identical
# to the field names. If you are consuming and producing data that does not match your schema,
# you can specify the output keys via the data_key argument.

class UserSchema(Schema):
    name = fields.String()
    email = fields.Email(data_key="emailAddress")


s = UserSchema()

data = {"name": "Mike", "email": "foo@bar.com"}
result = s.dump(data)
# {'name': u'Mike',
# 'emailAddress': 'foo@bar.com'}

data = {"name": "Mike", "emailAddress": "foo@bar.com"}
result = s.load(data)
# {'name': u'Mike',
# 'email': 'foo@bar.com'}


'''
        Ordering Output
'''
# To maintain field ordering, set the ordered option to True.
# This will instruct marshmallow to serialize data to a collections.OrderedDict.

from collections import OrderedDict
from pprint import pprint

from marshmallow import Schema, fields


class UserSchema(Schema):
    first_name = fields.String()
    last_name = fields.String()
    email = fields.Email()

    class Meta:
        ordered = True


u = User("Charlie", "Stones", "charlie@stones.com")
schema = UserSchema()
result = schema.dump(u)
assert isinstance(result, OrderedDict)
pprint(result, indent=2)
#  OrderedDict([('first_name', 'Charlie'),
#              ('last_name', 'Stones'),
#              ('email', 'charlie@stones.com')])


'''
                Nesting Schemas
'''
# Schemas can be nested to represent relationships between objects (e.g. foreign key relationships).

import datetime as dt


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()
        self.friends = []
        self.employer = None


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author  # A User object


# Use a Nested field to represent the relationship, passing in a nested schema.
from marshmallow import Schema, fields


class UserSchema(Schema):
    name = fields.String()
    email = fields.Email()
    created_at = fields.DateTime()


class BlogSchema(Schema):
    title = fields.String()
    author = fields.Nested(UserSchema)

# The serialized blog will have the nested user representation.
from pprint import pprint

user = User(name="Monty", email="monty@python.org")
blog = Blog(title="Something Completely Different", author=user)
result = BlogSchema().dump(blog)
pprint(result)
# {'title': u'Something Completely Different',
#  'author': {'name': u'Monty',
#             'email': u'monty@python.org',
#             'created_at': '2014-08-17T14:58:57.600623+00:00'}}


# If the field is a collection of nested objects, pass the Nested field to List.
collaborators = fields.List(fields.Nested(UserSchema))


'''
            Specifying Which Fields to Nest
'''
# You can explicitly specify which attributes of the nested objects you want to
# (de)serialize with the only argument to the schema.

class BlogSchema2(Schema):
    title = fields.String()
    author = fields.Nested(UserSchema(only=("email",)))


schema = BlogSchema2()
result = schema.dump(blog)
pprint(result)
# {
#     'title': u'Something Completely Different',
#     'author': {'email': u'monty@python.org'}
# }


# Dotted paths may be passed to only and exclude to specify nested attributes.
class SiteSchema(Schema):
    blog = fields.Nested(BlogSchema2)


schema = SiteSchema(only=("blog.author.email",))
result = schema.dump(site)
pprint(result)
# {
#     'blog': {
#         'author': {'email': u'monty@python.org'}
#     }
# }


# You can replace nested data with a single value (or flat list of values if many=True) using the Pluck field.
class UserSchema(Schema):
    name = fields.String()
    email = fields.Email()
    friends = fields.Pluck("self", "name", many=True)


# ... create ``user`` ...
serialized_data = UserSchema().dump(user)
pprint(serialized_data)
# {
#     "name": "Steve",
#     "email": "steve@example.com",
#     "friends": ["Mike", "Joe"]
# }
deserialized_data = UserSchema().load(result)
pprint(deserialized_data)
# {
#     "name": "Steve",
#     "email": "steve@example.com",
#     "friends": [{"name": "Mike"}, {"name": "Joe"}]
# 


# Partial Loading - Nested schemas also inherit the partial parameter of the parent load call.
class UserSchemaStrict(Schema):
    name = fields.String(required=True)
    email = fields.Email()
    created_at = fields.DateTime(required=True)


class BlogSchemaStrict(Schema):
    title = fields.String(required=True)
    author = fields.Nested(UserSchemaStrict, required=True)


schema = BlogSchemaStrict()
blog = {"title": "Something Completely Different", "author": {}}
result = schema.load(blog, partial=True)
pprint(result)
# {'author': {}, 'title': 'Something Completely Different'}


# You can specify a subset of the fields to allow partial loading using dot delimiters.
author = {"name": "Monty"}
blog = {"title": "Something Completely Different", "author": author}
result = schema.load(blog, partial=("title", "author.created_at"))
pprint(result)
# {'author': {'name': 'Monty'}, 'title': 'Something Completely Different'}

'''
            Two-way Nesting
'''
# If you have two objects that nest each other, you can pass a callable to Nested.
# This allows you to resolve order-of-declaration issues,
# such as when one schema nests a schema that is declared below it.

class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()

    # Make sure to use the 'only' or 'exclude'
    # to avoid infinite recursion
    author = fields.Nested(lambda: AuthorSchema(only=("id", "title")))


class AuthorSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()

    books = fields.List(fields.Nested(BookSchema(exclude=("author",))))

from marshmallow import pprint
from mymodels import Author, Book

author = Author(name="William Faulkner")
book = Book(title="As I Lay Dying", author=author)
book_result = BookSchema().dump(book)
pprint(book_result, indent=2)
# {
#   "id": 124,
#   "title": "As I Lay Dying",
#   "author": {
#     "id": 8,
#     "name": "William Faulkner"
#   }
# }

author_result = AuthorSchema().dump(author)
pprint(author_result, indent=2)
# {
#   "id": 8,
#   "name": "William Faulkner",
#   "books": [
#     {
#       "id": 124,
#       "title": "As I Lay Dying"
#     }
#   ]
# }

# You can also pass a class name as a string to Nested.
# This is useful for avoiding circular imports when your schemas are located in different modules.

# books.py
from marshmallow import Schema, fields


class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()

    author = fields.Nested("AuthorSchema", only=("id", "title"))

# authors.py
from marshmallow import Schema, fields


class AuthorSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()

    books = fields.List(fields.Nested("BookSchema", exclude=("author",)))


# If you have multiple schemas with the same class name, you must pass the full, module-qualified path.
author = fields.Nested("authors.BookSchema", only=("id", "title"))


# Nesting A Schema Within Itself
# If the object to be marshalled has a relationship to an object of the same type,
# you can nest the Schema within itself by passing a callable that returns an instance of the same schema.

class UserSchema(Schema):
    name = fields.String()
    email = fields.Email()
    # Use the 'exclude' argument to avoid infinite recursion
    employer = fields.Nested(lambda: UserSchema(exclude=("employer",)))
    friends = fields.List(fields.Nested(lambda: UserSchema()))


user = User("Steve", "steve@example.com")
user.friends.append(User("Mike", "mike@example.com"))
user.friends.append(User("Joe", "joe@example.com"))
user.employer = User("Dirk", "dirk@example.com")
result = UserSchema().dump(user)
pprint(result, indent=2)
# {
#     "name": "Steve",
#     "email": "steve@example.com",
#     "friends": [
#         {
#             "name": "Mike",
#             "email": "mike@example.com",
#             "friends": [],
#             "employer": null
#         },
#         {
#             "name": "Joe",
#             "email": "joe@example.com",
#             "friends": [],
#             "employer": null
#         }
#     ],
#     "employer": {
#         "name": "Dirk",
#         "email": "dirk@example.com",
#         "friends": []
#     }
# }



