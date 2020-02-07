# monsternames-api

This repo hosts code for the monsternames-api.

This API allows you to generate random names for the following types of monsters:

- goatmen
- goblins
- ogres
- orcs
- skeletons
- trolls

It originally arose from my attempt at creating a python text based game: https://github.com/Sudoblark/Butterchase

If you're just interested in the endpoints, go to the endpoints section. Otherwise the rest of the repo details technical things like how to contribute to the Project or how to setup a local version of it for yourself.

If you want to contribute to the database of potential names please contact me directly @ bclark@sudoblark.com and I'll set you up with an API key :unicorn:


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


# Suggested Production Deployment

- Create AWS RDS Instance
- Create AWS Ububtu 18.06 instance
- SSH to instance
- Change to home dir

```bash
cd /home
```

- Clone to Server

```bash
git clone https://github.com/Sudoblark/monsternames-api.git monsternames_api
```

- Update machine

```bash
sudo apt-get update
```

- Install nginx

```bash
sudo apt install nginx
```

- Configure nginx site for api

```bash
sudo nano /etc/nginx/sites-enabled/monsternames_api

server {
        listen 80;
        server_name SERVERNAME;

        location / {
                proxy_pass http://127.0.0.1:8000;
                proxy_set_header Host $host;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;


        }

}
```

- Unlink default site

```bash
sudo unlink /etc/nginx/sites-enabled/default
```

- Reload nginx

```bash
sudo nginx -s reload
```

- Go to the site URL and confirm you get a bad gateway error

- Install virtualenv

```bash
sudo apt-get install virtualenv
```

Note: If you get issues about the python path not existing then run 

```bash
sudo apt-get install python
```

- Create a new virtualenv inside default user directory - to ensure we have full access to do what we need - then activate it

```bash
sudo virtualenv /home/ubuntu/.env
source /home/ubuntu/.env/bin/activate
```

- Install required packages
```bash
pip install -r /home/monsternames_api/requirements.txt
```

Note: If you get issues about permission denied when installing packages then recursively give yourself all the permissions 
```bash 
sudo chmod a+rwx -R /home/ubuntu/.env
```

- Create config file

```bash
sudo nano /etc/config.json

{
        "dbHost" : "YOUR-HOST",
        "dbName" : "DB-NAME",
        "dbPassword" : "PASSWORD",
        "dbUser" : "USER"

}
```


- Install supervisor (for auto-reloading of the application)

```bash
sudo apt-get install supervisor
```

- Create supervisor script

```bash
sudo nano /etc/supervisor/conf.d/monsternames_api.conf

[program:monsternames_api]
directory=/home/monsternames_api
command=/home/ubuntu/.env/bin/gunicorn --workers=3 application:application
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stderr_logfile=/var/log/monsternames_api/application.err.log
stdout_logfile=/var/log/monsternames_api/application.out.log
```

- Create the log directories and files

```bash
sudo mkdir /var/log/monsternames_api
sudo touch /var/log/monsternames_api/application.out.log
sudo touch /var/log/monsternames_api/application.err.log
```

- Apply supervisor changes

```bash
sudo supervisorctl reload
```

- You should now be able to access the app at the specified url

If you have issue consult the logs you created. The most likely issue is that a package did not install or there are permission issues with the directory of the virtualenv.

# Auditing

All POST requests are audited in the postaudit table. The purpose of this information is just so I can track how many awesome things have been contributed, and by who, so i can give shoutouts and make pretty graphs.

```sql
mysql> select * from postaudit;
+----+-----------+--------------------------------------------+
| id | user      | message                                    |
+----+-----------+--------------------------------------------+
|  1 | Ben Clark | GoatmenFirstName record "Fluffy" created   |
+----+-----------+--------------------------------------------+
1 row in set (0.05 sec)

mysql> 
```

# POST Notes

All post requests require an x-api-key header and relevent key/value pairs in the body

