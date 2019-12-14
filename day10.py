# Advent of Code 2019
# Day 10

import intcode_final as ic
import math
import matplotlib.pyplot as plt

working_code = [3, 8, 1005, 8, 345, 1106, 0, 11, 0, 0, 0, 104, 1, 104, 0, 3, 8, 102, -1, 8, 10, 1001, 10, 1, 10, 4, 10,
                108, 1, 8, 10, 4, 10, 102, 1, 8, 28, 1006, 0, 94, 2, 106, 5, 10, 1, 1109, 12, 10, 3, 8, 1002, 8, -1, 10,
                1001, 10, 1, 10, 4, 10, 1008, 8, 1, 10, 4, 10, 101, 0, 8, 62, 1, 103, 6, 10, 1, 108, 12, 10, 3, 8, 102,
                -1, 8, 10, 1001, 10, 1, 10, 4, 10, 1008, 8, 0, 10, 4, 10, 102, 1, 8, 92, 2, 104, 18, 10, 2, 1109, 2, 10,
                2, 1007, 5, 10, 1, 7, 4, 10, 3, 8, 102, -1, 8, 10, 1001, 10, 1, 10, 4, 10, 108, 0, 8, 10, 4, 10, 102, 1,
                8, 129, 2, 1004, 15, 10, 2, 1103, 15, 10, 2, 1009, 6, 10, 3, 8, 102, -1, 8, 10, 1001, 10, 1, 10, 4, 10,
                1008, 8, 1, 10, 4, 10, 101, 0, 8, 164, 2, 1109, 14, 10, 1, 1107, 18, 10, 1, 1109, 13, 10, 1, 1107, 11,
                10, 3, 8, 102, -1, 8, 10, 101, 1, 10, 10, 4, 10, 108, 0, 8, 10, 4, 10, 1001, 8, 0, 201, 2, 104, 20, 10,
                1, 107, 8, 10, 1, 1007, 5, 10, 3, 8, 102, -1, 8, 10, 101, 1, 10, 10, 4, 10, 1008, 8, 1, 10, 4, 10, 101,
                0, 8, 236, 3, 8, 1002, 8, -1, 10, 1001, 10, 1, 10, 4, 10, 108, 0, 8, 10, 4, 10, 1001, 8, 0, 257, 3, 8,
                102, -1, 8, 10, 101, 1, 10, 10, 4, 10, 108, 1, 8, 10, 4, 10, 102, 1, 8, 279, 1, 107, 0, 10, 1, 107, 16,
                10, 1006, 0, 24, 1, 101, 3, 10, 3, 8, 102, -1, 8, 10, 101, 1, 10, 10, 4, 10, 108, 0, 8, 10, 4, 10, 1002,
                8, 1, 316, 2, 1108, 15, 10, 2, 4, 11, 10, 101, 1, 9, 9, 1007, 9, 934, 10, 1005, 10, 15, 99, 109, 667,
                104, 0, 104, 1, 21101, 0, 936995730328, 1, 21102, 362, 1, 0, 1105, 1, 466, 21102, 1, 838210728716, 1,
                21101, 373, 0, 0, 1105, 1, 466, 3, 10, 104, 0, 104, 1, 3, 10, 104, 0, 104, 0, 3, 10, 104, 0, 104, 1, 3,
                10, 104, 0, 104, 1, 3, 10, 104, 0, 104, 0, 3, 10, 104, 0, 104, 1, 21102, 1, 235350789351, 1, 21101, 0,
                420, 0, 1105, 1, 466, 21102, 29195603035, 1, 1, 21102, 1, 431, 0, 1105, 1, 466, 3, 10, 104, 0, 104, 0,
                3, 10, 104, 0, 104, 0, 21101, 0, 825016079204, 1, 21101, 0, 454, 0, 1105, 1, 466, 21101, 837896786700,
                0, 1, 21102, 1, 465, 0, 1106, 0, 466, 99, 109, 2, 21201, -1, 0, 1, 21101, 0, 40, 2, 21102, 1, 497, 3,
                21101, 0, 487, 0, 1105, 1, 530, 109, -2, 2106, 0, 0, 0, 1, 0, 0, 1, 109, 2, 3, 10, 204, -1, 1001, 492,
                493, 508, 4, 0, 1001, 492, 1, 492, 108, 4, 492, 10, 1006, 10, 524, 1101, 0, 0, 492, 109, -2, 2105, 1, 0,
                0, 109, 4, 2102, 1, -1, 529, 1207, -3, 0, 10, 1006, 10, 547, 21102, 1, 0, -3, 21201, -3, 0, 1, 22102, 1,
                -2, 2, 21101, 1, 0, 3, 21102, 1, 566, 0, 1105, 1, 571, 109, -4, 2106, 0, 0, 109, 5, 1207, -3, 1, 10,
                1006, 10, 594, 2207, -4, -2, 10, 1006, 10, 594, 21201, -4, 0, -4, 1106, 0, 662, 21201, -4, 0, 1, 21201,
                -3, -1, 2, 21202, -2, 2, 3, 21101, 613, 0, 0, 1105, 1, 571, 22101, 0, 1, -4, 21101, 0, 1, -1, 2207, -4,
                -2, 10, 1006, 10, 632, 21101, 0, 0, -1, 22202, -2, -1, -2, 2107, 0, -3, 10, 1006, 10, 654, 22101, 0, -1,
                1, 21102, 654, 1, 0, 105, 1, 529, 21202, -2, -1, -2, 22201, -4, -2, -4, 109, -5, 2105, 1, 0]


