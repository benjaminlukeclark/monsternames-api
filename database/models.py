import peewee
from peewee import *
from database import dbVars

# Connect to DB
db = MySQLDatabase(dbVars.dbName, host=dbVars.dbHost, port=3306, user=dbVars.dbUser, passwd=dbVars.dbPassword)

##### LIST OF DATABASE MODELS #####

class GoblinFirstName(peewee.Model):
    data = peewee.CharField()

    class Meta:
        database = db

class GoblinLastName(peewee.Model):
    data = peewee.CharField()

    class Meta:
        database = db

class GoatmenFirstName(peewee.Model):
    data = peewee.CharField()

    class Meta:
        database = db

class OgreFirstName(peewee.Model):
    data = peewee.CharField()

    class Meta:
        database = db

class OrcFirstName(peewee.Model):
    data = peewee.CharField()

    class Meta:
        database = db

class OrcLastName(peewee.Model):
    data = peewee.CharField()

    class Meta:
        database = db

class SkeletonFirstName(peewee.Model):
    data = peewee.CharField()

    class Meta:
        database = db

class SkeletonLastName(peewee.Model):
    data = peewee.CharField()

    class Meta:
        database = db

class TrollFirstName(peewee.Model):
    data = peewee.CharField()

    class Meta:
        database = db

class TrollLastName(peewee.Model):
    data = peewee.CharField()

    class Meta:
        database = db
