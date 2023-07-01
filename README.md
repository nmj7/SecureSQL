# SecureSQL
This repository contains a code snippet for a Flask application that demonstrates SQL injection (SQLi) protection techniques.The code showcases a user registration feature with input validation and parameterized queries to prevent SQLi attacks.

## Features
User Registration: The application allows users to register by providing a username and password.
Input Validation: The code validates the username and password inputs to ensure they meet specific criteria. It checks for the presence of both username and password and enforces complexity requirements for the password.
Parameterized Queries: To prevent SQLi attacks, the code uses parameterized queries when interacting with the database. This approach ensures that user input is properly sanitized and prevents malicious SQL commands from being executed.
Error Handling: Enhanced error handling is implemented to provide informative error messages without exposing sensitive information. Any errors that occur during registration or query execution are logged for debugging purposes, and a generic error message is returned to the user.

## Modules Used
The following modules are used in the code:
Flask: Flask is a web framework for building web applications in Python.
request: Part of Flask, the request module provides access to incoming request data, allowing the application to retrieve data sent by the client.
re: The re module is a built-in module in Python used for working with regular expressions. It is used in this code to validate the username against a specific pattern.
pymysql: pymysql is a Python library that provides an interface to interact with MySQL databases. It is used to establish a connection with the database, execute SQL queries, and fetch results.

## Usage
To run the application locally, follow these steps:

Make sure you have Python and the required dependencies installed.
Set up a MySQL database and configure the database connection details in the code (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME).
Install the required Python packages by running pip install -r requirements.txt.
Run the application using python app.py.
Access the application in your web browser at http://localhost:5000 or the specified host and port.
Feel free to customize the code based on your specific requirements. For further details, refer to the comments within the code and the documentation of the respective modules.
