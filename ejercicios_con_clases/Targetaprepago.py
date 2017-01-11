from ejerciciohora import Hora

class Targetaprepago():
	numeroTelefono = "971168215"
	nif = "41620806Y"
	saldo = 0.0
	consumo = Hora

def ingresarSaldo():
	CantidadIngreso = float(input("Introduce la cantidad de dinero que quieres ingresar: "))
	Targetaprepago.saldo = Targetaprepago.saldo + CantidadIngreso
	print("Su cantidad de dinero actual es de:",Targetaprepago.saldo)

def enviarMensaje():
	numerosMensaje = int(input("Introduce el numerode mensajes que quieres enviar: "))
	for n in range (0, numerosMensaje):
		Targetaprepago.saldo = Targetaprepago.saldo - 0.9
		print Targetaprepago.saldo

def realizarLlamada():
	Hora.segundos = (int(input("")))
	Targetaprepago.saldo = Targetaprepago.saldo - 0.15
	for n in range (0, Hora.segundos):
		Targetaprepago.saldo = Targetaprepago.saldo - 0.01
		print Targetaprepago.saldo

def consultarTargeta():
	print (Targetaprepago.numeroTelefono, Targetaprepago.nif, Targetaprepago.saldo, Targetaprepago.consumo)

