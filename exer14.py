# Algoritmo que evalué la formula cuadrática o general.  
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
if a == 0:
    print("Error: El coeficiente 'a' no puede ser cero en una ecuación cuadrática.")
else:
    discriminante = b**2 - 4 * a * c
    if discriminante > 0:
        x1 = (-b + discriminante**0.5) / (2 * a)
        x2 = (-b - discriminante**0.5) / (2 * a)
        print("La ecuación tiene dos soluciones reales:")
        print("Solucion 1 =", x1)
        print("Solucion 2 =", x2)
    elif discriminante == 0:
        x = -b / (2 * a)
        print("La ecuación tiene una solución real:")
        print("Solucion =", x)
    else:
        print("La ecuación tiene soluciones complejas y no se pueden calcular en este formato básico.")