import c_lexer
import c_parser
import os

parser = c_parser.parser
dir_func = c_parser.dir_func


#a = input("direccion: ")
a = 'ejercicio.draws'
if ( os.path.exists (a)):
    f = open(a)
    data = f.read()
    f.close()
    parser.parse(data)
    print(dir_func)
else:
    print("El archivo no existe")