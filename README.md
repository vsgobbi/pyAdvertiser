## ATNAP (Aqui tem Nova Alta Paulista) project. A python Web Advertiser: Flask RESTful API with PynamoDB and AWS Lambda

## Description
Project created by ATNAP team as designed for Hackatrouble. (https://www.hackatrouble.com.br/)
Web project development of an API using Flask, designed with Blueprints pattern, 
database created with NoSQL DynamoDB as PynamoDB (https://github.com/pynamodb/PynamoDB).
Using AWS KMS service to encrypt hashed passwords and secure login system.
In order to deploy at Amazon Web Services for Lambda with Python 3.7 environment we use Serverless framework.
Using Serverless framework to deploy on localhost and deploying it to AWS Lambda as well. 
Used NodeJS Axios to access created API routes with front end client requests. <br />
Our website: https://master.d1jjesgxkfrs63.amplifyapp.com/ <br />
API Documentation: https://documenter.getpostman.com/view/6679239/Szf6WTn4?version=latest <br />
Our purpose (project video in pt-br): https://youtu.be/8zPwqxar7Q4 <br />
This project is ***GPL v3.0 licensed***.

## Table of Contents


- [Install it](#install)
- [Endpoints](#current-endpoints)
- [Front End](#current-front-end-website-hosted-by-aws-amplify)
- [Running application](#running-application)
- [Contributing](#contributing)
- [License](#license)

## Install

### Crate virtualenvironment 'venv' using Python3.7
```
$ virtualenv -p python3.7 venv
$ source venv/bin/activate
```
### Install requirements
```
$ pip install -r requirements
```
### In order to deploy web applications on localhost or on AWS Lambda and AWS API Gateway use Serverless framework:
```
$ npm install -g serverless
```

### Check serverless.yml file (choose AWS region to 'us-east-2', runtime to 'python3.7', service name pyAdvertiser):
```
$ nano serverless.yml
```

### Install serverless plugins:
```
$ sls plugin install -n serverless-wsgi
$ sls plugin install -n serverless-python-requirements
```
### Use the 'default' created config in ~/.aws/config
### Create default bucket
### check serverless.yml and deploy: 
```
$ sls wsgi serve
```
### Running app in aws lambda:
```
$ sls deploy
```
### Checking logs from application:
```
$ sls logs -f app
```
### Current endpoints:
#### Endpoints and API V1 Documentation: <a href="https://documenter.getpostman.com/view/6679239/Szf6WTn4?version=latest" target="_blank">ATNAP API v1</a>

### User registration:
```
$ /api/v1/register
```
### User login/authentication:
```
$ /api/v1/login
```
### Advertiser, company informations and registration:
```
$ /api/v1/advertiser
```
### Advertisement, company detailed advertisements:
```
$ /api/v1/advertisement
```

## Current Front-end Website Hosted by AWS Amplify: <br />
<a href="https://master.d1jjesgxkfrs63.amplifyapp.com/" target="_blank">PORTAL ATNAP</a>

## Current Front-end git repo: <br />
<a href="https://github.com/PatrickCalorioCarvalho/hackatrouble-ATNAP" target="_blank">Front-end with ReactJs</a>

## Running Application
### check serverless.yml and deploy on localhost: 
```
$ sls wsgi serve
```
### Running app in aws lambda:
```
$ sls deploy
```
### Run VUEjs application locally to test client frontend
```
$ npm run serve
```

## Contributing

- **Step 1**
    - 🍴 Fork this repo!

- **Step 2**
    - 🔨🔨 Clone this repo to your local machine using:
```
git clone https://github.com/vsgobbi/pyAdvertiser
```

- **Step 3**
    - 🔃 Create a new pull request using 
    <a href="https://github.com/vsgobbi/pyAdvertiser/compare/" target="_blank">`https://github.com/vsgobbi/pyAdvertiser/compare`</a>

## License

 [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
- **[GPL license](https://www.gnu.org/licenses/gpl-3.0)**
- Copyright 2020 © <a href="https://github.com/vsgobbi" target="_blank">Vitor Gabriel Sgobbi</a>.
