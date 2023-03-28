from input import ask_for_string, ask_for_integer, generate_id
from file import save_project_to_the_file, edit_project_from_the_file, get_all_projects_from_file, find_project, delete_project_from_the_file

def create_project():
    title = ask_for_string("please enter Title: ")
    details = ask_for_string("please enter Details: ")
    total_target = ask_for_integer("please enter Total Target: ")
    start_time = ask_for_string("please enter Start Time: ")
    end_time = ask_for_string("please enter End Time: ")

    project_id = generate_id()
    project_data = f"{project_id}:{title}:{details}:{total_target}:{start_time}:{end_time}\n"

    added = save_project_to_the_file(project_data)
    if added:
        print("---project added successfully---")
    else:
        print("---try again please---")

def display_all_projects():
    projects = get_all_projects_from_file()

    if projects:
        for project in projects:
            print(project)
    else:
        print("---error--- please try again ")

def delete_project():
    project_id = ask_for_integer("please enter the id of the project you want to delete: ")
    found = find_project(project_id)
    if found:
        print("---project found ---")

        removed = delete_project_from_the_file(found[1])
        if removed:
            print("--project deleted successfully--")
        else:
            print("problem happened while deleting the project --- ")
    else:
        print("---please try again with valid id ")

def edit_project():
    project_id = ask_for_integer("please enter the id of the project you want to edit: ")
    found = find_project(project_id)
    if found:
        print("---project found ---")
        edit = edit_project_from_the_file(found[1])
        if edit:
            print("edit project success")
        else:
            print("error")
    else:
        print("---please try again with valid id ")