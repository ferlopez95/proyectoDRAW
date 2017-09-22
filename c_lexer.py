# -*- encondig: utf-8 -*-

import ply.lex as lex
import os

reserved = {
    #Palabras Reservadas
    
    'if' : 'IF',
    'else' : 'ELSE',
    'int' : 'INT',
    'float' : 'FLOAT',
    'boolean' : 'BOOLEAN',
    'draw' : 'DRAW',
    'array' : 'ARRAY',
    'main' : 'MAIN',
    'global' : 'GLOBAL',
    'def' : 'DEF',
    'end' : 'END',
    'void' : 'VOID',
    'while' : 'WHILE',
    'for' : 'FOR',
    'return' : 'RETURN',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'setPosition' : 'SETPOSITION',
    'setColor' : 'SETCOLOR',
    'speed' : 'SPEED',
    'forward' : 'FORWARD',
    'left' : 'LEFT',
    'right' : 'RIGHT',
    'back' : 'BACK',
    'hide' : 'HIDE',
    'show' : 'SHOW',
    'clear' : 'CLEAR',
    'square' : 'SQUARE',
    'circle' : 'CIRCLE',
    'length' : 'LENGTH',
    'Draw' : 'NEWDRAW',
    
}

# lista de tokens
tokens = (

    # Symbolos
    
    'POINT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'DEQUAL',
    'DISTINT',
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'QUOTES',
    'PERCENT',
    'AND',
    'OR',


    #Otros
    'ID',
    'CTE_I',
    'CTE_F',
    
) + tuple(reserved.values())


# Reglas de Expresiones Regualres para token de Contexto simple

t_PLUS = r'\+'
t_MINUS = r'-'
t_POINT = r'\.'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
t_LESS = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_QUOTES = r'\"'
t_AND = r'&&'
t_OR = r'\|\|'
t_PERCENT = r'%'
t_LESSEQUAL = r'<='
t_GREATEREQUAL = r'>='

def t_CTE_F(t):
    r'\d+\.\d+'
    return t

def t_CTE_I(t):
    r'\d+'
    t.value = int(t.value)
    return t    

def t_ID(t):
    r'\w+(_\d\w)*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_DEQUAL(t):
    r'=='
    return t

def t_DISTINT(t):
    r'!='
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'


def t_error(t):
    print (("Error Lexico: " + str(t.value[0])))
    t.lexer.skip(1)


def test(data, lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print (tok)

lexer = lex.lex()

#def Analizador_lexico():
#    a = input("direccion: ")
#    if ( os.path.exists (a)):
#        f = open(a)
#        data = f.read()
#        f.close()
#        #Build lexer and try on
#        lexer.input(data)
#        test(data, lexer)
#    else:
#        print ("El archivo no existe")

VERBOSE = 1

def p_programa(p):
    '''programa : globales funcion main
    | main
    | funcion main'''
    pass

def p_globales(p):
    '''globales : GLOBAL vars'''
    pass

def p_bloque(p):
    '''bloque : estatuto bloque
    | empty'''
    pass

def p_data_type(p):
    '''data_type : INT
    | FLOAT
    | BOOLEAN'''
    pass

def p_main(p):
    '''main : DEF VOID MAIN LPAREN RPAREN bloque END'''
    pass

def p_estatuto(p):
    '''estatuto : asignacion
    | condicion
    | ciclo
    | accion
    | vars
    | llamada SEMICOLON'''
    pass

def p_asignacion(p):
    '''asignacion : ID asignacion_2'''
    pass

def p_asignacion_2(p):
    '''asignacion_2 : EQUAL expresion
    | LBRACKET CTE_I asignacion_3'''
    pass
    
def p_asignacion_3(p):
    '''asignacion_3 : RBRACKET
    | COMMA CTE_I RBRACKET'''
    pass

def p_vars(p):
    '''vars : DRAW ID EQUAL NEWDRAW LPAREN RPAREN SEMICOLON
    | data_type ID vars2
    | ARRAY ID vars3'''
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
    '''llamada : ID LPAREN llamada_2'''
    pass

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
    '''def_array : LBRACKET def_array_2'''
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
    '''var_cte : ID
    | CTE_I
    | CTE_F
    | TRUE
    | FALSE
    | llamada'''
    pass

def p_factor(p):
    '''factor : LPAREN expresion RPAREN
    | addop var_cte
    | var_cte
    | ID LBRACKET exp factor_2'''
    pass

def p_factor_2(p):
    '''factor_2 : RBRACKET
    | COMMA exp RBRACKET'''
    pass

def p_condicion(p):
    '''condicion : IF LPAREN expresion RPAREN bloque condicion_2'''
    pass

def p_condicion_2(p):
    '''condicion_2 : END
    | ELSE  bloque END'''
    pass

def p_ciclo(p):
    '''ciclo : for
    | while'''
    pass

def p_accion(p):
    '''accion : ID POINT llamada SEMICOLON'''
    pass

def p_for(p):
    '''for : FOR LPAREN CTE_I COMMA CTE_I RPAREN bloque END'''
    pass

def p_while(p):
    '''while : WHILE LPAREN expresion RPAREN bloque END'''
    pass

def p_funcion(p):
    '''funcion :  DEF data_type ID var_local bloque funcion_2'''
    pass

def p_funcion_2(p):
    '''funcion_2 : RETURN expresion END
    | END'''
    pass

def p_var_local(p):
    '''var_local : ID LPAREN var_local_2 RPAREN'''
    pass

def p_var_local_2(p):
    '''var_local_2 : data_type ID var_local_3'''
    pass

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
    print("Error")
    #print str(dir(p))
    #print str(dir(c_lexer))
    #if VERBOSE:
    #    if p is not None:
    #        print "Error en Sintaxis linea: " + str(p.lexer.lineno)+ "  Error de Contexto " + str(p.value)
    #    else:
    #        print "Error en Lexico linea: " + str(c_lexer.lexer.lineno)
    #else:
    #    raise Exception('Syntax', 'error')

import ply.yacc as yacc
parser = yacc.yacc()

a = input("direccion: ")
if ( os.path.exists (a)):
    f = open(a)
    data = f.read()
    f.close()
    parser.parse(data)
else:
    print("El archivo no existe")



