from ant_animate import Visual_App
import random


def food_points(nb_food: int = 8) -> tuple:
    """
    Gets the number of food points and outputs two tuples with
    the random coordinates of food points in the range of 1 to 20 each
    :param nb_food: the number of food points to be and by default will
     be 8
    :return: returns coodinator which are two tuples
    """
    return tuple(random.sample((range(1, 20)), nb_food)), tuple(random.sample((range(1, 20)), nb_food))


def ant_creator(ants_number: int = 8, food_number: int = 10, delay: int = 750) -> None:
    """
    Gets the food positions,number of ants and delay then creates the dictionary of
    ants feeds it into ant animate program for graphics
    :param delay: the delay after each tour for an ant to animate
    and default is 750
    :param ants_number:The number of ants to be taken into the program
     and by default is 8
    :param food_number:The number of food positions to be allocated by default is
    10
    """
    foodx, foody = food_points(food_number)
    ant_dict = {
    }
    for one_ant in range(ants_number):
        z = tuple(i for i in zip(foodx, foody))
        x = [random.randint(1, 20)]
        y = [random.randint(1, 20)]
        pv = [20]
        while pv[len(pv) - 1] > 1:
            indextocheck = (x[len(x) - 1], y[len(y) - 1])
            pv.append(pv[len(pv) - 1] - 2) if tuple(indextocheck) not in z else pv.append(20)
            directions = ('south', 'north', 'east', 'west')
            direction = random.choice(directions)
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
    app = Visual_App(ant_dict, foodx, foody, pv=20, delay=delay)
    app.run()


ant_creator(5, 15)
