#A ciertos estudiantes se les dice que su calificación final será el promedio de las dos calificaciones más altas de entre las tres que se han obtenido en el curso. Haga un algoritmo que permita a un estudiante efectuar el cálculo correspondiente a su nota final.
a = float(input("Ingrese la primera nota: "))
b = float(input("Ingrese la segunda nota: "))
c = float(input("Ingrese la tercera nota: "))
if (a > b and a > c):
 if b > c:
  promedio = (a+b)/2
 else: 
  promedio = (a+c)/2
elif (b > a and b > c):
 if c > a:
  promedio = (b+c)/2
 else:
  promedio = (b+a)/2
else:
  if c > b:
   promedio = (c+a)/2
  else:
   promedio = (c+b)/2
print("El promedio es ", promedio)