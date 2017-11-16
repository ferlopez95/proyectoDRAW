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

        Memory.__init__(self, int, int_limit, float, float_limit, bool, bool_limit)

# Variables locales
class Locals(Memory):
    def __init__(self):
        ## Enteras locales
        int = 10000
        int_limit = 11999

        # Flotantes locales
        float = 12000
        float_limit = 13999

        # Booleanas locales
        bool = 14000
        bool_limit = 15999

        Memory.__init__(self, int, int_limit, float, float_limit, bool, bool_limit)

# Variables temporales
class Temps(Memory):
    def __init__(self):
        # Enteras temporales
        int = 16000
        int_limit = 19999

        # Flotantes globales
        float = 20000
        float_limit = 23999

        # Temporales booleanas
        bool = 24000
        bool_limit = 27999

        Memory.__init__(self, int, int_limit, float, float_limit, bool, bool_limit)

# Variables constantes
class Constants(Memory):
    def __init__(self):
        # Constantes enteras
        int= 28000
        int_limit = 31999

        # Constantes flotantes
        float= 32000
        float_limit = 35999

        # Constantes booleanas
        bool= 36000
        bool_limit = 39999

        Memory.__init__(self, int, int_limit, float, float_limit, bool, bool_limit)

    def next_int(self, cte):
        for dir_virtual, cte_val in self.var_int.items():
            if cte_val == cte:
                return dir_virtual
        self.var_int[self.int] = cte
        return Memory.next_int(self)

    def next_float(self, cte):
        for dir_virtual, cte_val in self.var_float.items():
            if cte_val == cte:
                return dir_virtual
        self.var_float[self.float] = cte
        return Memory.next_float(self)

    def next_boolean(self, cte):
        if(cte == 'true'):
            return 36000
        else:
            return 36001
