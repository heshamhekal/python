from input import ask_for_string, ask_for_integer

def save_project_to_the_file(project_data):
    try:
        fileobj = open("project.txt", 'a')
    except Exception as e:
        print(e)
        return False
    else:
        fileobj.write(project_data)
        fileobj.close()
        return True

def get_all_projects_from_file():
    try:
        fileobj = open("project.txt", 'r')
    except Exception as e:
        print(e)
        return False
    else:
        projects = fileobj.readlines()
        return projects

def find_project(project_id):
    projects = get_all_projects_from_file()
    print(projects)
    for project in projects:
        project_details = project.strip('\n').split(":")
        if project_details[0] == str(project_id):
            return True, project
    else:
        return False

def save_projects_to_the_file(list_of_projects):
    try:
        fileobj = open("project.txt", 'w')
    except Exception as e:
        print(e)
        return False
    else:
        fileobj.writelines(list_of_projects)
        fileobj.close()
        return True

def delete_project_from_the_file(project):
    projects = get_all_projects_from_file()
    projects.remove(project)
    removed = save_projects_to_the_file(projects)
    return removed


def edit_project_from_the_file(project):
    edit_project = project
    print(project)
    choice = input(
        "Enter \n 't' to edit title \n 'd' to edit details \n 'pg' to edit total pages \n 's' to edit start time \n 'e' to edit end time \n 'tt' to edit total target time\n")

    if choice == 't':
        new_value = ask_for_string("Enter the new title: ")
        project_parts = edit_project.split(':')
        project_parts[1] = new_value
        edit_project = ':'.join(project_parts)
        print("The project title has been updated to:", new_value)

    elif choice == 'd':
        new_value = ask_for_string("Enter the new details: ")
        project_parts = edit_project.split(':')
        project_parts[2] = new_value
        edit_project = ':'.join(project_parts)
        print("The project details have been updated to:", new_value)

    elif choice == 'pg':
        new_value = ask_for_integer("Enter the new total pages: ")
        project_parts = edit_project.split(':')
        project_parts[3] = str(new_value)
        edit_project = ':'.join(project_parts)
        print("The project total pages have been updated to:", new_value)

    elif choice == 's':
        new_value = ask_for_string("Enter the new start time: ")
        project_parts = edit_project.split(':')
        project_parts[4] = new_value
        edit_project = ':'.join(project_parts)
        print("The project start time has been updated to:", new_value)

    elif choice == 'e':
        new_value = ask_for_string("Enter the new end time: ")
        project_parts = edit_project.split(':')
        project_parts[5] = new_value
        edit_project = ':'.join(project_parts)
        print("The project end time has been updated to:", new_value)

    elif choice == 'tt':
        new_value = ask_for_string("Enter the new total target time: ")
        project_parts = edit_project.split(':')
        project_parts.append(new_value)
        edit_project = ':'.join(project_parts)
        print("The project total target time has been updated to:", new_value)

    else:
        print("Invalid choice. Please enter 't', 'd', 'pg', 's', 'e' or 'tt'.")
        return

    projects = get_all_projects_from_file()
    projects.append(edit_project)
    edit_t = save_projects_to_the_file(projects)
    delete_project_from_the_file(project)
    return edit_t

