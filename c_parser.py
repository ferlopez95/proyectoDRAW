# encoding=utf8  
import sys  

#reload(sys)  
#sys.setdefaultencoding('utf8')

import c_lexer
import ply.yacc as yacc
from HelperClass import HelperClass

tokens = c_lexer.tokens

drawCompiler = HelperClass('global')
drawCompiler.add_func('void', 'global')


def p_programa(p):
    '''programa : globales init funciones programa_end
    | init funciones programa_end'''

def p_init(p):
    ''' init : empty '''
    drawCompiler.add_quad("GOTO", -1, -1,-1)
    drawCompiler.add_pJumps(drawCompiler.get_cont()-1)

def p_programa_end(p):
    ''' programa_end : empty '''
    #drawCompiler.erase_dir_func()

def p_funciones(p):
    '''funciones : funciones_2 main'''
    pass

def p_funciones_2(p):
    '''funciones_2 : funcion funciones_2
    | empty'''
    pass

def p_globales(p):
    '''globales : global_1 vars globales_2'''
    pass

def p_globales_2(p):
    ''' globales_2 : global_1 vars globales_2
    | empty '''
    pass

def p_global_1(p):
    ''' global_1 : GLOBAL '''
    pass

def p_bloque(p):
    '''bloque : estatuto bloque
    | empty'''
    pass

def p_data_type(p):
    '''data_type : INT
    | FLOAT
    | BOOLEAN'''
    p[0] = p[1]

def p_data_type_func(p):
    '''data_type_func : INT
    | FLOAT
    | BOOLEAN'''
    p[0] = p[1]

def p_main(p):
    '''main : main_1 bloque END'''
    pass

def p_main_1(p):
    ''' main_1 : MAIN LPAREN RPAREN'''
    drawCompiler.actual_scope = p[1]
    drawCompiler.add_func("void", p[1])
    drawCompiler.add_main_counter()
    drawCompiler.fill(drawCompiler.pop_pJumps(), drawCompiler.get_cont())

def p_estatuto(p):
    '''estatuto : asignacion
    | condicion
    | ciclo
    | accion
    | vars
    | llamada SEMICOLON
    | print'''
    pass

def p_print(p):
    ''' print : PRINT LPAREN super_exp RPAREN SEMICOLON '''
    op = drawCompiler.pop_pilaO()
    op_type = drawCompiler.pop_pType()
    drawCompiler.add_quad("PRINT", op, -1, -1)

def p_asignacion(p):
    '''asignacion : asignacion_id asignacion_2 SEMICOLON'''
    pass

def p_asignacion_id(p):
    '''asignacion_id : ID asignacion_array'''
    if not drawCompiler.exists_in_scope(p[1]) : 
        message = "Error: The variable " + p[1] + " is not defined (Line " + str(p.lexer.lineno) + ")"
        print(message)
        sys.exit()
    else:
        dir_virtual = drawCompiler.get_dir_virtual(p[1])
        if(p[2] == 1):
            obj = drawCompiler.pop_pilaO()
            dim1 = drawCompiler.next_var_cte('int',drawCompiler.get_dim1_array(p[1]))
            cero = drawCompiler.next_var_cte('int',0)
            drawCompiler.add_quad("VERIFICA",obj,cero,dim1)
            next_temp = drawCompiler.next_temp('int')
            dir_virtual_cte = drawCompiler.next_var_cte('int',dir_virtual)
            drawCompiler.add_quad('+',obj,dir_virtual_cte, next_temp)
            drawCompiler.add_pilaO("("+str(next_temp)+")")
            drawCompiler.add_pType(drawCompiler.get_type(p[1]))
        elif(p[2] == 2):
            obj2 = drawCompiler.pop_pilaO()
            obj = drawCompiler.pop_pilaO()
            dim1 = drawCompiler.next_var_cte('int',drawCompiler.get_dim1_array(p[1]))
            dim2 = drawCompiler.next_var_cte('int',drawCompiler.get_dim2_array(p[1]))
            cero = drawCompiler.next_var_cte('int',0)
            next_temp = drawCompiler.next_temp('int')
            drawCompiler.add_quad("VERIFICA",obj,cero,dim1)
            drawCompiler.add_quad('*',obj,dim2, next_temp)
            drawCompiler.add_quad("VERIFICA",obj2,cero,dim2)
            next_temp2 = drawCompiler.next_temp('int')
            drawCompiler.add_quad('+',obj2,next_temp, next_temp2)
            next_temp3 = drawCompiler.next_temp('int')
            dir_virtual_cte = drawCompiler.next_var_cte('int',dir_virtual)
            drawCompiler.add_quad('+',next_temp2,dir_virtual_cte,next_temp3)     
            drawCompiler.add_pilaO("("+str(next_temp3)+")")
            drawCompiler.add_pType(drawCompiler.get_type(p[1]))
        else:
            drawCompiler.add_pilaO(dir_virtual)
            drawCompiler.add_pType(drawCompiler.get_type(p[1]))

