from ListCells import ListCells

class NodePeriod:
    def __init__(self, next=None, period=ListCells()):
        self.__next = next
        self.__period = period

    def getNext(self):
        return self.__next
    
    def getPeriod(self):
        return self.__period

    def setNext(self, next):
        self.__next = next

    def setPeriod(self, period):
        self.__period = period