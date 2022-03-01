


if __name__ == '__main__':
	menordeedad = float(0)
	femperc = float(0)
	rangemen = float(0)
	othercity = float(0)
	n = float(0)
	sexo = float(0)
	registro_del_carro = float(0)
	tecla_repetir = str(0)
	edad = float(0)
	ano_actual = float(0)
	ano_de_nacimiento = float(0)
	numeropersonas = float(0)

	print("Ingresa el valor de ano actual:", end="")
	ano_actual = float(input())
	while True:
		print("Ingresa el valor de ano de nacimiento:", end="")
		ano_de_nacimiento = float(input())
		print("Selecciona el valor de sexo.")
		print("    1.- Femenino")
		print("    2.- Masculino")
		print("    :", end="")
		while True:
			sexo = float(input())
			if sexo<1 or sexo>2:
				print("Valor incorrecto. Ingr�salo nuevamente.: ", end="")
			if sexo>=1 and sexo<=2: break
		print("Selecciona el valor de registro del carro.")
		print("    1.- medellin")
		print("    2.- Otras ciudades")
		print("    :", end="")
		while True:
			registro_del_carro = float(input())
			if registro_del_carro<1 or registro_del_carro>2:
				print("Valor incorrecto. Ingr�salo nuevamente.: ", end="")
			if registro_del_carro>=1 and registro_del_carro<=2: break
		edad = ano_actual-ano_de_nacimiento
		if edad<25:
			menordeedad = menordeedad+1
		if sexo==1:
			femperc = femperc+1
		if sexo==2 and edad>=12 and edad<=30:
			rangemen = rangemen+1
		if registro_del_carro==2:
			othercity = othercity+1
		print("Valor de edad: ",edad)
		print("")
		numeropersonas = numeropersonas+1
		while True:
			print("Deseas repetir el proceso? (S/N):", end="")
			tecla_repetir = input()
			if tecla_repetir=="s" or tecla_repetir=="n" or tecla_repetir=="S" or tecla_repetir=="N": break
		if tecla_repetir=="n" or tecla_repetir=="N": break
	if n==menordeedad:
		menordeedad = 0
	else:
		menordeedad = menordeedad/numeropersonas
	if n==femperc:
		femperc = 0
	else:
		femperc = femperc/numeropersonas
	if n==rangemen:
		rangemen = 0
	else:
		rangemen = rangemen/100.0
	if n==othercity:
		othercity = 0
	else:
		othercity = othercity/numeropersonas
	print("menores de 25 anios: ",menordeedad,"%")
	print("procentaje de mujeres: ",femperc,"%")
	print("rango de hombres de 12 anios hasta 30 anios: ",rangemen,"%")
	print("porcentaje de carros fuera de medellin : ",othercity,"%")

