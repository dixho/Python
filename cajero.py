import time # Modulo Time para los tiempos de espera

usuarios=["flf","janf"]
pins =  [5486 , 3457]
masterpin = 1234

    # Monederos

monedero3457=254654
monedero5486=1000

    # Variable Bucle
bucle = 5

idioma=int(input("Seleccione idioma / Select language:\n 1. Español\n 2. English\n: "))
# Español
if idioma == 1:
    usuario=input("Ingrese su usuario: ")
    pin=int(input("Ingrese su PIN: "))


    # Usuario flf
    if usuario == "flf":
        if pin == 5486 or pin == masterpin:
            if pin == masterpin:
                print("Usuario Maestro")
            while bucle == 5:

                

                seleccion=int(input("Bienvenido, elija una opción:\n 1 Ver Saldo\n 2 Ingresar dinero\n 3 Retirar dinero\n 4 Salir\n:"))
                
                if seleccion == 1: # Saldo
                    print("El saldo actual es de :", monedero5486,"€")
                    time.sleep(1.5)
                    print("\n")
                
                if seleccion == 2: # Ingresar
                    ingreso=int(input("Dinero a ingresar: "))
                    if ingreso < 0:
                        print("Cantidad incorrecta")
                    else:
                        monedero5486=ingreso + monedero5486
                    print("¿Desea ver su saldo?")
                    seleccion2=input("Sí/No: ")
                    if seleccion2 == "Sí" or seleccion2 == "Si" or seleccion2 == "s" or seleccion2 == "S":
                        print(monedero5486,"€")
                        time.sleep(1.5)
                        print("\n")
                    else:
                        time.sleep(1)
                        print("\n")
                
                if seleccion == 3: # Retirar
                    retiro=int(input("Dinero a retirar: "))
                    if monedero3457 < 0:
                        print("Cantidad incorrecta")
                    if retiro < monedero5486:
                        monedero5486=monedero5486-retiro
                        if monedero5486 <= 0:
                            print("Saldo insuficiente")
                        print("¿Desea ver su saldo?")
                        seleccion2=input("Sí/No: ")
                        if seleccion2 == "Sí" or seleccion2 == "Si" or seleccion2 == "s" or seleccion2 == "S":
                            print(monedero5486,"€")
                    else:
                        monedero5486=0
                        
                if seleccion == 4: # Salir
                    print("Gracias por su visita")
                    bucle = 6

    # Usuario janf
    if usuario == "janf":
        if pin == 3457 or pin == masterpin:
            if pin == masterpin:
                print("Usuario Maestro")
            while bucle == 5:

                

                seleccion=int(input("Bienvenido, elija una opción:\n 1 Ver Saldo\n 2 Ingresar dinero\n 3 Retirar dinero\n 4 Salir\n: "))
                
                if seleccion == 1: # Saldo
                    print("El saldo actual es de :", monedero3457,"€")
                    time.sleep(1.5)
                    print("\n")
                
                if seleccion == 2: # Ingresar
                    ingreso=int(input("Dinero a ingresar: "))
                    if ingreso < 0:
                        print("Cantidad incorrecta")
                    else:
                        monedero3457=ingreso + monedero3457
                    print("¿Desea ver su saldo?")
                    seleccion2=input("Sí/No: ")
                    if seleccion2 == "Sí" or seleccion2 == "Si" or seleccion2 == "s" or seleccion2 == "S":
                        print(monedero3457,"€")
                        time.sleep(1.5)
                        print("\n")
                    else:
                        time.sleep(1)
                        print("\n")
                
                if seleccion == 3: # Retirar
                    retiro=int(input("Dinero a retirar: "))
                    if monedero3457 < 0:
                        print("Cantidad incorrecta")
                    if retiro < monedero3457:
                        monedero3457=monedero3457-retiro
                        if monedero3457 <= 0:
                            print("Saldo insuficiente")
                        print("¿Desea ver su saldo?")
                        seleccion2=input("Sí/No: ")
                        if seleccion2 == "Sí" or seleccion2 == "Si" or seleccion2 == "s" or seleccion2 == "S":
                            print(monedero3457,"€")
                    else:
                        monedero3457=0
                    
                if seleccion == 4: # Salir
                    print("Gracias por su visita")
                    bucle = 6
