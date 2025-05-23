
# Online Book Store

This Django project was developed by Amr Elsayed for Paymob's task. It runs using Docker and Docker Compose. The following sections provide a quick walkthrough of the project’s folder structure.


## Contents
1- Introduction

2- How to run the app

3- Test Cases & Coverage

4- Postman Collection

### 1- Introduction
This project consists of 3 main applications as follows:

A. "User" application is responsible for creating the user model and could manage user profile endpoints in the futuure.

B. "Authenticate" application is responsible for the register and sign-in with all of the needed validations.

C. "Books" application is responsible for creating the main 3 models (Author - Book - Review) and has all needed endpoints to interact with them.

### 2- How to run the app
This project uses Docker along with Docker-Compose to manage the connection and the network between Django application, Postgresql DB and Nginx.

To run this app write the below command in the terminal

`docker-compose up --build`

Note that we need .env file in order to init the app, A mock .env file has been added to the repo files just for test puropse as this is not recommended in a real life project

After the containers are up, The application will be served on port 80 using Nginx, As it's acting as a reverse proxy to the Django app that is running through Gunicorm on port 8000.

### 3- Test Cases & Coverage
This app has test cases with 2 types, Integration test cases and unit test cases.

The "Integration" test cases are testing the REST endpoints, And the "Unit" test cases are testing the model functionalities and relations

The test cases are inisde tests folder inside (authenticate, user and books) folder, We are using Mixer in order to create mock instances to interact with

To run the test cases through django run the following command in the terminal `python3 manage.py test` and to run with coverage `coverage run manage.py test`, Both commands should run inside the django app container.

I also assured to cover all possible test cases, And when running `coverage report -m` We gonna get 100% on all of our code which means it's fully covered.

### 4- Postman Collection
In case you wanted to test some endpoints, You will find a postman collection in the project directory under the name (amr_book_store_postman_collection.json), Just import it into postman and register then sign-in, And that's it, No need to save the JWT Token anywhere i already specified a script to put it in the golbal vars of Postman, So you can test the endpoints directly.