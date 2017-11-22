from Vars import Globals
from Vars import Locals
from Vars import Temps
from Vars import Constants

class MemoryManager:

    def __init__(self):
        self.mem_global = Globals()
        self.mem_const = Constants()
        self.mem_local_stack = [Locals()]
        self.mem_temp_stack = [Temps()]
        self.read_last = False

    def add_var(self, dir_virtual, val):
        self.get_type(dir_virtual).add_var(dir_virtual, val)

    def get_var(self, dir_virtual):
        return self.get_type(dir_virtual).get_var(dir_virtual)

    # Funcion para checar el tope de la pila
    def mem_local(self):
        if (self.read_last == True):
            return self.mem_local_stack[len(self.mem_local_stack) - 2]
        else:
            return self.mem_local_stack[len(self.mem_local_stack) - 1]
        
    def mem_temp(self):
        if (self.read_last == True):
            return self.mem_temp_stack[len(self.mem_temp_stack) - 2]
        else:
            return self.mem_temp_stack[len(self.mem_temp_stack) - 1]

    def read_last_memory(self, value):
        self.read_last = value

    # Funcion para saber si la direccion virtual esta entre otras dos direcciones
    def between(self, dir_virtual, dir_inicial, dir_final):
        return dir_virtual >= dir_inicial and dir_virtual <= dir_final

    # Funcion para saber el tipo de memoria al que se quiere acceder de acuerdo a la direccion virtual
    def get_type(self, dir_virtual):
        if (self.between(dir_virtual, self.mem_global.int, self.mem_global.draw_limit)):
            return self.mem_global
        elif (self.between(dir_virtual, self.mem_local().int, self.mem_local().draw_limit)):
            return self.mem_local()
        elif (self.between(dir_virtual, self.mem_temp().int, self.mem_temp().boolean_limit)):
            return self.mem_temp()
        elif (self.between(dir_virtual, self.mem_const.int, self.mem_const.boolean_limit)):
            return self.mem_const

    def copy(self, mem):
        self.mem_const.var_int = mem.mem_const.var_int
        self.mem_const.var_float = mem.mem_const.var_float
        self.mem_const.var_boolean = mem.mem_const.var_boolean
        self.mem_global.var_int = mem.mem_global.var_int
        self.mem_global.var_float = mem.mem_global.var_float
        self.mem_global.var_boolean = mem.mem_global.var_boolean
        self.mem_global.var_draw = mem.mem_global.var_draw

    def reset_memory(self):
        self.mem_local().next_var_int = 12000
        self.mem_local().next_var_float = 14000
        self.mem_local().next_var_boolean = 16000
        self.mem_local().draw_next = 18000
        self.mem_temp().next_var_int = 20000
        self.mem_temp().next_var_float = 22000
        self.mem_temp().next_var_boolean = 24000

    def add_context(self):
        self.mem_local_stack.append(Locals())
        self.mem_temp_stack.append(Temps())

    def erase_context(self):
        self.mem_local_stack.pop()
        self.mem_temp_stack.pop()
