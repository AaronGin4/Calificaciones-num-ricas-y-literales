def calcular_interes(saldo):
    if saldo < 10000:
        interes = saldo * 0.03
    else:
        interes = saldo * 0.04
    return interes

def calcular_saldo_final(saldo):
    interes = calcular_interes(saldo)
    saldo_final = saldo + interes
    return saldo_final

# Solicitar al usuario ingresar el saldo inicial
saldo_inicial = float(input("Ingrese el saldo inicial: "))

# Calcular el saldo final
saldo_final = calcular_saldo_final(saldo_inicial)

# Mostrar el saldo final
print("El saldo final es:", saldo_final)