## Clase memoria
## Contiene 3 diccionarios para almacenar variables enteras, flotantes y booleanas
import turtle

class Memory:
    # Método que inicializa las variables de la clase memory
    # Recibe como parámetros, la dirección de inicio y fin de los enteros
    #   la dirección de inicio y fin de los flotantes y la dirección de inicio y fin de los booleanos
    # No regresa nada
    # La clase Vars es la unica que hace uso de esta
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

        if (boolean == 34000):
            self.var_boolean[34000] = True
            self.var_boolean[34001] = False

    # Método que obtiene la siguiente dirección de entero y actualiza el valor
    # No recibe parámetros
    # Regresa la siguiente dirección disponible
    def next_int(self):
        actual = self.next_var_int
        self.next_var_int += 1
        return actual

    # Método que obtiene la siguiente dirección de flotante y actualiza el valor
    # No recibe parámetros
    # Regresa la siguiente dirección disponible
    def next_float(self):
        actual = self.next_var_float
        self.next_var_float += 1
        return actual

    # Método que obtiene la siguiente dirección de boolenao y actualiza el valor
    # No recibe parámetros
    # Regresa la siguiente dirección disponible
    def next_boolean(self):
        actual = self.next_var_boolean
        self.next_var_boolean += 1
        return actual

    # Método que agrega un valor a una dirección sabiendo que es entero
    # Recibe la dirección y el valor como parámetros
    # No regresa nada
    def add_int(self, dir, val):
        self.var_int[dir] = val

    # Método que agrega un valor a una dirección sabiendo que es flotante
    # Recibe la dirección y el valor como parámetros
    # No regresa nada
    def add_float(self, dir, val):
        self.var_float[dir] = val

    # Método que agrega un valor a una dirección sabiendo que es booleano
    # Recibe la dirección y el valor como parámetros
    # No regresa nada
    def add_boolean(self, dir, val):
        self.var_boolean[dir] = val

    # Método que agrega un valor a una dirección sabiendo que es un objeto draw
    # Recibe la dirección y el valor como parámetros
    # No regresa nada
    def add_draw(self, dir, val):
        self.var_draw[dir] = val

    # Método que agrega un valor a una dirección sin saber su tipo
    # Recibe la dirección y el valor como parámetros
    # No regresa nada
    def add_var(self, dir_virtual, val):
        type = self.get_type(dir_virtual)
        if (type == 'int'):
            self.add_int(dir_virtual, int(float(val)))
        elif (type == 'float'):
            self.add_float(dir_virtual, float(val))
        elif (type == 'boolean'):
            self.add_boolean(dir_virtual, val)
        elif (type == 'draw'):
            self.add_draw(dir_virtual)

    # Método que obtiene la variable dada una dirección
    # Recibe la dirección como parámetro
    # Regresa el valor que este en dicha dirección
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

    # Método que verifica si una dirección esta dentro del rango
    # Recibe la dirección virtual, la dirección inicial y dirección final como parámetros
    # Regresa true o false dependiendo si se encuentra dentro del rango o no
    def between(self, dir_virtual, dir_inicial, dir_final):
        return dir_virtual >= dir_inicial and dir_virtual <= dir_final

    # Método que regresa el tipo de una variable dada su dirección virtual
    # Recibe como parámetro la dirección virtual
    # Regresa el tipo de la variable
    def get_type(self, dir_virtual):
        if (self.between(dir_virtual, self.int, self.int_limit)):
            return 'int'
        elif (self.between(dir_virtual, self.float, self.float_limit)):
            return 'float'
        elif (self.between(dir_virtual, self.boolean, self.boolean_limit)):
            return 'boolean'
        elif (self.between(dir_virtual, 10000, 11999)):
            return 'draw'

    # Método que actualiza la siguiente variable disponible despues de la declaración de un arreglo
    # Recibe el tipo la dirección virtual y la dimensión como parámetros
    # No regresa nada
    def array_dim(self,type,dir_virtual,dim):
        if(type == 'int'):
            self.next_var_int = self.next_var_int + dim - 1
        elif(type == 'float'):
            self.next_var_float = self.next_var_float + dim - 1
        elif(type == 'boolean'):
            self.next_var_boolean = self.next_var_boolean + dim - 1
