class HelperClass(object):

    def __init__(self, actual_scope):
        self.actual_scope = actual_scope
        self.dir_func = {}

    def exists_in_scope(self, id):
        if (len(self.dir_func[self.actual_scope]['inner_scope']) >= 1):
            if (id in self.dir_func[self.actual_scope]['vars']) or (id in self.dir_func['global']['vars']) :
                return 1
            for key in self.dir_func[self.actual_scope]['inner_scope']:
                if id in key:
                    return 1
        else:
            if (id in self.dir_func[self.actual_scope]['vars']) or (id in self.dir_func['global']['vars']) :
                return 1

    def add_var(self, type, id):
        if (len(self.dir_func[self.actual_scope]['inner_scope']) >= 1):
            inner = self.dir_func[self.actual_scope]['inner_scope'].pop()
            inner[id] = {'type' : type}
            self.dir_func[self.actual_scope]['inner_scope'].append(inner)
        else:
            self.dir_func[self.actual_scope]['vars'][id] = {'type' : type}

    def add_func(self, type, id):
        self.dir_func[id] = {'type' : type, 'vars' : {}, 'inner_scope' : []}

    def exists_func(self, id):
        return id in self.dir_func

    def add_inner_scope(self):
        self.dir_func[self.actual_scope]['inner_scope'].append({})

    def pop_inner_scope(self):
        self.dir_func[self.actual_scope]['inner_scope'].pop()
