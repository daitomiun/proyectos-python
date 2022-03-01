# Cálcular la suma de todos los elementos de un vector de 15 elementos, así como la media
# aritmética. El vector es de tipo real.



def add(div_add= 0):
  print(div_add)

def run(num_array=[]):
  print("sacar media aritmetica")

  n = input("""Introduce cuantos numeros quieras para sacar
  la media aritmetica, cuando termines presiona la 'q' para ejecutar: """)
  if n == "q":
      division = len(num_array)
      print("hay ", division)
      print(num_array)
      add_num= 0

      for num_array in num_array:
        add_num +=num_array
      print(add_num)
      print(add_num/division)
      
      # print(div_add)
      return num_array
  else:
      num_array.append(float(n))
      
      
      return run(num_array)

if __name__ == "__main__":
  run()