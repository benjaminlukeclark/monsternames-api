from flask import make_response, jsonify
import database.models as models

# Connect to db
models.db.connect()