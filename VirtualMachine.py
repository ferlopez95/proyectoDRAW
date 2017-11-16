from MemoryManager import MemoryManager

class VirtualMachine:

    def __init__(self, quadruples, mem):
        self.quadruples = quadruples
        self.memory = MemoryManager()
        self.memory.copy(mem)
        i = 0
        while i < len(quadruples) :
            quad = quadruples[i]
            operator = quad['operator']
            leftOperand = quad['leftOperand']
            rightOperand = quad['rightOperand']
            result = quad['result']

            if("(" in str(leftOperand)):
                new_dir = int(leftOperand[1:-1])
                print("funciona " + str(new_dir))
                leftOperand = self.memory.get_var(new_dir)

            if("(" in str(rightOperand)):
                print("funciona ")
                new_dir = int(rightOperand[1:-1])
                rightOperand = self.memory.get_var(new_dir)

            if("(" in str(result)):
                print("funciona")
                new_dir = int(result[1:-1])
                result = self.memory.get_var(new_dir)

            ## Obtener valores para los operadores que usan numeros
            if (operator in ['+','-','*','/','%','<','>','<=','>=']):
                value1 = float(self.memory.get_var(leftOperand))
                value2 = float(self.memory.get_var(rightOperand))
                print(value1)
                print(value2)


            if (operator == '='):
                print(leftOperand)
                value = self.memory.get_var(leftOperand)
                self.memory.add_var(result, value)
            elif (operator == 'PRINT'):
                value = self.memory.get_var(leftOperand)
                print(value)
            elif (operator == '+'):
                print(result)
                total = value1 + value2
                self.memory.add_var(result, total)
            elif (operator == '-'):
                total = value1 - value2
                self.memory.add_var(result, total)
            elif (operator == '*'):
                total = value1 * value2
                print("total = " + str(total))
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
            i+=1
