pin=int(input("Ingrese su PIN: "))

monedero=1000
bucle = 5
while bucle == 5:
    if pin == 5486:
        seleccion=int(input("Bienvenido, elija una opción:\n 1 Ver Saldo\n 2 Ingresar dinero\n 3 Retirar dinero\n 4 Salir\n:"))
        if seleccion == 1:
            print("El saldo actual es de :", monedero)
        if seleccion == 2:
            ingreso=int(input("Dinero a ingresar: "))
            monedero=ingreso + monedero
            print("¿Desea ver su saldo?")
            seleccion2=input("Sí/No: ")
            if seleccion2 == "Sí":
                print(monedero)
        if seleccion == 3:
            retiro=int(input("Dinero a retirar: "))
            if retiro < monedero:
                monedero=monedero-retiro
                print("¿Desea ver su saldo?")
                seleccion2=input("Sí/No: ")
                if seleccion2 == "Sí" or seleccion2 == "Si" or seleccion2 == "s" or seleccion2 == "S":
                    print(monedero)
            if retiro > monedero:
                seleccion3=int(input("Saldo insuficiente, elija una opción:\n 1. Retirar cantidad exacta dejando la cuenta en negativo\n 2. Retirar total del saldo\n : "))
                if seleccion3 == 1:
                    monedero=monedero-retiro
                if seleccion3 == 2:
                    monedero = 0
        if seleccion == 4:
            print("Gracias por su visita")
            bucle = 6

if pin != 5486:
    print("PIN Incorrecto")


