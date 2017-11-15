# encoding=utf8  
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

import c_lexer
import ply.yacc as yacc
from HelperClass import HelperClass

tokens = c_lexer.tokens

drawCompiler = HelperClass('global')
drawCompiler.add_func('void', 'global')


def p_programa(p):
    '''programa : init globales funciones programa_end
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
    '''asignacion_id : ID'''
    if not drawCompiler.exists_in_scope(p[1]):
        message = "Error: La variable " + p[1] + " no está definida (Línea " + str(p.lexer.lineno) + ")"
        print(message)
        sys.exit(message)
    else:
        dir_virtual = drawCompiler.get_dir_virtual(p[1])
        drawCompiler.add_pilaO(dir_virtual)
        drawCompiler.add_pType(drawCompiler.get_type(p[1]))

def p_asignacion_2(p):
    '''asignacion_2 : asignacion_equal super_exp
    | LBRACKET exp asignacion_3 EQUAL super_exp'''
    if(len(p) == 3 and drawCompiler.top_pOper() == '='):
        rightOperand = drawCompiler.pop_pilaO()
        right_type = drawCompiler.pop_pType()
        leftOperand = drawCompiler.pop_pilaO()
        left_type = drawCompiler.pop_pType()
        operator = drawCompiler.pop_pOper()
        result_type = drawCompiler.semantic_check(left_type,right_type,operator)
        if(result_type != 'error'):
            drawCompiler.add_quad(operator,rightOperand,"",leftOperand)
        else:
            drawCompiler.erase_dir_func()
            message = "Type Mismatch in line " + str(p.lexer.lineno)
            print(message)
            sys.exit(message)

def p_asignacion_equal(p):
    '''asignacion_equal : EQUAL'''
    drawCompiler.add_pOper(p[1])
    
def p_asignacion_3(p):
    '''asignacion_3 : RBRACKET
    | COMMA exp RBRACKET'''
    pass

def p_vars(p):
    '''vars : DRAW ID EQUAL NEWDRAW LPAREN RPAREN SEMICOLON
    | vars_id vars2
    | vars_aux'''
    if len(p) >= 4:
        if drawCompiler.exists_in_scope(p[2]):
            message = "Error: La variable " + p[2] + " ya está definida (Línea " + str(p.lexer.lineno) + ")"
            print(message)
            sys.exit(message)
        else:
            drawCompiler.add_var(p[1], p[2])

def p_vars_id(p):
    '''vars_id : data_type ID'''
    if drawCompiler.exists_in_scope(p[2]):
        message = "Error: La variable " + p[2] + " ya está definida (Línea " + str(p.lexer.lineno) + ")"
        print(message)
        sys.exit(message)
    else:
        dir_virtual = drawCompiler.next_var(p[1])
        drawCompiler.add_var(p[1], p[2], dir_virtual)
        drawCompiler.add_pilaO(dir_virtual)
        drawCompiler.add_pType(p[1])

def p_vars_aux(p):
    ''' vars_aux : array ID vars3 '''
    if drawCompiler.exists_in_scope(p[2]):
        message = "Error: La variable " + p[2] + " ya está definida (Línea " + str(p.lexer.lineno) + ")"
        print(message)
        sys.exit(message)
    else:
        drawCompiler.add_var('array', p[2])

def p_array(p):
    ''' array : ARRAY LESS data_type COMMA CTE_I array_2 GREATER '''
    pass

def p_array_2(p) :
    ''' array_2 : COMMA CTE_I
    | empty '''
    pass

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
            drawCompiler.add_quad(operator,rightOperand,"",leftOperand)
        else:
            drawCompiler.erase_dir_func()
            message = "Type Mismatch in line " + str(p.lexer.lineno)
            print(message)
            sys.exit(message)
    else:
        drawCompiler.pop_pilaO()
        drawCompiler.pop_pType()

def p_vars_3(p):
    '''vars3 : EQUAL def_array SEMICOLON
    | SEMICOLON'''
    pass

def p_llamada(p):
    '''llamada : llamada_id llamada_2'''
    drawCompiler.add_quad("GOSUB",p[1],-1,-1)
    drawCompiler.param_k = 0
    if(drawCompiler.dir_func[p[1]]['type'] != "void"):
        drawCompiler.add_pType(drawCompiler.dir_func[p[1]]['type'])
        next_var = drawCompiler.find_func(drawCompiler.dir_func[p[1]]['type'],p[1])
        drawCompiler.add_quad("=",p[1],-1,next_var)
        drawCompiler.add_pilaO(next_var)

def p_llamada_id(p):
    ''' llamada_id : ID LPAREN'''
    if not drawCompiler.exists_func(p[1]):
        message = "Error: La función " + p[1] + " no está definida (Línea " + str(p.lexer.lineno) + ")"
        print(message)
        sys.exit(message)
    else:
        drawCompiler.add_quad("ERA",p[1],"-1","-1")
        drawCompiler.param_k = 0
        drawCompiler.params = drawCompiler.dir_func[p[1]]['parameters']
        p[0] = p[1]

def p_llamada_2(p):
    '''llamada_2 : llamada_exp llamada_rparen
    | llamada_rparen'''
    pass

def p_llamada_rparen(p):
    '''llamada_rparen : RPAREN'''
    if(drawCompiler.param_k != len(drawCompiler.params)-1):
        message = "Error: Wrong number of parameters, Línea " + str(p.lexer.lineno) + ")"
        print(message)
        sys.exit(message)
        
def p_llamada_exp(p):
    '''llamada_exp : llamada_super_exp llamada_exp2'''
    pass

def p_llamada_super_exp(p):
    '''llamada_super_exp : super_exp'''
    argument = drawCompiler.pop_pilaO()
    argumentType = drawCompiler.pop_pType()
    if(argumentType == drawCompiler.params[drawCompiler.param_k]):
        drawCompiler.add_quad("param",argument,-1,"param" + str(drawCompiler.param_k))
    else:
        message = "Error: Type Mismatch in Parameters, Línea " + str(p.lexer.lineno) + ")"
        print(message)
        sys.exit(message)

def p_llamada_exp_2(p):
    '''llamada_exp2 : llamada_comma llamada_exp
    | empty'''
    pass

def p_llamada_comma(p):
    '''llamada_comma : COMMA'''
    drawCompiler.param_k = drawCompiler.param_k + 1

def p_def_array(p):
    '''def_array : LBRACKET def_array_2 '''
    pass

def p_def_array_2(p):
    '''def_array_2 : def_array_cte RBRACKET
    | RBRACKET'''
    pass

def p_def_array_cte(p):
    '''def_array_cte : var_cte def_array_cte_2'''
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
            message = "Type Mismatch in line " + str(p.lexer.lineno)
            print(message)
            sys.exit(message)

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
            message = "Type Mismatch in line " + str(p.lexer.lineno)
            print(message)
            sys.exit(message)

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
            message = "Type Mismatch in line " + str(p.lexer.lineno)
            print(message)
            sys.exit(message)
        
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
    ''' var_cte_i : CTE_I '''
    dir_virtual = drawCompiler.next_var_cte('int',p[1])
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
        message = "Error: La variable " + p[1] + " no esta definida (Línea " + str(p.lexer.lineno) + ")"
        print(message)
        sys.exit(message)
    else:
        dir_virtual = drawCompiler.get_dir_virtual(p[1])
        drawCompiler.add_pilaO(dir_virtual)
        drawCompiler.add_pType(drawCompiler.get_type(p[1]))

def p_var_cte_2(p):
    ''' var_cte_2 : LBRACKET exp var_cte_3
    | empty '''
    pass

def p_var_cte_3(p):
    '''var_cte_3 : RBRACKET
    | COMMA exp RBRACKET'''
    pass

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
                message = "Type Mismatch in line " + str(p.lexer.lineno)
                print(message)
                sys.exit(message)

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
        message = "Type Mismatch in line " +  str(p.lexer.lineno) + " expression should be boolean"
        print(message)
        sys.exit(message)
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
    '''accion : ID POINT accion_nombre accion_params SEMICOLON'''
    pass

def p_accion_params(p):
    ''' accion_params : LPAREN accion_params_2 '''
    pass

def p_accion_params_2(p):
    ''' accion_params_2 : accion_params_cte RPAREN
    | RPAREN '''
    pass

def p_accion_params_cte(p):
    ''' accion_params_cte : var_cte accion_params_cte_2'''
    pass

def p_accion_params_cte_2(p):
    ''' accion_params_cte_2 : COMMA accion_params_cte
    | empty '''
    pass

def p_accion_llamada(p):
    ''' accion_nombre :  SETPOSITION
    | CIRCLE
    | RIGHT
    | LEFT
    | HIDE
    | SQUARE
    | CLEAR
    | SHOW
    | BACK
    | SPEED
    | FORWARD
    | SETCOLOR '''
    pass

def p_for(p):
    '''for : for_init LPAREN for_exp COMMA for_exp COMMA for_exp2 for_rparen bloque for_end'''
    pass

def p_for_exp(p):
    '''for_exp : exp'''
    if (drawCompiler.top_pType() != "int" and drawCompiler.top_pType() != "float"):
        message = "Type Mismatch in line " +  str(p.lexer.lineno) + " expression should be int or float"
        print(message)
        sys.exit(message)

def p_for_exp2(p):
    '''for_exp2 : exp'''
    if (drawCompiler.top_pType() != "int" and drawCompiler.top_pType() != "float"):
        message = "Type Mismatch in line " +  str(p.lexer.lineno) + " expression should be int or float"
        print(message)
        sys.exit(message)
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
        message = "Type Mismatch in line " +  str(p.lexer.lineno) + " expression should be boolean"
        print(message)
        sys.exit(message)
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
    pass

def p_funcion_aux(p):
    ''' funcion_aux : funcion_1 var_local bloque funcion_2
        | funcion_void var_local bloque funcion_end'''
    drawCompiler.add_quad("ENDPROC", -1, -1, -1)

def p_funcion_void(p):
    '''funcion_void :  VOID ID'''
    if drawCompiler.exists_func(p[2]):
        message = "La función " + str(p[2]) + " ya está definida"
        print(message)
        sys.exit(message)
    else:
        drawCompiler.actual_scope = p[2]
        drawCompiler.add_func(p[1], p[2])
    
def p_funcion_1(p):
    '''funcion_1 :  data_type_func ID'''
    if drawCompiler.exists_func(p[2]):
        message = "La función " + str(p[2]) + " ya está definida"
        print(message)
        sys.exit(message)
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
        drawCompiler.erase_temps()
    else:
        message = "El valor de retorno de la función " + str(drawCompiler.actual_scope) + " no es correcto, como esperaba " + str(func_type) + " se regreso " + str(result_type)
        print(message)
        sys.exit(message)

def p_funcion_end(p):
    ''' funcion_end : END '''
    drawCompiler.actual_scope = 'global'
    drawCompiler.erase_temps()

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
        message = "Error: La variable " + p[2] + " ya está definida (Línea " + str(p.lexer.lineno) + ")"
        print(message)
        sys.exit(message)
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
        message = "Error en Sintaxis linea: " + str(p.lexer.lineno)+ "  Error de Contexto " + str(p.value)
    else:
        message = "Error en Lexico linea: " + str(c_lexer.lexer.lineno)
    print(message)
    sys.exit(message)

parser = yacc.yacc()