def p_asignacion_2(p):
    '''asignacion_2 : asignacion_equal super_exp'''
    if(len(p) == 3 and drawCompiler.top_pOper() == '='):
        rightOperand = drawCompiler.pop_pilaO()
        right_type = drawCompiler.pop_pType()
        leftOperand = drawCompiler.pop_pilaO()
        left_type = drawCompiler.pop_pType()
        operator = drawCompiler.pop_pOper()
        result_type = drawCompiler.semantic_check(left_type,right_type,operator)
        if(result_type != 'error'):
            drawCompiler.add_quad(operator,rightOperand,-1,leftOperand)
        else:
            drawCompiler.erase_dir_func()
            message = "Error: Type Mismatch in line " + str(p.lexer.lineno)
            print(message)
            sys.exit()

def p_asignacion_array(p):
    '''asignacion_array : LBRACKET super_exp asignacion_3
    | empty'''
    if(len(p) == 4):
        p[0] = 1 + p[3]
    else:
        p[0] = 0

def p_asignacion_equal(p):
    '''asignacion_equal : EQUAL'''
    drawCompiler.add_pOper(p[1])
    
def p_asignacion_3(p):
    '''asignacion_3 : RBRACKET
    | COMMA super_exp RBRACKET'''
    if(len(p) == 4):
        p[0] = 1
    else:
        p[0] = 0

def p_vars(p):
    '''vars : DRAW ID EQUAL DRAW LPAREN RPAREN SEMICOLON
    | vars_id vars2
    | vars_aux'''
    if len(p) >= 4:
        if drawCompiler.exists_in_scope(p[2]):
            message = "Error: The variable " + p[2] + " is already defined (Line " + str(p.lexer.lineno) + ")"
            print(message)
            sys.exit()
        else:
            next_dir = drawCompiler.next_var_draw()
            print(next_dir)
            drawCompiler.add_var(p[1], p[2], next_dir)
            drawCompiler.add_quad("NEWDRAW",-1,-1,next_dir)

def p_vars_id(p):
    '''vars_id : data_type ID'''
    if drawCompiler.exists_in_scope(p[2]):
        message = "Error: The variable " + p[2] + " is already defined (Line " + str(p.lexer.lineno) + ")"
        print(message)
        sys.exit()
    else:
        dir_virtual = drawCompiler.next_var(p[1])
        drawCompiler.add_var(p[1], p[2], dir_virtual)
        drawCompiler.add_pilaO(dir_virtual)
        drawCompiler.add_pType(p[1])

def p_vars_aux(p):
    ''' vars_aux : array vars3 '''
    if(p[2] == 1):
        dir_virtual_arr = drawCompiler.get_dir_virtual(p[1])
        dim_array = drawCompiler.get_dim_array(p[1])
        cont = 0
        while(drawCompiler.top_pilaO() != None and cont < dim_array):
            obj = drawCompiler.get_pilaO()
            drawCompiler.add_quad("=",obj,-1,dir_virtual_arr)
            dir_virtual_arr = dir_virtual_arr + 1
            cont = cont + 1

