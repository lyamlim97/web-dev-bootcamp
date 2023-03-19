friends = {'Bob', 'Rolf', 'Anne'}
abroad = {'Bob', 'Anne'}

local = friends.difference(abroad)
print(local)

print(abroad.difference(friends))  # returns empty set


# union of two sets
local = {'Rolf'}
abroad = {'Bob', 'Anne'}

friends = local.union(abroad)
print(friends)


# intersection of two sets
art = {'Bob', 'Jen', 'Rolf', 'Charlie'}
science = {'Bob', 'Jen', 'Adam', 'Anne'}

both = art.intersection(science)
print(both)
