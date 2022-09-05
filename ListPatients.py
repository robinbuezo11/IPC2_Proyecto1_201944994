from colorama import Fore
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
        if self.__first.getPatient().getName() is None:
            print(Fore.RED + 'No se tiene ningún paciente, debe cargar información')
            return
        else:
            node = self.__first
            while node:
                print('Nombre: ',node.getPatient().getName(),'\nEdad: ',node.getPatient().getAge(),'\nPeriodos: ',node.getPatient().getPeriods(),
                        '\nMatriz: ',node.getPatient().getMatrix())
                node.getPatient().getCells().printMatrix()
                print('')
                node = node.getNext()
    
    def printPatientsNames(self):
        if self.__first.getPatient().getName() is None:
            print(Fore.RED + 'No se tiene ningún paciente, debe cargar información')
            return
        else:
            node = self.__first
            num = 1
            while node:
                print(f'{num}) {node.getPatient().getName()}')
                node = node.getNext()
                num += 1

    def searchForNum(self,num):
        if self.__first.getPatient().getName() is None:
            print(Fore.RED + 'No se tiene ningún paciente, debe cargar información')
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
            print(Fore.RED + 'Paciente no encontrado')

