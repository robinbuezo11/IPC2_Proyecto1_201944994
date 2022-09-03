from Cell import Cell
from Node import Node

class ListCell:
    def __init__(self):
        self.__first = Node()

    def insert(self, cell=Cell()):
        if self.__first is None:
            self.__first = Node(cell=cell)
            return
        
        node = self.__first
        while node.getNext:
            node = node.getNext
        node.getNext = Node(cell=cell)

    