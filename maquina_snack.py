saldo = 5.0
cantidad = 0

while True:
    print("\n MÁQUINA DE SNACKS ")
    print(f"Saldo: Bs. {saldo:.2f}")
    print("1. Papas      - Bs. 1.50")
    print("2. Chocolate  - Bs. 2.00")
    print("3. Refresco   - Bs. 2.50")
    print("0. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "0":
        print(f"Compraste {cantidad} producto(s). ¡Adiós!")
        break
    elif opcion == "1":
        precio = 1.50
        nombre = "Papas"
    elif opcion == "2":
        precio = 2.00
        nombre = "Chocolate"
    elif opcion == "3":
        precio = 2.50
        nombre = "Refresco"
    else:
        print("Opción no válida")
        continue

    if saldo >= precio:
        saldo = saldo - precio
        cantidad = cantidad + 1
        print(f"Compraste {nombre}. Saldo restante: Bs. {saldo:.2f}")
    else:
        print("Saldo insuficiente")