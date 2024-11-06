# Algoritmo que capture un número y diga si negativo o  positivo. 
numero = float(input("Ingrese un número: "))
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")