def inversion(numero):
  numero_invertido= numero[:: -1]
  print(numero_invertido)

def run():
  numero= input('escribe una numero: ')
  print(numero)
  la_inversion= inversion(numero)

if __name__== '__main__':
  run()

