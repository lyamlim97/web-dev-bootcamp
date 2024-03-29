def add(x, y):
    result = x + y
    print(result)


add(2, 3)


# if a function doesn't have a parameter, you can't give it arguments
def say_hello():
    print('Hello!')


# say_hello('Bob') # error


# if u add a parameter, then you must give it an argument
def say_hello(name):
    print(f'Hello, {name}!')


say_hello('Bob')
# say_hello() # error


def say_hello(name):
    print(f'Hello, {name}!')


say_hello(name='Bob')


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend/divisor)
    else:
        print('You fool!')


divide(dividend=15, divisor=3)
divide(15, 0)
divide(15, divisor=0)
