from flask import make_response, jsonify
import database.models as models
from peewee import fn


def verify_user(xApiKey):
    # If there is no xApiKey provided...
    if xApiKey is None:
        raise IndexError
    # Connect to db
    models.db.connect(reuse_if_open=True)
    # Check if the key exists
    apiKeyCheck = models.ApiKeys.select().where(models.ApiKeys.apiKey == xApiKey)
    models.db.close()
    if apiKeyCheck.exists():
        return apiKeyCheck[0].user
    else:
        raise ReferenceError