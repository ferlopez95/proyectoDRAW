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

    def next_int_func(self, cte):
        for dir_virtual, cte_val in self.var_int.items():
            if cte_val == cte:
                return dir_virtual
        self.var_int[self.next_var_int] = cte
        return Memory.next_int(self)

    def next_float_func(self, cte):
        for dir_virtual, cte_val in self.var_float.items():
            if cte_val == cte:
                return dir_virtual
        self.var_float[self.next_var_float] = cte
        return Memory.next_float(self)

    def next_boolean_func(self, cte):
        for dir_virtual, cte_val in self.var_boolean.items():
            if cte_val == cte:
                return dir_virtual
        self.var_boolean[self.next_var_boolean] = cte
        return Memory.next_boolean(self)

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

        self.draw = 18000
        self.draw_next = 18000
        self.draw_limit = 19999

        Memory.__init__(self, int, int_limit, float, float_limit, bool, bool_limit)

    def next_draw(self):
        actual = self.draw_next
        self.draw_next = self.draw_next + 1
        return actual

# Variables temporales
class Temps(Memory):
    def __init__(self):
        # Enteras temporales
        int = 20000
        int_limit = 21999

        # Flotantes globales
        float = 22000
        float_limit = 23999

        # Temporales booleanas
        bool = 24000
        bool_limit = 25999

        Memory.__init__(self, int, int_limit, float, float_limit, bool, bool_limit)

# Variables constantes
class Constants(Memory):
    def __init__(self):
        # Constantes enteras
        int= 26000
        int_limit = 27999

        # Constantes flotantes
        float= 28000
        float_limit = 29999

        # Constantes booleanas
        bool= 30000
        bool_limit = 30001

        Memory.__init__(self, int, int_limit, float, float_limit, bool, bool_limit)

    def next_int(self, cte):
        for dir_virtual, cte_val in self.var_int.items():
            if cte_val == cte:
                return dir_virtual
        self.var_int[self.next_var_int] = cte
        return Memory.next_int(self)

    def next_float(self, cte):
        for dir_virtual, cte_val in self.var_float.items():
            if cte_val == cte:
                return dir_virtual
        self.var_float[self.next_var_float] = cte
        return Memory.next_float(self)

    def next_boolean(self, cte):
        if(cte == 'True'):
            return 30000
        else:
            return 30001
