# Elaborar un programa para sumar dos matrices cuadradas. El orden de las matrices se
# recibe por teclado. Basarse en algebra lineal.

print("suma de matrices")
rows = int(input("pon el numero de filas"))
columns= int(input("pon el numero de columnas"))


matriz_a=[]
matriz_b=[]
matriz_c=[]
i=0


#viejo

# for i in range(rows):
#   matriz_a.append([0]*columns)
#   print("matriz A",matriz_a[i])
#   # print(i)
#   i += 1
# for i in range(rows):
#   matriz_b.append([0]*columns)
#   print("matriz B",matriz_b[i])
#   # print(i)
#   i += 1
# for i in range(rows):
#   matriz_c.append([0]*columns)
#   print("matriz C",matriz_b[i])
#   # print(i)
#   i += 1

#nuevo

def cycle(switch = 0):
  for i in range(rows):
    tomo = len(matriz_a)
    revision = int(tomo +1)        
    if switch ==0:
      matriz_a.append([0]*columns)
      print("matriz A",matriz_a[i])
    if revision == rows:
      for i in range(rows):
        matriz_b.append([0]*columns)
        print("matriz B",matriz_b[i])
      continue
      
  for i in range(rows):
    matriz_c.append([0]*columns)
    print("matriz C",matriz_b[i])
    # print(i)
    i += 1
  for i in range(rows):
    for j in range(columns):
      matriz_a[i][j]= int(input('dame el componente a (%d, %d)'%(i,j)))

  for i in range(rows):
    print(matriz_a[i])



  for i in range(rows):

    for j in range(columns):
      matriz_b[i][j]= int(input('dame el componente b (%d, %d)'%(i,j)))


  for i in range(rows):
    print(matriz_b[i])


  for i in range(rows):
    for j in range(columns):
      matriz_c[i][j]= matriz_a[i][j] + matriz_b[i][j]

  for i in range(rows):
    R=[]
    for j in range(columns):
      R.append(matriz_c[i][j])
    print(R)



if __name__ == "__main__":
  cycle()
 









