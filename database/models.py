import peewee
from peewee import *
try:
    # direct import is for when this is run from setup.py
    import dbVars
except Exception:
    # database.dbVars import is for when this is run from app.py
    import database.dbVars as dbVars


# Connect to DB
db = MySQLDatabase(dbVars.dbName, host=dbVars.dbHost, port=3306, user=dbVars.dbUser, passwd=dbVars.dbPassword)

##### LIST OF DATABASE MODELS #####

class GoblinFirstName(peewee.Model):
    firstName = peewee.CharField()

    class Meta:
        database = db

class GoblinLastName(peewee.Model):
    lastName = peewee.CharField()

    class Meta:
        database = db

class GoatmenFirstName(peewee.Model):
    firstName = peewee.CharField()

    class Meta:
        database = db

class OgreFirstName(peewee.Model):
    firstName = peewee.CharField()

    class Meta:
        database = db

class OrcFirstName(peewee.Model):
    firstName = peewee.CharField()

    class Meta:
        database = db

class OrcLastName(peewee.Model):
    lastName = peewee.CharField()

    class Meta:
        database = db

class SkeletonFirstName(peewee.Model):
    firstName = peewee.CharField()

    class Meta:
        database = db

class SkeletonLastName(peewee.Model):
    lastName = peewee.CharField()

    class Meta:
        database = db

class TrollFirstName(peewee.Model):
    firstName = peewee.CharField()

    class Meta:
        database = db

class TrollLastName(peewee.Model):
    lastName = peewee.CharField()

    class Meta:
        database = db

class ApiKeys(peewee.Model):
    apiKey = peewee.CharField()
    user = peewee.CharField()

    class Meta:
        database = db

class PostAudit(peewee.Model):
    user = peewee.CharField()
    message = peewee.CharField()

    class Meta:
        database = db
