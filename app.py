# First task - Variables
age = 7
name = 'Nemo'

print('My name is: ', name, 'and my age is: ', age)

# Second task - Functions
def add_two_numbers(x, y):
    total = x + y
    return total

output = add_two_numbers(5, 5)
print(output)

# Third task - List

people = ['Nemo', 'Veronica', 'Gizmo', 'Aladdin']
people.append('Nelson') # This adds
print(people)

name = people.pop() # Removes last item
print(name)
print(people)

people.remove('Veronica') # Removes specifict item
print(people)

people.append(5) # Possible to mix types
print(people)

# Fourth task - Tuples
dogs = ('Nemo', 'Nelson')
print(dogs)

dogs = (1, 2) # Override items
print(dogs)

# Fifth task - Conditional statement
age = 25

if age < 19:
    print('Person is a child')
elif age < 70:
    print('The person is an adult')
else:
    print('The person is an senior')

# Sixth task - For loop
people = ['Nemo', 'Veronica', 'Gizmo', 'Aladdin']

for name in people:
    print(name)

def print_sq_values(numbers):
    for n in numbers:
        sq = n*n
        print('Squared of ', n, 'is ', sq)

numbers = [1, 2, 3, 4, 5]
print_sq_values(numbers)

# Seventh task - User input
name = input('Enter your name: ')
print(name)
print(type(name)) # Always a string

# Eighth task - While loop
user_input = input('Fake python editor >>> ')

while user_input != 'exit':
    user_input = input('>>> ')
    print('You entered: ', user_input)

print('Goodbye!')

# Ninth task - To-Do list
data = []

def show_menu():
    print('Menu:')
    print('1. Add an item:')
    print('2. Mark as done:')
    print('3. View items:')
    print('4. Exit:')

while user_input != '4':

    show_menu()

    user_input = input('Enter your choice ')
    if user_input == '1':
        item = input('What is to be done?')
        data.append(item)
        print('Added item: ', data)
    elif user_input == '2':
        item = input('What is to be marked as done?')
        if item in data:
            data.remove(item)
            print('Removed item: ', item)
        else:
            print('Item does not exist in list')
    elif user_input == '3':
        print('List of to do items: ')
        for item in data:
            print(item)
    elif user_input == '4':
        print('Goodbye!')
    else:
        print(' Please enter one of 1, 2, 3, 4')