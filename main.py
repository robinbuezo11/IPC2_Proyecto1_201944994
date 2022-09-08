from cgitb import text
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
            textin = input(Fore.YELLOW + "Ingrese el numero de la opción que desee ")
            if textin != '':
                option = int(textin)
            else:
                option = 0
        except Exception as e:
            print(Fore.RED + f'{e}')
        
        if option == 1:
            try:
                path = input(Fore.YELLOW + '\nIngrese la ruta del archivo ')
                data =  OpenFile(path)
                patients = data.readFile()
                if patients != None:
                    print(Fore.GREEN + 'Archivo cargado exitosamente')
            except Exception as e:
                print(Fore.RED + f'{e}')
        elif option == 2:
            print('')
            patients.printPatientsNames()
            
            text = ''
            while text == '':
                text = input(Fore.YELLOW + '\nIngrese el número del paciente ')
            patient = patients.searchForNum(int(text))
            if patient != None:
                print(Fore.BLUE + f'\nPaciente: {patient.getPatient().getName()}')
                patientoption = 0
            else:
                patientoption = 9
            
            while patientoption != 9:
                print(Fore.BLUE + '\n------------------MENU------------------')
                print(Fore.BLUE + '1) Valuar siguiente Periodo')
                print(Fore.BLUE + '2) Valuar todos los periodos')
                print(Fore.BLUE + '3) Graficar')
                print(Fore.BLUE + '9) REGRESAR\n')

                try:
                    textin = input(Fore.YELLOW + 'Ingrese el numero de la opción que desee ')
                    if textin != '':
                        patientoption = int(textin)
                    else:
                        patientoption = 0
                except Exception as e:
                    print(Fore.RED + f'{e}')

                if patientoption == 1:
                    try:
                        patient.getPatient().getCells().graphMatrix(patient.getPatient().getPeriod())
                        patient.getPatient().ValueNextPeriod()
                        patient.getPatient().getCells().graphMatrix(patient.getPatient().getPeriod())
                    except Exception as e:
                        print(Fore.RED + f'{e}')
                elif patientoption == 2:
                    try:
                        iterator = 1
                        if patient.getPatient().getResult() == 'Leve':
                            patient.getPatient().getCells().graphMatrix(patient.getPatient().getPeriod())
                            while iterator <= patient.getPatient().getPeriods() and patient.getPatient().getResult() == 'Leve' and patient.getPatient().ValueNextPeriod() != False:
                                patient.getPatient().getCells().graphMatrix(patient.getPatient().getPeriod())
                                iterator += 1
                        else:
                            print(Fore.CYAN + 'Ya se encontró un patrón repetido')
                    except Exception as e:
                        print(Fore.RED + f'{e}')
                elif patientoption == 3:
                    try:
                        patient.getPatient().getCells().graphMatrix(patient.getPatient().getPeriod())
                    except Exception as e:
                        print(Fore.RED + f'{e}')
        elif option == 3:
            try:
                patients.generateXML()
                print(Fore.GREEN + 'XML generado exitosamente')
            except Exception as e:
                print(Fore.RED + f'{e}')


main()