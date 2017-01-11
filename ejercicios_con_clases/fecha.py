class Fecha():
	dia = 0
	mes = 0 
	ano = 0

	def defaultDate():
		Fecha.dia = 01
		Fecha.mes = 01
		Fecha.ano = 1900

	def ponerFecha():
		dia = int(input("Introduce el numero de dia: "))
		mes = int(input("Introduce el numero de mes: "))
		ano = int(input("Introduce el numero de ano: "))

		if (dia >= 0 and dia <= 31):
			Fecha.dia = dia
		else:
			Fecha.dia = 0

		if (mes >= 0 and mes <= 12):
			Fecha.mes = mes
		else: 
			Fecha.mes = 0

		if (ano >= 1900 and ano <=3000):
			Fecha.ano = ano
		else:
			Fecha.ano = 0

def setFecha():
	Fecha.ponerFecha()

def incrementarFecha():
	numeroDias = int(input("Introduce una cantidad de dias: "))
	Fecha.dia = Fecha.dia + numeroDias

def imprimirFecha():
	print (Fecha.dia, Fecha.mes, Fecha.ano)





