from MemoryManager import MemoryManager

class VirtualMachine:

    def __init__(self, quadruples, mem):
        self.quadruples = quadruples
        self.memory = MemoryManager()
        self.memory.copy(mem)
        i = 1
        for quad in quadruples :
            operator = quad['operator']
            leftOperand = quad['leftOperand']
            rightOperand = quad['rightOperand']
            result = quad['result']

            ## Obtener valores para los operadores que usan numeros
            if (operator in ['+','-','*','/','%','<','>','<=','>=']):
                value1 = float(self.memory.get_var(leftOperand))
                value2 = float(self.memory.get_var(rightOperand))

            if (operator == '='):
                value = self.memory.get_var(leftOperand)
                self.memory.add_var(result, value)
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
                value2 = self.memory.get_var(leftOperand)
                total = value1 and value2
                self.memory.add_var(result, total)

            print (str(i) + ": " + str(quad))
            i = i + 1

