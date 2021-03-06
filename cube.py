import copy

default = ["L", "L'", "L2", "R", "R'", "R2", "U", "U'", "U2", "D", "D'", "D2","F", "F'", "F2", "B", "B'", "B2"]
class Cube:
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

        if clockwise:
            (self.rubik[0][0], self.rubik[0][3], self.rubik[0][6]) = (actual[4][0], actual[4][3], actual[4][6])
            (self.rubik[2][2], self.rubik[2][5], self.rubik[2][8]) = (actual[5][6], actual[5][3], actual[5][0])
            (self.rubik[4][0], self.rubik[4][3], self.rubik[4][6]) = (actual[2][8], actual[2][5], actual[2][2])
            (self.rubik[5][0], self.rubik[5][3], self.rubik[5][6]) = (actual[0][0], actual[0][3], actual[0][6])

        else:
            (self.rubik[0][0], self.rubik[0][3], self.rubik[0][6]) = (actual[5][0], actual[5][3], actual[5][6])
            (self.rubik[2][2], self.rubik[2][5], self.rubik[2][8]) = (actual[4][6], actual[4][3], actual[4][0])
            (self.rubik[4][0], self.rubik[4][3], self.rubik[4][6]) = (actual[0][0], actual[0][3], actual[0][6])
            (self.rubik[5][0], self.rubik[5][3], self.rubik[5][6]) = (actual[2][8], actual[2][5], actual[2][2])

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
    
    def down(self, clockwise=True):
        actual = copy.deepcopy(self.rubik)

        if clockwise:
            (self.rubik[0][6], self.rubik[0][7], self.rubik[0][8]) = (actual[1][6], actual[1][7], actual[1][8])
            (self.rubik[1][6], self.rubik[1][7], self.rubik[1][8]) = (actual[2][6], actual[2][7], actual[2][8])
            (self.rubik[2][6], self.rubik[2][7], self.rubik[2][8]) = (actual[3][6], actual[3][7], actual[3][8])
            (self.rubik[3][6], self.rubik[3][7], self.rubik[3][8]) = (actual[0][6], actual[0][7], actual[0][8])
        else:
            (self.rubik[0][6], self.rubik[0][7], self.rubik[0][8]) = (actual[3][6], actual[3][7], actual[3][8])
            (self.rubik[1][6], self.rubik[1][7], self.rubik[1][8]) = (actual[0][6], actual[0][7], actual[0][8])
            (self.rubik[2][6], self.rubik[2][7], self.rubik[2][8]) = (actual[1][6], actual[1][7], actual[1][8])
            (self.rubik[3][6], self.rubik[3][7], self.rubik[3][8]) = (actual[2][6], actual[2][7], actual[2][8])

        self.rotate(clockwise, self.rubik[5])
    
    def face(self, clockwise=True):
        actual = copy.deepcopy(self.rubik)

        if clockwise:
            (self.rubik[1][2], self.rubik[1][5], self.rubik[1][8]) = (actual[5][0], actual[5][1], actual[5][2])    
            (self.rubik[3][0], self.rubik[3][3], self.rubik[3][6]) = (actual[4][6], actual[4][7], actual[4][8])
            (self.rubik[4][6], self.rubik[4][7], self.rubik[4][8]) = (actual[1][8], actual[1][5], actual[1][2])
            (self.rubik[5][0], self.rubik[5][1], self.rubik[5][2]) = (actual[3][6], actual[3][3], actual[3][0])
        else:
            (self.rubik[1][2], self.rubik[1][5], self.rubik[1][8]) = (actual[4][8], actual[4][7], actual[4][6])
            (self.rubik[3][0], self.rubik[3][3], self.rubik[3][6]) = (actual[5][2], actual[5][1], actual[5][0])
            (self.rubik[4][6], self.rubik[4][7], self.rubik[4][8]) = (actual[3][0], actual[3][3], actual[3][6])
            (self.rubik[5][0], self.rubik[5][1], self.rubik[5][2]) = (actual[1][2], actual[1][5], actual[1][8])

        self.rotate(clockwise, self.rubik[0])

    def back(self, clockwise=True):
        actual = copy.deepcopy(self.rubik)

        if clockwise:
            (self.rubik[1][0], self.rubik[1][3], self.rubik[1][6]) = (actual[4][2], actual[4][1], actual[4][0])    
            (self.rubik[3][2], self.rubik[3][5], self.rubik[3][8]) = (actual[5][8], actual[5][7], actual[5][6])
            (self.rubik[4][0], self.rubik[4][1], self.rubik[4][2]) = (actual[3][2], actual[3][5], actual[3][8])
            (self.rubik[5][6], self.rubik[5][7], self.rubik[5][8]) = (actual[1][0], actual[1][3], actual[1][6])
            
            
        else:
            (self.rubik[1][0], self.rubik[1][3], self.rubik[1][6]) = (actual[5][6], actual[5][7], actual[5][8])
            (self.rubik[3][2], self.rubik[3][5], self.rubik[3][8]) = (actual[4][0], actual[4][1], actual[4][2])
            (self.rubik[4][0], self.rubik[4][1], self.rubik[4][2]) = (actual[1][8], actual[1][5], actual[1][2])
            (self.rubik[5][6], self.rubik[5][7], self.rubik[5][8]) = (actual[3][8], actual[3][5], actual[3][2])

        self.rotate(clockwise, self.rubik[2])

    def apply(self, moviments=[]):
        for move in moviments:
            if move not in default:
                print("nao existe esse movimento")

            if len(move) == 1:
                if move[0] == "L":
                    self.left()
                elif move[0] == "R":
                    self.rigth()
                elif move[0] == "U":
                    self.up()
                elif move[0] == "D":
                    self.down()
                elif move[0] == "F":
                    self.face()
                elif move[0] == "B":
                    self.back()

            elif move[1] == "'":
                if move[0]== "L":
                    self.left(False)
                elif move[0]== "R":
                    self.rigth(False)
                elif move[0]== "U":
                    self.up(False)
                elif move[0]== "D":
                    self.down(False)
                elif move[0]== "F":
                    self.face(False)
                elif move[0]== "B":
                    self.back(False)

            elif move[1] == "2":
                if move[0] == "L":
                    self.left()
                    self.left()
                elif move[0] == "R":
                    self.rigth()
                    self.rigth()
                elif move[0] == "U":
                    self.up()
                    self.up()
                elif move[0] == "D":
                    self.down()
                    self.down()
                elif move[0] == "F":
                    self.face()
                    self.face()
                elif move[0] == "B":
                    self.back()
                    self.back()