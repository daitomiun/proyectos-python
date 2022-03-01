# cuenta-elementos-de-lista-1.py

# cadenaPalabras = 'it was the best of times it was the worst of times '
# cadenaPalabras += 'it was the age of wisdom it was the age of foolishness'

listaPalabras =["praga", "berlin", "amsterdam", "paris","praga", "berlin", "amsterdam", "paris","praga", "berlin", "amsterdam", "paris","praga", "berlin", "amsterdam", "paris"]
print(listaPalabras)

frecuenciaPalab = []
for w in listaPalabras:
    frecuenciaPalab.append(listaPalabras.count(w))

print("Lista\n" ,str(listaPalabras) , "\n")
print("Frecuencias\n", str(frecuenciaPalab) , "\n")
print("Pares\n", str(list(zip(listaPalabras, frecuenciaPalab))))
