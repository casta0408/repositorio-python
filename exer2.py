# algoritmo sueldo + aumento 
sueldo = float(input("Ingresa el sueldo del trabajador: "))
if sueldo < 300000:
    aumento = int(sueldo * 0.15)
    nuevo_sueldo = sueldo + aumento
    print("Sueldo original: $" , sueldo)
    print("Aumento aplicado: $" , aumento)
    print("Nuevo sueldo: $" , nuevo_sueldo)
else:
    print("Sueldo sin aumento: $" , sueldo)