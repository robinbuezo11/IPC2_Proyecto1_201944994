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
                        patient.setPeriods(int(data.text))
                    if data.tag == 'm':
                        patient.setMatrix(int(data.text))
                        patient.getCells().setMatrixWithMagnitude(int(data.text))
                patients.insert(patient=patient)
            return patients
        except Exception as e:
            print(e)

op = OpenFile('XMLentrada.xml')
patients = op.readFile()
patients.printPatients()
