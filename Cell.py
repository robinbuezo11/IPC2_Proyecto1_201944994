class Cell:
    def __init__(self, status=None, row=None, column=None):
        self.__status = status
        self.__row = row
        self.__column = column

    def getStatus(self):
        return self.__status

    def getRow(self):
        return self.__row()

    def getColumn(self):
        return self.__column()

    def setStatus(self, status):
        self.__status = status