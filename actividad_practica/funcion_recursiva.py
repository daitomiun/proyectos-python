# Escribir el algoritmo de una función recursiva que: a) calcule la factorial de un número entero
# positivo, b) la potencia de un número entero positivo.


def run():
  numero = int(input("escribe un numero: "))
  decision = int(input("quieres calcular su factorial o su potencia? factorial=1 potencia=2: "))
  if decision == 1:
    factorial = numero
    for i in range(1, numero):
      factorial *= i
      print(factorial)
  elif decision >= 2:
    for i in range(1, 11):
      conversor = str(i)
      conversor_numero = str(numero)
      print("la "+conversor+ " potencia de " + conversor_numero+ " es ")
      print(numero**i)
  else:
    print("ponga un numero correcto")



if __name__ == "__main__":
  run()