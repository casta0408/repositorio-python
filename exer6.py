# algoritmo para dterminar edad,sexo,nombre etc
nombre = input("Ingresa el nombre de la persona: ")
edad = int(input("Ingresa la edad de la persona: "))
sexo = input("Ingresa el sexo de la persona (M para hombre, F para mujer): ")
estado_civil = input("Ingresa el estado civil de la persona (Casado o Soltero): ")
if sexo == 'M' and estado_civil == 'Casado' and edad > 40:
    print(nombre, " es un hombre casado mayor de 40 años.")
elif sexo == 'F' and estado_civil == 'Soltero' and edad < 50:
    print(nombre, " es una mujer soltera menor de 50 años.")
else:
    print(nombre, " no cumple con los criterios especificados.")
