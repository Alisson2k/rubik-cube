import copy

class Moviments:
    def __init__(self):
        self.rubik = self.initialize()

    def initialize(self):
        return [
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']
        ]

    def __str__(self):
        str = ""

        for face in self.rubik:
            str += "[ "
            for piece in face:
                str += "'" + piece + "' "
            str += "]\n"

        str += "\n\n\n"

        return str

    def rotate(self, clockwise, piece):
        actual = copy.deepcopy(piece)

        if clockwise:
            piece[0] = actual[6]
            piece[1] = actual[3]
            piece[2] = actual[0]
            piece[3] = actual[7]
            piece[5] = actual[1]
            piece[6] = actual[8]
            piece[7] = actual[5]
            piece[8] = actual[2]
        else:
            piece[0] = actual[2]
            piece[1] = actual[5]
            piece[2] = actual[8]
            piece[3] = actual[1]
            piece[5] = actual[7]
            piece[6] = actual[0]
            piece[7] = actual[3]
            piece[8] = actual[6]

    def left(self, clockwise=True):
        actual = copy.deepcopy(self.rubik)

        # in order, GREEN - BLUE - WHITE - YELLOW

        if clockwise:
            (self.rubik[0][0], self.rubik[0][3], self.rubik[0][6]) = (actual[4][0], actual[4][3], actual[4][6])
            (self.rubik[2][2], self.rubik[2][5], self.rubik[2][8]) = (actual[5][6], actual[5][3], actual[5][0])
            (self.rubik[4][0], self.rubik[4][3], self.rubik[4][6]) = (actual[2][8], actual[2][5], actual[2][2])
            (self.rubik[5][0], self.rubik[5][3], self.rubik[5][6]) = (actual[0][0], actual[0][3], actual[0][6])

        else:
            (self.rubik[0][0], self.rubik[0][3], self.rubik[0][6]) = (actual[5][0], actual[5][3], actual[5][6])
            (self.rubik[2][2], self.rubik[2][5], self.rubik[2][8]) = (actual[4][2], actual[4][5], actual[4][8])
            (self.rubik[4][0], self.rubik[4][3], self.rubik[4][6]) = (actual[0][0], actual[0][3], actual[0][6])
            (self.rubik[5][0], self.rubik[5][3], self.rubik[5][6]) = (actual[2][0], actual[2][3], actual[2][6])

        self.rotate(clockwise, self.rubik[1])


    def rigth(self, clockwise=True):
        actual = copy.deepcopy(self.rubik)

        if clockwise:
            (self.rubik[0][2], self.rubik[0][5], self.rubik[0][8]) = (actual[5][2], actual[5][5], actual[5][8])
            (self.rubik[2][0], self.rubik[2][3], self.rubik[2][6]) = (actual[4][8], actual[4][5], actual[4][2])
            (self.rubik[4][2], self.rubik[4][5], self.rubik[4][8]) = (actual[0][2], actual[0][5], actual[0][8])
            (self.rubik[5][2], self.rubik[5][5], self.rubik[5][8]) = (actual[2][6], actual[2][3], actual[2][0])
        else:
            (self.rubik[0][2], self.rubik[0][5], self.rubik[0][8]) = (actual[4][2], actual[4][5], actual[4][8])
            (self.rubik[2][0], self.rubik[2][3], self.rubik[2][6]) = (actual[5][8], actual[5][5], actual[5][2])
            (self.rubik[4][2], self.rubik[4][5], self.rubik[4][8]) = (actual[2][6], actual[2][3], actual[2][0])
            (self.rubik[5][2], self.rubik[5][5], self.rubik[5][8]) = (actual[0][2], actual[0][5], actual[0][8])
        
        self.rotate(clockwise, self.rubik[3])

    def up(self, clockwise=True):
        actual = copy.deepcopy(self.rubik)

        if clockwise:
            (self.rubik[0][0], self.rubik[0][1], self.rubik[0][2]) = (actual[3][0], actual[3][1], actual[3][2])
            (self.rubik[1][0], self.rubik[1][1], self.rubik[1][2]) = (actual[0][0], actual[0][1], actual[0][2])
            (self.rubik[2][0], self.rubik[2][1], self.rubik[2][2]) = (actual[1][0], actual[1][1], actual[1][2])
            (self.rubik[3][0], self.rubik[3][1], self.rubik[3][2]) = (actual[2][0], actual[2][1], actual[2][2])
        else:
            (self.rubik[0][0], self.rubik[0][1], self.rubik[0][2]) = (actual[1][0], actual[1][1], actual[1][2])
            (self.rubik[1][0], self.rubik[1][1], self.rubik[1][2]) = (actual[2][0], actual[2][1], actual[2][2])
            (self.rubik[2][0], self.rubik[2][1], self.rubik[2][2]) = (actual[3][0], actual[3][1], actual[3][2])
            (self.rubik[3][0], self.rubik[3][1], self.rubik[3][2]) = (actual[0][0], actual[0][1], actual[0][2])

        self.rotate(clockwise, self.rubik[4])
    
    