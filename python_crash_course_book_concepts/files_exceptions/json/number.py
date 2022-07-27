import json

# numbers = [1, 2, 3, 4, 5, 6, 67, 8, 9]
filename = 'numbers.py'

# with open(filename, 'w') as file_object:
# json.dump(numbers, file_object)

with open(filename) as f:
    numbers = json.load(f)

print(numbers)