Failure to provide an x-api-key will result in an error similar to below:

```bash
{
  "error": "unauthorised.", 
  "errorMessage": "no x-api-key provided"
}
```

Failure to provide a valid x-api-key will result in an error similar to below:

```bash
{
  "error": "unauthorised.", 
  "errorMessage": "unknown x-api-key provided"
}
```

Failure to provide required key/value pairs in the body will result to an error similar to below:

```bash
{
  "error": "Invalid key error.", 
  "errorMessage": "Ensure firstName key/value is in body"
}
```

Attempting to create an entry which already exists will return an error similar to below:

```bash
{
  "error": "Duplicate record", 
  "message": "Record already exists"
}
```

Successful creation of a new record will result in a response similar to the below:

```bash
{
  "lastName": "Kornertabel", 
  "message": "New record created"
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
### Naming theme
Goatmen first names should fit in the theme of 'cute pet names'

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
### Naming theme
Goblin last names should fit in the theme of 'typical bloke names'

### POST

Requires a ```x-www-form-urlencoded``` body with the following key value pair: ```firstName=NAME```

Requires a valid x-api-key header. See 'Obtaining an API Key' section for info in how to get a key.

Sending a post request will add another goblin first name value to the database. See below for an example:

```bash
curl -d "firstName=$i" -X POST http://127.0.0.1:5000/api/v1.0/goblin/firstName -H "x-api-key:MU123"
```

## /api/v1.0/goblin/lastName
### Naming theme
Goblin last names should fit in the theme of 'typical bloke names'

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
### Naming theme
Ogre first names should fit in the theme of 'dumb sounding cavemen'

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
### Naming theme
Orc first names should fit in the theme of 'random nouns'

### POST

Requires a ```x-www-form-urlencoded``` body with the following key value pair: ```firstName=NAME```

Requires a valid x-api-key header. See 'Obtaining an API Key' section for info in how to get a key.

Sending a post request will add another Orc first name value to the database. See below for an example:

```bash
curl -d "firstName=$i" -X POST http://127.0.0.1:5000/api/v1.0/orc/firstName -H "x-api-key:MU123"

```

## /api/v1.0/orc/lastName
### Naming theme
Orc last names should fit in the theme of 'negative adjectives'

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
### Naming theme
Skeleton first names should fit in the theme of 'classy'

### POST

Requires a ```x-www-form-urlencoded``` body with the following key value pair: ```firstName=NAME```

Requires a valid x-api-key header. See 'Obtaining an API Key' section for info in how to get a key.

Sending a post request will add another Skeleton first name value to the database. See below for an example:

```bash
curl -d "firstName=$i" -X POST http://127.0.0.1:5000/api/v1.0/skeleton/firstName -H "x-api-key:MU123"

```

## /api/v1.0/skeleton/lastName
### Naming theme
Skeleton last names should fit in the theme of 'classy'

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
### Naming theme
Troll first names should fit in the theme of 'sounds vaguely Scandinavian'

### POST

Requires a ```x-www-form-urlencoded``` body with the following key value pair: ```firstName=NAME```

Requires a valid x-api-key header. See 'Obtaining an API Key' section for info in how to get a key.

Sending a post request will add another Troll first name value to the database. See below for an example:

```bash
curl -d "firstName=$i" -X POST http://127.0.0.1:5000/api/v1.0/troll/firstName -H "x-api-key:MU123"

```

## /api/v1.0/troll/lastName
### Naming theme
Troll last names should fit in the theme of 'sounds vaguely Scandinavian'

### POST

Requires a ```x-www-form-urlencoded``` body with the following key value pair: ```lastName=NAME```

Requires a valid x-api-key header. See 'Obtaining an API Key' section for info in how to get a key.

Sending a post request will add another Troll last name value to the database. See below for an example:

```bash
curl -d "lastName=$i" -X POST http://127.0.0.1:5000/api/v1.0/troll/lastName -H "x-api-key:MU123"
```

