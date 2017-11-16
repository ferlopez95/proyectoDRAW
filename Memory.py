## Clase memoria
## Contiene 3 diccionarios para almacenar variables enteras, flotantes y booleanas
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

        if (boolean == 36000):
            self.var_boolean[36000] = True
            self.var_boolean[36001] = False

    def next_int(self):
        actual = self.int
        self.int += 1
        return actual

    def next_float(self):
        actual = self.float
        self.float += 1
        return actual

    def next_boolean(self):
        actual = self.boolean
        self.boolean += 1
        return actual

    def add_int(self, dir, val):
        self.var_int[dir] = val

    def add_float(self, dir, val):
        self.var_float[dir] = val

    def add_boolean(self, dir, val):
        self.var_boolean[dir] = val

    def add_var(self, dir_virtual, val):
        type = self.get_type(dir_virtual)
        if (type == 'int'):
            self.add_int(dir_virtual, int(val))
        elif (type == 'float'):
            self.add_float(dir_virtual, float(val))
        elif (type == 'boolean'):
            self.add_boolean(dir_virtual, val)

    def get_var(self, dir_virtual):
        type = self.get_type(dir_virtual)
        if (type == 'int'):
            return self.var_int[dir_virtual]
        elif (type == 'float'):
            return self.var_float[dir_virtual]
        elif (type == 'boolean'):
            return self.var_boolean[dir_virtual]

    def between(self, dir_virtual, dir_inicial, dir_final):
        return dir_virtual >= dir_inicial and dir_virtual <= dir_final

    def get_type(self, dir_virtual):
        if (self.between(dir_virtual, self.int, self.int_limit)):
            return 'int'
        elif (self.between(dir_virtual, self.float, self.float_limit)):
            return 'float'
        elif (self.between(dir_virtual, self.boolean, self.boolean_limit)):
            return 'boolean'

    def array_dim(self,type,dir_virtual,dim):
        if(type == 'int'):
            self.int = self.int + dim - 1
        elif(type == 'float'):
            self.float = self.float + dim - 1
        elif(type == 'boolean'):
            self.boolean = self.boolean + dim - 1
