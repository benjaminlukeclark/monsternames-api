import models
import traceback
import logging

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(app_name)s : %(message)s')
logger.addHandler(stream_handler)

logger.info("Attempting DB connection...")
try:
    # Connect to DB
    models.db.connect(reuse_if_open=True)
    # Create tables
    models.GoblinFirstName.create_table()
    models.GoblinLastName.create_table()
    models.GoatmenFirstName.create_table()
    models.OgreFirstName.create_table()
    models.OrcFirstName.create_table()
    models.OrcLastName.create_table()
    models.SkeletonFirstName.create_table()
    models.SkeletonLastName.create_table()
    models.TrollFirstName.create_table()
    models.TrollLastName.create_table()
    models.ApiKeys.create_table()
    models.PostAudit.create_table()

    # Commit new tables
    models.db.commit()

    # Output success
    logger.info("Successfully connected to DB and, if required, created tables.")
except Exception as error:
    logger.error("Unable to connect to DB and/or create tables")
    logger.error(str(error))
    logger.error(traceback())




