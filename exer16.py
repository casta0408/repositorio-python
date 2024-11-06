# Algoritmo que lea tres números y diga si uno es divisible del otro.
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
if num1 != 0 and num2 % num1 == 0:
    print(num2,"es divisible por ", num1)
elif num1 != 0 and num3 % num1 == 0:
    print(num3," es divisible por " ,num1)
elif num2 != 0 and num1 % num2 == 0:
    print(num1," es divisible por " ,num2)
elif num2 != 0 and num3 % num2 == 0:
    print(num3," es divisible por " ,num2)
elif num3 != 0 and num1 % num3 == 0:
    print(num1," es divisible por " ,num3)
elif num3 != 0 and num2 % num3 == 0:
    print(num2," es divisible por " ,num3)
else:
    print("Ningún número es divisible por otro.")