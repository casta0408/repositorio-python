#Dados tres números enteros únicos, a, b y c. Elabore un algoritmo que los ordene de mayor a menor e imprímalos. 
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segindo numero: "))
c = int(input("Ingrese el tercer numero: "))
if a > b and a > c:
    if b > c:
        orden = a,b,c 
    else :
        orden = a,c,b
elif b > a and b > c:
    if a > c:
        orden = b,a,c
    else:
        orden = b,c,a
else:
    if a > b:
        orden = c,a,b
    else:
        orden = c,b,a                          
print ("El orden de los numeros de mayor a menor es: ", orden)