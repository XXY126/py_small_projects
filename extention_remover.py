import os
import sys

print("Inserire il percorso della cartella")
path_demo = input()
print("Inserire tipo di estensinoe")
ext = input()

#tolgo gli spazi finali della stringa, di solito quando si copia incolla il percorso si lascia sempre uno spazio
path = path_demo.rstrip()

os.chdir(path)

#"estraggo" tutti i file in una lista
dir_list = os.listdir(str(path))

for x in dir_list:
    if(str(ext) in x):
        os.remove(x)
