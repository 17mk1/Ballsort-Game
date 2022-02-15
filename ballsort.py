import random

class container:
    def __init__(self, object, balls):
        self.object = object
        self.balls = balls


class ball:
    def __init__(self, colour):
        self.colour = colour


def colour(colours, containerNo):  # creates random list of colours

    bl = []
    for i in colours:
        for j in range(containerNo - 1):
            bl.append(i)
    random.shuffle(bl)
    return bl


def containers(colours):
    ct = []
    for i in colours:
        aContainer = container(capacity, balls)
        ct.append(aContainer)
    return ct


def balls(colours):  # creates balls using generated colours
    bl = []
    for i in colours:
        aBall = ball(i)
        bl.append(aBall)
    return bl


def placement(containerNo, ballList):  # place balls in containers [start of game]
    ct = []
    for i in range(containerNo):
        balls = ballList[0:containerNo - 1]
        contain = container(containerNo, balls)
        del ballList[0:containerNo - 1]
        ct.append(contain)
    return ct
