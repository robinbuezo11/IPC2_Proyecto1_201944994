from Patient import Patient
from NodoPatient import NodePatient

class ListPatient:
    def __init__(self):
        self.__first = NodePatient()

    def insert(self, patient=Patient()):
        if self.__first.getPatient().getName() is None:
            self.__first = NodePatient(patient=patient)
            return
        
        node = self.__first
        while node.getNext():
            node = node.getNext()
        node.setNext(NodePatient(patient=patient))

    def printPatients(self):
        node = self.__first
        while node:
            print('Nombre: ',node.getPatient().getName(),'\nEdad: ',node.getPatient().getAge(),'\nPeriodos: ',node.getPatient().getPeriods(),
                    '\nMatriz: ',node.getPatient().getMatrix())
            node.getPatient().getCells().printMatrix()
            print('')
            node = node.getNext()