def p_array(p):
    ''' array : ARRAY LESS data_type COMMA CTE_I array_2 GREATER ID'''
    if drawCompiler.exists_in_scope(p[8]):
        message = "Error: The variable " + p[8] + " is already defined (Line " + str(p.lexer.lineno) + ")"
        print(message)
        sys.exit()
    else:
        if(p[5] >= 1):
            if(p[6] == "vacio"):
                dir_virtual = drawCompiler.next_var(p[3])
                drawCompiler.add_array(p[3], p[8], dir_virtual, p[5], -1)
            elif(p[6] >= 1):
                dir_virtual = drawCompiler.next_var(p[3])
                drawCompiler.add_array(p[3], p[8], dir_virtual, p[5], p[6])
            else:
                message = "Error: The dimesion " + p[8] + " can not be negative (Line " + str(p.lexer.lineno) + ")"
                print(message)
                sys.exit()
            p[0] = p[8]
        else:
            message = "Error: The dimension " + p[8] + " can not be negative (Line " + str(p.lexer.lineno) + ")"
            print(message)
            sys.exit()

def p_array_2(p) :
    ''' array_2 : COMMA CTE_I
    | empty '''
    if(len(p) == 3):
        p[0] = p[2]
    else:
        p[0] = "vacio"

def p_vars_2(p):
    '''vars2 : asignacion_equal super_exp SEMICOLON
    | SEMICOLON'''
    if(len(p) == 4 and drawCompiler.top_pOper() == '='):
        rightOperand = drawCompiler.pop_pilaO()
        right_type = drawCompiler.pop_pType()
        leftOperand = drawCompiler.pop_pilaO()
        left_type = drawCompiler.pop_pType()
        operator = drawCompiler.pop_pOper()
        result_type = drawCompiler.semantic_check(left_type,right_type,operator)
        if(result_type != 'error'):
            drawCompiler.add_quad(operator,rightOperand,-1,leftOperand)
        else:
            drawCompiler.erase_dir_func()
            message = "Error: Type Mismatch in line " + str(p.lexer.lineno)
            print(message)
            sys.exit()
    else:
        drawCompiler.pop_pilaO()
        drawCompiler.pop_pType()

def p_vars_3(p):
    '''vars3 : EQUAL def_array SEMICOLON
    | SEMICOLON'''
    if(len(p) == 4):
        p[0] = 1
    else:
        p[0] = 0

def p_llamada(p):
    '''llamada : llamada_id llamada_2'''
    counter = drawCompiler.next_var_cte('int',drawCompiler.dir_func[p[1]]['counter'])
    drawCompiler.add_quad("GOSUB",counter,-1,-1)
    drawCompiler.param_k = 0
    if(drawCompiler.dir_func[p[1]]['type'] != "void"):
        type = drawCompiler.dir_func[p[1]]['type']
        next_temp = drawCompiler.next_temp(type)
        drawCompiler.add_pType(type)
        drawCompiler.add_pilaO(next_temp)
        dir = drawCompiler.find_func(drawCompiler.dir_func[p[1]]['type'],p[1])
        drawCompiler.add_quad('=',dir,-1,next_temp)


def p_llamada_id(p):
    ''' llamada_id : ID LPAREN'''
    if not drawCompiler.exists_func(p[1]):
        message = "Error: The function " + p[1] + " is not defined (Line " + str(p.lexer.lineno) + ")"
        print(message)
        sys.exit()
    else:
        drawCompiler.add_pOper("(")
        drawCompiler.add_quad("ERA",-1,-1,-1)
        drawCompiler.param_k = 0
        drawCompiler.params = drawCompiler.dir_func[p[1]]['parameters']
        p[0] = p[1]


def p_llamada_2(p):
    '''llamada_2 : llamada_exp llamada_rparen
    | llamada_rparen'''
    pass

def p_llamada_rparen(p):
    '''llamada_rparen : RPAREN'''
    if(drawCompiler.param_k != len(drawCompiler.params)):
        message = "Error: Wrong number of parameters (Line " + str(p.lexer.lineno) + ")"
        print(message)
        sys.exit()
    drawCompiler.pop_pOper()

def p_llamada_exp(p):
    '''llamada_exp : llamada_super_exp llamada_exp2'''
    pass

