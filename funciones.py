def imprimir_mensaje():
  print("mensaje funcion")

def conversacion(mensaje):
  print("hola")
  print("como estas")
  print(mensaje)
  print("adios")



opcion = int(input("elige una opcion (1,2,3)"))

if opcion == 1:
  conversacion("elegiste la conversacion "+  str(opcion))
elif opcion == 2:
  conversacion("elegiste la conversacion "+  str(opcion))

elif opcion == 3:
  conversacion("elegiste la conversacion "+  str(opcion))

else:
  print("escribe la opcion correcta")

