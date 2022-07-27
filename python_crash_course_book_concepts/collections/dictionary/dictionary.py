alien_0 = {'color': 'blue', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])
# accessing the value by using the key
# print(f"You Earned {alien_0['points']} in the snake game")

# dictionary is dynamic collection type
# adding the information about the alien at any time
alien_0['x_position'] = 0
alien_0['y_position'] = 25
# print(alien_0)
# print('====================')
# for alien in alien_0:
#     print(alien_0[alien])

# alien_0['color'] = 'yellow'
# alien_0['speed'] = 'medium'
# print(alien_0)
#
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# print('orginal x position ',alien_0['x_position'])
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print('new x position ', alien_0['x_position'])

# print(alien_0)
# del alien_0['points']
# print(alien_0)

# favorite_languages = {
#     'arun': 'c',
#     'bala': 'java',
#     'chand': 'python',
#     'jagan': 'javascript'
# }

# language = favorite_languages['jagan']
# print(f'jagan favorite language is {language.title()}')
# print(favorite_languages['jagan'])
# print(favorite_languages.get('ja','respective key not available'))

# access key and values
# for key, value in favorite_languages.items():
#     print(f"{key} favorite language is {value}")

# In the dictionary default we can access keys or with key() method
# for key in favorite_languages.keys(): # easy to read this approach
#     print(key)
# for value in favorite_languages.values():
#     print(value)

# looping through the dictionary keys

# friends=['jagan','arun','erin']

# for name in favorite_languages.keys():
#     print(name)
#
#     if name in friends:
#         language=favorite_languages[name].title()
#         print(f"  {name} favorite language is {language}")


# if 'erin' not in favorite_languages.keys():
#     print(f"erin ,please take our poll")

# List Dictionary

# favorite_languages = {
#     'arun': ['C', 'Java', 'Go'],
#     'bharath': ['C++', 'Java', 'javascript'],
#     'jagan': ['c', 'java', 'javascript', 'python', 'html', 'css']
# }
# for name,languages in favorite_languages.items():
#     print(f"\n{name.title()} favorite language is :")
#     for language in languages:
#         print(f"\t {language.title()}")

# =====================================

# Dictionary have nested dictionary

# users = {
#     'jagan': {
#         'first_name': 'Jagan',
#         'last_name': 'N',
#         'location': 'chennai-india'
#     },
#     'hemanth': {
#         'first_name': 'hemanth',
#         'last_name': 'R',
#         'location': 'vellore-india'
#     },
#     'ramesh': {
#         'first_name': 'ramesh',
#         'last_name': 'G',
#         'location': 'vellore-india'
#     }
# }
# for username, userinfo in users.items():
#     full_name = f"{userinfo['first_name']} {userinfo['last_name']}"
#     location = f"{userinfo['location']}"
#     print(f"\nUserName : {username.title()} ")
#     print(f'Fullname : {full_name}')
#     print(f'Location : {location}')