# English
if idioma == 2:
    usuario=input("User: ")
    pin=int(input("PIN: "))

    # User flf
    if usuario == "flf":
        if pin == 5486 or pin == masterpin:
            if pin == masterpin:
                print("Master User")
            while bucle == 5:

                

                seleccion=int(input("Welcome, Chose an option:\n 1 See balance\n 2 Deposit money\n 3 Withdrawals\n 4 Exit\n: "))
                
                if seleccion == 1: # Balance
                    print("The current balance is :", monedero5486,"€")
                    time.sleep(1.5)
                    print("\n")
                
                if seleccion == 2: # Deposit
                    ingreso=int(input("Money to deposit: "))
                    if ingreso < 0:
                        print("Incorrect amount")
                    else:
                        monedero5486=ingreso + monedero5486
                    print("Do you want to see your balance?")
                    seleccion2=input("Yes/No: ")
                    if seleccion2 == "Yes" or seleccion2== "yes" or seleccion2 == "y" or seleccion2 =="Y":
                        print(monedero5486,"€")
                        time.sleep(1.5)
                        print("\n")
                    else:
                        time.sleep(1)
                        print("\n")
                
                if seleccion == 3: # Withdraw
                    retiro=int(input("Money to withdraw: "))
                    if monedero3457 < 0:
                        print("Incorrect amount")
                    if retiro < monedero5486:
                        monedero5486=monedero5486-retiro
                        if monedero5486 <= 0:
                            print("Insufficient balance")
                        print("Do you want to see your balance?")
                        seleccion2=input("Yes/No: ")
                        if seleccion2 == "Yes" or seleccion2== "yes" or seleccion2 == "y" or seleccion2 =="Y":
                            print(monedero5486,"€")
                    else:
                        monedero5486=0
                        
                if seleccion == 4: # Exit
                    print("Thanks for your visit")
                    bucle = 6

    # User janf
    if usuario == "janf":
        if pin == 3457 or pin == masterpin:
            if pin == masterpin:
                print("Master User")
            while bucle == 5:

                

                seleccion=int(input("Welcome, Chose an option:\n 1 See balance\n 2 Deposit money\n 3 Withdrawals\n 4 Exit\n:"))
                
                if seleccion == 1: # Balance
                    print("The current balance is :", monedero3457,"€")
                    time.sleep(1.5)
                    print("\n")
                
                if seleccion == 2: # Deposit
                    ingreso=int(input("Money to deposit: "))
                    if ingreso < 0:
                        print("Incorrect amount")
                    else:
                        monedero3457=ingreso + monedero3457
                    print("Do you want to see your balance?")
                    seleccion2=input("Yes/No: ")
                    if seleccion2 == "Yes" or seleccion2== "yes" or seleccion2 == "y" or seleccion2 =="Y":
                        print(monedero3457,"€")
                        time.sleep(1.5)
                        print("\n")
                    else:
                        time.sleep(1)
                        print("\n")
                
                if seleccion == 3: # Withdraw
                    retiro=int(input("Money to withdraw: "))
                    if monedero3457 < 0:
                        print("Incorrect amount")
                    if retiro < monedero3457:
                        monedero3457=monedero3457-retiro
                        if monedero3457 <= 0:
                            print("Insufficient balance")
                        print("Do you want to see your balance?")
                        if seleccion2 == "Yes" or seleccion2== "yes" or seleccion2 == "y" or seleccion2 =="Y":
                            print(monedero3457,"€")
                    else:
                        monedero3457=0
                    
                if seleccion == 4: # Exit
                    print("Thanks for your visit")
                    bucle = 6
