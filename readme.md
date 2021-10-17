<div id="top"></div>



<!-- PROJECT SHIELDS -->
TBC - maybe circleCI?



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Sudoblark/monsternames-api">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">monsternames-api</h3>

  <p align="center">
    Pseudo-random monster name generate
    <br />
    <a href="https://monsternames-api.com/"><strong>See the site»</strong></a>
    <br />
    <br />
    <a href="https://monsternames-api.com/endpoints">Consume the API</a>
    ·
    <a href="https://monsternames-api.com/contributionGuide">Contribute names programmatically</a>
    ·
    <a href="https://monsternames-api.com/addNames">Contribute names in GUI</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This API was originally a standalone name generation program in a text-based adventure I was making.

That adventure never got off the ground, but the name generation did. So I decided to make name generation its own thing and host it in an API.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [peewee](http://docs.peewee-orm.com/en/latest/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
To get a local dev copy up and running follow these example steps.

Note that all instructions are for development on Windows 10 using Ubuntu 20.04 LTS WSL.

If you're using other platforms same concepts apply just will need to localise to your OS.

~~I don't have a shiny Mac for personal dev purposes just work~~

### Prerequisites

* Docker desktop for Windows 10
* A MySQL 5.7.22 instance
    * This can be spun up relatively easily with docker locally:
    ```sh
    # Create custom network so we can connect using docker MySQL client later
    docker network create monsternames
    # Pull MySQL 5.7.22 server image from dockerhub
    docker pull mysql:5.7.22
    # Setup MySQL server using image
    docker run -p 3306:3306 --network monsternames --name monsternames_db_container -e MYSQL_ROOT_PASSWORD=password -d mysql:5.7.22 mysqld
    ```
* Single database on instance, and user with full access to that database using mysql_native_password
    * Example below of how to create DB and user on docker mysql created in last step:
    ```sh
    # Run interactive docker image with mysql client connected to previous made docker image 
    # hosting MySQL 5.7.22 on our custom network
    docker run -it --network monsternames --rm mysql:5.7.22 mysql -hmonsternames_db_container -uroot -p
    ...
    # Create a dedicated monsternames database
    CREATE DATABASE development;
    # Setup user for local dev environment to use, ensuring mysql_native_password is used for pymysql compatibility
    CREATE USER 'dev'@'%' IDENTIFIED WITH mysql_native_password BY 'helloWorld!1';
    # Then grant appropriate permissions
    GRANT ALL ON development.* TO 'dev'@'%';
    ```
### Installation

1. Clone the repo
    ```sh
   git clone https://github.com/Sudoblark/monsternames-api
    ```

2. Run docker build with appropriate tagging and passthru of DB connection details for docker sql container:
   1. _example below uses settings appropriately for docker database created in pre-requirement examples_
   ```sh
    docker build -t monsternames:v0.1 . --build-arg db_host='host.docker.internal' --build-arg db_name='development' --build-arg db_user='dev' --build-arg db_pwd='helloWorld!1' --build-arg web_host='localhost:5000'
    ```
3. Spin up the docker container, mapping container 5000 to host 5000, in detached mode:

   ```sh
   docker run -d -p 5000:5000 monsternames:v0.1
   ```

4. You should then be able to query logs, and confirm in MySQL client, to show that database has been intialised:

    ```sh
    PS D:\Github\monsternames-api> docker container logs 3153fdac23864ec7a24189b458f8ff10084de1ccf64960a2e66438e845010b9b
    Attempting DB connection... 
    Connected to DB and created tables 
   ...
   mysql> USE development;
    Reading table information for completion of table and column names
    You can turn off this feature to get a quicker startup with -A
    
    Database changed
    mysql> SHOW TABLES;
    +-----------------------+
    | Tables_in_development |
    +-----------------------+
    | apikeys               |
    | goatmenfirstname      |
    | goblinfirstname       |
    | goblinlastname        |
    | ogrefirstname         |
    | orcfirstname          |
    | orclastname           |
    | postaudit             |
    | skeletonfirstname     |
    | skeletonlastname      |
    | trollfirstname        |
    | trolllastname         |
    +-----------------------+
    12 rows in set (0.00 sec)

    mysql>
    ```

5. And hit the home page...

<img src="images/home_example.png" alt="home_page_example" width="80" height="80">

6... then see logs confirming this:
   ```sh
   PS D:\Github\monsternames-api> docker container logs bcfefca0903dce9d05df6f0a7fd4e9305eacaadcadb5d6c5a34e238804f2413b
   ...
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://172.17.0.2:5000/ (Press CTRL+C to quit)
172.17.0.1 - - [17/Oct/2021 11:30:05] "GET / HTTP/1.1" 200 -
   ```

7. You can then make an API key in the database for authentication...
    ```sh
    INSERT INTO development.apikeys (apiKey, `user`)
    VALUES ('helloworld', 'testUser');
    ```
8. ... and use this to create new names...
    ```sh
    curl -d "firstName=hello" -X POST http://localhost:5000/api/v1.0/goatmen/firstName -H "x-api-key:helloworld"
   {"firstName":"hello","message":"New record created"}
    ```

9. Which the API then returns:
    ```sh
    curl -d "firstName=hello" -X GET http://localhost:5000/api/v1.0/goatmen
    {"firstName": "hello", "fullName": "hello"}
    ```

From there you should be good to go for local development with:
- Locker docker instance running monsternames api
- Local docker instance running MySQL backend
- API key setup in DB for POST functionality

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

* [monsternames-api](https://monsternames-api.com/) is where I've got my flavour of the API sitting
* [monster by mnuh](https://monster.mnuh.org/) is a cool monster card generator combining my API with others to make cards

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [x] Get local dev docker image working
- [x] Get DB initialisation working on local dev environment
- [ ] Refactor DB initialisation to obscure secrets
- [ ] Add Behave! behaviour testing with Python using docker image in circleCI
- [ ] Add unit tests
- [ ] Add CI deployment of docker contain to ECS

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Benjamin Clark - [LinkedIn](https://www.linkedin.com/in/benni/) - bclark@sudoblark.com

Project Link: [monsternames api](https://github.com/Sudoblark/monsternames-api)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Monster Creatures Fantasty](https://luizmelo.itch.io/monsters-creatures-fantasy) by luizmelo contains project logo
* [othneildrew/Best-README-Template](https://github.com/othneildrew/Best-README-Template) for providing readme template

<p align="right">(<a href="#top">back to top</a>)</p>