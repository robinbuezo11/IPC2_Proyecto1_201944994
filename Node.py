from Cell import Cell

class Node:
    def __init__(self, next=None, cell=Cell()):
        self.__next = next
        self.__cell = cell

    def getNext(self):
        return self.__next

    def getCell(self):
        return self.__cell

    def setNext(self, next):
        self.__next = next

    def setCell(self, cell):
        self.__cell = cell