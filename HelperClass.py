from SemanticCube import SemanticCube
from MemoryManager import MemoryManager

class HelperClass(object):

    # Metodo que inicializa las variables de la clase
    # Recibe como parámetros el scope actual
    # No genera nada de salida
    # Todos los métodos de esta clase son importantes para el parser
    def __init__(self, actual_scope):
        self.actual_scope = actual_scope
        self.dir_func = {}
        self.pOper = []
        self.pType = []
        self.pilaO = []
        self.quad = []
        self.pJumps = []
        self.cont = 0
        self.param_k = 0
        self.params = []
        self.sem_cube = SemanticCube().cube
        self.memory_manager = MemoryManager()

    # Método que resetea las variables para el scope global
    # No recibe parametros
    # No genera salida
    # La clase parser es la que hace más uso de el
    def reset(self):
        self.actual_scope = 'global'
        self.dir_func = {}
        self.pOper = []
        self.pType = []
        self.pilaO = []
        self.quad = []
        self.temp = 0
        self.pJumps = []
        self.cont = 0
        self.param_k = 0
        self.params = []
        self.sem_cube = SemanticCube().cube
        self.memory_manager = MemoryManager()
        self.add_func('void', 'global')

    # Verifica si la variable ya existe en el scope actual
    # Recibe como parámetros el id a buscar
    # Regresa 1 si encontró el id en la tabla de variables
    def exists_in_scope(self, id):
        if (id in self.vars_table()) :
               return 1
        if (len(self.inner_scopes()) >= 1):
            if (id in self.vars_table()) :
                return 1
            for key in self.inner_scopes():
                if id in key:
                    return 1
        global_table = self.dir_func['global']['vars']
        if (id in global_table):
            return 1

    # Método que agrega una variable al directorio de funciones
    # Recibe como parámetro el tipo, el id y una dirección virtual
    # No regresa nada
    def add_var(self, type, id, dir_virtual):
        if (len(self.inner_scopes()) >= 1):
            inner = self.inner_scopes().pop()
            inner[id] = {'type' : type, 'dir_virtual' : dir_virtual}
            self.inner_scopes().append(inner)
        else:
            self.vars_table()[id] = {'type' : type, 'dir_virtual' : dir_virtual}
        self.add_total_var()

    # Método que aumenta en uno la variable de total_vars de un scope
    # No recibe parametros
    # No regresa nada
    def add_total_var(self):
        self.dir_func[self.actual_scope]['total_vars'] += 1

    # Método que agrega una función al directorio de funciones
    # Recibe el tipo y el id
    # No regresa nada
    def add_func(self, type, id):
        self.dir_func[id] = {'type' : type, 'parameters' : [], 'total_vars' : 0, 'vars' : {}, 'inner_scope' : [], 'counter' : 0, 'dir' : self.next_func(type,id)}

    # Método que agrega el tipo de un parámetro a una función dependiendo del scope
    # Recibe el tipo del parámetro
    # No regresa nada
    def add_param(self, type):
        self.dir_func[self.actual_scope]['parameters'].append(type)

    # Método que agrega el cuadruplo donde inicia la función
    # No recibe parámetros
    # No regresa nada
    def add_func_counter(self):
        self.dir_func[self.actual_scope]['counter'] = self.get_cont()

    # Método que agrega el cuadruplo donde inicia el main
    # No recibe parámetros
    # No regresa nada
    def add_main_counter(self):
        self.dir_func['main']['counter'] = self.get_cont() + 1

    # Método que verifica si existe una función
    # Recibe el id de la función
    # Regresa el mismo id si lo encontro
    def exists_func(self, id):
        return id in self.dir_func

    # Método que agrega un scope al directorio de funciones
    # No recibe parámetros
    # No regresa nada
    def add_inner_scope(self):
        self.inner_scopes().append({})

    # Método que quita un scope del directorio de funciones
    # No recibe parámetros
    # No regresa nada
    def pop_inner_scope(self):
        scope = self.inner_scopes().pop()

    # Método que regresa los scopes utilizados dentro de una funcion
    # No recibe parámetros
    # Un diccionario con las variables del scope
    def inner_scopes(self):
        return self.dir_func[self.actual_scope]['inner_scope']

    # Método que regresa las variables del scope actual
    # No recibe parámetros
    # No regresa nada
    def vars_table(self):
        return self.dir_func[self.actual_scope]['vars']

    # Método que regresa las variables globales del programa
    # No recibe parámetros
    # Regresa un diccionario con la lista de variables globales
    def global_vars(self):
        return self.dir_func['global']['vars']

    # Método que elimina el directorio de funciones
    # No recibe parámetros
    # Regresa 1 cuando lo elimina
    def erase_dir_func(self):
        return 1
        #self.dir_func = {}

    # Método que mete un id a la pila de Operandos
    # Recibe el id como parámetro
    # No regresa nada
    def add_pilaO(self, id):
        self.pilaO.append(id)

    # Método que mete un operador a la pila de Operadores
    # Recibe el operador como parámetro
    # No regresa nada
    def add_pOper(self, oper):
        self.pOper.append(oper)

    # Método que mete un tipo a la lista de Tipos
    # Recibe el tipo como parametro
    # No regresa nada
    def add_pType(self, type):
        self.pType.append(type)

    # Método que saca el último valor del stack de la pila de Operandos
    # No recibe parámetros
    # Regresa el último valor del stack
    def pop_pilaO(self):
        if (len(self.pilaO) > 0):
            return self.pilaO.pop()

    # Método que saca el último valor del stack de la pila de Operadores
    # No recibe parametros
    # Regresa el último valor del stack
    def pop_pOper(self):
        if (len(self.pOper) > 0):
            return self.pOper.pop()

    # Método que saca el último valor del stack de la pila de Tipos
    # No recibe parametros
    # Regresa el último valor del stack
    def pop_pType(self):
        if (len(self.pType) > 0):
            return self.pType.pop()

    # Método que obtiene el último valor de la pila de Operadores sin sacarlos
    # No recibe parámetros
    # Regresa el valor si la pila no esta vacia si no -1
    def top_pOper(self):
        if (len(self.pOper) > 0):
            return self.pOper[len(self.pOper)-1]
        else:
            return -1

    # Método que obtiene el último valor de la pila de Tipos sin sacarlos
    # No recibe parámetros
    # Regresa el valor si la pila no esta vacia si no -1
    def top_pType(self):
        if (len(self.pType) > 0):
            return self.pType[len(self.pType)-1]
        else:
            return -1

    # Método que obtiene el último valor de la pila de Operandos sin sacarlos
    # No recibe parámetros
    # Regresa el valor si la pila no esta vacia si no -1
    def top_pilaO(self):
        if (len(self.pilaO) > 0):
            return self.pilaO[len(self.pilaO)-1]
        else:
            return None

    # Método que obtiene el primer valor de la pila de Operandos
    # No recibe parámetros
    # Regresa el primer valor del stack
    def get_pilaO(self):
        if (len(self.pilaO) > 0):
            return self.pilaO.pop(0)

    # Método que obtiene el tipo de una variable y lo busca en el dir_func
    # Recibe el id como parámetro
    # Regresa el tipo si lo encuentra si no -1
    def get_type(self, id):
        if (id in self.vars_table()) :
            return self.vars_table()[id]['type']
        elif(id in self.global_vars()):
            return self.global_vars()[id]['type']
        for key in self.inner_scopes():
            if id in key:
                return key[id]['type']
        return -1

    # Método que agrega un cuadruplo a la lista de cuádruplos y aumenta el contador en 1
    # Recibe como parámetro el operador, el operando izquierdo, el operando dereacho y el resultado
    # No regresa nada
    def add_quad(self,operator,leftOperand,rightOperand,result):
        self.quad.append({'operator':operator,'leftOperand':leftOperand,'rightOperand':rightOperand,'result':result})
        self.cont = self.cont + 1

    # Método que obtiene la siguiente direccion temporal usando la clase memory manager
    # Recibe el tipo como parámetro
    # Regresa cual es la siguiente dirección disponible
    def next_temp(self,var_type):
        if var_type == 'int':
            return self.memory_manager.mem_temp().next_int()
        elif var_type == 'float':
            return self.memory_manager.mem_temp().next_float()
        elif var_type == 'boolean':
            return self.memory_manager.mem_temp().next_boolean()

    # Método que obtiene la siguiente dirección local o global usando la clase memory manager
    # Recibe el tipo como parámetro
    # Regresa cual es la siguiente dirección disponible        
    def next_var(self,var_type):
        if(self.actual_scope == "global"):
            if var_type == 'int':
                return self.memory_manager.mem_global.next_int();
            elif var_type == 'float':
                return self.memory_manager.mem_global.next_float();
            elif var_type == 'boolean':
                return self.memory_manager.mem_global.next_boolean();
        else:
            if var_type == 'int':
                return self.memory_manager.mem_local().next_int();
            elif var_type == 'float':
                return self.memory_manager.mem_local().next_float();
            elif var_type == 'boolean':
                return self.memory_manager.mem_local().next_boolean();

    # Método que obtiene la siguiente dirección de constante usando la clase memory manager
    # Recibe el tipo y el valor de la constante como parámetros
    # Regresa cual es la siguiente dirección disponible
    def next_var_cte(self,cte_type,cte):
        if cte_type == 'int':
            return self.memory_manager.mem_const.next_int(cte)
        elif cte_type == 'float':
            return self.memory_manager.mem_const.next_float(cte)
        elif cte_type == 'boolean':
            return self.memory_manager.mem_const.next_boolean(cte)

    # Método que obtiene la siguiente dirección temporal para un ciclo for
    # No recibe parámetros
    # Regresa cual es la siguiente dirección disponible
    def next_var_for(self):
        return self.memory_manager.mem_temp().next_float()

    # Método que obtiene la siguiente dirección global usando la clase memory manager
    # Recibe el tipo y el valor de la constante como parámetros
    # Regresa cual es la siguiente dirección disponible
    def next_func(self,var_type,cte):
        if var_type == 'int':
            return self.memory_manager.mem_global.next_int_func(cte)
        elif var_type == 'float':
            return self.memory_manager.mem_global.next_float_func(cte)
        elif var_type == 'boolean':
            return self.memory_manager.mem_global.next_boolean_func(cte)

    # Método que obtiene la siguiente dirección global usando la clase memory manager
    # No recibe parámetros
    # Regresa cual es la siguiente dirección disponible
    def next_var_draw(self):
        if(self.actual_scope == 'global'):
            return self.memory_manager.mem_global.next_draw()
        else:
            return self.memory_manager.mem_local().next_draw()


    # Método que busca la dirección global de una función
    # Recibe el tipo de la función y su id como parámetros
    # Regresa la dirección virtual de la función
    def find_func(self,func_type,func_id):
        if func_type == 'int':
            for dir_virtual, cte_val in self.memory_manager.mem_global.var_int.items():
                if cte_val == func_id:
                    return dir_virtual
        elif func_type == 'float':
            for dir_virtual, cte_val in self.memory_manager.mem_global.var_float.items():
                if cte_val == func_id:
                    return dir_virtual
        elif func_type == 'boolean':
            for dir_virtual, cte_val in self.memory_manager.mem_global.var_boolean.items():
                if cte_val == func_id:
                    return dir_virtual

    # Método que hace la verificación semántica de los tipos de operaciones
    # Recibe el tipo izquierdo, el tipo derecho y el operador como parámetros
    # Regresa el tipo que debe de tener el resultado, y error si no lo encuentra
    def semantic_check(self,left_type,right_type,operator):
        if left_type in self.sem_cube:
            if right_type in self.sem_cube[left_type]:
                if operator in self.sem_cube[left_type][right_type]:
                    return self.sem_cube[left_type][right_type][operator]
        return 'error'

    # Método que mete un salto a la pila de Saltos
    # Recibe el cuadruplo del salto como parámetro
    # No regresa nada
    def add_pJumps(self, jump):
        self.pJumps.append(jump)

    # Método que saca el último valor del stack de la pila de Saltos
    # No recibe parámetros
    # Regresa el último valor del stack
    def pop_pJumps(self):
        if (len(self.pJumps) > 0):
            return self.pJumps.pop()

    # Método que obtiene el contador en el que van los cuádruplos
    # No recibe parámetros
    # Regresa el cuadruplo en el que va la cuenta
    def get_cont(self):
        return self.cont

    # Método que llena un cuadruplo vacio de saltos
    # Recibe como parámetros la linea y el contador del salto
    def fill(self, line, value):
        self.quad[line]['result'] = value

    # Método que obtiene la dirección virtual de una variable
    # Recibe el id como parámetro
    # Regresa la dirección de memoria en la que se encuentra el id
    def get_dir_virtual(self, id):
        if (id in self.vars_table()) :
            return self.dir_func[self.actual_scope]['vars'][id]['dir_virtual']

        if (len(self.inner_scopes()) >= 1):
            for scope in self.inner_scopes():
                if id in scope:
                    return scope[id]['dir_virtual']

        global_table = self.dir_func['global']['vars']
        if (id in global_table):
            return self.dir_func['global']['vars'][id]['dir_virtual']


    # Método que obtiene las dimensiones de un arreglo o matriz
    # Recibe el id como parámetro
    # Regresa la dimensión total del arreglo o matriz
    def get_dim_array(self,id):
        if (id in self.vars_table()) :
            return self.dir_func[self.actual_scope]['vars'][id]['dim_total']

        if (len(self.inner_scopes()) >= 1):
            for scope in self.inner_scopes():
                if id in scope:
                    return scope[id]['dim_total']

        global_table = self.dir_func['global']['vars']
        if (id in global_table):
            return self.dir_func['global']['vars'][id]['dim_total']

    # Método que obtiene la primera dimensión de un arreglo
    # Recibe el id como parámetro
    # Regresa la dimensión
    def get_dim1_array(self,id):
        if (id in self.vars_table()) :
            return self.dir_func[self.actual_scope]['vars'][id]['dim1']

        if (len(self.inner_scopes()) >= 1):
            for scope in self.inner_scopes():
                if id in scope:
                    return scope[id]['dim1']

        global_table = self.dir_func['global']['vars']
        if (id in global_table):
            return self.dir_func['global']['vars'][id]['dim1']

    # Método que obtiene la segunda dimensión de una matriz
    # Recibe el id como parámetro
    # Regresa la dimensión
    def get_dim2_array(self,id):
        if (id in self.vars_table()) :
            return self.dir_func[self.actual_scope]['vars'][id]['dim2']

        if (len(self.inner_scopes()) >= 1):
            for scope in self.inner_scopes():
                if id in scope:
                    return scope[id]['dim2']

        global_table = self.dir_func['global']['vars']
        if (id in global_table):
            return self.dir_func['global']['vars'][id]['dim2']

    # Método que agrega un arreglo o matriz al directorio de funciones
    # Recibe el tipo, el id, la dirección virtual, y las dimensiones como parámetros
    # No regresa nada
    def add_array(self, type, id, dir_virtual, dim1, dim2):
        if (len(self.inner_scopes()) >= 1):
            inner = self.inner_scopes().pop()
            if(dim2 != -1):
                inner[id] = {'type' : type, 'dir_virtual' : dir_virtual, 'array' : True, 'dim1': dim1, 'dim2' : dim2, 'dim_total' : dim1*dim2}
                if(self.actual_scope == "global"):
                    self.memory_manager.mem_global.array_dim(type,dir_virtual,dim1*dim2)
                else:
                    self.memory_manager.mem_local().array_dim(type,dir_virtual,dim1*dim2)
            else:
                inner[id] = {'type' : type, 'dir_virtual' : dir_virtual, 'array' : True, 'dim1': dim1, 'dim_total' : dim1}
                if(self.actual_scope == "global"):
                    self.memory_manager.mem_global.array_dim(type,dir_virtual,dim1)
                else:
                    self.memory_manager.mem_local().array_dim(type,dir_virtual,dim1)
            self.inner_scopes().append(inner)
        else:
            if(dim2 != -1):
                self.vars_table()[id] = {'type' : type, 'dir_virtual' : dir_virtual, 'array' : True, 'dim1': dim1, 'dim2' : dim2, 'dim_total' : dim1*dim2}
                if(self.actual_scope == "global"):
                    self.memory_manager.mem_global.array_dim(type,dir_virtual,dim1*dim2)
                else:
                    self.memory_manager.mem_local().array_dim(type,dir_virtual,dim1*dim2)
            else:
                self.vars_table()[id] = {'type' : type, 'dir_virtual' : dir_virtual, 'array' : True, 'dim1': dim1, 'dim_total' : dim1}
                if(self.actual_scope == "global"):
                    self.memory_manager.mem_global.array_dim(type,dir_virtual,dim1)
                else:
                    self.memory_manager.mem_local().array_dim(type,dir_virtual,dim1)
        self.add_total_var()

    # Método que resetea la memoria al término de una función para variables locales y temporales
    # No recibe parámetros
    # No regresa nada
    def reset_memory(self):
        self.memory_manager.reset_memory()
