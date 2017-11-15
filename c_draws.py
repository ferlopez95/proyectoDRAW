import c_lexer
import c_parser
import os
from VirtualMachine import VirtualMachine


parser = c_parser.parser
drawCompiler = c_parser.drawCompiler

#a = input("direccion: ")
a = "mini_prueba.draws"
if ( os.path.exists (a)):
    f = open(a)
    data = f.read()
    f.close()
    parser.parse(data)
    
    for key, value in drawCompiler.dir_func.items() :
        print(str(key) + " : " + str(value))
    print("Cuadruplos")
    i = 0
    for quad in drawCompiler.quad :
        print(str(i) + " " + str(quad))
        i += 1
    #print(drawCompiler.pilaO)
    #print(drawCompiler.pType)
    #print(drawCompiler.pOper)
    #print(drawCompiler.memoria)
    virtual = VirtualMachine(drawCompiler.quad, drawCompiler.memory_manager)
    print(virtual.memory.mem_local.var_int)
    print(virtual.memory.mem_local.var_float)
    print(virtual.memory.mem_local.var_boolean)
else:
    print("El archivo no existe")
