# unpacking krwargs
def named(**kwargs):
    print(kwargs)


named(name='Bob', age=25)
#named({'name': 'Bob', 'age': 25})
named(**{'name': 'Bob', 'age': 25})


details = {'name': 'Bob', 'age': 25}
named(**details)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f'{arg}: {value}')


print_nicely(name='Bob', age=25)


# both args and kwargs
def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name='Bob', age=25)


'''
def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)
'''


def myfunction(**kwargs):
    print(kwargs)


myfunction(**{'name': 'Bob', 'age': 25})
# myfunction(**'Bob')
# myfunction(**None)
