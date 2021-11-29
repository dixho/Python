import time # Modulo Time para los tiempos de espera

usuarios=["flf","janf", "test"]
pins =  [5486 , 3457]
masterpin = 1234

    # Monederos

monedero3457=253000
monedero5486=1000
monederotest= 1000000

    # Variable Bucle
bucle = True

idioma=int(input("Seleccione idioma / Select language:\n 1. Español\n 2. English\n: "))
# Español
if idioma == 1:
    usuario=input("\nIngrese su usuario: ")
    pin=int(input("\nIngrese su PIN: "))


    # Usuario flf
    if usuario == "flf":
        if pin == 5486 or pin == masterpin:
            if pin == masterpin:
                print("Usuario Maestro")
            while bucle:

                

                seleccion=int(input("\nBienvenido, elija una opción:\n 1 Ver Saldo\n 2 Ingresar dinero\n 3 Retirar dinero\n 4 Salir\n :"))
                
                if seleccion == 1: # Saldo
                    print("\nEl saldo actual es de :", monedero5486,"€")
                    time.sleep(1.5)
                    print("\n")
                
                if seleccion == 2: # Ingresar
                    ingreso=int(input("\nDinero a ingresar: "))
                    if ingreso < 0:
                        print("Cantidad incorrecta")
                    else:
                        monedero5486=ingreso + monedero5486
                    print("¿Desea ver su saldo?")
                    seleccion2=input("Sí/No: ")
                    if seleccion2 == "Sí" or seleccion2 == "Si" or seleccion2 == "s" or seleccion2 == "S":
                        print("\n",monedero5486,"€")
                        time.sleep(1.5)
                        print("\n")
                    else:
                        time.sleep(1)
                        print("\n")
                
                if seleccion == 3: # Retirar
                    retiro=int(input("\nDinero a retirar: "))
                    if monedero3457 < 0:
                        print("Cantidad incorrecta")
                    if retiro < monedero5486:
                        monedero5486=monedero5486-retiro
                        if monedero5486 <= 0:
                            print("Saldo insuficiente")
                        print("¿Desea ver su saldo?")
                        seleccion2=input("Sí/No: ")
                        if seleccion2 == "Sí" or seleccion2 == "Si" or seleccion2 == "s" or seleccion2 == "S":
                            print("\n",monedero5486,"€")
                    else:
                        monedero5486=0
                        
                if seleccion == 4: # Salir
                    print("\n Gracias por su visita")
                    time.sleep(1)
                    bucle = False

    # Usuario janf
    if usuario == "janf":
        if pin == 3457 or pin == masterpin:
            if pin == masterpin:
                print("Usuario Maestro")
            while bucle == 5:

                

                seleccion=int(input("\nBienvenido, elija una opción:\n 1 Ver Saldo\n 2 Ingresar dinero\n 3 Retirar dinero\n 4 Salir\n : "))
                
                if seleccion == 1: # Saldo
                    print("\nEl saldo actual es de :", monedero3457,"€")
                    time.sleep(1.5)
                    print("\n")
                
                if seleccion == 2: # Ingresar
                    ingreso=int(input("\nDinero a ingresar: "))
                    if ingreso < 0:
                        print("Cantidad incorrecta")
                    else:
                        monedero3457=ingreso + monedero3457
                    print("¿Desea ver su saldo?")
                    seleccion2=input("Sí/No: ")
                    if seleccion2 == "Sí" or seleccion2 == "Si" or seleccion2 == "s" or seleccion2 == "S":
                        print("\n",monedero3457,"€")
                        time.sleep(1.5)
                        print("\n")
                    else:
                        time.sleep(1)
                        print("\n")
                
                if seleccion == 3: # Retirar
                    retiro=int(input("\nDinero a retirar: "))
                    if monedero3457 < 0:
                        print("Cantidad incorrecta")
                    if retiro < monedero3457:
                        monedero3457=monedero3457-retiro
                        if monedero3457 <= 0:
                            print("Saldo insuficiente")
                        print("¿Desea ver su saldo?")
                        seleccion2=input("Sí/No: ")
                        if seleccion2 == "Sí" or seleccion2 == "Si" or seleccion2 == "s" or seleccion2 == "S":
                            print("\n",monedero3457,"€")
                    else:
                        monedero3457=0
                    
                if seleccion == 4: # Salir
                    print("\n Gracias por su visita")
                    time.sleep(1)
                    bucle = 6

    # Usuario test
    if usuario == "test":
        if pin == 0000 or pin == masterpin:
            if pin == masterpin:
                print("Usuario Maestro")
            while bucle == 5:

                

                seleccion=int(input("\nBienvenido, elija una opción:\n 1 Ver Saldo\n 2 Ingresar dinero\n 3 Retirar dinero\n 4 Salir\n : "))
                
                if seleccion == 1: # Saldo

                    print("\nEl saldo actual es de :", monederotest,"€")

                    time.sleep(1.5)
                    print("\n")
                
                if seleccion == 2: # Ingresar
                    ingreso=int(input("\nDinero a ingresar: "))
                    if ingreso < 0:
                        print("Cantidad incorrecta")
                    else:
                        monederotest=ingreso + monederotest
                    print("¿Desea ver su saldo?")
                    seleccion2=input("Sí/No: ")
                    if seleccion2 == "Sí" or seleccion2 == "Si" or seleccion2 == "s" or seleccion2 == "S":
                        print("\n",monederotest,"€")
                        time.sleep(1.5)
                        print("\n")
                    else:
                        time.sleep(1)
                        print("\n")
                
                if seleccion == 3: # Retirar
                    retiro=int(input("\nDinero a retirar: "))
                    if monederotest < 0:
                        print("Cantidad incorrecta")
                    if retiro < monederotest:
                        monederotest=monederotest-retiro
                        if monederotest <= 0:
                            print("Saldo insuficiente")
                        print("¿Desea ver su saldo?")
                        seleccion2=input("Sí/No: ")
                        if seleccion2 == "Sí" or seleccion2 == "Si" or seleccion2 == "s" or seleccion2 == "S":
                            print("\n",monederotest,"€")
                    else:
                        monederotest=0
                    
                if seleccion == 4: # Salir
                    print("\n Gracias por su visita")
                    time.sleep(1)
                    bucle = 6
