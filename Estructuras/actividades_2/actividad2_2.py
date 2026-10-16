edad_texto = input("Edad: ")
edad_texto = edad_texto.strip()
 
dia = input("Día de la semana: ")
dia = dia.lower()
dia = dia.strip()
 
es_3d = input("¿Sesión 3D? (si/no): ")
es_3d = es_3d.lower()
es_3d = es_3d.strip()
 
# esto lo he buscado en la ia porque no me salia ponerlo de manera en que pusiese una a y me reventara el sistema
if edad_texto.isdigit() == False:
    print("Edad no válida")
else:
    edad = int(edad_texto)
 
    if edad < 12:
        precio = 5
        print("Entrada menor de 12 años: 5 €")
    elif edad >= 65:
        precio = 6
        print("Entrada de 65 años o más: 6 €")
    else:
        precio = 8
        print("Entrada general: 8 €")
 
    if dia == "miercoles" or dia == "miércoles":
        precio -= 1
        print("Descuento miércoles: -1 €")
 
    if es_3d == "si" or es_3d == "sí":
        precio += 2
        print("Suplemento 3D: +2 €")
 
    print("Precio final:", precio, "€")