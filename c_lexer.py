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
    'window' : 'WINDOW',
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
    'setBackground' : 'SETBACKGROUND',
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
    'Window' : 'NEWWINDOW',
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

def Analizador_lexico():
    a = input("direccion: ")
    if ( os.path.exists (a)):
        f = open(a)
        data = f.read()
        f.close()
        #Build lexer and try on
        lexer.input(data)
        test(data, lexer)
    else:
        print ("El archivo no existe")


# Test
if __name__ == '__main__':

    # Test  ESTO ES SOLO PARA PROBAR EL FUNCINAMIENTO DE ANIZADOR LEXICO.
    #Cargamos el archivo "c.cpp" que esta en la carpeta ejemplos y lo guardamos
    #la variable data para despues enviarla al analizador lexico para que la
    #descomponga en tokes

    f = open('fuente/c.cpp')
    data = f.read()
    f.close()
    #Build lexer and try on
    lexer.input(data)
    test(data, lexer)


