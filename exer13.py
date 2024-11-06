# Algoritmo que evalué la siguiente expresión aritmética 1/n. 
n = float(input("Ingrese un valor para n: "))
if n != 0:
    resultado = 1/n
    print("El resultado de la expresión 1/n es:", resultado)
else:
    print("Error: No se puede dividir entre cero.")
    