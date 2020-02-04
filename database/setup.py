import peewee
from peewee import *
import models

# Connect to DB
models.db.connect()

# Create tables
models.GoatmenFirstName.create_table()
models.GoblinLastName.create_table()
models.GoatmenFirstName.create_table()
models.OgreFirstName.create_table()
models.OrcFirstName.create_table()
models.OrcLastName.create_table()
models.SkeletonFirstName.create_table()
models.SkeletonLastName.create_table()
models.TrollFirstName.create_table()
models.TrollLastName.create_table()

# Commit new tables
models.db.commit()


