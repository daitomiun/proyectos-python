# Elaborar una clase y los métodos que considere necesarios para encontrar la suma y el
# promedio de n números.


class promedio:
  contador=0
  suma=0
  numero=1
  def print_info( self,contador, suma, numero):
    while numero !=0:
      numero = int(input('pon un numero entero(pon 0 para terminar): '))
      suma += numero
      contador +=1
    
    if contador == 0:
      print('fin de programa')
    else:
      promedio = suma/contador
      print('el promedio de {} estos numeros es igual a {}'.format(contador,promedio))

proceso = promedio()
proceso.numero = 1
proceso.contador=0
proceso.suma=0
proceso.print_info(proceso.contador, proceso.suma, proceso.numero)


