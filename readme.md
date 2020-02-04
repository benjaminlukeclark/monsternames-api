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

# Usage

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



## DB Data Entry


# Endpoints

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
someLaptop:~/Documents/Development/monsternames-api$ curl -i http://127.0.0.1:5000/api/v1.0/goatmen
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

Requires a ```x-www-form-urlencoded``` body with the following key value pair:

```
firstName=NAME
```

For example:

```bash
someLaptop:~/Documents/Development/monsternames-api$ curl -d "firstName=SomeGuy" -X POST http://127.0.0.1:5000/api/v1.0/goatmen
{
  "message": "New record created", 
  "name": "SomeGuy"
}
```

## /api/v1.0/goblin

## /api/v1.0/ogre

## /api/v1.0/orc

## /api/v1.0/skeleton

## /api/v1.0/troll
