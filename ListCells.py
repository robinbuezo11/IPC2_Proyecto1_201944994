from Cell import Cell
from NodeCell import NodeCell

class ListCells:
    def __init__(self):
        self.__first = NodeCell()
        self.__magnitude = None

    def insert(self, cell=Cell()):
        if self.__first.getCell().getStatus() is None:
            self.__first = NodeCell(cell=cell)
            return
        
        node = self.__first
        while node.getNext():
            node = node.getNext()
        node.setNext(NodeCell(cell=cell))

    def updateCell(self, cell=Cell()):
        node = self.__first
        while node:
            if node.getCell().getRow() == cell.getRow() and node.getCell().getColumn() == cell.getColumn():
                node.setCell(cell=cell)
                return
            node = node.getNext()
        print('Nodo no encontrado para configurar valor')

    def printMatrix(self):
        node = self.__first
        while node:
            if node.getNext() == None:
                print(node.getCell().getStatus())
            elif node.getCell().getRow()==node.getNext().getCell().getRow():
                print(node.getCell().getStatus(),end='')
            else:
                print(node.getCell().getStatus())
            node = node.getNext()
        
    def setMatrixWithMagnitude(self, magnitude):
        self.__magnitude = magnitude
        iter = 0
        row = 1
        column = 1
        while iter < magnitude*magnitude:
            self.insert(Cell(status=0, row=row, column=column))
            if column == magnitude:
                column = 1
                row +=1
            else:
                column += 1
            
            if row > magnitude:
                return
            iter+=1

    def ValueNextPeriod(self):
        node = self.__first
        while node:
            nodeaux = self.__first
            infectedcells = 0
            while nodeaux:
                if (nodeaux.getCell().getRow()==node.getCell().getRow()-1  or 
                nodeaux.getCell().getRow()==node.getCell().getRow() or 
                nodeaux.getCell().getRow()==node.getCell().getRow()+1) and (nodeaux.getCell().getColumn()==node.getCell().getColumn()-1 or 
                nodeaux.getCell().getColumn()==node.getCell().getColumn() or 
                nodeaux.getCell().getColumn()==node.getCell().getColumn()+1) and node != nodeaux and nodeaux.getCell().getStatus()==1:
                    infectedcells += 1
            
                if node.getCell().getStatus() == 0 and infectedcells == 3:
                    node.getCell().setStatus(1)
                elif node.getCell().getStatus() == 1 and infectedcells != 2 and infectedcells != 3:
                    node.getCell().setStatus(0)
                
                nodeaux = nodeaux.getNext()
            node = node.getNext()