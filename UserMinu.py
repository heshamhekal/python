from os import name
import re
import datetime
from register import registration ,login
from projects import mainmnu
r = "\033[31m"
r1 = "\033[0m"
g = "\033[32m"
g1 = "\033[0m"
def displayMenu():
    while True:
        print("\nPlease select an option:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            registration()
        elif choice == "2":
            login()
            break
            break
        elif choice == "3":
            print(f"{g}Thank you for using our app!{g1}")
            break
        else:
            print(f"{r}Invalid choice! Please select a valid option.{r1}")

displayMenu()
mainmnu()