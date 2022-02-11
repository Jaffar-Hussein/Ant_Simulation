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


#
# x = [random.randint(1, 20)]
# y = [random.randint(1, 20)]
# choices = ['east', 'west', 'north', 'south']
# for a in range(8):
#     choice = random.choice(choices)
#     if choice == 'east' and x[a] != 20:
#         x.append(x[a] + 1)
#         y.append(y[a])
#     elif choice == 'west' and x[a] != 1:
#         x.append(x[a] - 1)
#         y.append(y[a])
#     elif choice == 'north' and y[a] != 20:
#         x.append(x[a])
#         y.append(y[a] + 1)
#     elif choice == 'south' and y[a] != 1:
#         x.append(x[a])
#         y.append(y[a] - 1)
#     else:
#         x.append(x[a])
#         y.append(y[a])
# print(x)
# print(y)
ants_dict = {}
for b in range(2):

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
    food_positionx, food_positiony = food_points(5)

    interx = set(food_positionx).intersection(x)
    intery = set(food_positiony).intersection(y)
    print("y:", intery)
    print(x)
    print("x:", interx)
    print(y)

    pv = [20]
    for c in range(len(x)):
        if x[c] in interx and y[c] in intery:
            pv.append(20)
            print("x:------   ",x[c])

            print("y:-----   ",y[c])

        else:
            pv.append(pv[c] - 2)

    # print("*"*50)
    print(pv)

    ants_dict[b] = {
        "x": x,
        'y': y,
        'pv': pv
    }
#