def p_llamada_super_exp(p):
    '''llamada_super_exp : super_exp'''
    argument = drawCompiler.pop_pilaO()
    argumentType = drawCompiler.pop_pType()

    if(len(drawCompiler.params)>drawCompiler.param_k):
        if(argumentType == drawCompiler.params[drawCompiler.param_k]):
            drawCompiler.add_quad("PARAM",argument,-1,"param" + str(drawCompiler.param_k))
            drawCompiler.param_k = drawCompiler.param_k + 1;
        else:
            message = "Error: Type Mismatch in Parameters (Line " + str(p.lexer.lineno) + ")"
            print(message)
            sys.exit()
    else:
        message = "Error: Wrong number of parameters (Line " + str(p.lexer.lineno) + ")"
        print(message)
        sys.exit()

def p_llamada_exp_2(p):
    '''llamada_exp2 : COMMA llamada_exp
    | empty'''
    pass

def p_def_array(p):
    '''def_array : LBRACKET def_array_2 '''
    pass

def p_def_array_2(p):
    '''def_array_2 : def_array_cte RBRACKET
    | RBRACKET'''
    pass

def p_def_array_cte(p):
    '''def_array_cte : super_exp def_array_cte_2'''
    pass

def p_def_array_cte_2(p):
    '''def_array_cte_2 : COMMA def_array_cte
    | empty'''
    pass

def p_super_exp(p):
    '''super_exp : expresion super_exp_2'''
    pass

def p_super_exp_2(p):
    '''super_exp_2 :  logicop super_exp
    | empty'''

def p_expresion(p):
    '''expresion : exp expresion_2'''
    if(drawCompiler.top_pOper() == '&&' or drawCompiler.top_pOper() == '||'):
        rightOperand = drawCompiler.pop_pilaO()
        right_type = drawCompiler.pop_pType()
        leftOperand = drawCompiler.pop_pilaO()
        left_type = drawCompiler.pop_pType()
        operator = drawCompiler.pop_pOper()
        result_type = drawCompiler.semantic_check(left_type,right_type,operator)
        if(result_type != 'error'):
            result = drawCompiler.next_temp(result_type)
            drawCompiler.add_quad(operator,leftOperand,rightOperand,result)
            drawCompiler.add_pilaO(result)
            drawCompiler.add_pType(result_type)
        else:
            drawCompiler.erase_dir_func()
            message = "Error: Type Mismatch in line " + str(p.lexer.lineno)
            print(message)
            sys.exit()

def p_expresion_2(p):
    '''expresion_2 : relop exp
    | empty'''
    pass

def p_relop(p):
    '''relop : GREATER
    | GREATEREQUAL
    | LESS
    | LESSEQUAL
    | DEQUAL
    | DISTINT'''
    drawCompiler.add_pOper(p[1])

def p_exp(p):
    '''exp : termino exp_2'''
    if(drawCompiler.top_pOper() in ['>','<','>=','<=','!=','==']):
        rightOperand = drawCompiler.pop_pilaO()
        right_type = drawCompiler.pop_pType()
        leftOperand = drawCompiler.pop_pilaO()
        left_type = drawCompiler.pop_pType()
        operator = drawCompiler.pop_pOper()

        result_type = drawCompiler.semantic_check(left_type,right_type,operator)
        if(result_type != 'error'):
            result = drawCompiler.next_temp(result_type)
            drawCompiler.add_quad(operator,leftOperand,rightOperand,result)
            drawCompiler.add_pilaO(result)
            drawCompiler.add_pType(result_type)
        else:
            drawCompiler.erase_dir_func()
            message = "Error: Type Mismatch in line " + str(p.lexer.lineno)
            print(message)
            sys.exit()

def p_exp_2(p):
    '''exp_2 : addop exp
    | empty'''
    pass

def p_termino(p):
    '''termino : factor termino_2'''
    if(drawCompiler.top_pOper() == '+' or drawCompiler.top_pOper() == '-'):
        rightOperand = drawCompiler.pop_pilaO()
        right_type = drawCompiler.pop_pType()
        leftOperand = drawCompiler.pop_pilaO()
        left_type = drawCompiler.pop_pType()
        operator = drawCompiler.pop_pOper()
        result_type = drawCompiler.semantic_check(left_type,right_type,operator)
        if(result_type != 'error'):
            result = drawCompiler.next_temp(result_type)
            drawCompiler.add_quad(operator,leftOperand,rightOperand,result)
            drawCompiler.add_pilaO(result)
            drawCompiler.add_pType(result_type)
        else:
            drawCompiler.erase_dir_func()
            message = "Error: Type Mismatch in line " + str(p.lexer.lineno)
            print(message)
            sys.exit()
        
