
def nif():
    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
    numeros = "1234567890"
    nif = raw_input("Introduzca el NIF: ")
    respuesta = "No ha introducido un NIF valido"

    if (len(nif) == 9):
        letraControl = nif[8].upper()
        dni = nif[:8]

        if ( len(dni) == len( [n for n in dni if n in numeros] ) ):

            if tabla[int(dni)%23] == letraControl:
                respuesta="El NIF introducido es correcto"

    print respuesta

nif()
	