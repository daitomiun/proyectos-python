# Crear una clase Libro que modele la información que se mantiene en una biblioteca sobre
# cada libro: título, autor, ISBN, páginas, edición, editorial, lugar (ciudad y país) y fecha de
# edición. 

# La clase debe proporcionar los siguientes servicios: método para leer la
# información y método para mostrar la información. Este último método mostrará la
# información del libro con este formato:

# Título: Introducción a java programming
# 3ª. edición
# Autor: Liang, Y. Daniel
# ISBN:0-13-031997-X
# Prentice Hall, New Jersey (USA), viernes 16 de noviembre de 2001,
# 784 páginas

class Libro:
  title=''
  author=''
  ISBN=''
  pages=''
  edition=''
  editorial=''
  country_city=''
  date_edition=''
  def print_info( self,title, author, ISBN, pages, edition, editorial,country_city,date_edition):
    print("libro: "+self.title)
    print("Autor: "+self.author)
    print("ISBN: "+self.ISBN)
    print("paginas: "+self.pages)
    print ("edicion: "+self.edition)
    print ("editorial: "+self.editorial)
    print ("pais: "+self.country_city)
    print ("fecha de edicion: "+self.date_edition)

java = Libro()
java.title =input("nombre del libro: ")
java.author =input("nombre del autor: ")
java.ISBN =input("ISBN: ")
java.pages =input("paginas del libro: ")
java.edition =input("edicion del libro: ")
java.editorial =input("editorial del libro: ")
java.country_city =input("pais del libro: ")
java.date_edition =input("fecha de edicion del libro: ")


print("clases de libro")
java.print_info(java.title, java.author, java.ISBN, java.pages, java.edition, java.editorial,java.country_city,java.date_edition)
  