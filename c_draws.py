import c_lexer
import c_parser
import os

parser = c_parser.parser



a = input("direccion: ")
if ( os.path.exists (a)):
    f = open(a)
    data = f.read()
    f.close()
    parser.parse(data)
else:
    print("El archivo no existe")