import sys
import os

# Recibimos la salida de pytest y lo guardamos en un fichero txt
arg = sys.argv

f = open("out.txt", "w")
f.write(arg)
f.close()

os.system("C:/Users/sauri/AppData/Local/Programs/Python/Python311/python.exe c:/Users/sauri/Documents/Proyectos/python/PyTest-Notion/notion.py")