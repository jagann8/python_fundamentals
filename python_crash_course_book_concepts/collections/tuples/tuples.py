# tuples = ('apple', 'banana', 'cake', 'dairy milk')

# tuples[1]='jagan'  # cannot change the existing value
# print(tuples)
#
# tuples_coma = (3,)
# print(type(tuples_coma))


# orginal dimensions

# dimensions = (200, 100)
# for dimension in dimensions:
#     print('Orginal dimensions')
#     print(dimension)
#
# dimensions = (300, 100)
# for dimension in dimensions:
#     print('Modified dimensions')
#     print(dimension)

# conditional statements

# cars = ['audi', 'bmw', 'ford', 'suziki']
#
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())


# relational statements

# number_one = 12
# number_two = 2
#
# if number_one <= 15 and number_two >= 20:
#     print('Operation success')
#
# if number_one <= 15 or number_two >= 20:
#     print('Operation success')
#
# if number_one != number_two:
#     print('operation success')


# String comparison => python is sensitive in string format

# car = 'Audi'
# if car == 'audi':
#     print(True)
# else:
#     print(False) # False

# we can set lowercase before the comparison

# car = 'Audi'
# if car.lower()=='audi':
#     print(True)  # True


# checking the value is not in the list

# registered_employees=['arun','bala','charan','diva']
# new_employee='jagan'
#
# if new_employee not in registered_employees:
#     print(f'{new_employee.title()} you can order any food has u wish ')

#   request to add the list

# requested_toppings=['mushroom','extra cheese']
#
# if 'mushroom' in requested_toppings:
#     print('adding the mushrooms')

# ===============================
#  if-elif-else

# name='king'
# if name=='jagan':
#     print('Hi, ',name)
# elif name=='king':
#     print('Hey, ',name)
# else:
#     print('incorrect data')

# using multiple lists:

# available_pizzas = ['mushroom', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
# requested_pizzas = ['mushroom', 'french fries', 'extra cheese']
# for requested_pizza in requested_pizzas:
#     if requested_pizza in available_pizzas:
#         print(f"Addiing the {requested_pizza} pizza")
#     else:
#         print("Sorry! we dont have a pizza that you requested .... ",requested_pizza)
#
# print("\n Finally the order completed successfully")

# ==================
# Exercise

# user_names = ['admin', 'jagan', 'hemanth']
#
# for user in user_names:
#     if user == 'admin':
#         print(f"Hello {user}, would like to see a status report")
#     else:
#         print(f"Hello {user}, thank you for logging in again")

# to find out unique names

# current_users = ['arun', 'babu', 'chand', 'diva']
# new_users = ['jagan', 'ARUN']
#
# for user in new_users:
#     if user.lower() in current_users:
#         print('Please enter new user name')
#     else:
#         print(user,'Username is available to use')