def p_termino_2(p):
    '''termino_2 : timesop termino
    | empty'''
    pass

def p_var_cte(p):
    '''var_cte : var_cte_1
    | var_cte_i
    | var_cte_f
    | var_cte_b
    | llamada'''
    pass

def p_var_cte_i(p):
    ''' var_cte_i : CTE_I
    | MINUS CTE_I '''
    if(len(p) == 2):
        dir_virtual = drawCompiler.next_var_cte('int',p[1])
    else:
        dir_virtual = drawCompiler.next_var_cte('int',-1*p[2])
    drawCompiler.add_pilaO(dir_virtual)
    drawCompiler.add_pType("int")

def p_var_cte_f(p):
    ''' var_cte_f : CTE_F '''
    dir_virtual = drawCompiler.next_var_cte('float',p[1])
    drawCompiler.add_pilaO(dir_virtual)
    drawCompiler.add_pType("float")

def p_var_cte_b(p):
    ''' var_cte_b : TRUE
    | FALSE '''
    dir_virtual = drawCompiler.next_var_cte('boolean',p[1])
    drawCompiler.add_pilaO(dir_virtual)
    drawCompiler.add_pType("boolean")

def p_var_cte_1(p):
    ''' var_cte_1 : ID var_cte_2 '''
    if not drawCompiler.exists_in_scope(p[1]) : 
        message = "Error: The variable " + p[1] + " is not defined (Line " + str(p.lexer.lineno) + ")"
        print(message)
        sys.exit()
    else:
        dir_virtual = drawCompiler.get_dir_virtual(p[1])
        if(p[2] == 1):
            obj = drawCompiler.pop_pilaO()
            dim1 = drawCompiler.next_var_cte('int',drawCompiler.get_dim1_array(p[1]))
            cero = drawCompiler.next_var_cte('int',0)
            drawCompiler.add_quad("VERIFICA",obj,cero,dim1)
            next_temp = drawCompiler.next_temp('int')
            dir_virtual_cte = drawCompiler.next_var_cte('int',dir_virtual)
            drawCompiler.add_quad('+',obj,dir_virtual_cte, next_temp)
            drawCompiler.add_pilaO("("+str(next_temp)+")")
            drawCompiler.add_pType(drawCompiler.get_type(p[1]))
        elif(p[2] == 2):
            obj2 = drawCompiler.pop_pilaO()
            obj = drawCompiler.pop_pilaO()
            dim1 = drawCompiler.next_var_cte('int',drawCompiler.get_dim1_array(p[1]))
            dim2 = drawCompiler.next_var_cte('int',drawCompiler.get_dim2_array(p[1]))
            cero = drawCompiler.next_var_cte('int',0)
            next_temp = drawCompiler.next_temp('int')
            drawCompiler.add_quad("VERIFICA",obj,cero,dim1)
            drawCompiler.add_quad('*',obj,dim2, next_temp)
            drawCompiler.add_quad("VERIFICA",obj2,cero,dim2)
            next_temp2 = drawCompiler.next_temp('int')
            drawCompiler.add_quad('+',obj2,next_temp, next_temp2)
            next_temp3 = drawCompiler.next_temp('int')
            dir_virtual_cte = drawCompiler.next_var_cte('int',dir_virtual)
            drawCompiler.add_quad('+',next_temp2,dir_virtual_cte,next_temp3)     
            drawCompiler.add_pilaO("("+str(next_temp3)+")")
            drawCompiler.add_pType(drawCompiler.get_type(p[1]))
        else:
            drawCompiler.add_pilaO(dir_virtual)
            drawCompiler.add_pType(drawCompiler.get_type(p[1]))

def p_var_cte_2(p):
    ''' var_cte_2 : var_cte_2_lbracket super_exp var_cte_3
    | empty '''
    if(len(p) == 4):
        p[0] = 1 + p[3]
    else:
        p[0] = 0

def p_var_cte_2_lbracket(p):
    ''' var_cte_2_lbracket : LBRACKET '''
    drawCompiler.add_pOper("(")

