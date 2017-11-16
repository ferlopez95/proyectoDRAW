from Vars import Globals
from Vars import Locals
from Vars import Temps
from Vars import Constants

class MemoryManager:

    def __init__(self):
        self.mem_global = Globals()
        self.mem_local = Locals()
        self.mem_temp = Temps()
        self.mem_const = Constants()

    def add_var(self, dir_virtual, val):
        self.get_type(dir_virtual).add_var(dir_virtual, val)

    def get_var(self, dir_virtual):
        return self.get_type(dir_virtual).get_var(dir_virtual)

    # Funcion para saber si la direccion virtual esta entre otras dos direcciones
    def between(self, dir_virtual, dir_inicial, dir_final):
        return dir_virtual >= dir_inicial and dir_virtual <= dir_final

    # Funcion para saber el tipo de memoria al que se quiere acceder de acuerdo a la direccion virtual
    def get_type(self, dir_virtual):
        if (self.between(dir_virtual, self.mem_global.int, self.mem_global.boolean_limit)):
            return self.mem_global
        elif (self.between(dir_virtual, self.mem_local.int, self.mem_local.boolean_limit)):
            return self.mem_local
        elif (self.between(dir_virtual, self.mem_temp.int, self.mem_temp.boolean_limit)):
            return self.mem_temp
        elif (self.between(dir_virtual, self.mem_const.int, self.mem_const.boolean_limit)):
            return self.mem_const

    def copy(self, mem):
        self.mem_const.var_int = mem.mem_const.var_int
        self.mem_const.var_float = mem.mem_const.var_int
        self.mem_const.var_ = mem.mem_const.var_int
