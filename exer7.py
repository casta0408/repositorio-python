# algoritmo para determinar numero medio 
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))
if (a > b and a < c) or (a > c and a < b):
    medio = a
elif (b > a and b < c) or (b > c and b < a):
    medio = b
else:
    medio = c
print("El número medio es: ", medio)