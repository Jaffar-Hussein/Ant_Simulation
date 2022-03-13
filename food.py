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


def ant_creator(ants_number, food_number):
    """

    :return:

    """

    foodx, foody = food_points(food_number)
    ant_dict = {

    }
    for one_ant in range(ants_number):

        z = tuple(i for i in zip(foodx, foody))
        # print(z)

        x = [random.randint(1, 20)]
        y = [random.randint(1, 20)]
        pv = [20]

        while len(x) <= 10 and len(pv) <= 10:
            # pv check
            indextocheck = [x[len(x) - 1], y[len(y) - 1]]
            pv.append(20) if tuple(indextocheck) in z else pv.append(pv[len(pv) - 1] - 2)
            # print(indextocheck)
            # print(tuple(indextocheck))
            # Direction check
            directions = ['south', 'north', 'east', 'west']
            direction = random.choice(directions)
            # print(f"x is {x}")
            # print(f"y is {y}")
            # print(f"pv is {pv}")
            # print(f"direction is {foodx}")
            if direction == 'east' and x[len(x) - 1] < 20:
                x.append((x[len(x) - 1] + 1))
                y.append(y[len(y) - 1])
            elif direction == 'west' and x[len(x) - 1] > 1:
                x.append(x[len(x) - 1] - 1)
                y.append(y[len(y) - 1])
            elif direction == 'south' and y[len(y) - 1] > 1:
                y.append(y[len(y) - 1] - 1)
                x.append(x[len(x) - 1])
            elif direction == 'north' and y[len(y) - 1] < 20:
                y.append(y[len(y) - 1] + 1)
                x.append(x[len(x) - 1])
        ant = {
            "x": x,
            "y": y,
            "pv": pv
        }
        ant_dict[one_ant] = ant

    return (ant_dict,
            foodx,
            foody
            )


#
# def ant_multiplier():
#     ant_dict = {}
#     for w in range(8):
#         ant_dict[w] = ant_creator()
#         print('=' * 50)
#     return ant_dict
# print(*ant_dict.values())


# indextocheck2 = [x[len(x) - 1], y[len(y) - 1]]
# xval, yval = indextocheck2
# print(f"x value {xval}")
# print(f"y value {yval}")
# if xval <= 1:
#     x.append(20)
#     y.append(y[len(y) - 1])
# elif yval <= 1:
#     x.append(x[len(x) - 1])
#     y.append(20)
# if xval >= 20:
#     x.append(1)
#     y.append(x[len(y) - 1])
# elif yval >= 20:
#     x.append(x[len(x) - 1])
#     y.append(1)

# def ant_generator(n):
#     ant_creator()
#     for w in range(n):
#         ants_dictionary = {
#             n: {
#                 "x": x,
#                 "y": y,
#                 "pv": pv
#
#             }
#         }
#     return ants_dictionary

# ants_dict = {0: {
#     "x": x,
#     'y': y,
#     'pv': pv
# }}
delay = 750

# print(ant_creator(5,15)
#       )
ant_dict, foodx, foody = ant_creator(5, 15)
#
app = Visual_App(ant_dict, foodx, foody, pv=20, delay=delay)
app.run()
