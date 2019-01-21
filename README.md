# QUESTIONER-API-V2

Questioner is a platform that allows users to crowd source ideas for meetups

## Badges

[![Build Status](https://travis-ci.com/MaggieKimani1/QUESTIONER-API-V2.svg?branch=develop)](https://travis-ci.com/MaggieKimani1/QUESTIONER-API-V2)
[![Coverage Status](https://coveralls.io/repos/github/MaggieKimani1/QUESTIONER-API-V2/badge.svg?branch=develop)](https://coveralls.io/github/MaggieKimani1/QUESTIONER-API-V2?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/aaeed3bf4e4500252ec6/maintainability)](https://codeclimate.com/github/MaggieKimani1/QUESTIONER-API-V2/maintainability)

### Pivotal Tracker Board

[https://www.pivotaltracker.com/n/projects/2238740]

### Deploy

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/2db8f93a867d0db9b225)

### Pre-requisites

1. Python3
2. Flask
3. Flask restful
4. Postman
5. Postgres

### Getting started

Clone this repository
[https://github.com/MaggieKimani1/QUESTIONER-API-V2.git]

Navigate to the cloned repository
`cd Questioner-API-v2`

### Installation

Create a virtual environment

`virtualenv -p python3 venv`

Activate the virtual environment

`source venv/bin/activate`

Install git

`sudo apt-get install git-all`

Switch to 'develop' branch

`git checkout develop`

Install requirements

`pip install -r requirements.txt`

Run the application

`python run.py`

### Testing

Run this command on the terminal

`pytest --cov=app`

### User Endpoints

| Endpoint        |           Functionality            |
| --------------- | :--------------------------------: |
| POST/auth       | Allows a User to create an account |
| POST/auth/login |       Allows a user to login       |

## Author

MAGGIE KIMANI

### License

This project is licensed under the MIT license.
