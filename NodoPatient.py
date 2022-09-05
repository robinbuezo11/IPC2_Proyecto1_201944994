from Patient import Patient

class NodePatient:
    def __init__(self, next=None, patient=Patient()):
        self.__next = next
        self.__patient = patient

    def getNext(self):
        return self.__next

    def getPatient(self):
        return self.__patient

    def setNext(self, next):
        self.__next = next
    
    def setPatient(self, patient):
        self.__patient = patient
