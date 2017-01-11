class Hora():
	hora = 0
	minutos = 0
	segundos = 0

def setHora(hora, minutos, segundos):
	if (hora >= 0 and hora <=24):
		Hora.hora = hora 
	else:
		return hora

	if (minutos >= 0 and minutos <= 59):
		Hora.minutos = minutos
	else:
		return minutos

	if (segundos >= 0 and segundos <= 59):
		Hora.segundos = segundos
	else:
		return segundos

def getHora():
	listaHora = [Hora.hora, Hora.minutos, Hora.segundos]
	print (listaHora)
	print  ("hora:", Hora.hora," minutos:",Hora.minutos," segundos:",Hora.segundos)


def imprimirHora():
	getHora()

