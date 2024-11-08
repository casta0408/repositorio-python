# algoritmo de la varilla
longitud = float(input("Ingrese la longitud de la varilla en cm: "))
diametro = float(input("Ingrese el diámetro de la varilla en cm: "))
densidad = 3.5  
masa = (diametro * longitud) / densidad
if 7.5 < longitud <= 9 and 0.5 <= diametro <= 1.3 and masa <= 5.8:
    print("La varilla es aceptada.")
else:
    print("La varilla es rechazada.")