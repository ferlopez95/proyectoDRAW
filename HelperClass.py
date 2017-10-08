class HelperClass(object):

    def __init__(self, actual_scope):
        self.actual_scope = actual_scope
        self.dir_func = {}

    def exists_in_scope(self, id):
        if (len(self.inner_scopes()) >= 1):
            if (id in self.vars_table()) or (id in self.global_vars()) :
                return 1
            for key in self.inner_scopes():
                if id in key:
                    return 1
        else:
            if (id in self.vars_table()) or (id in self.global_vars()) :
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