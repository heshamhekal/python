from project_function import  create_project, edit_project,display_all_projects, delete_project
import json
import datetime
# ANSI escape codes for colors
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"
reset = "\033[0m"
r1 = "\033[0m"
g1 = "\033[0m"
def welcome():
    print(f"\n{cyan}##=============================================================================##")
    print(f'''{blue}     
               
      ___________  ________  __       ________  ________  ______   ___  ___           
      |___    ___||   _____||  |     |   _____||   ____/ /  __  \ |   \/   |
          |  |    |  /_____ |  |     |  /_____ |  |     |  |  |  ||  \  /  |
          |  |    |   _____||  |     |   _____||  |     |  |  |  ||  |\/|  |
          |  |    |  /_____ |  |____ |  /_____ |  |_____|  |__|  ||  |  |  |             
          |__|    |________||_______||________||_______/ \______/ |__|  |__| \n''')

    print(f'''{blue}                 Welcome to the Crowd-Funding Console App!
                        Created by {magenta}#Hesham Hekal#{g1}{r1}
                  {green}Telecom Applications Development Track''')
    print(f"{cyan}##=============================================================================##{r1}")
welcome()
def mainmnu():
    while True:
        choice = input("please enter \n 'n' for new: \n 'l' for list all: \n 'e' for edit: \n 'd' for delete: \n 'x' for exit: \n ")
        if choice == 'n':
            create_project()
        elif choice == 'l':
            display_all_projects()
        elif choice == 'e':
            edit_project()
        elif choice == 'd':
            delete_project()
        elif choice == 'x':
            print("----bye---")
            exit()