def p_var_cte_3(p):
    '''var_cte_3 : RBRACKET
    | COMMA super_exp RBRACKET'''
    if(len(p) == 4):
        p[0] = 1
    else:
        p[0] = 0
    drawCompiler.pop_pOper()

def p_factor(p):
    '''factor : lparen_factor super_exp rparen_factor
    | addop var_cte
    | var_cte'''
    if (len(p) == 2 or len(p) == 3):
        if(drawCompiler.top_pOper() == '*' or drawCompiler.top_pOper() == '/' or drawCompiler.top_pOper() == '%'):
            rightOperand = drawCompiler.pop_pilaO()
            right_type = drawCompiler.pop_pType()
            leftOperand = drawCompiler.pop_pilaO()
            left_type = drawCompiler.pop_pType()
            operator = drawCompiler.pop_pOper()
            result_type = drawCompiler.semantic_check(left_type,right_type,operator)
            if(result_type != 'error'):
                result = drawCompiler.next_temp(result_type)
                drawCompiler.add_quad(operator,leftOperand,rightOperand,result)
                drawCompiler.add_pilaO(result)
                drawCompiler.add_pType(result_type)
            else:
                drawCompiler.erase_dir_func()
                message = "Error: Type Mismatch in line " + str(p.lexer.lineno)
                print(message)
                sys.exit()

def p_lparen_factor(p):
    '''lparen_factor : LPAREN'''
    drawCompiler.add_pOper(p[1])

def p_rparen_factor(p):
    '''rparen_factor : RPAREN'''
    drawCompiler.pop_pOper()

def p_condicion(p):
    '''condicion : condicion_id LPAREN super_exp rparen_condicion bloque condicion_2'''
    pass

def p_rparen_condicion(p):
    ''' rparen_condicion : RPAREN '''
    exp_type = drawCompiler.pop_pType()
    if(exp_type != 'boolean'):
        message = "Error: Type Mismatch in line " +  str(p.lexer.lineno) + " expression should be boolean"
        print(message)
        sys.exit()
    else:
        result = drawCompiler.pop_pilaO()
        drawCompiler.add_quad("GOTOF", result, -1, -1)
        drawCompiler.add_pJumps(drawCompiler.get_cont()-1)


def p_condicion_id(p):
    '''condicion_id : IF'''
    drawCompiler.add_inner_scope()

def p_condicion_2(p):
    '''condicion_2 : condicion_end
    | condicion_else  bloque condicion_end'''
    pass

def p_condicion_else(p):
    ''' condicion_else : ELSE '''
    drawCompiler.add_quad("GOTO", -1, -1 ,-1)
    falso = drawCompiler.pop_pJumps()
    drawCompiler.add_pJumps(drawCompiler.get_cont()-1)
    drawCompiler.fill(falso, drawCompiler.get_cont())

def p_condicion_end(p):
    ''' condicion_end : END '''
    end = drawCompiler.pop_pJumps()
    drawCompiler.fill(end, drawCompiler.get_cont())
    drawCompiler.pop_inner_scope()

def p_ciclo(p):
    '''ciclo : for
    | while'''
    pass

def p_accion(p):
    '''accion : accion_id POINT accion_params SEMICOLON'''
    action_name = p[3]['action']
    params = p[3]['params']
    params.reverse()
    for param in params:
        drawCompiler.add_quad("DRAWPARAM", param, -1, -1)
    drawCompiler.add_quad(action_name, -1, -1, p[1])

def p_accion_id(p):
    ''' accion_id : ID '''
    type = drawCompiler.get_type(p[1])
    if(type == "Draw"):
        p[0] = drawCompiler.get_dir_virtual(p[1])
    else:
        if(drawCompiler.exists_in_scope(p[1])):
            message = "Error: Unknown function for " + type + " object in line " +  str(p.lexer.lineno)
        else:
            message = "Error: Variable was not declared in line " + str(p.lexer.lineno)
        print(message)
        sys.exit()

