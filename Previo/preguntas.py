print("Recuerda escribir la primera con mayscula, sin tildes y entre comillas")
print("Empecemos!")
a=input("Cuanto es 12*23?")
if not a=="276":
    print("Nooo, era 276")
    print("Esto se acaba aqui")
if a=="276":
    print("Corrrrrrecectooo!")
    print("Siguiente pregunta:")
    b=input("Cual es la capital de Extremadura?")
    if not b=="Merida":
        print("Nooo, era Merida")
        print("Perdiste")
    if b=="Merida":
        print("Exacto")
        print("Vamos con la ultima")
        c=input("En que ano finalizo la Reconquista (cuando expulsaron a los arabes de la Peninsula Iberica)?")
        if not c=="1492":
            print("Estuviste a punto, fue en el 1492")
        if c=="1492":
            print("Has ganado!!!!")
