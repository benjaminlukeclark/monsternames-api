# Usage notes

- Querying endpoints with get/post will probably be the main usage
- For mass contribution of data (i.e. my initial port of names from https://github.com/Sudoblark/Butterchase into this) you can quite easily just make a dictionary of data you want to upload then enumerate through it and do post requests on each

# Setup for local development

- clone repo

```bash
git clone https://github.com/Sudoblark/monsternames-api
```

- If not already installed, then install virtualenv

```bash
pip install virtualenv
```

- Ensure terminal is running in virtualenv

```bash
source .env/bin/active
```

- Install requirements in virtualenv

```
pip install -r monsternames-api/requirements.txt
```

## DB Setup for development

After following instructions in setup for local development...

- Change vars in ```monsternames-api/database/dbVars.py``` to point to your DB...

```bash
nano monsternames-api/database/dbVars.py


dbHost = 'url of DB Server'
dbName = 'name of database'
dbUser = 'user'
dbPassword = 'pwd'

```

- Run setup.py to create required tables in database

```bash 
cd monsternames-api
python database/setup.py
```

- For POST of data you'll need to manually create API Keys in the DB and associate with users for auditing purposes

## API

- Run app.py to run a development instance of the API

```bash
python app.py

 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 224-606-382

```

- When running a development version you can see errors etc in the terminal when you try to access endpoints



# Auditing

All POST requests are audited in the postaudit table. The purpose of this information is just so I can track how many awesome things have been contributed, and by who, so i can give shoutouts and make pretty graphs.

```sql
mysql> select * from postaudit;
+----+-----------+--------------------------------------------+
| id | user      | message                                    |
+----+-----------+--------------------------------------------+
|  1 | Ben Clark | GoatmenFirstName record "SomeGuy2" created |
+----+-----------+--------------------------------------------+
1 row in set (0.05 sec)

mysql> 
```




# Endpoints

# POST Notes

All post requests require an x-api-key header and relevent key/value pairs in the body

Failure to provide an x-api-key will result in an error similar to below:

```bash
benjamin@localhost:~/Documents/Development/monsternames-api$ curl -d "firstName=SomeGuy" -X POST http://127.0.0.1:5000/api/v1.0/goatmen
{
  "error": "unauthorised.", 
  "errorMessage": "no x-api-key provided"
}
```

Failure to provide required key/value pairs in the body will result to an error similar to below:

```bash
benjamin@localhost:~/Documents/Development/monsternames-api$ curl -X POST http://127.0.0.1:5000/api/v1.0/goatmen -H "x-api-key:MU123"
{
  "error": "Invalid key error.", 
  "errorMessage": "Ensure firstName key/value is in body"
}
```

## Obtaining an api key
For now you'll need to contact me directly for API Key creation.

## /api/v1.0/goatmen
### GET

Returns a random name for a Goatman. Goatmen names just contain a first name and will return in the following JSON:

```json
{
  "name": "Dave"
}
```

For example: 

```bash
benjamin@localhost:~/Documents/Development/monsternames-api$ curl -i http://127.0.0.1:5000/api/v1.0/goatmen
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 21
Server: Werkzeug/0.16.1 Python/3.6.9
Date: Tue, 04 Feb 2020 23:38:33 GMT

{
  "name": "Dave"
}
```

### POST

Requires a ```x-www-form-urlencoded``` body with the following key value pair: ```firstName=NAME```

Requires a valid x-api-key header. See 'Obtaining an API Key' section for info in how to get a key.

Example POST:

```bash
benjamin@localhost:~/Documents/Development/monsternames-api$ curl -d "firstName=SomeGuy2" -X POST http://127.0.0.1:5000/api/v1.0/goatmen -H "x-api-key:MU123"
{
  "message": "New record created", 
  "name": "SomeGuy2"
}

```

## /api/v1.0/goblin

## /api/v1.0/ogre

## /api/v1.0/orc

## /api/v1.0/skeleton

## /api/v1.0/troll

