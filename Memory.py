## Clase memoria
## Contiene 3 diccionarios para almacenar variables enteras, flotantes y booleanas
import turtle

class Memory:
    def __init__(self, int, int_limit, float, float_limit, boolean, boolean_limit ):
        self.var_int = {}
        self.var_float = {}
        self.var_boolean = {}
        self.int = int
        self.int_limit = int_limit
        self.float = float
        self.float_limit = float_limit
        self.boolean = boolean
        self.boolean_limit = boolean_limit
        self.next_var_int = self.int
        self.next_var_float = self.float
        self.next_var_boolean = self.boolean
        self.var_draw = {}

        if (boolean == 30000):
            self.var_boolean[30000] = True
            self.var_boolean[30001] = False

    def next_int(self):
        actual = self.next_var_int
        if(actual == self.int_limit):
            print("Error: No memory available")
            return None
        else:
            self.next_var_int += 1
            return actual

    def next_float(self):
        actual = self.next_var_float
        if(actual == self.float_limit):
            print("Error: No memory available")
            return None
        else:
            self.next_var_float += 1
            return actual

    def next_boolean(self):
        actual = self.next_var_boolean
        if(actual == self.boolean_limit):
            print("Error: No memory available")
            return None
        else:
            self.next_var_boolean += 1
            return actual

    def add_int(self, dir, val):
        self.var_int[dir] = val

    def add_float(self, dir, val):
        self.var_float[dir] = val

    def add_boolean(self, dir, val):
        self.var_boolean[dir] = val

    def add_draw(self, dir, val):
        self.var_draw[dir] = val

    def add_var(self, dir_virtual, val):
        type = self.get_type(dir_virtual)
        if (type == 'int'):
            self.add_int(dir_virtual, int(float(val)))
        elif (type == 'float'):
            self.add_float(dir_virtual, float(val))
        elif (type == 'boolean'):
            self.add_boolean(dir_virtual, val)
        elif (type == 'draw'):
            self.add_draw(dir_virtual, val)

    def get_var(self, dir_virtual):
        type = self.get_type(dir_virtual)
        if (type == 'int'):
            return self.var_int[dir_virtual]
        elif (type == 'float'):
            return self.var_float[dir_virtual]
        elif (type == 'boolean'):
            return self.var_boolean[dir_virtual]
        elif (type == 'draw'):
            return self.var_draw[dir_virtual]

    def between(self, dir_virtual, dir_inicial, dir_final):
        return dir_virtual >= dir_inicial and dir_virtual <= dir_final

    def get_type(self, dir_virtual):
        if (self.between(dir_virtual, self.int, self.int_limit)):
            return 'int'
        elif (self.between(dir_virtual, self.float, self.float_limit)):
            return 'float'
        elif (self.between(dir_virtual, self.boolean, self.boolean_limit)):
            return 'boolean'
        elif (self.between(dir_virtual, 10000, 11999) or self.between(dir_virtual, 18000, 19999)):
            return 'draw'

    def array_dim(self,type,dir_virtual,dim):
        if(type == 'int'):
            self.next_var_int = self.next_var_int + dim - 1
        elif(type == 'float'):
            self.next_var_float = self.next_var_float + dim - 1
        elif(type == 'boolean'):
            self.next_var_boolean = self.next_var_boolean + dim - 1
