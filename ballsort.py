import random

'''
WHAT'S NEEDED:
1. set up containers [DONE]
2. randomize balls [DONE]
    # of balls = colours*(containers-1)
-------
3. have win condition
4. be able to move balls b/w containers
'''


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


def main():
    colours = ["red", "blue", "yellow", "green", "orange"]
    containerNo = len(colours)
    '''
    # !!!TESTS!!!

    colourList = colour(colours, containerNo)
    print(colourList)

    # print()# end colour test

    ballList = balls(colourList)
    #print(ballList)

    # print()# end balls test

    containers = placement(containerNo, ballList)
    # print(containers, "\n")

    for i in containers:
        print("this container has balls with the colours: ")
        for j in i.balls:
            print(j.colour)
        print()
    '''

    # print()  # end placement test


main()





