def get_all_user_from_file():
    try:
        fileobj = open("user.txt", 'r')
    except Exception as e:
        print(e)
        return False
    else:
        users = fileobj.readlines()
        return users
def find_user(email, password):
    users = get_all_user_from_file()
    for user in users:
        user_details = user.strip('\n').split(":")
        if user_details[2] == email and user_details[3] == password:
            return True, user
    return False, None


def save_data_in_the_file(new_user):
    try:
       fileobj = open("user.txt",'a')
    except Exception as e :
        print(e)
    else:
        fileobj.write(new_user)
        fileobj.close()
