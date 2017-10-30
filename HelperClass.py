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

        self.sem_cube = {'int' : {'int' : {'+': 'int',
                                            '-': 'int',
                                            '/': 'float',
                                            '*': 'int',
                                            '%': 'int',
                                            '<': 'boolean',
                                            '>': 'boolean',
                                            '<=': 'boolean',
                                            '>=': 'boolean',
                                            '!=': 'boolean',
                                            '==': 'boolean',
                                            '=': 'int'},
                                  'float': {'+': 'float',
                                            '-': 'float',
                                            '/': 'float',
                                            '*': 'float',
                                            '%': 'float',
                                            '<': 'boolean',
                                            '>': 'boolean',
                                            '<=': 'boolean',
                                            '>=': 'boolean',
                                            '!=': 'boolean',
                                            '==': 'boolean',
                                            '=': 'int'}},
                         'float' : {'int' : {'+': 'float',
                                            '-': 'float',
                                            '/': 'float',
                                            '*': 'float',
                                            '%': 'float',
                                            '<': 'boolean',
                                            '>': 'boolean',
                                            '<=': 'boolean',
                                            '>=': 'boolean',
                                            '!=': 'boolean',
                                            '==': 'boolean',
                                             '=': 'float'},
                                  'float': {'+': 'float',
                                            '-': 'float',
                                            '/': 'float',
                                            '*': 'float',
                                            '%': 'float',
                                            '<': 'boolean',
                                            '>': 'boolean',
                                            '<=': 'boolean',
                                            '>=': 'boolean',
                                            '!=': 'boolean',
                                            '==': 'boolean',
                                            '=': 'float'}},
                         'boolean' : {'boolean' : {'&&' : 'boolean',
                                             '||' : 'boolean',
                                             '=' : 'boolean'}}}

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

    def add_var(self, type, id):
        if (len(self.inner_scopes()) >= 1):
            inner = self.inner_scopes().pop()
            inner[id] = {'type' : type}
            self.inner_scopes().append(inner)
        else:
            self.vars_table()[id] = {'type' : type}

    def add_func(self, type, id):
        self.dir_func[id] = {'type' : type, 'vars' : {}, 'inner_scope' : []}

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
