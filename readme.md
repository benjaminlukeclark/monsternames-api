# monsternames-api

This repo hosts code for the monsternames-api hosted at https://monsternames-api.com.

This API allows you to generate random names for monsters.

It originally arose from my attempt at creating a python text based game: https://github.com/Sudoblark/Butterchase

See the website for more details or browse the html directly in the repo if you're adventurous.

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

- Generate an SSL cert
```bash
cd ubutu
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
cd ..
```

- Configure nginx site for api

```bash
sudo nano /etc/nginx/sites-enabled/monsternames_api

server {
        listen 443 ssl;
        server_name SERVERNAME;
        ssl_certificate /path/to/cert.key;
        ssl_certificate_key /path/to/key.pem;

        location / {
                proxy_pass http://127.0.0.1:8000;
                proxy_set_header Host $host;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

}

server {
        listen 80;
        server_name SERVERNAME;

        location / {
                return 301 https://$host$request_uri;
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

# Using Lets Encrypt for an actually trusted certificate
Luckily, as we're using nginx for the proxy of this, we can setup an actually trusted certificate (method above will be self-signed) and have automatic renewal. Neat.

If you already have a self-signed certificiate, ensure you remove the following lines from ```/etc/nginx/sites-enabled/monsternames_api``` before continuing:
```bash
ssl_certificate = xxx
ssl_certificate_key = xxx
```
Ensure you also reboot nginx after to prevent any errors

1) First, trust the [certbot](https://certbot.eff.org/) repo:

```bash
add-apt-repository ppa:certbot/certbot
```

2) Install certbot:

```bash
apt-get update
apt-get install python-certbot-nginx
```

3) Generate an SSL cert:

```bash
sudo certbot --nginx -d monsternames-api.com
```

Now if you view ```/etc/nginx/sites-enabled/monsternames_api``` you should see that the ```ssl_certificate``` and ```ssl_certificate_key``` blocks state they're managed by certbot.

If, for whatever reason, the certificate was created but not installed then you'll need to manually add ssl_certificate and ssl_certificate_key directives to the server block in nginx.

What's also neat about this is that we can schedule a cronjob so that the cert automatically renews:

```bash
crontab -e
0 12 * * * /usr/bin/certbot renew --quiet
```

# Projects that use this API
## [Monster Generator](https://monster.mnuh.org/)
Cool monster generator that mashes this API and a few others to generate monster 'cards' like a playing deck! Created by [Mishael Nuh](https://github.com/mishaelnuh).
