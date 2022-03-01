def run():
  mi_diccionario = {
    'llave1': 1,
    'llave2': 2,
    'llave3': 3,

  }
  mi_pais = {
    'argentina': 1,
    'colombia': 2,
    'mexico': 3,

  }
  print(mi_diccionario['llave1'])
  print(mi_pais['argentina'])

  #error
  # print(mi_pais['bolivia'])


  for pais in mi_pais.keys():
    print(pais)

  for pais in mi_pais.values():
    print(pais)

  for pais, poblacion in mi_pais.items():
    print(pais + ' tiene ' + str(poblacion) + ' habitantes')


if __name__ == '__main__':
  run()