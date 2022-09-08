from colorama import Fore
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
        self.__period = 0
        self.__n = 0
        self.__n1 = 0
        self.__result = 'Leve'

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

    def getPeriod(self):
        return self.__period

    def getN(self):
        return self.__n

    def getN1(self):
        return self.__n1

    def getResult(self):
        return self.__result

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def setPeriods(self, periods):
        self.__periods = periods

    def setMatrix(self, matrix):
        self.__matrix = matrix
    
    def setCells(self, cells=ListCells()):
        self.__cells = cells

    def setListPeriods(self, listperiods=ListPeriods()):
        self.__listperiods = listperiods

    def setPeriod(self, period):
        self.__period = period

    def setN(self, n):
        self.__n = n

    def setN1(self, n1):
        self.__n1 = n1

    def setResult(self, result):
        self.__result = result

    def ValueNextPeriod(self):
        if self.__period < self.__periods:
            self.__listperiods.insert(self.__cells)
            self.__period += 1
            self.__cells = self.__cells.ValueNextPeriod()
            self.study(self.__cells)
            print(Fore.CYAN + f'Periodo evaluado: {self.__period}, N: {self.__n}, N1: {self.__n1},  Enfermedad: {self.__result}')
        else:
            print(Fore.RED + 'Ya se cumplió el límite de periodos')
            return False

    def study(self, cells):
        period = self.__listperiods.searchInList(cells)
        if period == 0 and self.__period == 1:
            if self.__result == 'Leve':
                self.__n = self.__period
                self.__result = 'Mortal'
            print(Fore.RED + 'Se encontró un patrón repetido')
        elif period == 0 and self.__period != 1:
            if self.__result == 'Leve':
                self.__n = self.__period
                self.__result = 'Grave'
            print(Fore.RED + 'Se encontró un patrón repetido')
        elif period != None:
            if period != 0 and (self.__period-period) == 1:
                if self.__result == 'Leve':
                    self.__n = self.__period
                    self.__n1 = self.__period-period
                    self.__result = 'Mortal'
                print(Fore.RED + 'Se encontró un patrón repetido')
            elif period != 0 and (self.__period-period) != 1:
                if self.__result == 'Leve':
                    self.__n = self.__period
                    self.__n1 = self.__period-period
                    self.__result = 'Grave'
                print(Fore.RED + 'Se encontró un patrón repetido')



    