def p_accion_params(p):
    ''' accion_params :  SETPOSITION LPAREN exp COMMA exp RPAREN
    | CIRCLE LPAREN exp RPAREN
    | RIGHT LPAREN exp RPAREN
    | LEFT LPAREN exp RPAREN
    | HIDE LPAREN RPAREN
    | SQUARE LPAREN exp RPAREN
    | CLEAR LPAREN RPAREN
    | SHOW LPAREN RPAREN
    | BACK LPAREN exp RPAREN
    | SPEED LPAREN exp RPAREN
    | FORWARD LPAREN exp RPAREN 
    | SETCOLOR LPAREN exp COMMA exp COMMA exp RPAREN'''
    if (len(p) == 4):
        p[0] = {
            'action' : p[1],
            'params' : []
        }
    elif (len(p) == 5):
        p[0] = {
            'action' : p[1],
            'params' : [drawCompiler.pop_pilaO()]
        }
    elif (len(p) == 7):
        p[0] = {
            'action' : p[1],
            'params' : [drawCompiler.pop_pilaO(), drawCompiler.pop_pilaO()]
        }
    elif (len(p) == 9):
        p[0] = {
            'action' : p[1],
            'params' : [drawCompiler.pop_pilaO(), drawCompiler.pop_pilaO(), drawCompiler.pop_pilaO()]
        }

def p_for(p):
    '''for : for_init LPAREN for_exp COMMA for_exp COMMA for_exp2 for_rparen bloque for_end'''
    pass

def p_for_exp(p):
    '''for_exp : exp'''
    if (drawCompiler.top_pType() != "int" and drawCompiler.top_pType() != "float"):
        message = "Error: Type Mismatch in line " +  str(p.lexer.lineno) + " expression should be int or float"
        print(message)
        sys.exit()

def p_for_exp2(p):
    '''for_exp2 : exp'''
    if (drawCompiler.top_pType() != "int" and drawCompiler.top_pType() != "float"):
        message = "Error: Type Mismatch in line " +  str(p.lexer.lineno) + " expression should be int or float"
        print(message)
        sys.exit()
    else:
        result3 = drawCompiler.pop_pilaO()
        result2 = drawCompiler.pop_pilaO()
        result1 = drawCompiler.pop_pilaO()
        next_var_for = drawCompiler.next_var_for()
        drawCompiler.add_quad('=',result1,-1,next_var_for)
        drawCompiler.add_pilaO(next_var_for)
        next_var_for = drawCompiler.next_var_for()
        drawCompiler.add_quad('=',result2,-1,next_var_for)
        drawCompiler.add_pilaO(next_var_for)
        next_var_for = drawCompiler.next_var_for()
        drawCompiler.add_quad('=',result3,-1,next_var_for)
        drawCompiler.add_pilaO(next_var_for)

def p_for_rparen(p):
    '''for_rparen : RPAREN'''
    drawCompiler.add_pJumps(drawCompiler.get_cont())
    drawCompiler.add_pJumps(drawCompiler.get_cont()+1)
    result3 = drawCompiler.pop_pilaO()
    result2 = drawCompiler.pop_pilaO()
    result1 = drawCompiler.pop_pilaO()
    next_var_for = drawCompiler.next_var_for()
    drawCompiler.add_quad('<=',result1,result2,next_var_for)
    drawCompiler.add_quad('GOTOF',next_var_for,-1,-1)
    drawCompiler.add_pilaO(result1)
    drawCompiler.add_pilaO(result2)
    drawCompiler.add_pilaO(result3)
    
def p_for_init(p):
    ''' for_init : FOR '''
    drawCompiler.add_inner_scope()

def p_for_end(p):
    ''' for_end : END '''
    drawCompiler.pop_inner_scope()
    returns = drawCompiler.pop_pJumps()
    condition = drawCompiler.pop_pJumps()
    result3 = drawCompiler.pop_pilaO()
    result2 = drawCompiler.pop_pilaO()
    result1 = drawCompiler.pop_pilaO()
    drawCompiler.add_quad('+',result1,result3,result1)
    drawCompiler.add_quad('GOTO',-1,-1,condition)
    drawCompiler.fill(returns, drawCompiler.get_cont())
    drawCompiler.pop_pType()
    drawCompiler.pop_pType()
    drawCompiler.pop_pType()

def p_while(p):
    '''while : while_init LPAREN super_exp rparen_while bloque while_end'''
    pass
    
def p_while_init(p):
    ''' while_init : WHILE '''
    drawCompiler.add_inner_scope()
    drawCompiler.add_pJumps(drawCompiler.get_cont())

