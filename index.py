#ejercicio 1
# Leer tres números del usuario
num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")
num3 = input("Ingrese el tercer número: ")

# Crear una lista con los tres números
numeros = [num1, num2, num3]

# Ordenar la lista en orden ascendente
numeros.sort()

# Imprimir los números ordenados
print("Los números en orden ascendente son:", numeros)

############################################################
#ejercico 4.15
def dibujar_cuadrado(N):
    # Paso 1: Dibujar la fila superior de asteriscos
    print('*' * N)

    # Paso 2: Dibujar los lados laterales con el centro en blanco
    for i in range(N - 2):
        print('*' + ' ' * (N - 2) + '*')

    # Paso 3: Dibujar la fila inferior de asteriscos
    if N > 1:
        print('*' * N)

# Solicitar al usuario que ingrese el número de asteriscos por lado
N = int(input("Ingrese el número de asteriscos por lado del cuadrado: "))

# Dibujar el cuadrado
dibujar_cuadrado(N)
