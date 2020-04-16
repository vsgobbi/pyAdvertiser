## Flask RESTful API with PynamoDB and AWS Lambda

## Description
Web project development of an API using Flask, designed with Blueprints pattern, 
database created with NoSQL DynamoDB as PynamoDB (https://github.com/pynamodb/PynamoDB) 
and VueJs (https://vuejs.org/) in order to deploy at Amazon Web Services for Lambda Python 3.7 environment.
Using Serverless framework to deploy on localhost and deploying it to AWS Lambda as well. 
Used NodeJS Axios to access created API routes with front end client requests. Building UI using VueJs
framework. This project is ***GPL v3.0 licensed***.

## Table of Contents


- [Install it](#install)
- [Running application](#running)
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
### Creating VUEjs front end application:
### first install nodejs and npm
### Install vue cli: 
```
$ npm install -g @vue/cli
```
### Create VUE project 'client' for Single Page Application
```
$ vue create client
```
### Install vuetify and select 'Default' preset:
```
$ cd client && vue add vuetify
```
### Install nodejs Axios on client to consume our API:
```
$ npm install -S axios
```
### Deploy frontend and run client 
```
$ npm run serve
```

## Running
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
    - 🔨🔨 Clone this repo to your local machine using `https://github.com/vsgobbi/pyAdvertiser`

- **Step 3**
    - 🔃 Create a new pull request using 
    <a href="https://github.com/vsgobbi/pyAdvertiser/compare/" target="_blank">`https://github.com/vsgobbi/pyAdvertiser/compare`</a>

## License

 [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
- **[GPL license](https://www.gnu.org/licenses/gpl-3.0)**
- Copyright 2020 © <a href="https://github.com/vsgobbi" target="_blank">Vitor Gabriel Sgobbi</a>.