class Robot():

    def __init__(self, identification: str, intcode: ic.IntCode):
        self.id = identification
        self.x = 0
        self.y = 0
        self.facing = 90
        self.instructions = []
        self.painted = []
        self.pc = intcode
        self.env = {(0, 0): 1, (0, 1): 0}

    #       This is the starting environment for part 1:
    #       self.env = {(0, 0): 0, (0, 1): 0}

    def showLocation(self):
        print((self.x, self.y))
        return

    def paint(self, code):
        if code == 0:
            self.env[(self.x, self.y)] = 0
            if (self.x, self.y) not in self.painted:
                self.painted.append((self.x, self.y))
            else:
                return
        elif code == 1:
            self.env[(self.x, self.y)] = 1
            if (self.x, self.y) not in self.painted:
                self.painted.append((self.x, self.y))
            else:
                return
        # From Part 1
        # self.showLocation()

    def move(self):
        self.x += int(math.cos(math.radians(self.facing)))
        self.y += int(math.sin(math.radians(self.facing)))
        return

    def turn(self, code):
        # Turn left if 0, right if 1
        if code == 0:
            self.facing = self.facing + 90
            self.move()
            return
        elif code == 1:
            self.facing = self.facing - 90
            self.move()
            return

    def scan(self):
        try:
            code = self.env[(self.x, self.y)]
        except KeyError:
            self.env[(self.x, self.y)] = 0
            code = self.env[(self.x, self.y)]
        self.pc.writeRam(code)
        self.pc.runToDoubleOutput()

    def execute(self):
        try:
            move_order = self.pc.readRam()
            paint_order = self.pc.readRam()
        except IndexError:
            print("Final coordinate: ")
            self.showLocation()
            # From Part 1
            # print(len(self.painted))
            return 0
        self.paint(paint_order)
        self.turn(move_order)
        return 1

    def startRobot(self):
        running = 1
        while running:
            self.scan()
            running = self.execute()

    def drawPainted(self):
        list_x, list_y = zip(*self.painted)
        colors = []
        for x, y in zip(list_x, list_y):
            colors.append(self.env[(x, y)])

        plt.scatter(list_x, list_y, s=100, marker='o', c=colors)
        plt.show()


software = ic.IntCode("Software", working_code.copy())

friend = Robot("Friend", software)
friend.startRobot()
friend.drawPainted()
