#!/usr/bin/python

import Tkinter
import random

order = 4
blank_tile = str(order * order)

class tile(object):
    def __init__(self, puzzle, master, row, col, label):
        self._puzzle = puzzle
        self._row = row
        self._col = col
        self._label = label
        self._button_text = Tkinter.StringVar()
        if self._label == blank_tile:
            self._button_text.set('')
        else:
            self._button_text.set(self._label)
        self._button = Tkinter.Button(master, width=1,
                                      textvariable=self._button_text,
                                      command=self.buttonClick)
        self._button.grid(row=self._row, column=self._col)

    @property
    def label(self):
        return self._label

    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col

    @label.setter
    def label(self, value):
        self._label = value
        if self._label == blank_tile:
            self._button_text.set('')
        else:
            self._button_text.set(self._label)


    def buttonClick(self):
        print(self._label)
        if not self.isBlank():
            puzzle.moveMe(self)

    def isBlank(self):
        return self._label == blank_tile

    def doCheck(self):
        


class Puzzle(Tkinter.Frame):

    def __init__(self, master=None):
        Tkinter.Frame.__init__(self, master)
        self.buttons = [[0 for x in range(order)] for
                        y in range(order)]

        for i in range(order):
            for j in range(order):
                self.buttons[i][j] = tile(self, master, i, j,
                                          str(j + 1 + (i * order)))
        self.shuffle()

    def shuffle(self):
        row = 3
        col = 3
        for i in range(1,101):
            blank = self.buttons[row][col]
            direction = random.randint(1,4)
            if direction == 1:
                try:
                    up = self.buttons[row - 1][col]
                    self.swapLabels(up, blank)
                    row = row - 1
                except:
                    continue
            elif direction == 2:
                try:
                    down = self.buttons[row + 1][col]
                    self.swapLabels(down, blank)
                    row = row + 1
                except:
                    continue
            elif direction == 3:
                try:
                    right = self.buttons[row][col + 1]
                    self.swapLabels(right, blank)
                    col = col + 1
                except:
                    continue
            elif direction == 4:
                try:
                    left = self.buttons[row][col - 1]
                    self.swapLabels(left, blank)
                    col = col - 1
                except:
                    continue

    def swapLabels(self, first, second):
        if first.isBlank():
            first.label = second.label
            second.label = blank_tile
        elif second.isBlank():
            second.label = first.label
            first.label = blank_tile
        else:
            raise Exception("Illegal swap")

    def moveMe(self, clicked):
        row = clicked.row
        col = clicked.col
        print("%s %s" % (row, col))
        if self.moveDown(clicked):
            print("Moved down")
        elif self.moveUp(clicked):
            print("Moved up")
        elif self.moveRight(clicked):
            print("Moved right")
        elif self.moveLeft(clicked):
            print("Moved left")
        else:
            print("Could not move")

    def moveDown(self, clicked):
        row = clicked.row
        col = clicked.col
        #clicked = self.buttons[row][col]
        if row >= order - 1:
            return False
        below = self.buttons[row + 1][col]
        if below.isBlank():
            self.swapLabels(below, clicked)
            self.check()
            return True

    def moveUp(self, clicked):
        row = clicked.row
        col = clicked.col
        #clicked = self.buttons[row][col]
        if row == 0:
            return False
        above = self.buttons[row - 1][col]
        if above.isBlank():
            self.swapLabels(above, clicked)
            self.check()
            return True

    def moveRight(self, clicked):
        row = clicked.row
        col = clicked.col
        #clicked = self.buttons[row][col]
        if col >= order - 1:
            return False
        right = self.buttons[row][col + 1]
        if right.isBlank():
            self.swapLabels(right, clicked)
            self.check()
            return True

    def moveLeft(self, clicked):
        row = clicked.row
        col = clicked.col
        #clicked = self.buttons[row][col]
        if col == 0:
            return False
        left = self.buttons[row][col - 1]
        if left.isBlank():
            self.swapLabels(left, clicked)
            self.check()
            return True


if __name__ == "__main__":
    puzzle = Puzzle()
    puzzle.mainloop()
