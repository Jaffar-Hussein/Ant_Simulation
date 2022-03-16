import random

x = [random.randint(1, 20)]
y = [random.randint(1, 20)]
pv = [20]

indextocheck = [x[len(x) - 1], y[len(y) - 1]]
print(tuple(indextocheck))

directions = ['south', 'north', 'east', 'west']
a = random.choice(directions)

print(a)
