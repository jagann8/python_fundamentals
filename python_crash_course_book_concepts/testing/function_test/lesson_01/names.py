from name_function import get_formatted_name

print('Enter the "q" any time exit!')
while True:
    first = input('Enter the first name ')
    if first == 'q':
        break
    last = input('Enter the last name ')
    if last == 'q':
        break
    fullname = get_formatted_name(first, last)
    print(f"\nNeatly formatted name {fullname}")
