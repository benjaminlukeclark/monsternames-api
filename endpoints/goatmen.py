from flask import make_response, jsonify
import database.models as models
from peewee import fn

# Connect to db
models.db.connect()

def return_name():
    # Connect to db
    models.db.connect()
    # Get random record
    nameQuery = models.GoatmenFirstName.select().order_by(fn.Rand()).limit(1)
    print(nameQuery.data)
    # Disconnect from DB
    models.db.close()
    # Return json data
    #return make_response(jsonify({'name': name}), 200)
    return "Hello"