import peewee
from peewee import *

# Connect to DB
db = MySQLDatabase(vars.dbName, user=vars.dbPassword, passwd=vars.dbUser)

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
