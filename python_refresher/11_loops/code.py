# while loop
number = 7
user_input = input('Would you like to play? (Y/n)')

while user_input != 'n':
    user_number = int(input('Guess our number: '))
    if user_number == number:
        print('You guessed correctly!')
    elif abs(number - user_number) == 1:
        print('You were off by 1.')
    else:
        print('Sorry, it\'s wrong!')

    user_input = input('Would you like to play? (Y/n)')


# break keyword
while True:
    user_input = input('Would you like to play? (Y/n)')

    if user_input == 'n':
        break

    user_number = int(input('Guess our number: '))
    if user_number == number:
        print('You guessed correctly!')
    elif abs(number - user_number) == 1:
        print('You were off by 1.')
    else:
        print('Sorry, it\'s wrong!')


# for loop
friends = ['Rolf', 'Jen', 'Bob', 'Anne']
for friend in friends:
    print(f'{friend} is my friend.')


# for loop to calculate average
grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)


# rewrite with sum()
grades = [35, 67, 98, 100, 100]
total = sum(grades)
amount = len(grades)

print(total / amount)
