import time
pin=int(input("Ingrese su PIN: "))
masterpin = 1
monedero=1000
bucle = 5
if pin == 5486 or pin == masterpin:
    if pin == masterpin:
        print("Usuario Maestro")
    while bucle == 5:
        
        seleccion=int(input("Bienvenido, elija una opción:\n 1 Ver Saldo\n 2 Ingresar dinero\n 3 Retirar dinero\n 4 Salir\n:"))
        
        if seleccion == 1: # Saldo
            print("El saldo actual es de :", monedero,"€")
            time.sleep(3)
            print("\n")
        
        if seleccion == 2: # Ingresar
            ingreso=int(input("Dinero a ingresar: "))
            if ingreso < 0:
                print("Cantidad incorrecta")
            else:
                monedero=ingreso + monedero
            print("¿Desea ver su saldo?")
            seleccion2=input("Sí/No: ")
            if seleccion2 == "Sí" or seleccion2 == "Si" or seleccion2 == "s" or seleccion2 == "S":
                print(monedero,"€")
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
                if retiro < monedero:
                    monedero=monedero-retiro
                    print("¿Desea ver su saldo?")
                    seleccion2=input("Sí/No: ")
                    if seleccion2 == "Sí" or seleccion2 == "Si" or seleccion2 == "s" or seleccion2 == "S":
                        print(monedero,"€")
                if retiro > monedero:
                    seleccion3=int(input("Saldo insuficiente, elija una opción:\n 1. Retirar cantidad exacta dejando la cuenta en negativo\n 2. Retirar total del saldo\n : "))
                    if seleccion3 == 1:
                        monedero=monedero-retiro
                    if seleccion3 == 2:
                        monedero = 0
                        print("¿Desea ver su saldo?")
                        seleccion2=input("Sí/No: ")
                        if seleccion2 == "Sí" or seleccion2 == "Si" or seleccion2 == "s" or seleccion2 == "S":
                            print(monedero,"€")
        
        if seleccion == 4: # Salir
            print("Gracias por su visita")
            bucle = 6

else:
    print("PIN Incorrecto")


