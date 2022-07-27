# my_list = ['apple', 'bell', 'chat', 'drop']
# print(my_list[1].upper())
# access last element in list
# print(my_list[-1])
# message=f'I Eat Very rare in {my_list[0].title()} fruit'
# print(message)
# for item in my_list:
#     print(item)

# change the existing element in list
# print(my_list)
# my_list[1] = 'banana'
# print(my_list)

# adding the elements in list by append
# its add the element the end of the list without affecting the previous list
# print(my_list)
# my_list.append('egg')
# print(my_list)

# adding the element in list by inserting
# insert method is used to add the element where ever we want the list
# print(my_list)
# my_list.insert(2, 'bhoomi')
# print(my_list)

# remove the element in list by del statement
# print(my_list)
# del my_list[2]
# print(my_list)

# remove the element in list by using pop method
# print(my_list)
# my_list.pop(2)
# print(my_list)

##
# when do we use del statement or pop method
# when we don't use element in list then use del statement.
# when we use element in list , then we use pop method.

# ##

# removing the item by using the values

# sometimes we dont know the index of the element in list
# then we pass the value in remove method.
##

# print(my_list)
# my_list.remove('drop')
# print(my_list)

# exercises:
# invite_folks = ['hemanth', 'jagan', 'ramesh', 'maya', 'kiran', 'mani', 'bush', 'riya', 'diya', 'dhana']
# # print(invite_folks)
# def remove_list(idx):
#     for i in range(idx):
#         invite_folks.pop()
#
#     print('Sorry we have 2 seat for dinning table to eat the food')
#
#
# remove_list(6)
# print(invite_folks)
# for item in invite_folks:
#     print('item => ',item)
#     del invite_folks[invite_folks.index(item)]
#
# print(invite_folks)
# =====================================
# sorting can change orginal order.

# cars = ['bmw', 'audi', 'ferrari', 'lamborgini']
# cars.sort(reverse=True)
# print(cars)

# sorting function can be used to sort the list tempravory.

# fruits = ['pineapple', 'mango', 'orange', 'apple']
# print('Orginal Order => ', fruits)
# print('Sorted Order => ', sorted(fruits))
# print('Orginal Order => ', fruits)

# print('the length of the list => ' , len(fruits))

# exercises:

# places_visit = ['nellore', 'new_delhi', 'chennai', 'thanjavoor', 'new_york']
# print('orginal list => ',places_visit)
# print('sorted the list ',sorted(places_visit))
# print('orginal list => ',places_visit)

# print('orginal order => ', places_visit)
# places_visit.reverse()
# print('reverse order =>  ', places_visit)
# places_visit.reverse()
# print('reverse order =>  ', places_visit)

# print('orginal order => ', places_visit)
# places_visit.sort()
# print('sort order => ',places_visit)
# places_visit.sort()
# print('sort order in reverse alphabetic => ',places_visit)

# print(len(places_visit))


# loops

# magicians = ['alice', 'david', 'caroline']
# for magician in magicians:
#     print(magician)
#
#     print(f'hai {magician}')

# pizza exercise
# pizzas = ['apple', 'banana', 'egg']
# for item in pizzas:
#     print(f'I like a {item} pizza')
# print('I really dont like a pizza')

# making numerical numbers

# for value in range(10):
#     print(value)

# my_list=list(range(1,6))
# print(my_list)

# even_numbers=list(range(2,11,2))
# print(even_numbers)

# squares = []
# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)
#
# print('squares list => ', squares)

# Statistics
# numbers = [1, 1, 1, 4, 1, 6, 1, 1,4, 0, 2, 8]
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# lambda function
# result = lambda a: a + a
# print(result(3))


# list comprehensions
# it acts like for loop and append the element to the list

# squares = [value ** 2 for value in range(1, 11)]
# print(squares)

# suming = list(range(1_000_000))
# print(sum(suming))

# slice

# even=list(range(2,11,2))
# print(even[-3:])

# players = ['kholi', 'dhoni', 'dhavan', 'hardhik']
# for player in players[-2:]:
#     print(player.title())
#
# print(players)

# ======================

