import time
usuario=input("Ingrese su usuario: ")
pin=int(input("Ingrese su PIN: "))
usuarios=["flf","janf"]
pins =  [5486 , 3457]
masterpin = 1234

# Monederos

monedero5486=1000
monedero3457=254654


bucle = 5

# Usuario flf

if pin == 5486 or pin == masterpin and usuario == "flf":
    if pin == masterpin:
        print("Usuario Maestro")
    while bucle == 5:
        
        seleccion=int(input("Bienvenido, elija una opción:\n 1 Ver Saldo\n 2 Ingresar dinero\n 3 Retirar dinero\n 4 Salir\n:"))
        
        if seleccion == 1: # Saldo
            print("El saldo actual es de :", monedero5486,"€")
            time.sleep(3)
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
                time.sleep(3)
                print("\n")
            else:
                time.sleep(2)
                print("\n")
        
        if seleccion == 3: # Retirar
            retiro=int(input("Dinero a retirar: "))
            if retiro < 0:
                print("Cantidad incorrecta")
            else:
                if retiro < monedero5486:
                    monedero5486=monedero5486-retiro
                    print("¿Desea ver su saldo?")
                    seleccion2=input("Sí/No: ")
                    if seleccion2 == "Sí" or seleccion2 == "Si" or seleccion2 == "s" or seleccion2 == "S":
                        print(monedero5486,"€")
                if retiro > monedero5486:
                    seleccion3=int(input("Saldo insuficiente, elija una opción:\n 1. Retirar cantidad exacta dejando la cuenta en negativo\n 2. Retirar total del saldo\n : "))
                    if seleccion3 == 1:
                        monedero5486=monedero5486-retiro
                    if seleccion3 == 2:
                        monedero5486 = 0
                        print("¿Desea ver su saldo?")
                        seleccion2=input("Sí/No: ")
                        if seleccion2 == "Sí" or seleccion2 == "Si" or seleccion2 == "s" or seleccion2 == "S":
                            print(monedero5486,"€")
        
        if seleccion == 4: # Salir
            bucle = 6

    #Usuario janf    
if usuario == "janf":
    if pin == 3457 or pin == masterpin:
        if pin == masterpin:
            print("Usuario Maestro")
        while bucle == 5:
            
            seleccion=int(input("Bienvenido, elija una opción:\n 1 Ver Saldo\n 2 Ingresar dinero\n 3 Retirar dinero\n 4 Salir\n:"))
            
            if seleccion == 1: # Saldo
                print("El saldo actual es de :", monedero3457,"€")
                time.sleep(3)
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
                    time.sleep(3)
                    print("\n")
                else:
                    time.sleep(2)
                    print("\n")
            
            if seleccion == 3: # Retirar
                retiro=int(input("Dinero a retirar: "))
                if retiro < 0:
                    print("Cantidad incorrecta")
                else:
                    if retiro < monedero3457:
                        monedero3457=monedero3457-retiro
                        print("¿Desea ver su saldo?")
                        seleccion2=input("Sí/No: ")
                        if seleccion2 == "Sí" or seleccion2 == "Si" or seleccion2 == "s" or seleccion2 == "S":
                            print(monedero3457,"€")
                    if retiro > monedero3457:
                        seleccion3=int(input("Saldo insuficiente, elija una opción:\n 1. Retirar cantidad exacta dejando la cuenta en negativo\n 2. Retirar total del saldo\n : "))
                        if seleccion3 == 1:
                            monedero3457=monedero3457-retiro
                        if seleccion3 == 2:
                            monedero3457 = 0
                            print("¿Desea ver su saldo?")
                            seleccion2=input("Sí/No: ")
                            if seleccion2 == "Sí" or seleccion2 == "Si" or seleccion2 == "s" or seleccion2 == "S":
                                print(monedero3457,"€")
            
            if seleccion == 4: # Salir
                bucle = 6

if bucle != 5:
    print("Gracias por su visita")

else:
    print("PIN Incorrecto")


