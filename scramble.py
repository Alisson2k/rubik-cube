import random

class Scramble(object):
    def __init__(self):
        self.moviments = ["L", "L'", "L2", "R", "R'", "R2", "U", "U'", "U2", "D", "D'", "D2","F", "F'", "F2", "B", "B'", "B2"]

    def go(self, num=20):
        value = []

        for i in range(num):
            value.append(random.choice(self.moviments))

        return value
