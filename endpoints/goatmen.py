from flask import make_response, jsonify
import database.models as models
from peewee import fn

def return_name():
    # Connect to db
    models.db.connect()
    # Get random record
    names = models.GoatmenFirstName.select().order_by(fn.Rand()).limit(1)
    result = (names[0].data)
    # Disconnect from DB
    models.db.close()
    # Return json data
    return make_response(jsonify({'name' : result}), 200)