# English
if idioma == 2:
    usuario=input("\nUser: ")
    pin=int(input("\nPIN: "))

    # User flf
    if usuario == "flf":
        if pin == 5486 or pin == masterpin:
            if pin == masterpin:
                print("Master User")
            while bucle == 5:

                

                seleccion=int(input("\nWelcome, Chose an option:\n 1 See balance\n 2 Deposit money\n 3 Withdrawals\n 4 Exit\n: "))
                
                if seleccion == 1: # Balance
                    print("\nThe current balance is :", monedero5486,"€")
                    time.sleep(1.5)
                    print("\n")
                
                if seleccion == 2: # Deposit
                    ingreso=int(input("\nMoney to deposit: "))
                    if ingreso < 0:
                        print("Incorrect amount")
                    else:
                        monedero5486=ingreso + monedero5486
                    print("Do you want to see your balance?")
                    seleccion2=input("Yes/No: ")
                    if seleccion2 == "Yes" or seleccion2== "yes" or seleccion2 == "y" or seleccion2 =="Y":
                        print("\n",monedero5486,"€")
                        time.sleep(1.5)
                        print("\n")
                    else:
                        time.sleep(1)
                        print("\n")
                
                if seleccion == 3: # Withdraw
                    retiro=int(input("\nMoney to withdraw: "))
                    if monedero3457 < 0:
                        print("Incorrect amount")
                    if retiro < monedero5486:
                        monedero5486=monedero5486-retiro
                        if monedero5486 <= 0:
                            print("Insufficient balance")
                        print("Do you want to see your balance?")
                        seleccion2=input("Yes/No: ")
                        if seleccion2 == "Yes" or seleccion2== "yes" or seleccion2 == "y" or seleccion2 =="Y":
                            print("\n",monedero5486,"€")
                    else:
                        monedero5486=0
                        
                if seleccion == 4: # Exit
                    print("\n Thanks for your visit")
                    time.sleep(1)
                    bucle = 6

    # User janf
    if usuario == "janf":
        if pin == 3457 or pin == masterpin:
            if pin == masterpin:
                print("Master User")
            while bucle == 5:

                

                seleccion=int(input("\nWelcome, Chose an option:\n 1 See balance\n 2 Deposit money\n 3 Withdrawals\n 4 Exit\n:"))
                
                if seleccion == 1: # Balance
                    print("\nThe current balance is :", monedero3457,"€")
                    time.sleep(1.5)
                    print("\n")
                
                if seleccion == 2: # Deposit
                    ingreso=int(input("\nMoney to deposit: "))
                    if ingreso < 0:
                        print("Incorrect amount")
                    else:
                        monedero3457=ingreso + monedero3457
                    print("Do you want to see your balance?")
                    seleccion2=input("Yes/No: ")
                    if seleccion2 == "Yes" or seleccion2== "yes" or seleccion2 == "y" or seleccion2 =="Y":
                        print("\n",monedero3457,"€")
                        time.sleep(1.5)
                        print("\n")
                    else:
                        time.sleep(1)
                        print("\n")
                
                if seleccion == 3: # Withdraw
                    retiro=int(input("\nMoney to withdraw: "))
                    if monedero3457 < 0:
                        print("Incorrect amount")
                    if retiro < monedero3457:
                        monedero3457=monedero3457-retiro
                        if monedero3457 <= 0:
                            print("Insufficient balance")
                        print("Do you want to see your balance?")
                        if seleccion2 == "Yes" or seleccion2== "yes" or seleccion2 == "y" or seleccion2 =="Y":
                            print("\n",monedero3457,"€")
                    else:
                        monedero3457=0
                    
                if seleccion == 4: # Exit
                    print("\n Thanks for your visit")
                    time.sleep(1)
                    bucle = 6

    # User test
    if usuario == "test":
        if pin == 0000 or pin == masterpin:
            if pin == masterpin:
                print("Master User")
            while bucle == 5:

                

                seleccion=int(input("\nWelcome, Chose an option:\n 1 See balance\n 2 Deposit money\n 3 Withdrawals\n 4 Exit\n:"))
                
                if seleccion == 1: # Balance
                    print("\nThe current balance is :", monederotest,"€")
                    time.sleep(1.5)
                    print("\n")
                
                if seleccion == 2: # Deposit
                    ingreso=int(input("\nMoney to deposit: "))
                    if ingreso < 0:
                        print("Incorrect amount")
                    else:
                        monederotest=ingreso + monederotest
                    print("Do you want to see your balance?")
                    seleccion2=input("Yes/No: ")
                    if seleccion2 == "Yes" or seleccion2== "yes" or seleccion2 == "y" or seleccion2 =="Y":
                        print("\n",monederotest,"€")
                        time.sleep(1.5)
                        print("\n")
                    else:
                        time.sleep(1)
                        print("\n")
                
                if seleccion == 3: # Withdraw
                    retiro=int(input("\nMoney to withdraw: "))
                    if monederotest < 0:
                        print("Incorrect amount")
                    if retiro < monederotest:
                        monederotest=monederotest-retiro
                        if monederotest <= 0:
                            print("Insufficient balance")
                        print("Do you want to see your balance?")
                        if seleccion2 == "Yes" or seleccion2== "yes" or seleccion2 == "y" or seleccion2 =="Y":
                            print("\n",monederotest,"€")
                    else:
                        monederotest=0
                    
                if seleccion == 4: # Exit
                    print("\n Thanks for your visit")
                    time.sleep(1)
                    bucle = 6
