import c_lexer
import c_parser
import os

parser = c_parser.parser
drawCompiler = c_parser.drawCompiler


#a = input("direccion: ")
a = "ejemplo.draws"
if ( os.path.exists (a)):
    f = open(a)
    data = f.read()
    f.close()
    parser.parse(data)
    for key, value in drawCompiler.dir_func.items() :
        print(str(key) + " : " + str(value))
    print(drawCompiler.pilaO)
    print(drawCompiler.pType)
    print(drawCompiler.pOper)
    print(drawCompiler.memoria)
    i = 1
    for quad in drawCompiler.quad : 
        print (str(i) + ": " + str(quad))
        i = i + 1
else:
    print("El archivo no existe")
