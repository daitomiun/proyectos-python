def run():
  LIMITE = 10

  contador = 0
  while contador < LIMITE:
    contador= contador+1
    potencia_2 = 2**contador
    print('2 elevado a ' + str(contador) + ' e sigual a: ' + str(potencia_2))

if __name__== '__main__':
  run()