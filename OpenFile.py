from colorama import Fore
import xml.etree.ElementTree as et
from Cell import Cell
from ListCells import ListCells
from ListPatients import ListPatient

from Patient import Patient

class OpenFile():
    def __init__(self, ruta) -> None:
        self.__tree = et.parse(ruta)
        self.__root = self.__tree.getroot()

    def readFile(self):
        patients = ListPatient()
        try:
            for itrpatient in self.__root:
                cells=ListCells()
                patient=Patient(cells=cells)
                for data in itrpatient:
                    for item in data:
                        if item.tag == 'nombre':
                            patient.setName(item.text)
                        elif item.tag == 'edad':
                            patient.setAge(item.text)
                        elif item.tag == 'celda':
                            patient.getCells().updateCell(Cell(status=1, row=int(item.attrib['f']), column=int(item.attrib['c'])))
                    if data.tag == 'periodos':
                        if int(data.text) > 10000:
                            print(Fore.RED + 'La cantidad de periodos no puede ser mayor a 10,000')
                            return None
                        patient.setPeriods(int(data.text))
                    if data.tag == 'm':
                        if int(data.text) > 10000:
                            print(Fore.RED + 'La matriz no puede ser mayor a 10,000')
                            return None
                        if (int(data.text) % 10) != 0:
                            print(Fore.RED + 'La matriz debe ser multiplo de 10')
                            return None
                        patient.setMatrix(int(data.text))
                        patient.getCells().setMatrixWithMagnitude(int(data.text))
                patients.insert(patient=patient)
            return patients
        except Exception as e:
            print(e)
