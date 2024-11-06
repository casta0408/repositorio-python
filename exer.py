# algoritmo para leer numero en positivo o negativo
numero = int(input("Ingresa un número: "))
if numero < 0:
    positivo = int(numero * -1)
    print("Número ingresado: ", numero)
    print("Equivalente positivo: " , positivo)
else:
    print("El número ingresado no es negativo.")