# 📚 Online Book Store

This Django project was developed by **Amr Elsayed** for a Paymob task. It leverages **Docker** and **Docker Compose** to streamline the development and deployment process. Below is a comprehensive overview of the project’s structure and usage.

---

## 📂 Contents
1. [Introduction](#1-introduction)  
2. [How to Run the App](#2-how-to-run-the-app)  
3. [Test Cases & Coverage](#3-test-cases--coverage)  
4. [Postman Collection](#4-postman-collection)

---

## 1. 📘 Introduction

This project includes three core Django applications:

- **User**:  
  Handles the custom user model. Future features may include user profile endpoints.

- **Authenticate**:  
  Manages user registration and login, with complete validation mechanisms.

- **Books**:  
  Provides the core models — `Author`, `Book`, and `Review` — and the endpoints necessary for interaction with them.

---

## 2. 🚀 How to Run the App

The project utilizes **Docker** and **Docker Compose** to connect:

- Django (running on Gunicorn)  
- PostgreSQL (Database)  
- Nginx (as a reverse proxy)

### 🛠️ Steps to Run:

1. Clone the repository.
2. Ensure Docker and Docker Compose are installed.
3. Use the following command to build and start the services:
   ```bash
   docker-compose up --build
Note that we need .env file in order to init the app, A mock .env file has been added to the repo files just for test puropse as this is not recommended in a real life project

After the containers are up, The application will be served on port 80 using Nginx, As it's acting as a reverse proxy to the Django app that is running through Gunicorm on port 8000.

---

## 3. 🛠️ Test Cases & Coverage
This project includes both unit and integration test cases:

    Integration Tests: Validate REST API endpoints.

    Unit Tests: Validate models, logic, and relationships.

Test files are located in the tests folders within each app (authenticate, user, books).
🧬 Tools Used:

    Django Test Framework

    Mixer for generating mock objects

✅ Run Tests:
To run the test cases through django run the following command in the terminal `python3 manage.py test` and to run with coverage `coverage run manage.py test`, Both commands should run inside the django app container.

I also assured to cover all possible test cases, And when running `coverage report -m` We gonna get 100% on all of our code which means it's fully covered.

---

## 4. 📭 Postman Collection
You can find a ready-to-use Postman collection in the root directory:

amr_book_store_postman_collection.json
💡 Instructions:

  Import the file into Postman.

  Register and sign in.

  JWT tokens are automatically set via a Postman script—no manual setup needed.

  Start testing endpoints immediately!

---
## Finally !!
🧑‍💻 Built with ❤️ by Amr Elsayed
