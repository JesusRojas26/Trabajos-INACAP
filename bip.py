from shutil import SameFileError
from tkinter.filedialog import SaveFileDialog


saldo = 0
recarga = 0
estudiante = 230
adulto = 760
pagar = 0

seguir = True
cargar_bip = False
pagar_bip = False
saldo_bip = False
salir = False

while seguir:

    print("Menú")
    print("1- Saldo \n2- Pagar \n3- Recargar \n4- Salir")

    pregunta = int(input("¿Que sea realizar? : "))

    if pregunta == 1:
        saldo_bip = True
    if pregunta == 2:
        pagar_bip = True
    if pregunta == 3:
        cargar_bip = True
    if pregunta == 4:
        seguir = False

    while saldo_bip:

        print("Su saldo bip es de : ", saldo)

        pregunta1 = input("¿Desea volver al menú principal? : [S/N]")

        if pregunta1.upper() == "S":
            saldo_bip = False
        if pregunta1.upper() == "N":
            saldo_bip = True
    
    while pagar_bip:

        pregunta2 = input("¿Desea pagar adulto o estudiante? : [ADULTO/ESTUDIANTE] ")

        if pregunta2.upper() == "ADULTO":

            saldo-= adulto

            print("Usted pago tarifa adulto, su nuevo saldo es : ", saldo)

        if pregunta2.upper() == "ESTUDIANTE":

            saldo -= estudiante

            print("Usted pago tarifa estudiante, su nuevo saldo es : ", saldo)
        
        pregunta3 = input("¿Desea volver al menú principal? : [S/N]")

        if pregunta3.upper() == "S":
            pagar_bip = False
        if pregunta3.upper() == "N":
            pagar_bip = True
    
    while cargar_bip:

        pregunta4 = int(input("¿Cuanto desea recargar? : "))

        saldo+= pregunta4

        print("Su nuevo saldo es de: ", saldo)

        pregunta5 = input("¿Desea volver al menú principal? : [S/N]")

        if pregunta5.upper() == "S":
            cargar_bip = False
        if pregunta5.upper() == "N":
            cargar_bip = True

print("....Programa finalizado....")