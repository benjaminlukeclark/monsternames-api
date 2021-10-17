import models
import logging
logger = logging.getLogger(__name__)
syslog = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(app_name)s : %(message)s')
logger.addHandler(syslog)

models.db.connect()

logging.info("Connected to DB")

models.ApiKeys.create(apiKey="helloworld", user="ci_test")

logging.info("Created CI user")

