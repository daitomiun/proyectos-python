#hacer un programa que la suma de los primeros numeros n numeros reales

def run():
  n = int(input("escribe un numero para sumarlo cada uno:"))

  print("sumando del 1 al")
  print(n)


  suma= n*(n+1)/2
  print("la suma es ")
  print(suma)

if __name__ == "__main__":
  run()