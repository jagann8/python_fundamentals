# message = input('Enter your name ')
# print(f'{message} says Hi!')

# number = int(input('enter the number , i will check even or odd '))
#
# if number % 2 == 0:
#     print(f'{number} is even')
# else:
#     print(f'{number} is odd')

# while_loop
# count=0
# while count<=5:
#     print('count : ',count)
#     count+=1
# =====================================

# letting the user choose when to quit

# prompt = '\nTell me something, i will back repeat to you'
# prompt += '\nEnter your name : '
# message = ''
# while message != 'quit':
#     message = input(prompt)
#     print(message)

# ========================================
# moving the one list to another list

# unconfirmed_users = ['john', 'steve', 'ervin', 'kevin']
# confirmed_users = []
# while unconfirmed_users:
#     user = unconfirmed_users.pop()
#     confirmed_users.append(user)
#
# print(unconfirmed_users)
# print(confirmed_users)
# ========================================
# removing all instances specific value in the list.

# pets = ['cat', 'dog', 'snake', 'rabbit', 'goldfish']
#
# while 'cat' in pets:
#     pets.remove('cat ')
#
# print(pets)

# we use user information to make the dictionary

responses = {}
polling_status = True
while polling_status:
    name = input('enter the name : ')
    response = input('enter the user response : ')
    responses[name] = response

    repeat = input('would like to add another response : ')
    if repeat == 'no':
        polling_status = False

print('------- Polling Finished -------')
for name,response in responses.items():
    print(f"\n{name} would like to hear {response}")
