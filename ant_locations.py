import random

x = [random.randint(1, 20)]
y = [random.randint(1, 20)]
choices = ['east', 'west', 'north', 'south']
for a in range(8):
    choice = random.choice(choices)
    if choice == 'east' and x[a] != 20:
        x.append(x[a] + 1)
        y.append(y[a])
    elif choice == 'west' and x[a] != 1:
        x.append(x[a] - 1)
        y.append(y[a])
    elif choice == 'north' and y[a] != 20:
        x.append(x[a])
        y.append(y[a] + 1)
    elif choice == 'south' and y[a] != 1:
        x.append(x[a])
        y.append(y[a] - 1)
    else:
        x.append(x[a])
        y.append(y[a])
print(x)
print(y)