def p_rparen_while(p):
    '''rparen_while : RPAREN'''
    exp_type = drawCompiler.pop_pType()
    if(exp_type != 'boolean'):
        message = "Error: Type Mismatch in line " +  str(p.lexer.lineno) + " expression should be boolean"
        print(message)
        sys.exit()
    else:
        result = drawCompiler.pop_pilaO()
        drawCompiler.add_quad("GOTOF", result, -1, -1)
        drawCompiler.add_pJumps(drawCompiler.get_cont()-1)

def p_while_end(p):
    ''' while_end : END '''
    end = drawCompiler.pop_pJumps()
    returns = drawCompiler.pop_pJumps()
    drawCompiler.add_quad("GOTO",-1,-1,returns)
    drawCompiler.fill(end, drawCompiler.get_cont())
    drawCompiler.pop_inner_scope()

def p_funcion(p):
    '''funcion :  DEF funcion_aux '''
    drawCompiler.add_quad("ENDPROC", -1, -1, -1)
    drawCompiler.reset_memory()

def p_funcion_aux(p):
    ''' funcion_aux : funcion_1 var_local bloque funcion_2
        | funcion_void var_local bloque funcion_end'''
    pass

def p_funcion_void(p):
    '''funcion_void :  VOID ID'''
    if drawCompiler.exists_func(p[2]):
        message = "The function " + str(p[2]) + " is already defined"
        print(message)
        sys.exit()
    else:
        drawCompiler.actual_scope = p[2]
        drawCompiler.add_func(p[1], p[2])
    
def p_funcion_1(p):
    '''funcion_1 :  data_type_func ID'''
    if drawCompiler.exists_func(p[2]):
        message = "The function " + str(p[2]) + " is already defined"
        print(message)
        sys.exit()
    else:
        drawCompiler.actual_scope = p[2]
        drawCompiler.add_func(p[1], p[2])
        drawCompiler.next_func(p[1],p[2])

def p_funcion_2(p):
    '''funcion_2 : RETURN super_exp SEMICOLON END'''
    result_type = drawCompiler.pop_pType()
    func_type = drawCompiler.dir_func[drawCompiler.actual_scope]['type']
    if (func_type == result_type):
        result = drawCompiler.pop_pilaO()
        drawCompiler.add_quad("RETURN",result,-1,-1)
        drawCompiler.actual_scope = 'global'
    else:
        message = "The return value of the function " + str(drawCompiler.actual_scope) + " is not right, it expected " + str(func_type) + " but the return value was " + str(result_type)
        print(message)
        sys.exit()

def p_funcion_end(p):
    ''' funcion_end : END '''
    drawCompiler.actual_scope = 'global'

def p_var_local(p):
    '''var_local : LPAREN var_local_2 RPAREN'''
    drawCompiler.add_func_counter();

def p_var_local_2(p):
    '''var_local_2 : var_local_2_1 var_local_3
    | empty'''
    pass

def p_var_local_2_1(p):
    '''var_local_2_1 : data_type ID '''
    if drawCompiler.exists_in_scope(p[2]):
        message = "Error: The variable " + p[2] + " is already defined(Line " + str(p.lexer.lineno) + ")"
        print(message)
        sys.exit()
    else:
        dir_virtual = drawCompiler.next_var(p[1])
        drawCompiler.add_param(p[1])
        drawCompiler.add_var(p[1], p[2], dir_virtual)

def p_var_local_3(p):
    '''var_local_3 : COMMA var_local_2
    | empty'''
    pass

def p_addop(p):
    '''addop : PLUS
    | MINUS'''
    drawCompiler.add_pOper(p[1])

def p_timesop(p):
    '''timesop : TIMES
    | DIVIDE
    | PERCENT'''
    drawCompiler.add_pOper(p[1])

def p_logicop(p):
    '''logicop : AND
    | OR'''
    drawCompiler.add_pOper(p[1])

def p_empty(p):
    'empty :'
    pass



def p_error(p):
    if p is not None:
        message = "Sintaxis error in line: " + str(p.lexer.lineno)+ "  Error of context " + str(p.value)
    else:
        message = "Lexic error in line: " + str(c_lexer.lexer.lineno)
    print(message)
    sys.exit()

parser = yacc.yacc()


