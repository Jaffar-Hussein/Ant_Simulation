from ant_animate import Visual_App
import random


def food_points(nb_food: int) -> tuple:
    """
    Gets the number of food points and outputs a set of two lists with
    the random coordinates of food points in the range of 1 to 20 each
    :param nb_food: the number of food points to be
    :return: returns coodinator which is a set of two lists
    """

    coodinator = {"x": random.sample((range(1, 20)), nb_food), "y": random.sample((range(1, 20)), nb_food)}
    # for x in range(nb_food):

    return tuple(coodinator["x"]), tuple(coodinator["y"])
    # return coodinator


fooooood = food_points(15)
a, b = fooooood

z = tuple(i for i in zip(a, b))
print(z)

x = [random.randint(1, 20)]
y = [random.randint(1, 20)]
pv = [20]

while len(x) <= 10 and len(pv) <= 10:
    directions = ['south', 'north', 'east', 'west']
    indextocheck = [x[len(x) - 1], y[len(y) - 1]]
    print(indextocheck)
    print(tuple(indextocheck))
    a = random.choice(directions)
    pv.append(20) if tuple(indextocheck) in z else pv.append(pv[len(pv) - 1] - 2)
    print(f"direction is {a}")
    print(f"x is {x}")
    print(f"y is {y}")
    print(f"pv is {pv}")
    if a == 'east':
        x.append((x[len(x) - 1] + 1))
        y.append(y[len(y) - 1])
    elif a == 'west':
        x.append(x[len(x) - 1] + 1)
        y.append(y[len(y) - 1])
    elif a == 'south':
        y.append(y[len(y) - 1] - 1)
        x.append(x[len(x) - 1])
    elif a == 'north':
        y.append(y[len(y) - 1] + 1)
        x.append(x[len(x) - 1])
    indextocheck2 = [x[len(x) - 1], y[len(y) - 1]]
    xval, yval = indextocheck2
    print(f"x value {xval}")
    print(f"y value {yval}")
    if xval <= 1:
        x.append(20)
        y.append(y[len(y) - 1])
    elif yval <= 1:
        x.append(x[len(x) - 1])
        y.append(20)
    if xval >= 20:
        x.append(1)
        y.append(x[len(y) - 1])
    elif yval >= 20:
        x.append(x[len(x) - 1])
        y.append(1)

ants_dict = {0: {
    "x": x,
    'y': y,
    'pv': pv
}}
delay = 2000
foodx, foody = fooooood

app = Visual_App(ants_dict, foodx, foody, pv=20, delay=delay)
app.run()
