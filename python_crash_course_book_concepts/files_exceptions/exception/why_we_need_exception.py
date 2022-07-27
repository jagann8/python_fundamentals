
# before exception

# print(5/0) # error of dicvison by zero

# when error raise the program is cant run.
"""so we need to solve these issues when error
   happens .Here we using try_except block.

"""

try:
    print(5/0)
except ZeroDivisionError:
    print('u cant division by zero')


print('rest of the lines executed ..')