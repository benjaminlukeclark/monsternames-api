import json

with open('/etc/config.json') as config_file:
        config = json.load(config_file)

dbHost = config.get('dbHost')
dbName = config.get('dbName')
dbUser = config.get('dbUser')
dbPassword = config.get('dbPwd')