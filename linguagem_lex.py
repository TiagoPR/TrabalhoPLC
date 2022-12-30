import re
import ply.lex as lex

literals = ['+', '-', '*', '/', '=', '(', ')','.','!']

tokens = (
    'IF',
    'TRUE',
    'FALSE',
    'EQUAL',
    'INF',
    'INFEQ',
    'SUP',
    'SUPEQ',
    'DIFF',
    'INPUT',
    'PRINT',
    'INT',
    'OU',
    'E',
    'THEN',
    'ELSE',
    'WHILE',
    'begin',
    'return',
    'end',
    'DO',
    'NUM',
    'ID',
    'FRASE',

)

t_TRUE = r'true'

t_FALSE = r'false'

t_EQUAL = r'\=\='

t_DIFF = r'\!\='

t_INF = r'\<'

t_INFEQ = r'\<\='

t_SUP = r'\>'

t_SUPEQ = r'\>\='

t_INPUT = r'input'

t_PRINT = r'print'

t_INT = r'int'

t_OU = r'\|'

t_E = r'\^'

t_THEN = r'then'

t_ELSE = r'else'

t_WHILE = r'while'

t_begin = r'begin'

t_return = r'return'

t_end = r'end'

t_ID = r'\w+'

t_NUM = r'[0-9]+'

t_FRASE = r'\"[^\"]*\"'

t_ANY_ignore = ' \n\t'

def t_IF(t):
    r'if'
    return t

def t_DO(t):
    r'do'
    return t

def t_ANY_error(t):
    print('Illegal character: %s', t.value[0])


lexer = lex.lex()



