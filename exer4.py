# algoritmo organizar nuemeros del mayor al menoor 
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))
if numero1 >= numero2 and numero1 >= numero3:
    mayor = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    mayor = numero2
else:
    mayor = numero3
if numero1 <= numero2 and numero1 <= numero3:
    menor = numero1
elif numero2 <= numero1 and numero2 <= numero3:
    menor = numero2
else:
    menor = numero3

if numero1 == numero2 == numero3:
    iguales = "Los tres números son iguales."
elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
    iguales = "Hay dos números iguales."
else:
    iguales = "Los tres números son diferentes."
print("El numero mayor es: " , mayor)
print("El numero menor es: " , menor)
print(iguales)
