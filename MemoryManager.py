from Vars import Globals
from Vars import Locals
from Vars import Temps
from Vars import Constants

class MemoryManager:

    # Método que inicializa las variables de la clase memoryManager
    # No recibe parámetros
    # No regresa nada
    # La clase Helper, y Virtual Machine hacen uso de esta clase
    def __init__(self):
        self.mem_global = Globals()
        self.mem_const = Constants()
        self.mem_local_stack = [Locals()]
        self.mem_temp_stack = [Temps()]
        self.read_last = False

    # Método que agrega una variable a memoria obteniendo su tipo primero
    # Recibe la direción virtual y el valor como parámetros
    # No regresa nada
    def add_var(self, dir_virtual, val):
        self.get_type(dir_virtual).add_var(dir_virtual, val)

    # Método que obtiene la variable obteniendo su tipo primero
    # Recibe la dirección virtual como parámetro
    # Regresa el valor de la variable que se encuentra en esa dirección
    def get_var(self, dir_virtual):
        return self.get_type(dir_virtual).get_var(dir_virtual)

    # Método para checar el tope de la pila del stack de memorias locales
    def mem_local(self):
        if (self.read_last == True):
            return self.mem_local_stack[len(self.mem_local_stack) - 2]
        else:
            return self.mem_local_stack[len(self.mem_local_stack) - 1]

    # Método para checar el tope de la pila del stack de mermorias temporales
    def mem_temp(self):
        if (self.read_last == True):
            return self.mem_temp_stack[len(self.mem_temp_stack) - 2]
        else:
            return self.mem_temp_stack[len(self.mem_temp_stack) - 1]

    # Método para veficiar el contexto en el que se encuentra
    # Recibe el valor de true o false como parametro
    def read_last_memory(self, value):
        self.read_last = value

    # Método para saber si la direccion virtual esta entre otras dos direcciones
    # Recibe la dirección virtual, la inicial y la final como parámetros
    # Regresa si true si se encuentra entre esas dos direcciones si no false
    def between(self, dir_virtual, dir_inicial, dir_final):
        return dir_virtual >= dir_inicial and dir_virtual <= dir_final

    # Método para saber el tipo de memoria al que se quiere acceder de acuerdo a la direccion virtual
    # Recibe la dirección virtaul como parámetro
    # Regresa la memoria en la que se encuentra esa dirección
    def get_type(self, dir_virtual):
        if (self.between(dir_virtual, self.mem_global.int, self.mem_global.draw_limit)):
            return self.mem_global
        elif (self.between(dir_virtual, self.mem_local().int, self.mem_local().boolean_limit)):
            return self.mem_local()
        elif (self.between(dir_virtual, self.mem_temp().int, self.mem_temp().boolean_limit)):
            return self.mem_temp()
        elif (self.between(dir_virtual, self.mem_const.int, self.mem_const.boolean_limit)):
            return self.mem_const

    # Método para compiar las constantes y globales de una memoria a otra
    # Recibe una memoria como parámetro
    # No regresa nada
    def copy(self, mem):
        self.mem_const.var_int = mem.mem_const.var_int
        self.mem_const.var_float = mem.mem_const.var_float
        self.mem_const.var_boolean = mem.mem_const.var_boolean
        self.mem_global.var_int = mem.mem_global.var_int
        self.mem_global.var_float = mem.mem_global.var_float
        self.mem_global.var_boolean = mem.mem_global.var_boolean
        self.mem_global.var_draw = mem.mem_global.var_draw

    # Método que resetea la memoria de locales y temporales
    # No recibe parámetros
    # No regresa nada
    def reset_memory(self):
        self.mem_local().next_var_int = 12000
        self.mem_local().next_var_float = 14000
        self.mem_local().next_var_boolean = 16000
        self.mem_temp().next_var_int = 18000
        self.mem_temp().next_var_float = 22000
        self.mem_temp().next_var_boolean = 26000

    # Método que agrega un contexto de variables locales y temporales a su respectiva pila
    # No recibe parámetros
    # No regresa nada
    def add_context(self):
        self.mem_local_stack.append(Locals())
        self.mem_temp_stack.append(Temps())

    # Método que borra un contexto de la pila de variables locales y temporales
    # No recibe parámetros
    # No regresa nada
    def erase_context(self):
        self.mem_local_stack.pop()
        self.mem_temp_stack.pop()
