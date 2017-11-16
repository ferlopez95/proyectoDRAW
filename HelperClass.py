from SemanticCube import SemanticCube
from MemoryManager import MemoryManager

class HelperClass(object):

    def __init__(self, actual_scope):
        self.actual_scope = actual_scope
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
        self.vgi = 4000
        self.vgf = 6000
        self.vgb = 8000
        self.vli = 10000
        self.vlf = 12000
        self.vlb = 14000
        self.tgi = 16000
        self.tgf = 20000
        self.tgb = 24000
        self.ctei= 28000
        self.ctef= 32000
        self.cteb= 36000
        
        

        self.memoria = {'Vgi':{},'Vgf':{},'Vgb':{},
                        'Vli':{},'Vlf':{},'Vlb':{},
                        'Tgi':{},'Tgf':{},'Tgb':{},
                        'Ctei':{},'Ctef':{},'Cteb':{36000:'true',36001:'false'}}

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
        self.vgi = 4000
        self.vgf = 6000
        self.vgb = 8000
        self.vli = 10000
        self.vlf = 12000
        self.vlb = 14000
        self.tgi = 16000
        self.tgf = 20000
        self.tgb = 24000
        self.ctei= 28000
        self.ctef= 32000
        self.cteb= 36000
        self.add_func('void', 'global')
        

        self.memoria = {'Vgi':{},'Vgf':{},'Vgb':{},
                        'Vli':{},'Vlf':{},'Vlb':{},
                        'Tgi':{},'Tgf':{},'Tgb':{},
                        'Ctei':{},'Ctef':{},'Cteb':{36000:'true',36001:'false'}}


    def exists_in_scope(self, id):
        if (len(self.inner_scopes()) >= 1):
            if (id in self.vars_table()) :
                return 1
            for key in self.inner_scopes():
                if id in key:
                    return 1
        else:
            if (id in self.vars_table()) :
                return 1

    def add_var(self, type, id, dir_virtual):
        if (len(self.inner_scopes()) >= 1):
            inner = self.inner_scopes().pop()
            inner[id] = {'type' : type, 'dir_virtual' : dir_virtual}
            self.inner_scopes().append(inner)
        else:
            self.vars_table()[id] = {'type' : type, 'dir_virtual' : dir_virtual}
        self.add_total_var()

    def add_total_var(self):
        self.dir_func[self.actual_scope]['total_vars'] += 1

    def add_func(self, type, id):
        self.dir_func[id] = {'type' : type, 'parameters' : [], 'total_vars' : 0, 'vars' : {}, 'inner_scope' : [], 'counter' : 0}

    def add_param(self, type):
        self.dir_func[self.actual_scope]['parameters'].append(type)

    def add_func_counter(self):
        self.dir_func[self.actual_scope]['counter'] = self.get_cont()

    def add_main_counter(self):
        self.dir_func['main']['counter'] = self.get_cont() + 1


    def exists_func(self, id):
        return id in self.dir_func

    def add_inner_scope(self):
        self.inner_scopes().append({})

    def pop_inner_scope(self):
        self.inner_scopes().pop()

    def inner_scopes(self):
        return self.dir_func[self.actual_scope]['inner_scope']

    def vars_table(self):
        return self.dir_func[self.actual_scope]['vars']

    def global_vars(self):
        return self.dir_func['global']['vars']

    def erase_dir_func(self):
        return 1
        #self.dir_func = {}

    def add_pilaO(self, id):
        self.pilaO.append(id)

    def add_pOper(self, oper):
        self.pOper.append(oper)

    def add_pType(self, type):
        self.pType.append(type)

    def pop_pilaO(self):
        if (len(self.pilaO) > 0):
            return self.pilaO.pop()

    def pop_pOper(self):
        if (len(self.pOper) > 0):
            return self.pOper.pop()

    def pop_pType(self):
        if (len(self.pType) > 0):
            return self.pType.pop()

    def top_pOper(self):
        if (len(self.pOper) > 0):
            return self.pOper[len(self.pOper)-1]
        else:
            return -1

    def top_pType(self):
        if (len(self.pType) > 0):
            return self.pType[len(self.pType)-1]
        else:
            return -1

    def top_pilaO(self):
        if (len(self.pilaO) > 0):
            return self.pilaO[len(self.pilaO)-1]
        else:
            return None

    def get_pilaO(self):
        if (len(self.pilaO) > 0):
            return self.pilaO.pop(0)

    def get_type(self, id):
        if (id in self.vars_table()) :
            return self.vars_table()[id]['type']
        elif(id in self.global_vars()):
            return self.global_vars()[id]['type']
        for key in self.inner_scopes():
            if id in key:
                return key[id]['type']
        return -1

    def add_quad(self,operator,leftOperand,rightOperand,result):
        self.quad.append({'operator':operator,'leftOperand':leftOperand,'rightOperand':rightOperand,'result':result})
        self.cont = self.cont + 1

    def next(self):
        self.temp = self.temp + 1
        return self.temp

    def next_temp(self,var_type):
        if var_type == 'int':
            return self.memory_manager.mem_temp.next_int()
        elif var_type == 'float':
            return self.memory_manager.mem_temp.next_float()
        elif var_type == 'boolean':
            return self.memory_manager.mem_temp.next_boolean()
            
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
                return self.memory_manager.mem_local.next_int();
            elif var_type == 'float':
                return self.memory_manager.mem_local.next_float();
            elif var_type == 'boolean':
                return self.memory_manager.mem_local.next_boolean();

    def next_var_cte(self,cte_type,cte):
        if cte_type == 'int':
            return self.memory_manager.mem_const.next_int(cte);
        elif cte_type == 'float':
            return self.memory_manager.mem_const.next_float(cte);
        elif cte_type == 'boolean':
            return self.memory_manager.mem_const.next_boolean(cte);

    def next_var_for(self):
        return self.memory_manager.mem_temp.next_float()

    def next_func(self,var_type,cte):
        if var_type == 'int':
            for dir_virtual, cte_val in self.memoria['Vgi'].items():
                if cte_val == cte:
                    return dir_virtual
            var_avail = self.vgi
            self.vgi = self.vgi + 1
            self.memoria['Vgi'][var_avail] = cte
            return var_avail
        elif var_type == 'float':
            for dir_virtual, cte_val in self.memoria['Vgf'].items():
                if cte_val == cte:
                    return dir_virtual
            var_avail = self.vgf
            self.vgf = self.vgf + 1
            self.memoria['Vgf'][var_avail] = cte
            return var_avail
        elif var_type == 'boolean':
            for dir_virtual, cte_val in self.memoria['Vgb'].items():
                if cte_val == cte:
                    return dir_virtual
            var_avail = self.vgb
            self.vgb = self.vgb + 1
            self.memoria['Vgb'][var_avail] = cte
            return var_avail

    def find_func(self,func_type,func_id):
        if func_type == 'int':
            for dir_virtual, cte_val in self.memoria['Vgi'].items():
                if cte_val == func_id:
                    return dir_virtual
        elif func_type == 'float':
            for dir_virtual, cte_val in self.memoria['Vgf'].items():
                if cte_val == func_id:
                    return dir_virtual
        elif func_type == 'boolean':
            for dir_virtual, cte_val in self.memoria['Vgb'].items():
                if cte_val == func_id:
                    return dir_virtual

    def semantic_check(self,left_type,right_type,operator):
        if left_type in self.sem_cube:
            if right_type in self.sem_cube[left_type]:
                if operator in self.sem_cube[left_type][right_type]:
                    return self.sem_cube[left_type][right_type][operator]
        return 'error'

    def add_pJumps(self, jump):
        self.pJumps.append(jump)

    def pop_pJumps(self):
        if (len(self.pJumps) > 0):
            return self.pJumps.pop()

    def get_cont(self):
        return self.cont

    def fill(self, line, value):
        self.quad[line]['result'] = value

    def erase_temps(self):
        self.vli = 10000
        self.vlf = 12000
        self.vlb = 14000
        self.tgi = 16000
        self.tgf = 20000
        self.tgb = 24000

    def get_dir_virtual(self, id):
        return self.dir_func[self.actual_scope]['vars'][id]['dir_virtual']

    def get_dim_array(self,id):
        return self.dir_func[self.actual_scope]['vars'][id]['dim_total']

    def get_dim1_array(self,id):
        return self.dir_func[self.actual_scope]['vars'][id]['dim1']

    def get_dim2_array(self,id):
        return self.dir_func[self.actual_scope]['vars'][id]['dim2']
    
    def add_array(self, type, id, dir_virtual, dim1, dim2):
        if (len(self.inner_scopes()) >= 1):
            inner = self.inner_scopes().pop()
            if(dim2 != -1):
                inner[id] = {'type' : type, 'dir_virtual' : dir_virtual, 'array' : True, 'dim1': dim1, 'dim2' : dim2, 'dim_total' : dim1*dim2}
                if(self.actual_scope == "global"):
                    self.memory_manager.mem_global.array_dim(type,dir_virtual,dim1*dim2)
                else:
                    self.memory_manager.mem_local.array_dim(type,dir_virtual,dim1*dim2)
            else:
                inner[id] = {'type' : type, 'dir_virtual' : dir_virtual, 'array' : True, 'dim1': dim1, 'dim_total' : dim1}
                if(self.actual_scope == "global"):
                    self.memory_manager.mem_global.array_dim(type,dir_virtual,dim1)
                else:
                    self.memory_manager.mem_local.array_dim(type,dir_virtual,dim1)
            self.inner_scopes().append(inner)
        else:
            if(dim2 != -1):
                self.vars_table()[id] = {'type' : type, 'dir_virtual' : dir_virtual, 'array' : True, 'dim1': dim1, 'dim2' : dim2, 'dim_total' : dim1*dim2}
                if(self.actual_scope == "global"):
                    self.memory_manager.mem_global.array_dim(type,dir_virtual,dim1*dim2)
                else:
                    self.memory_manager.mem_local.array_dim(type,dir_virtual,dim1*dim2)
            else:
                self.vars_table()[id] = {'type' : type, 'dir_virtual' : dir_virtual, 'array' : True, 'dim1': dim1, 'dim_total' : dim1}
                if(self.actual_scope == "global"):
                    self.memory_manager.mem_global.array_dim(type,dir_virtual,dim1)
                else:
                    self.memory_manager.mem_local.array_dim(type,dir_virtual,dim1)
        self.add_total_var()
