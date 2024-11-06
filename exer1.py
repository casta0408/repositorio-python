# algoritmo apobrado o no segun calificacion
calificacion = float(input("Ingresa la calificación del alumno: "))
if calificacion > 5:
    print("Nota no válida")
elif calificacion > 3:
    print("Aprobado")
else:
    print("No aprobado")