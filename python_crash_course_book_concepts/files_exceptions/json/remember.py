import json


#
# username = input('enter the name : ')
# filename = 'username.json'
# with open(filename, 'w') as f:
#     json.dump(username, f)
#     print(f"we will remember {username}")
# def greet():
#     filename = 'usernames.json'
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#
#     except FileNotFoundError:
#         username = input('Enter the your  name :')
#         with open(filename, 'w') as f:
#             json.dump(username, f)
#             print(f"we will remember your information {username}")
#     else:
#         print(f"Welcome back {username}")
#
#
# greet()

# ==================================================

# Refactor => easy to read,easy to extend and easy to understand

def get_stored_username():
    """"Get Stored username if available"""
    filename = 'sign_in_users.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input('enter the username : ')
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user name """
    username = get_stored_username()
    if username:
        print(f"Welcome back {username} ")

    else:
        username = get_new_username()
        print(f'We will remember you , when you are back {username}')


greet_user()
