#hacer un programa que lea un numero entero, diga cuantos digitos tiene y calcule la suma de estos


def run():
  num = input('calcular el navasesh del numero: ')
  suma = 0
  for caracter in num:
    
    conversor = int(caracter)
    suma= suma+ conversor
  
  print("tiene "+ caracter + " digitos")
  print("la suma de los "+ caracter +  " digitos es ")
  print(suma)
  
if __name__ == "__main__":
  run()