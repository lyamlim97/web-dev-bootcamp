numbers = [1, 3, 5]
doubled = [num * 2 for num in numbers]
print(doubled)


# dealing with strings
friends = ['Rolf', 'Sam', 'Samantha', 'Saurabh', 'Jen']
starts_s = []

for friend in friends:
    if friend.startswith('S'):
        starts_s.append(friend)

print(starts_s)


# using list comprehension
friends = ['Rolf', 'Sam', 'Samantha', 'Saurabh', 'Jen']
starts_s = [friend for friend in friends if friend.startswith('S')]
print(starts_s)


# list comprehensions creates a new list
friends = ['Sam', 'Samantha', 'Saurabh']
# same as above
starts_s = [friend for friend in friends if friend.startswith('S')]

print(friends)
print(starts_s)
print(friends is starts_s)
print('friends: ', id(friends), ' starts_s: ', id(starts_s))
