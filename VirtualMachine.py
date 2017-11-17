from MemoryManager import MemoryManager

class VirtualMachine:

    def __init__(self, quadruples, mem):
        self.quadruples = quadruples
        self.memory = MemoryManager()
        self.memory.copy(mem)
        self.stack = []
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
                continue
            elif (operator == "ENDPROC"):
                self.memory.erase_context()
                i = self.stack.pop()
                print(i)
                continue
            elif (operator == "GOSUB"):
                self.memory.add_context()
                self.stack.append(i + 1)
                i = self.memory.get_var(leftOperand)
                print(i)
                continue
            i+=1
