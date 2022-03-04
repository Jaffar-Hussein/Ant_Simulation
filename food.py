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


a, b = food_points(5)

z = tuple(i for i in zip(a, b))
print(z)

x = [random.randint(1, 20)]
y = [random.randint(1, 20)]
pv = [20]

indextocheck = [x[len(x) - 1], y[len(y) - 1]]
print(tuple(indextocheck))
for x in range(10):

    pv.append(20) if tuple(indextocheck) in z else pv.append(pv[len(pv)-1]-2)

print(pv)
