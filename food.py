def food_points(nb_food: int) -> dict:
    """
    Gets the number of food points and outputs a set of two lists with
    the random coordinates of food points in the range of 1 to 20 each
    :param nb_food: the number of food points to be
    :return: returns coodinator which is a set of two lists
    """

    coodinator = {"x": sample((range(1, 20)), nb_food), "y": sample((range(1, 20)), nb_food)}
    # for x in range(nb_food):

    # return tuple(coodinator["x"]), tuple(coodinator["y"])
    return coodinator