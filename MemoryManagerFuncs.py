from Vars import Locals
from Vars import Temps

class MemoryManagerFuncs:

    def __init__(self):
        self.mem_local = Locals()
        self.mem_temp = Temps()

    def add_var(self, dir_virtual, val):
        self.get_type(dir_virtual).add_var(dir_virtual, val)

    def get_var(self, dir_virtual):
        return self.get_type(dir_virtual).get_var(dir_virtual)

    # Funcion para saber si la direccion virtual esta entre otras dos direcciones
    def between(self, dir_virtual, dir_inicial, dir_final):
        return dir_virtual >= dir_inicial and dir_virtual <= dir_final

    # Funcion para saber el tipo de memoria al que se quiere acceder de acuerdo a la direccion virtual
    def get_type(self, dir_virtual):
        if (self.between(dir_virtual, self.mem_local.int, self.mem_local.boolean_limit)):
            return self.mem_local
        elif (self.between(dir_virtual, self.mem_temp.int, self.mem_temp.boolean_limit)):
            return self.mem_temp
