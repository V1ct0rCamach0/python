
TIEMPO_CINE = 2
DINERO_CINE = 10
TIEMPO_COMER = 2
DINERO_COMER = 30
TIEMPO_MUSEO = 1
DINERO_MUSEO = 5
TIEMPO_DEPORTE = 1
DIENERO_DEPORTE = 0
TIEMPO_DEPORTE = 3
DIENERO_DEPORTE = 0

tiempo = int(input("cuanto tiempo tenemos:"))
dinero = int(input("Cuanto dinero tienes:"))


def mostrar_opciones():
    print ("1 - ira al cine (10€ / 2 horas)" )
    print ("2 - salir a comer (30€ / 2 horas)")
    print ("3 - visitar un museo (5€ / 1 hora)")
    print ("4 - hacer deporte (0€ /1 hora)")
    print ("5 - quedarse en casa (0€ / 3 horas)")


mostrar_opciones()

def main ():
    TIEMPO_CINE = 2
    DINERO_CINE = 10
    TIEMPO_COMER = 2
    DINERO_COMER = 30
    TIEMPO_MUSEO = 1
    DINERO_MUSEO = 5
    TIEMPO_DEPORTE = 1
    DIENERO_DEPORTE = 0
    TIEMPO_DEPORTE = 3
    DIENERO_DEPORTE = 0

    tiempo = int(input("cuanto tiempo tenemos:"))
    dinero = int(input("Cuanto dinero tienes:"))
    actividades = ""
    
    while dinero > 0 and tiempo > 0 :
        mostrar_opciones()
        opcion = int(input("Que quieres hacer: "))
    
        match opcion:
            case "1":
                dinero -= DINERO_CINE
                tiempo -= TIEMPO_CINE    
                actividades += "ir al cine (10€ / 2 horas)"
            case "2":
                dinero -= DINERO_CINE
                tiempo -= TIEMPO_CINE    
                actividades += "ir al cine (10€ / 2 horas)"
        match opcion:
            case "3":
                dinero -= DINERO_CINE
                tiempo -= TIEMPO_CINE    
                actividades += "ir al cine (10€ / 2 horas)"
            case "4":
                dinero -= DINERO_CINE
                tiempo -= TIEMPO_CINE    
                actividades += "ir al cine (10€ / 2 horas)"
            case "5":
                dinero -= DINERO_CINE
                tiempo -= TIEMPO_CINE    
                actividades += "ir al cine (10€ / 2 horas)"
    print (actividades)
                
if __name__ == main:
    main()