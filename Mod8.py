
import copy

# using alias
animals = ['lion', 'bear', 'tiger']
animals2 = animals
animals3 = animals2

print(animals, animals2, animals3, sep = '\n')
print(id(animals), id(animals2), id(animals3), sep = '\n')

animals2 = ['dog', 'cat', 'bird']
animals3.append('cougar')

print(animals, animals2, animals3, sep = '\n')
print(id(animals), id(animals2), id(animals3), sep = '\n')


# using copy
animals = ['lion', 'bear', 'tiger']
animals2 = animals.copy()
animals3 = animals2.copy()
print(id(animals), id(animals2), id(animals3), sep = '\n')

animals.append("cougar")
print(animals)
print(animals2)


import itertools

# infinite iterator
a = [1,2,3,4,5]
for i in itertools.cycle(a):
    print (i)  # runs until truncated

# If I want it to stop
counter = 0
for i in itertools.cycle(a):
    print (i)
    counter = counter + 1
    if counter > 19:
        break



# itertools.cycle
for i in itertools.count(start = 1, step = 10):
    if i > 110:
        break
    else:                       # Don't need else statement. Can just use print statement
        print(i, end = " ")


for i in itertools.count(start = 1, step = 10):
    if i > 110:
        break
    print(i, end = " ")

# itertools.repeat

for i in itertools.repeat("Team", 5):
    print(i)