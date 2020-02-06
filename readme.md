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

- Setup env vars for connection to DB:

```bash
benjamin@localhost:~/Documents/Development/monsternames-api$ export dbHost='test-db-2.cflabebiquae.eu-west-2.rds.amazonaws.com'
benjamin@localhost:~/Documents/Development/monsternames-api$ export dbName='dev'
benjamin@localhost:~/Documents/Development/monsternames-api$ export dbUser='admin'
benjamin@localhost:~/Documents/Development/monsternames-api$ export dbPwd='HelloWorld'
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

# POST Notes

All post requests require an x-api-key header and relevent key/value pairs in the body

Failure to provide an x-api-key will result in an error similar to below:

```bash
benjamin@localhost:~/Documents/Development/monsternames-api$ curl -d "firstName=SomeGuy" -X POST http://127.0.0.1:5000/api/v1.0/goatmen/firstName
{
  "error": "unauthorised.", 
  "errorMessage": "no x-api-key provided"
}
```

Failure to provide required key/value pairs in the body will result to an error similar to below:

```bash
benjamin@localhost:~/Documents/Development/monsternames-api$ curl -X POST http://127.0.0.1:5000/api/v1.0/goatmen/firstName -H "x-api-key:MU123"
{
  "error": "Invalid key error.", 
  "errorMessage": "Ensure firstName key/value is in body"
}
```

## Obtaining an api key
For now you'll need to contact me directly for API Key creation.

# Mass upload example

If you're particularly taken with inspiration. A mass upload via a bash script is relatively easy:

```bash
## declare an array variable
declare -a goatmenarr=("Squiggles" "Fluffy" "Sparkles" "Rover" "Skip" "Dots" "Mittens" "Trixie" "Bubbles" "Giggles" "Floof" "Peaches" "Oreo" "Pebbles" "Polly" "Precious")

## now loop through the above array
for i in "${goatmenarr[@]}"
do
   curl -d "firstName=$i" -X POST http://127.0.0.1:5000/api/v1.0/goatmen/firstName -H "x-api-key:MU123"
   # or do whatever with individual element of the array
done
```

# Endpoints
## /api/v1.0/goatmen
### GET

Returns a random name for a Goatman. Goatmen names just contain a first name. See below for an example:

```bash
curl http://127.0.0.1:5000/api/v1.0/goatmen
{
  "firstName": "Oreo"
}
```

## /api/v1.0/goatmen/firstName
### POST

Requires a ```x-www-form-urlencoded``` body with the following key value pair: ```firstName=NAME```

Requires a valid x-api-key header. See 'Obtaining an API Key' section for info in how to get a key.

Sending a post request will add another goatman first name value to the database. See below for an example:

```bash
curl -d "firstName=$i" -X POST http://127.0.0.1:5000/api/v1.0/goatmen/firstName -H "x-api-key:MU123"
```

## /api/v1.0/goblin
### GET

Returns a random name for a Goblin. Goblins have first names, last names and full names. See an example below:

```bash
curl http://127.0.0.1:5000/api/v1.0/goblin
{
  "firstName": "Mick", 
  "fullName": "Mick Dramatic", 
  "lastName": "Dramatic"
}
```

## /api/v1.0/goblin/firstName
### POST

Requires a ```x-www-form-urlencoded``` body with the following key value pair: ```firstName=NAME```

Requires a valid x-api-key header. See 'Obtaining an API Key' section for info in how to get a key.

Sending a post request will add another goblin first name value to the database. See below for an example:

```bash
curl -d "firstName=$i" -X POST http://127.0.0.1:5000/api/v1.0/goblin/firstName -H "x-api-key:MU123"
```

## /api/v1.0/goblin/lastName
### POST

Requires a ```x-www-form-urlencoded``` body with the following key value pair: ```lastName=NAME```

Requires a valid x-api-key header. See 'Obtaining an API Key' section for info in how to get a key.

Sending a post request will add another goblin last name value to the database. See below for an example:

```bash
curl -d "lastName=$i" -X POST http://127.0.0.1:5000/api/v1.0/goblin/lastName -H "x-api-key:MU123"
```


## /api/v1.0/ogre
### GET

Returns a random name for a Ogre. Ogre names just contain a first name. See below for an example:

```bash
curl http://127.0.0.1:5000/api/v1.0/ogre
{
  "firstName": "Gunk"
}
```

## /api/v1.0/ogre/firstName
### POST

Requires a ```x-www-form-urlencoded``` body with the following key value pair: ```firstName=NAME```

Requires a valid x-api-key header. See 'Obtaining an API Key' section for info in how to get a key.

Sending a post request will add another ogre first name value to the database. See below for an example:

```bash
curl -d "firstName=$i" -X POST http://127.0.0.1:5000/api/v1.0/ogre/firstName -H "x-api-key:MU123"
```

## /api/v1.0/orc
### GET

Returns a random name for a Orc. Orcs have first names, last names and full names. See an example below:

```bash
curl http://127.0.0.1:5000/api/v1.0/orc
{
  "firstName": "Lemon", 
  "fullName": "Lemon The double dipper", 
  "lastName": "The double dipper"
}
```

## /api/v1.0/orc/firstName
### POST

Requires a ```x-www-form-urlencoded``` body with the following key value pair: ```firstName=NAME```

Requires a valid x-api-key header. See 'Obtaining an API Key' section for info in how to get a key.

Sending a post request will add another Orc first name value to the database. See below for an example:

```bash
curl -d "firstName=$i" -X POST http://127.0.0.1:5000/api/v1.0/orc/firstName -H "x-api-key:MU123"

