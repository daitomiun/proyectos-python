
def pesos_universales(mex_col_arg):

  pesos = input("¿cuantos pesos quieres convertir a dolares?: ")
  pesos = float(pesos)
  valor_dolar= mex_col_arg
  dolares= pesos/ valor_dolar
  dolares= round(dolares, 2)
  pesos=str(pesos)
  dolares= str(dolares)  
  print('convertiste ' + pesos+ ' pesos a ' + dolares+ ' dolares' )

arg= 105
col=3875
mex= 20

# tipo_conversion.lower()
# tipo_conversion.rstrip()
# tipo_conversion.lstrip()
tipo_conversion = str(input("peso: argentino  -  colombiano  -  mexicano: ")).lower().replace(' ', '')



if tipo_conversion== "argentino":
  pesos_universales(arg)
elif tipo_conversion=="colombiano":
  pesos_universales(col)
elif tipo_conversion=="mexicano":
  pesos_universales(mex)
else:
  print("pon una respuesta correcta")
