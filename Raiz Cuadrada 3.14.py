def dibujar_cuadrado(lado):
    for i in range(lado):
        for j in range(lado):
            if i == 0 or i == lado - 1 or j == 0 or j == lado - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

lado = int(input("Ingrese el tamaño del lado del cuadrado: "))
dibujar_cuadrado(lado)