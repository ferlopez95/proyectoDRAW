import c_lexer
import ply.yacc as yacc
from HelperClass import HelperClass

tokens = c_lexer.tokens

drawCompiler = HelperClass('global')


def p_programa(p):
    '''programa : globales funciones programa_end
    | funciones programa_end'''
    pass

def p_programa_end(p):
    ''' programa_end : empty '''
    drawCompiler.erase_dir_func()

def p_funciones(p):
    '''funciones : funcion main
    | main '''
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
    drawCompiler.add_func('void', p[1])

def p_bloque(p):
    '''bloque : estatuto bloque
    | empty'''
    pass

def p_data_type(p):
    '''data_type : INT
    | FLOAT
    | BOOLEAN'''
    p[0] = p[1]

def p_main(p):
    '''main : main_1 bloque END'''
    pass

def p_main_1(p):
    ''' main_1 : DEF VOID MAIN LPAREN RPAREN'''
    drawCompiler.actual_scope = p[3]
    drawCompiler.add_func(p[2], p[3])

def p_estatuto(p):
    '''estatuto : asignacion
    | condicion
    | ciclo
    | accion
    | vars
    | llamada SEMICOLON'''
    pass

def p_asignacion(p):
    '''asignacion : asignacion_id asignacion_2 SEMICOLON'''
    pass

def p_asignacion_id(p):
    '''asignacion_id : ID'''
    if not drawCompiler.exists_in_scope(p[1]):
        print ("Error: La variable " + p[1] + " no está definida (Línea " + str(p.lexer.lineno) + ")")

def p_asignacion_2(p):
    '''asignacion_2 : EQUAL expresion
    | LBRACKET exp asignacion_3 EQUAL expresion'''
    pass
    
def p_asignacion_3(p):
    '''asignacion_3 : RBRACKET
    | COMMA exp RBRACKET'''
    pass

def p_vars(p):
    '''vars : DRAW ID EQUAL NEWDRAW LPAREN RPAREN SEMICOLON
    | data_type ID vars2
    | vars_aux'''
    if len(p) >= 4:
        if drawCompiler.exists_in_scope(p[2]):
            print ("Error: La variable " + p[2] + " ya está definida (Línea " + str(p.lexer.lineno) + ")")
        else:
            drawCompiler.add_var(p[1], p[2])


def p_vars_aux(p):
    ''' vars_aux : array ID vars3 '''
    if drawCompiler.exists_in_scope(p[2]):
        print ("Error: La variable " + p[2] + " ya está definida (Línea " + str(p.lexer.lineno) + ")")
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
    '''vars2 : EQUAL expresion SEMICOLON
    | SEMICOLON'''
    pass

def p_vars_3(p):
    '''vars3 : EQUAL def_array SEMICOLON
    | SEMICOLON'''
    pass

def p_llamada(p):
    '''llamada : llamada_id LPAREN llamada_2'''
    pass

def p_llamada_id(p):
    ''' llamada_id : ID '''
    if not drawCompiler.exists_func(p[1]):
        print ("Error: La función " + p[1] + " no está definida (Línea " + str(p.lexer.lineno) + ")")
    

def p_llamada_2(p):
    '''llamada_2 : llamada_exp RPAREN
    | RPAREN'''
    pass

def p_llamada_exp(p):
    '''llamada_exp : expresion llamada_exp2'''
    pass

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
    '''def_array_cte : var_cte def_array_cte_2'''
    pass

def p_def_array_cte_2(p):
    '''def_array_cte_2 : COMMA def_array_cte
    | empty'''
    pass

def p_expresion(p):
    '''expresion : exp expresion_2'''
    pass

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
    pass

def p_exp(p):
    '''exp : termino exp_2'''
    pass

def p_exp_2(p):
    '''exp_2 : addop exp
    | empty'''
    pass

def p_termino(p):
    '''termino : factor termino_2'''
    pass

def p_termino_2(p):
    '''termino_2 : timesop termino
    | empty'''
    pass

def p_var_cte(p):
    '''var_cte : var_cte_1
    | CTE_I
    | CTE_F
    | TRUE
    | FALSE
    | llamada'''
    pass

def p_var_cte_1(p):
    ''' var_cte_1 : ID var_cte_2 '''
    if not drawCompiler.exists_in_scope(p[1]) : 
        print ("Error: La variable " + p[1] + " no esta definida (Línea " + str(p.lexer.lineno) + ")")

def p_var_cte_2(p):
    ''' var_cte_2 : LBRACKET exp var_cte_3
    | empty '''
    pass

def p_var_cte_3(p):
    '''var_cte_3 : RBRACKET
    | COMMA exp RBRACKET'''
    pass

def p_factor(p):
    '''factor : LPAREN expresion RPAREN
    | addop var_cte
    | var_cte'''
    pass

def p_condicion(p):
    '''condicion : condicion_id LPAREN expresion RPAREN bloque condicion_2'''
    pass


def p_condicion_id(p):
    '''condicion_id : IF'''
    drawCompiler.add_inner_scope()

def p_condicion_2(p):
    '''condicion_2 : condicion_end
    | ELSE  bloque condicion_end'''
    pass

def p_condicion_end(p):
    ''' condicion_end : END '''
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
    '''for : for_init LPAREN CTE_I COMMA CTE_I COMMA CTE_I RPAREN bloque for_end'''
    pass

def p_for_init(p):
    ''' for_init : FOR '''
    drawCompiler.add_inner_scope()

def p_for_end(p):
    ''' for_end : END '''
    drawCompiler.pop_inner_scope()

def p_while(p):
    '''while : while_init LPAREN expresion RPAREN bloque while_end'''
    pass

def p_while_init(p):
    ''' while_init : WHILE '''
    drawCompiler.add_inner_scope()

def p_while_end(p):
    ''' while_end : END '''
    drawCompiler.pop_inner_scope()

def p_funcion(p):
    '''funcion :  funcion_1 var_local bloque funcion_2'''
    pass

def p_funcion_1(p):
    '''funcion_1 :  DEF data_type ID'''
    drawCompiler.actual_scope = p[3]
    drawCompiler.add_func(p[2], p[3])

def p_funcion_2(p):
    '''funcion_2 : RETURN expresion SEMICOLON funcion_end
    | funcion_end'''
    pass

def p_funcion_end(p):
    ''' funcion_end : END '''
    drawCompiler.actual_scope = 'global'

def p_var_local(p):
    '''var_local : LPAREN var_local_2 RPAREN'''
    pass

def p_var_local_2(p):
    '''var_local_2 : var_local_2_1 var_local_3
    | empty'''
    pass

def p_var_local_2_1(p):
    '''var_local_2_1 : data_type ID '''
    if drawCompiler.exists_in_scope(p[2]):
        print("Error: La variable " + p[2] + " ya está definida (Línea " + str(p.lexer.lineno) + ")")

def p_var_local_3(p):
    '''var_local_3 : COMMA var_local_2
    | empty'''
    pass

def p_addop(p):
    '''addop : PLUS
    | MINUS'''
    pass

def p_timesop(p):
    '''timesop : TIMES
    | DIVIDE
    | PERCENT'''
    pass

def p_empty(p):
    'empty :'
    pass



def p_error(p):
    if p is not None:
        print ("Error en Sintaxis linea: " + str(p.lexer.lineno)+ "  Error de Contexto " + str(p.value))
    else:
        print ("Error en Lexico linea: " + str(c_lexer.lexer.lineno))


parser = yacc.yacc()


