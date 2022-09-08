import xml.etree.ElementTree as ET
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
            return None
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
            return None

    def generateXML(self):
        data = ET.Element('pacientes')

        node = self.__first
        while node:
            patient = ET.SubElement(data, 'paciente')
            personaldata = ET.SubElement(patient, 'datospersonales')
            name = ET.SubElement(personaldata, 'nombre')
            name.text = f'{node.getPatient().getName()}'
            age = ET.SubElement(personaldata, 'edad')
            age.text = f'{node.getPatient().getAge()}'
            periods = ET.SubElement(patient, 'periodos')
            periods.text = f'{node.getPatient().getPeriods()}'
            matrix = ET.SubElement(patient, 'm')
            matrix.text = f'{node.getPatient().getMatrix()}'
            result = ET.SubElement(patient, 'resultado')
            result.text = f'{node.getPatient().getResult()}'

            if node.getPatient().getResult() != 'Leve' and node.getPatient().getN1() == 0:
                n = ET.SubElement(patient, 'n')
                n.text = f'{node.getPatient().getN()}'
            elif node.getPatient().getResult() != 'Leve' and node.getPatient().getN1 != 0:
                n = ET.SubElement(patient, 'n')
                n.text = f'{node.getPatient().getN()}'
                n1 = ET.SubElement(patient, 'n1')
                n1.text = f'{node.getPatient().getN1()}'
            
            node = node.getNext()
        xml = ET.tostring(data)
        file = open("./XMLsalida.xml", "wb")
        file.write(xml)
                


