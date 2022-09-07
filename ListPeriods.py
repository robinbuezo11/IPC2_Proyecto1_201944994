from colorama import Fore
from ListCells import ListCells
from NodePeriod import NodePeriod

class ListPeriods:
    def __init__(self):
        self.__first = None

    def insert(self, period=ListCells()):
        if self.__first is None:
            self.__first = NodePeriod(period=period)
            return
        
        node = self.__first
        while node.getNext():
            node = node.getNext()
        node.setNext(NodePeriod(period=period))
    
    def searchForNum(self,num):
        if self.__first is None:
            print(Fore.RED + 'No se tiene ningún periodo, debe cargar información')
            return
        else:
            iter = 1
            node=self.__first
            while node:
                if iter == num:
                    return node
                else:
                    node = node.getNext()
                    iter += 1
            print(Fore.RED + 'Periodo no encontrado')

