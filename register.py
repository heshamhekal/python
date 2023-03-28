import re
from userfile import get_all_user_from_file , find_user , save_data_in_the_file
from projects import mainmnu
def validate_email(email):
    email_pattern = r"[^@]+@[^@]+\.[^@]+"
    return re.match(email_pattern, email)

def validate_mobile(mobile):
    mobile_v = r"(01)[0125][0-9]{8}"
    return re.match(mobile_v , mobile)

def registration():
    first_name = input("enter your first name ")
    last_name = input("enter your last name ")
    email=input("Email: ")
    while not validate_email(email):
        email = input("Invalid email format. Please enter a valid email: ")
    password = input("enter password")
    confirm_password=input("enter password again ")
    while password != confirm_password :
       confirm_password = input("Passwords do not match. Please confirm your password again: ")

    mobile = input("enter you mobile ")
    while not validate_mobile(mobile):
        mobile = input("Invalid mobile phone format. Please enter a valid Egyptian mobile phone number: ")
    new_user = (first_name, last_name, email, password, mobile)
    new_user = f"{first_name}:{last_name}:{email}:{password}:{mobile}\n"
    save_data_in_the_file(new_user)
    print(new_user)

def login():
    email=input("enter your mail: ")
    password=input("enter your password: ")
    found = find_user(email, password)
    if found :
        print("Login successful.")
        return
    else:
        print("Invalid email or password. Please try again.")

# registration()
# login()
# mainmnu()