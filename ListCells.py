from Cell import Cell
from NodeCell import NodeCell
import os

class ListCells:
    def __init__(self):
        self.__first = NodeCell()

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
        newcells = ListCells()
        node = self.__first
        while node:
            nodeaux = self.__first
            infectedcells = 0
            while nodeaux:
                if (nodeaux.getCell().getRow()==node.getCell().getRow()-1  or 
                nodeaux.getCell().getRow()==node.getCell().getRow() or 
                nodeaux.getCell().getRow()==node.getCell().getRow()+1) and (nodeaux.getCell().getColumn()==node.getCell().getColumn()-1 or 
                nodeaux.getCell().getColumn()==node.getCell().getColumn() or 
                nodeaux.getCell().getColumn()==node.getCell().getColumn()+1) and not (node.getCell().getColumn() == nodeaux.getCell().getColumn()
                and node.getCell().getRow() == nodeaux.getCell().getRow()) and nodeaux.getCell().getStatus()==1:
                    infectedcells += 1
                
                nodeaux = nodeaux.getNext()
            
            if node.getCell().getStatus() == 0 and infectedcells == 3:
                newcells.insert(Cell(status=1,row=node.getCell().getRow(),column=node.getCell().getColumn()))
                #node.getCell().setStatus(1)
            elif node.getCell().getStatus() == 1 and infectedcells != 2 and infectedcells != 3:
                newcells.insert(Cell(status=0,row=node.getCell().getRow(),column=node.getCell().getColumn()))
                #node.getCell().setStatus(0)
            else:
                newcells.insert(node.getCell())
            
            node = node.getNext()
        return newcells

    def graphMatrix(self,period):
        node = self.__first

        text = 'digraph { node[shape=box style=filled fillcolor="white"] l[label=<<TABLE cellpadding="20" style="dotted">'
        while node:
            if node.getNext() == None:
                if node.getCell().getStatus() == 0:
                    text += '<TD></TD></TR>'
                else:
                    text += '<TD  bgcolor="#1B76F5"></TD></TR>'
            elif node.getCell().getRow()==node.getNext().getCell().getRow() and node.getCell().getColumn() == 1:
                if node.getCell().getStatus() == 0:
                    text += '<TR><TD></TD>'
                else:
                    text += '<TR><TD  bgcolor="#1B76F5"></TD>'
            elif node.getCell().getRow()==node.getNext().getCell().getRow() and node.getCell().getColumn() != 1:
                if node.getCell().getStatus() == 0:
                    text += '<TD></TD>'
                else:
                    text += '<TD  bgcolor="#1B76F5"></TD>'
            else:
                if node.getCell().getStatus() == 0:
                    text += '<TD></TD></TR>'
                else:
                    text += '<TD  bgcolor="#1B76F5"></TD></TR>'
            node = node.getNext()
            
        text += '</TABLE>>];}'
        file = open("./period.dot", "w+")
        file.write(text)
        file.close()
        os.system(f'dot -Tpng period.dot -o periodo{period}.png') 

    def toString(self):
        node = self.__first
        text = ''
        while node:
            if node.getNext() == None:
                #print(node.getCell().getStatus())
                text += f'{node.getCell().getStatus()}\n'
            elif node.getCell().getRow()==node.getNext().getCell().getRow():
                #print(node.getCell().getStatus(),end='')
                text += f'{node.getCell().getStatus()}'
            else:
                #print(node.getCell().getStatus())
                text += f'{node.getCell().getStatus()}\n'
            node = node.getNext()
        return text