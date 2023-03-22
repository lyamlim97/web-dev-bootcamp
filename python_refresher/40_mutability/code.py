a = []
b = a

a.append(35)

print(a)
print(b)

print(id(a))
print(id(b))


a = []
b = []

a.append(35)

print(a)
print(b)

print(id(a))
print(id(b))


# imutable
a = 8597
b = 8597

print(id(a))
print(id(b))

a = 8598

print(id(a))
print(id(b))


a = 'hello'
b = a

print(id(a))
print(id(b))

a += 'world'

print(id(a))
print(id(b))
