from pizzas import function_01 as fs_1

# def greet_function(username):
# print('hello jagan')
# print(f"{username.title()} we have plan ")


# greet_function('jagan')

# ===========================================

# positional arguments

# def describe_pets(animal_type, pet_type):
"""Display information about the pet."""
# print(f"\nI have {animal_type.title()}")
# print(f"\nMy {animal_type.title()}'s name is {pet_type.title()}")


# describe_pets('sheep', 'kid_sheep')
# describe_pets('sheep', 'kid_sheep') # we can call multiple times of function
# describe_pets('sheep', 'kid_sheep')

# ===========================================

# keyword arguments
"""A keyword argument is a name-value pair that you pass to a function. You
directly associate the name and the value within the argument, so when you
pass the argument to the function, there’s no confusion (you won’t end up """

# def describe_pets(animal_type, pet_type):
#     """Display information about the pet."""
#     print(f"\nI have {animal_type.title()}")
#     print(f"\nMy {animal_type.title()}'s name is {pet_type.title()}")
#
#
# describe_pets(animal_type='sheep', pet_type='kid_sheep')

# =============================================
# default value in function

# def describe_pet(pet_name, animal_type='dog'):
#     print(f"\nI have a {animal_type.title()}")
#     print(f"\nMy {animal_type.title()}'s name is {pet_name.title()}")


# describe_pet(pet_name='willie',animal_type='cat')

# =============================================
# return value

# def user_information(name):
#     return name.title()


# message=user_information('Jagan')
# print(message)

# =============================================

# making the argument optional
""""When we dont need of middle name. we need set empty string and that parameter set to be last
     function parameter"""

# def get_format_name(first_name, last_name, middle_name=''):
#     full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
#     return full_name


# employee = get_format_name('king', 'jaga')
# print(employee)


# ===============================================

# return dictionary => any kind of data can be return in functions-
# -like list,set,tuples,dictionary

# def build_person(first_name, last_name, age=None):
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person


# musician = build_person('micheal', 'jackson',23)
# print(musician)

# ===============================================

# using function with while loop
#
# def get_formated_name():
#     while True:
#         print('enter the first name and last name :)')
#         print('enter the "q" to exit')
#         first_name = input('enter the first name : ')
#         if first_name == 'q':
#             break
#         last_name = input('enter the last name : ')
#         full_name = first_name + " " + last_name
#         print('Full name => ', full_name)


# get_formated_name()

# ==========================================

# passing the list in the function

# def bank_names(banks):
#     for bank in banks:
#         print(f"{bank.title()} Bank")


# bank_list=['american express','bank of baroda','canara','axis','hdfc','sbi','rbi']
# bank_names(bank_list)

# ==========================================

# remove the list items in the loop by using function

# def printed_model_making(unprinted_model, printed_model):
#     while unprinted_model:
#         item = unprinted_model.pop()
#         printed_model.append(item)
#
#
# unprinted_design = ['line coating', 'double coating', 'plain coating', 'checked coating']
# printed_design = []
# printed_model_making(unprinted_model=unprinted_design, printed_model=printed_design)
#
# for item in printed_design:
#     print(item)

# ==========================================

# passing on arbitrary number of arguments

# def make_pizza(*toppings):
#     print(toppings)
#
#
# make_pizza('apple','banana','mushroom','pepperoni')
# make_pizza('green  peppers')

# using the for loop

# def create_pizza(*toppings):
#     print("\nMaking the pizza with the following toppings")
#     for topping in toppings:
#         print(f"\n- {topping}")
#
#
# create_pizza('apple', 'mushroom', 'pepperoni', 'extra cheese')
# create_pizza('mushroom', 'pepperoni')
# ==========================================
#
# mixing positional arbitrary arguments

# def make_pizza(size,*topping):
#     print(f"topping size is {size}")
#     print(topping)
#
#
# make_pizza(18,'mushroom','pepperoni','extra cheese')

# ===========================================

# mixing arbitrary keywords

# def build_profile(first_name, last_name, **user_info):
#     user_info['firstname'] = first_name
#     user_info['lastname'] = last_name
#
#     return user_info
#
#
# user_profile = build_profile('king', 'jaga', field='ceo', location='india')
# print(user_profile)

# ==========================================
# import the specific function in the module

# fs_1()
# ===========================================


