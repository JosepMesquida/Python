class CuentaCorriente():
	nombre = "Josep"
	apellido = "Mesquida Sampol"
	direccion = "C/ Moli d'en Negre"
	telefono =  "629257378"
	saldo = 0.0

class Dni():
	nif = "41620806Y"

def retirarDinero():
	dineroRetirar = int(input("Introduce el dinero que quieres retirar: "))
	CuentaCorriente.saldo = CuentaCorriente.saldo - dineroRetirar
	print("")
	print("La operacion ha tenido exito")
	print("")

def ingresarDinero():
	dineroIngresar = int(input("Introduce el dinero que quieres retirar: "))
	CuentaCorriente.saldo = CuentaCorriente.saldo + dineroIngresar
	print("")
	print("La operacion ha tenido exito")
	print("")

def consultarCuenta():
	print("")
	print(CuentaCorriente.nombre, CuentaCorriente.apellido, CuentaCorriente.direccion, CuentaCorriente.telefono, CuentaCorriente.saldo)
def saldoNegativo():
	if (CuentaCorriente.saldo < 0):
		print (CuentaCorriente.saldo)
		print("")

	else:
		print("")
		print("No tienes saldo negativo")
		print("")

def menu():
	i = 0
	while (i==0):
		print("")
		print("1.Ingresar dinero")
		print("")
		print("2.Retirar dinero")
		print("")
		print("3.Consultar cuenta")
		print("")
		print("4.Consultar si hay saldo negativo")
		print("")
		print ("5.Salir")
		print("")
		numeroMenu = int(input("Introduce el numero de la operacipn que quieres realizar: "))
		print("")

		if (numeroMenu == 1):
			ingresarDinero()
		elif (numeroMenu == 2):
			retirarDinero()
		elif (numeroMenu == 3):
			consultarCuenta()
		elif (numeroMenu == 4):
			saldoNegativo()
		elif (numeroMenu == 5):
			break
		elif (numeroMenu < 0 or numeroMenu > 5):
			print("")
			print("Introduce una operacion disponible :)")
			print("")

menu()

