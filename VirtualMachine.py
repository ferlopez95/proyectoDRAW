from MemoryManager import MemoryManager

class VirtualMachine:

    def __init__(self, quadruples, mem, dir_func):
        self.quadruples = quadruples
        self.memory = MemoryManager()
        self.memory.copy(mem)
        self.stack = []
        self.dir_func = dir_func
        self.scope = []
        i = 0
        while i < len(quadruples) :
            quad = quadruples[i]
            operator = quad['operator']
            leftOperand = quad['leftOperand']
            rightOperand = quad['rightOperand']
            result = quad['result']

            if("(" in str(leftOperand)):
                new_dir = int(leftOperand[1:-1])
                leftOperand = self.memory.get_var(new_dir)

            if("(" in str(rightOperand)):
                new_dir = int(rightOperand[1:-1])
                rightOperand = self.memory.get_var(new_dir)

            if("(" in str(result)):
                new_dir = int(result[1:-1])
                result = self.memory.get_var(new_dir)

            try:
                if(leftOperand != -1):
                    value1 = self.memory.get_var(leftOperand)
                if(rightOperand != -1):
                    value2 = self.memory.get_var(rightOperand)
            except:
                print("Null pointer exception")
                break
            
            ## Obtener valores para los operadores que usan numeros
            if (operator in ['+','-','*','/','%','<','>','<=','>=']):
                value1 = float(self.memory.get_var(leftOperand))
                value2 = float(self.memory.get_var(rightOperand))

            if (operator == '='):
                value = self.memory.get_var(leftOperand)
                self.memory.add_var(result, value)
            elif (operator == 'PRINT'):
                value = self.memory.get_var(leftOperand)
                print(value)
            elif (operator == '+'):
                total = value1 + value2
                self.memory.add_var(result, total)
            elif (operator == '-'):
                total = value1 - value2
                self.memory.add_var(result, total)
            elif (operator == '*'):
                total = value1 * value2
                self.memory.add_var(result, total)
            elif (operator == '/'):
                total = value1 / value2
                self.memory.add_var(result, total)
            elif (operator == '<'):
                total = value1 < value2
                self.memory.add_var(result, total)
            elif (operator == '<='):
                total = value1 <= value2
                self.memory.add_var(result, total)
            elif (operator == '>'):
                total = value1 > value2
                self.memory.add_var(result, total)
            elif (operator == '>='):
                total = value1 > value2
                self.memory.add_var(result, total)
            elif (operator == '&&'):
                value1 = self.memory.get_var(leftOperand)
                value2 = self.memory.get_var(rightOperand)
                total = value1 and value2
                self.memory.add_var(result, total)
            elif (operator == '||'):
                value1 = self.memory.get_var(leftOperand)
                value2 = self.memory.get_var(rightOperand)
                total = value1 or value2
                self.memory.add_var(result, total)
            elif (operator == '=='):
                value1 = self.memory.get_var(leftOperand)
                value2 = self.memory.get_var(rightOperand)
                total = value1 == value2
                self.memory.add_var(result, total)
            elif (operator == '%'):
                value1 = self.memory.get_var(leftOperand)
                value2 = self.memory.get_var(rightOperand)
                total = value1 % value2
                self.memory.add_var(result, total)
            elif (operator == "GOTO"):
                i = result
                continue
            elif (operator == "GOTOF"):
                value = self.memory.get_var(leftOperand)
                if (value == False):
                    i = result
                    continue
            elif (operator == "VERIFICA"):
                value = self.memory.get_var(leftOperand)
                lim_sup = self.memory.get_var(result)
                if ( value < 0 or value >= lim_sup):
                    print("Index out of bound")
                    break
            elif (operator == "ERA"):
                self.memory.add_context()
                self.memory.read_last_memory(True)
            elif (operator == "PARAM"):
                mem = self.memory.get_type(leftOperand)
                value = self.memory.get_var(leftOperand)
                type = mem.get_type(leftOperand)
                self.memory.read_last_memory(False)
                next_dir = 0
                if(type == 'int'):
                    next_dir = self.memory.mem_local().next_int()
                    self.memory.mem_local().add_var(next_dir,value)
                elif(type == 'float'):
                    next_dir = self.memory.mem_local().next_float()
                    self.memory.mem_local().add_var(next_dir,value)
                elif(type == 'boolean'):
                    next_dir = self.memory.mem_local().next_boolean()
                    self.memory.mem_local().add_var(next_dir,value)
                self.memory.read_last_memory(True)
            elif (operator == "ENDPROC"):
                self.memory.erase_context()
                i = self.stack.pop()
                continue
            elif (operator == "GOSUB"):
                self.stack.append(i + 1)
                i = self.memory.get_var(leftOperand)
                self.memory.read_last_memory(False)
                for key, value in self.dir_func.items():
                    if(value['counter'] == i):
                        self.scope.append(key)
                continue
            elif (operator == "RETURN"):
                last_scope = self.scope.pop()
                result = self.memory.get_var(leftOperand)
                dir = self.dir_func[last_scope]['dir']
                self.memory.mem_global.add_var(dir, result)
            i+=1
