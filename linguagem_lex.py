import re
import ply.lex as lex

# states = [
#    ('VALUE', 'exclusive')
# ]

literals = ['+', '-', '*', '/', '=', '(', ')','.']

tokens = (
    'TRUE',
    'FALSE',
    'INF',
    'INFEQ',
    'SUP',
    'SUPEQ',
    'INPUT',
    'PRINT',
    'INT',

    'OU',
    'E',
    'IF',
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

t_INF = r'\<'

t_INFEQ = r'\<\='

t_SUP = r'\>'

t_SUPEQ = r'\>\='

t_INPUT = r'input'

t_PRINT = r'print'

t_INT = r'int'

t_OU = r'\|'

t_E = r'\^'

t_IF = r'if'

t_THEN = r'then'

t_ELSE = r'else'

t_WHILE = r'while'

t_begin = r'begin'

t_return = r'return'

t_end = r'end'

t_DO = r'do'

t_ID = r'\w+'

t_NUM = r'[0-9]+'

t_FRASE = r'\".*\"'

t_ANY_ignore = ' \n\t'


def t_ANY_error(t):
    print('Illegal character: %s', t.value[0])


# lexer = lex.lex()
# lexer = lex.lex(reflags=re.UNICODE)
lexer = lex.lex(reflags=re.IGNORECASE)
