import time
def ask_for_string(message):
    while True:
        instr = input(message)
        if instr.isalpha():
            return instr
        print("--Error-- please enter it again ")
def ask_for_integer(massage):
    while True:
        inint = input(massage)
        if inint.isdigit():
            return inint
        print("--Error-- please enter it again ")
def generate_id():
    return round(time.time())
