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

# z = tuple(i for i in zip(a, b))
# print(z)
z = ((3, 2), (4, 5), (6, 7), (9, 7))

y = z[2]

w = 'true' if (7, 9) in z else "false"
print(w)
