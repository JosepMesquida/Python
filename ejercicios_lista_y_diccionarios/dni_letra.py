letras = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]

def letraDni():
	while True:
		dni = str(input("Introduce tu dni y sabras la letra que te corresponde: "))
		if (len(dni) == 8):
			dni = int(dni)
			dni = dni % 23
			return letras[dni:dni+1]
		else:
			print("")
			print("Vuelve ha introducir tu dni, tiene que haber 8 numeros")
			print("")

print letraDni()