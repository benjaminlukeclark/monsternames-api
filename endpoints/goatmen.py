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

def insert_name(firstName):
    # Connect to db
    models.db.connect()
    # First check if the record already exists
    if (models.GoatmenFirstName.select().where(models.GoatmenFirstName.data == firstName)).exists():
        return make_response(jsonify({'error' : 'Duplicate record', 'message' : 'Record already exists'}), 400)
    # Insert
    models.GoatmenFirstName.create(data=firstName)
    models.db.commit()
    # Return success
    return make_response(jsonify({'name' : firstName, 'message' : 'New record created'}), 200)