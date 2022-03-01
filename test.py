# miVariable = 0

# mi_variable = {
#   "hola": 1,
#   "nada": 2,
#   "1": "oop"
# }
# mi_variable = (“plano”, 10, 3.4, “1”)
# mi_variable = False
# mi_variable= 10.78450294
# MI_VARIABLE = 10
# print(mi_variable[])


def crear_lista(lista=[]):
    n = input("Introduce un número o la 'q' para salir: ")
    if n == "q":
        print(lista)
        return lista
    else:
        lista.append(int(n))
        return crear_lista(lista)

if __name__ == "__main__":
  crear_lista()