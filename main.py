from colorama import Fore
from ListPatients import ListPatient
from OpenFile import OpenFile

def main():
    patients = ListPatient()
    option = 0
    while option != 9:
        print(Fore.BLUE + '------------------MENU------------------')
        print(Fore.BLUE + '1) Cargar archivo')
        print(Fore.BLUE + '2) Seleccionar paciente')
        print(Fore.BLUE + '9) SALIR\n')
        
        try:
            option = int(input(Fore.YELLOW + "Ingrese el numero de la opción que desee "))
        except Exception as e:
            print(e)
        
        if option == 1:
            path = input(Fore.YELLOW + 'Ingrese la ruta del archivo ')
            try:
                data =  OpenFile(path)
                patients = data.readFile()
                print(Fore.GREEN + 'Archivo cargado exitosamente\n')
            except Exception as e:
                print(e)
        elif option == 2:
            print('')
            patients.printPatientsNames()

            patient = patients.searchForNum(int(input(Fore.YELLOW + '\nIngrese el número del paciente ')))
            print(Fore.BLUE + f'\nPaciente: {patient.getPatient().getName()}\n')

            patientoption = 0
            while patientoption != 9:
                print(Fore.BLUE + '------------------MENU------------------')
                print(Fore.BLUE + '1) Valuar siguiente Periodo')
                print(Fore.BLUE + '2) Valuar todos los periodos')
                print(Fore.BLUE + '9) REGRESAR\n')

                patientoption = int(input(Fore.YELLOW + 'Ingrese el numero de la opción que desee '))

main()