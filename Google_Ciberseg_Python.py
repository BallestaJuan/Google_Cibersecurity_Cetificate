#
#   Este programa es la aplicación práctica de lo estudiado en la certificación de Google para Ciberseguridad.
#   Objetivo : retirar del un fichero texto con las "direcciones ip" correctas, la lista de direcciones que no deben ser accesibles 
#
#   Cargo el nombre del fichero con las direcciones en una variable de trabajo 
import_file = "direcciones.txt"

#   Identifico las direcciones que deben ser eliminadas en una variable tipo lista
remove_list = ["Direccion1", "Direccion15", "Direccion16", "Direccion2"]
#   muestro ambas variables por terminal
print(import_file)
print(remove_list)

#   Abro el fichero como lectura hacia la variable direcciones con todas las direcciones.
with open (import_file, "r") as file:
    direcciones = file.read()
# muestro la variable por terminal 
print(direcciones)
# convierto las direcciones en una variable tipo lista por la que poder iterar
direcciones = direcciones.split()
print(direcciones)
#   Itero por la variable direcciones con la variable element y hago un una comparación con if para eliminar la 
#dirección que corresponde si está en la lista 
for element in direcciones:
    if element in remove_list:
        direcciones.remove(element)
# muestro la lista corregida
print(direcciones)
# convierto la lista corregida en una cadena con el método join(), intercalando un retorno con"\n"
direcciones="\n".join(direcciones)
#   Abro el fichero en modo escritura para escribir con el método write() y cargo la lista corregida de direcciones
with open(import_file, "w") as file:
    file.write(direcciones)

#
#   Hemos creado un algoritmo que recorre una lista de "direcciones ip", que en la vida real será un log, y retira las direcciones identificadas como no autorizadas.
#
#   - para la gestión de ficheros 
#       - .read() - lee del fichero 
#       - .write() - escribe en el fichero 
#       - previamente con open(import_file, [param]) abrimos el fichero en la variable file
#   - para la gestión de cadenas/listas
#       - .split() - rompe una variable tipo cadena en sus componentes para convertirla en una lista
#       - .remove() - retira una variable de la lista
#       - .join() - une los elementos de una lista en una cadena de texto 