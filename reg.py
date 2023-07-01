from flask import Flask, request
import re
import pymysql

app = Flask(__name__)

# Database connection configuration
DB_HOST = 'localhost'
DB_USER = 'your_db_username'
DB_PASSWORD = 'your_db_password'
DB_NAME = 'your_database_name'

# Establish database connection
db = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_NAME)

# Input validation and parameterized queries
def execute_query(query, params=None):
    try:
        with db.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
        return result
    except pymysql.Error as e:
        # Log the error for debugging purposes
        print(f"Error executing query: {e}")
        raise Exception("An error occurred while processing your request. Please try again later.")

# Route for handling user registration
@app.route('/register', methods=['POST'])
def register():
    try:
        username = request.form.get('username')
        password = request.form.get('password')

        # Input validation
        if not (username and password):
            return "Please provide both username and password."

        if not is_valid_username(username):
            return "Invalid username. Please choose a valid username."

        if not is_valid_password(password):
            return "Invalid password. Please choose a stronger password."

        # Parameterized query
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        params = (username, password)
        execute_query(query, params)

        return "Registration successful!"
    except Exception as e:
        # Log the error for debugging purposes
        print(f"Error during registration: {e}")
        return "An error occurred while processing your registration. Please try again later."

# Function to validate username
def is_valid_username(username):
    return bool(username and re.match(r'^[a-zA-Z0-9_]+$', username))

# Function to validate password
def is_valid_password(password):
    return bool(password and len(password) >= 8 and
                any(char.isupper() for char in password) and
                any(char.islower() for char in password) and
                any(char.isdigit() for char in password))

if __name__ == '__main__':
    app.run()