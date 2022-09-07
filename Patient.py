from Cell import Cell
from ListCells import ListCells
from ListPeriods import ListPeriods

class Patient:
    def __init__(self, name=None, age=None, periods=None, matrix=None, cells=ListCells()):
        self.__name = name
        self.__age = age
        self.__periods = periods
        self.__matrix = matrix
        self.__cells = cells
        self.__listperiods = ListPeriods()

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age
    
    def getPeriods(self):
        return self.__periods
    
    def getMatrix(self):
        return self.__matrix

    def getCells(self):
        return self.__cells
    
    def getListPeriods(self):
        return self.__listperiods

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def setPeriods(self, listperiods):
        self.__listperiods = listperiods

    def setMatrix(self, matrix):
        self.__matrix = matrix
    
    def setCells(self, cells=ListCells()):
        self.__cells = cells

    def setPeriods(self, periods=ListPeriods()):
        self.__periods = periods

    def ValueNextPeriod(self):
        self.__listperiods.insert(self.__cells)
        self.__cells = self.__cells.ValueNextPeriod()




    