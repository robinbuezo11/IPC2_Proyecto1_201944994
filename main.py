from colorama import Fore
from ListPatients import ListPatient
from OpenFile import OpenFile

def main():
    patients = ListPatient()
    option = 0
    while option != 9:
        print(Fore.BLUE + '\n------------------MENU------------------')
        print(Fore.BLUE + '1) Cargar archivo')
        print(Fore.BLUE + '2) Seleccionar paciente')
        print(Fore.BLUE + '3) Generar XML')
        print(Fore.BLUE + '9) SALIR\n')
        
        try:
            option = int(input(Fore.YELLOW + "Ingrese el numero de la opción que desee "))
        except Exception as e:
            print(Fore.RED + e)
        
        if option == 1:
            path = input(Fore.YELLOW + 'Ingrese la ruta del archivo ')
            try:
                data =  OpenFile(path)
                patients = data.readFile()
                if patients != None:
                    print(Fore.GREEN + 'Archivo cargado exitosamente')
            except Exception as e:
                print(Fore.RED + e)
        elif option == 2:
            print('')
            patients.printPatientsNames()

            patient = patients.searchForNum(int(input(Fore.YELLOW + '\nIngrese el número del paciente ')))
            print(Fore.BLUE + f'\nPaciente: {patient.getPatient().getName()}\n')

            patientoption = 0
            while patientoption != 9:
                print(Fore.BLUE + '\n------------------MENU------------------')
                print(Fore.BLUE + '1) Valuar siguiente Periodo')
                print(Fore.BLUE + '2) Valuar todos los periodos')
                print(Fore.BLUE + '3) Graficar')
                print(Fore.BLUE + '9) REGRESAR\n')

                try:
                    patientoption = int(input(Fore.YELLOW + 'Ingrese el numero de la opción que desee '))
                except Exception as e:
                    print(Fore.RED + e)

                if patientoption == 1:
                    try:
                        patient.getPatient().ValueNextPeriod()
                        patient.getPatient().getCells().graphMatrix(patient.getPatient().getPeriod())
                    except Exception as e:
                        print(Fore.RED + e)
                elif patientoption == 2:
                    try:
                        iterator = 1
                        while iterator <= patient.getPatient().getPeriods() and patient.getPatient().getResult() == 'Leve':
                            patient.getPatient().ValueNextPeriod()
                            patient.getPatient().getCells().graphMatrix(patient.getPatient().getPeriod())
                            iterator += 1
                    except Exception as e:
                        print(Fore.RED + e)
                elif patientoption == 3:
                    try:
                        patient.getPatient().getCells().graphMatrix(patient.getPatient().getPeriod())
                    except Exception as e:
                        print(Fore.RED + e)
        elif option == 3:
            try:
                patients.generateXML()
                print(Fore.GREEN + 'XML generado exitosamente')
            except Exception as e:
                print(Fore.RED + e)


main()