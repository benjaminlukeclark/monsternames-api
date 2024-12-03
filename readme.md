> :warning: **ARCHIVED**: This has been migrated to [sudoblark.monsternames.api](https://github.com/sudoblark/sudoblark.monsternames.api)

<div id="top"></div>



<!-- PROJECT SHIELDS -->
[![Sudoblark](https://circleci.com/gh/Sudoblark/monsternames-api.svg?style=shield)](https://app.circleci.com/pipelines/github/Sudoblark/monsternames-api)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)






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
        <li><a href="#behave-tests">Behave tests</a></li>
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

Note that all instructions are for development on MacOS.

If you're using other platforms same concepts apply just will need to localise to your OS.

These are just development instructions, for prod run with a container orchestrator that has SSL in front via load balancer etc.

### Prerequisites

* Docker
* A MySQL 5.7.22 instance with a:
    * dedicated database for the API
    * user with full access to dedicated database
    * user using mysql_native_password authentication

_This can be spun up relatively easily with docker locally_
    
```sh
# Create custom network so we can communicate with DB later
docker network create monsternames
# Pull MySQL 5.7.22 server image from dockerhub
docker pull mysql:5.7.22
# Setup MySQL server using image
docker run -p 3306:3306 --network monsternames --name monsternames_db_container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=development -d mysql:5.7.22 mysqld
```
* Python 3.8.x

### Installation

1. Clone the repo
    ```sh
   git clone https://github.com/Sudoblark/monsternames-api
    ```

2. Run docker build with appropriate tagging and passthru of DB connection details for docker sql container:
   1. _example below uses settings appropriately for docker database created in pre-requirement examples_
   ```sh
    docker build -t monsternames:v0.1 . --build-arg db_host='host.docker.internal' --build-arg db_name='development' --build-arg db_user='root' --build-arg db_pwd='password' --build-arg web_host='localhost:5000'
    ```
3. Spin up the docker container, mapping container 5000 to host 5000, in detached mode:

   ```sh
   docker run -d -p 5000:5000 monsternames:v0.1
   ```
   
4. Connect to DB and create a new API key for POST requests

    ```sh
    docker run -it --network monsternames --rm mysql:5.7.22 mysql -hmonsternames_db_container -uroot -ppassword
    ...
    INSERT INTO development.apikeys (apiKey, `user`)
    VALUES ('helloworld', 'testUser');
    ```

5. Run behaviour tests to confirm functionality:

    ```sh
   python3 -m venv venv
   source venv/bin/activate
   pip3 install -r requirements.txt
   python -m behave
   ...
   1 feature passed, 0 failed, 0 skipped
   50 scenarios passed, 0 failed, 0 skipped
   150 steps passed, 0 failed, 0 skipped, 0 undefined
   Took 0m4.310s

   ```

6. You're good to go for development with:

- Locker docker instance running monsternames api
- Local docker instance running MySQL backend
- API key setup in DB for POST functionality
- Functionality confirmed with Behave! behaviour testing

<p align="right">(<a href="#top">back to top</a>)</p>


### Behave tests
There are behave feature tests setup to run behaviour tests, which tests:
* POST to every api endpoint with 5 unique values
  * This in turn tests that API authentication works via the `x-api-key` header
* GET to every api endpoint between 5-10 times depending on underlying monster schema


Tried to get working on circleCI, but the separation of docker environments there makes it a bit of a mess so for now just pushes to ECR. But behaviour tests can run run locally steps outlined in local setup instructions.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

* [monsternames-api](https://monsternames-api.com/) is where I've got my flavour of the API sitting
* [monster by mnuh](https://monster.mnuh.org/) is a cool monster card generator combining my API with others to make cards

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [ ] Update frontend with [WAI](https://www.w3.org/WAI/) and [WCAG2.1](https://www.w3.org/TR/WCAG21/) guidelines
- [ ] Decouple frontend (website) and backend (API)
- [ ] Add [seleneium](https://www.selenium.dev/) testing
- [ ] At some point, once it's covered in my uni studies, add an ML model that uses existing database to generate new names
- [ ] Maybe some plotly graphs to show usage, but given how this is probably not used that much the data might not be much to show

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

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

* [Monster Creatures Fantasty](https://luizmelo.itch.io/monsters-creatures-fantasy) by luizmelo contains project logo
* [othneildrew/Best-README-Template](https://github.com/othneildrew/Best-README-Template) for providing readme template

<p align="right">(<a href="#top">back to top</a>)</p>
