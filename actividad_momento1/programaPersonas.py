print("quien es mas joven?")

persona_1= int(input("cuanto años tienes tu?: "))
persona_2= int(input("cuanto años tienes tu amigo/a?: "))

if persona_1 > persona_2:
  print("tu amigo/a es mas joven!")
elif persona_1 < persona_2:
  print("eres mas joven!")
else:
  print("tienen la misma edad")