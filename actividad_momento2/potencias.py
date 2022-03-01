#implementa un programa que muestro todos los numeros potencia de 2 entre 20 y 230 ambos inclusive

def run():
  for i in range(20, 231):
    conversor = str(i)
    print("la "+conversor+ " potencia de 2 es ")
    print(2**i)

if __name__ == "__main__":
  run()