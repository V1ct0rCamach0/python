import random 

num_cuenta = random.randint(0,1000)

titular = "pepito"
cuenta = True
accion = input("que operacion quieres realizar: 1º ingresar , 2º cerrar, 3º retirar , 4º abrir, 5º consultar")

accion_limpia = accion.lower().strip()

match accion_limpia:
    case "ingresar":
        ingreso = int(input("cuanto desea ingresar"))
        if ingreso > 0:
            num_cuenta += ingreso
        else:
            print ("no es valida la operacion")        
    case "cerra":
        cuenta = False
        print ("hemos cerrado tu cuenta")
    case "retirar":
        retirar = int(input ("cuanto desea retirar:"))
        if retirar > 0 and num_cuenta >= retirar:
            num_cuenta -= retirar
        else:
            print("no se puede retirar ese dinero")
    case "abrir":
        cuenta = True
        print ("hemos habierto su cuenta")
    case "consultar":
        print (num_cuenta)
    case _:
        print ("operacion no valida")

print (num_cuenta)
