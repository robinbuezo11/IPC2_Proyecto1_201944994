import xml.etree.ElementTree as et

class OpenFile():
    def __init__(self, ruta) -> None:
        self.__tree = et.parse(ruta)
        self.__root = self.__tree.getroot()

    def printFile(self):
        for items in self.__root:
            print("\nAtributo name del padre: ", items.attrib['name'])
            for item in items:
                print("Atributo name del item: ", item.attrib['name'])
                print("Contenido del item: ", item.text)


op = OpenFile('prueba.xml')
op.printFile()

    