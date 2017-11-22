from Memory import Memory
## Cuatro clases diferentes que contienen los limites de memoria 
## para cada tipo de dato, todas heredan de la clase memoria

# Variables globales
class Globals(Memory):
    def __init__(self):
        # Enteras globales
        int = 4000
        int_limit = 5999

        # Flotantes globales
        float = 6000
        float_limit = 7999

        # Booleanas globales
        bool = 8000
        bool_limit = 9999

        self.draw = 10000
        self.draw_next = 10000
        self.draw_limit = 11999

        Memory.__init__(self, int, int_limit, float, float_limit, bool, bool_limit)

    # Método que busca un valor entero en memoria y obtiene su dirección,
    #   si no lo encuentra lo agrega y obtiene la siguiente dirección
    # Recibe un valor constante como parámetro
    # Regresa la dirección en la que lo ingresó o donde lo encontró
    def next_int(self, cte):
        for dir_virtual, cte_val in self.var_int.items():
            if cte_val == cte:
                return dir_virtual
        self.var_int[self.next_var_int] = cte
        return Memory.next_int(self)

    # Método que busca un valor flotante en memoria y obtiene su dirección,
    #   si no lo encuentra lo agrega y obtiene la siguiente dirección
    # Recibe un valor constante como parámetro
    # Regresa la dirección en la que lo ingresó o donde lo encontró
    def next_float(self, cte):
        for dir_virtual, cte_val in self.var_float.items():
            if cte_val == cte:
                return dir_virtual
        self.var_float[self.next_var_float] = cte
        return Memory.next_float(self)

    # Método que busca un valor booleano en memoria y obtiene su dirección,
    #   si no lo encuentra lo agrega y obtiene la siguiente dirección
    # Recibe un valor constante como parámetro
    # Regresa la dirección en la que lo ingresó o donde lo encontró
    def next_boolean(self, cte):
        for dir_virtual, cte_val in self.var_boolean.items():
            if cte_val == cte:
                return dir_virtual
        self.var_boolean[self.next_var_boolean] = cte
        return Memory.next_boolean(self)

    # Método que agrega un objeto draw a memoria y obtiene la siguiente dirección
    # No recibe parámetros
    # Regresa la dirección en la que lo ingresó
    def next_draw(self):
        actual = self.draw_next
        self.draw_next = self.draw_next + 1
        return actual

# Variables locales
class Locals(Memory):
    def __init__(self):
        ## Enteras locales
        int = 12000
        int_limit = 13999

        # Flotantes locales
        float = 14000
        float_limit = 15999

        # Booleanas locales
        bool = 16000
        bool_limit = 17999

        self.draw = 10000
        self.draw_next = 10000
        self.draw_limit = 11999

        Memory.__init__(self, int, int_limit, float, float_limit, bool, bool_limit)

    # Método que agrega un objeto draw a memoria y obtiene la siguiente dirección
    # No recibe parámetros
    # Regresa la dirección en la que lo ingresó
    def next_draw(self):
        actual = self.draw_next
        self.draw_next = self.draw_next + 1
        return actual

# Variables temporales
class Temps(Memory):
    def __init__(self):
        # Enteras temporales
        int = 18000
        int_limit = 21999

        # Flotantes globales
        float = 22000
        float_limit = 25999

        # Temporales booleanas
        bool = 26000
        bool_limit = 29999

        Memory.__init__(self, int, int_limit, float, float_limit, bool, bool_limit)

# Variables constantes
class Constants(Memory):
    def __init__(self):
        # Constantes enteras
        int= 30000
        int_limit = 31999

        # Constantes flotantes
        float= 32000
        float_limit = 33999

        # Constantes booleanas
        bool= 34000
        bool_limit = 34001

        Memory.__init__(self, int, int_limit, float, float_limit, bool, bool_limit)

    # Método que busca un valor entero en memoria y obtiene su dirección,
    #   si no lo encuentra lo agrega y obtiene la siguiente dirección
    # Recibe un valor constante como parámetro
    # Regresa la dirección en la que lo ingresó o donde lo encontró
    def next_int(self, cte):
        for dir_virtual, cte_val in self.var_int.items():
            if cte_val == cte:
                return dir_virtual
        self.var_int[self.next_var_int] = cte
        return Memory.next_int(self)

    # Método que busca un valor flotante en memoria y obtiene su dirección,
    #   si no lo encuentra lo agrega y obtiene la siguiente dirección
    # Recibe un valor constante como parámetro
    # Regresa la dirección en la que lo ingresó o donde lo encontró
    def next_float(self, cte):
        for dir_virtual, cte_val in self.var_float.items():
            if cte_val == cte:
                return dir_virtual
        self.var_float[self.next_var_float] = cte
        return Memory.next_float(self)

    # Método que busca un valor booleano en memoria y obtiene su dirección,
    #   si no lo encuentra lo agrega y obtiene la siguiente dirección
    # Recibe un valor constante como parámetro
    # Regresa la dirección en la que lo ingresó o donde lo encontró
    def next_boolean(self, cte):
        if(cte == 'True'):
            return 34000
        else:
            return 34001
