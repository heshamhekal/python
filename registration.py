import re
from projects import mainmnu
# Define a list to store registered users
users = []

class User:
    def __init__(self, first_name, last_name, email, password, mobile):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.mobile = mobile

# Function to validate email format
def validate_email(email):
    email_pattern = r"[^@]+@[^@]+\.[^@]+"
    return re.match(email_pattern, email)

# Function to validate Egyptian mobile phone format
def validate_mobile(mobile):
    mobile_pattern = r"(01)[0125][0-9]{8}"
    return re.match(mobile_pattern, mobile)

# Function to register a new user
def register():
    print("Please enter your details to register.")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email = input("Email: ")
    while not validate_email(email):
        email = input("Invalid email format. Please enter a valid email: ")
    password = input("Password: ")
    confirm_password = input("Confirm password: ")
    while password != confirm_password:
        confirm_password = input("Passwords do not match. Please confirm your password again: ")
    mobile = input("Mobile phone number: ")
    while not validate_mobile(mobile):
        mobile = input("Invalid mobile phone format. Please enter a valid Egyptian mobile phone number: ")
    new_user = User(first_name, last_name, email, password, mobile)
    users.append(new_user)
    print("Registration successful.")

# Function to login a user
def login():
    print("Please enter your login details.")
    email = input("Email: ")
    password = input("Password: ")
    for user in users:
        if user.email == email and user.password == password:
            print("Login successful.")
            return
    print("Invalid email or password. Please try again.")

# Example usage

