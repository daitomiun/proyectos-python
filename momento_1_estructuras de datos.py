import random
import collections

# podria usar un diccionario para tomar los datos de los paises

# ciudades = {"Praga":1, "Berlin":2, "Amsterdam":3, "Paris":4}


#de ahi sentenciar que ciudad va ir primero y se va primero
# for ciudad, id_ciudad in ciudades.items():
    # print(ciudad)
    # if id_ciudad == 1:
    #   print("esto es {}".format(ciudad))

    # if id_ciudad == 2:
    #   print("esto es {}".format(ciudad))
    # if id_ciudad == 3:
    #   print("esto es {}".format(ciudad))
    # if id_ciudad == 4:
    #   print("esto es {}".format(ciudad))


#genero id y referencia personalizada
def generar_id_ref(ref=[],id_fuente=[]):
  MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
  MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
  NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
  caracteres = MAYUS + MINUS +NUMS
  id_caracteres= NUMS
  conc_ref =[]
  conc_id =[]

  for i in range(10):
    caracter_random = random.choice(caracteres)
    id_random = random.choice(id_caracteres)
    conc_ref.append(caracter_random)
    conc_id.append(id_random)
    # print(conc_ref)
    # print(conc_id)
  conc_ref = ''.join(conc_ref)
  conc_id = ''.join(conc_id)
  ref.append(conc_ref)
  id_fuente.append(conc_id)
  generar_id_ref.tomar_datos_ref= ref
  generar_id_ref.tomar_datos_id= id_fuente

# quito un tiquete de la lista
def quitar_de_lista():
  tecla_repetir = str(0)    
  while True:
    while True:
      print("fecha: ", crear_lista.tomar_fecha)

      quitar_tiquete=input("cuantos tiquetes quieres eliminar? ")
      quitar_tiquete = int(quitar_tiquete)
      # test = len(generar_id_ref.tomar_datos_id)
      # print(test)

      if quitar_tiquete >= 0 and quitar_tiquete<= len(generar_id_ref.tomar_datos_id):
        for i in range(quitar_tiquete):
          generar_id_ref.tomar_datos_ref.pop(0)
          generar_id_ref.tomar_datos_id.pop(0)
          crear_lista.tomar_fecha.pop(0)
          crear_lista.tomar_ciudad.pop(0)


          print(i)
      else:
        continue

      print("Deseas repetir el proceso? (S/N):", end="")
      tecla_repetir = input()
      if tecla_repetir=="s" or tecla_repetir=="n" or tecla_repetir=="S" or tecla_repetir=="N": break
    if tecla_repetir=="n" or tecla_repetir=="N": break
  tecla_repetir_tiquete = True
  while tecla_repetir_tiquete== True:
    print("Deseas añadir mas tiquetes? (S/N):", end="")
    tecla_repetir_tiquete = input()
    print(tecla_repetir)
    if tecla_repetir_tiquete=="n" or tecla_repetir_tiquete=="N": 
      tecla_repetir_tiquete == False
    if tecla_repetir_tiquete=="s" or tecla_repetir_tiquete=="S": 
      tecla_repetir_tiquete == True
      crear_lista()
      

    #if tecla_repetir=="s" or tecla_repetir=="S" and tecla_repetir=="n" or tecla_repetir=="N": crear_lista()
    


def crear_lista(fecha=[], ciudad=[]):

  n = input("Introduce la 'q' para poder borrar datos, otro digito para seguir: ")
  if n == "q":
      quitar_de_lista()
  
      # print(fecha)
      return ciudad
  else:
      var_ciudad= input("ciudad del tiquete  --praga--berlin--amsterdam--paris: ").lower().replace(' ', '')
      var_fecha=input("fecha de entrada(solo el dia): ")
      generar_id_ref()
      ciudad.append(str(var_ciudad))
      fecha.append(int(var_fecha))
      crear_lista.tomar_fecha = fecha
      crear_lista.tomar_ciudad = ciudad


      return crear_lista(fecha, ciudad)
crear_lista()


  # print("referencia",ref)
  # print("fuente id",id_fuente)
# for i in range(20):
#   generar_id_ref()

# print("referencia",generar_id_ref.tomar_datos_ref)

# quitar_de_lista()


# print("referencia",generar_id_ref.tomar_datos_ref)
# print("id",generar_id_ref.tomar_datos_id)
# print("fecha: ", crear_lista.tomar_fecha)
# print("ciudad: ", crear_lista.tomar_ciudad)

# def ciclo_ciudad():
  
# ciudades = ["praga", "berlin", "amsterdam", "paris"]
ciclo = len(crear_lista.tomar_fecha)
# print(ciclo)
crear_tiquete = []
for tiquetes in range(ciclo):
  crear_tiquete.append((generar_id_ref.tomar_datos_ref[tiquetes],generar_id_ref.tomar_datos_id[tiquetes],crear_lista.tomar_fecha[tiquetes],crear_lista.tomar_ciudad[tiquetes]))
  print("referencia del tiquete: ",generar_id_ref.tomar_datos_ref[tiquetes])
  print("id del tiquete: ", generar_id_ref.tomar_datos_id[tiquetes])
  print("fecha del tiquete: ",crear_lista.tomar_fecha[tiquetes])
  print("ciudad del tiquete: ",crear_lista.tomar_ciudad[tiquetes],"\n")






# ciudad_fuente=["Praga", "Berlin", "Amsterdam", "Paris"]



  # print("es {}".format(ciudad))
  # print("es {}".format(ciudades[ciudad]))



