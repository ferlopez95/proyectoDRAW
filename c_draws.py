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
    for key, value in dir_func.items() :
        print(str(key) + " : " + str(value))
else:
    print("El archivo no existe")