```

## /api/v1.0/orc/lastName
### POST

Requires a ```x-www-form-urlencoded``` body with the following key value pair: ```lastName=NAME```

Requires a valid x-api-key header. See 'Obtaining an API Key' section for info in how to get a key.

Sending a post request will add another Orc last name value to the database. See below for an example:

```bash
curl -d "lastName=$i" -X POST http://127.0.0.1:5000/api/v1.0/orc/lastName -H "x-api-key:MU123"
```

## /api/v1.0/skeleton
### GET

Returns a random name for a Skeleton. Skeletons have first names, last names and full names. See an example below:

```bash
curl http://127.0.0.1:5000/api/v1.0/skeleton
{
  "firstName": "Cornelius", 
  "fullName": "Cornelius Plantagenate", 
  "lastName": "Plantagenate"
}
```

## /api/v1.0/skeleton/firstName
### POST

Requires a ```x-www-form-urlencoded``` body with the following key value pair: ```firstName=NAME```

Requires a valid x-api-key header. See 'Obtaining an API Key' section for info in how to get a key.

Sending a post request will add another Skeleton first name value to the database. See below for an example:

```bash
curl -d "firstName=$i" -X POST http://127.0.0.1:5000/api/v1.0/skeleton/firstName -H "x-api-key:MU123"

```

## /api/v1.0/skeleton/lastName
### POST

Requires a ```x-www-form-urlencoded``` body with the following key value pair: ```lastName=NAME```

Requires a valid x-api-key header. See 'Obtaining an API Key' section for info in how to get a key.

Sending a post request will add another Skeleton last name value to the database. See below for an example:

```bash
curl -d "lastName=$i" -X POST http://127.0.0.1:5000/api/v1.0/skeleton/lastName -H "x-api-key:MU123"
```

## /api/v1.0/troll
### GET

Returns a random name for a Troll. Trolls have first names, last names and full names. See an example below:

```bash
curl http://127.0.0.1:5000/api/v1.0/troll
{
  "firstName": "Bjon", 
  "fullName": "Bjon Angledik", 
  "lastName": "Angledik"
}
```

## /api/v1.0/troll/firstName
### POST

Requires a ```x-www-form-urlencoded``` body with the following key value pair: ```firstName=NAME```

Requires a valid x-api-key header. See 'Obtaining an API Key' section for info in how to get a key.

Sending a post request will add another Troll first name value to the database. See below for an example:

```bash
curl -d "firstName=$i" -X POST http://127.0.0.1:5000/api/v1.0/troll/firstName -H "x-api-key:MU123"

```

## /api/v1.0/troll/lastName
### POST

Requires a ```x-www-form-urlencoded``` body with the following key value pair: ```lastName=NAME```

Requires a valid x-api-key header. See 'Obtaining an API Key' section for info in how to get a key.

Sending a post request will add another Troll last name value to the database. See below for an example:

```bash
curl -d "lastName=$i" -X POST http://127.0.0.1:5000/api/v1.0/troll/lastName -H "x-api-key:MU123"
```

