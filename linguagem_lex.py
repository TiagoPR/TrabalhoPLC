import re
import ply.lex as lex

#states = [
#    ('VALUE', 'exclusive')
#]

literals = ['+','-','*','/','=','(',')',]

tokens = (
    'TRUE',
    'FALSE',
    'INF',
    'INFQE',
    'SUP',
    'SUPEQ',
    'INPUT',
    'FRASE',
    'PRINT',
    'TIPO',
    'ID',
    'OU',
    'E',
    'IF',
    'THEN',
    'ELSE',
    'WHILE',
    'DO',
    'NUM',
    'FRASE',
    
    
)


t_OU = r'or'

t_E = r'and'

t_IF = r'if'

t_THEN = r'then'

t_ELSE = r'else'

t_WHILE = r'while'

t_DO = r'do'

t_NUM = r'[0-9]+'

t_PAL = r'\".*\"'


    
t_ANY_ignore = ' \n\t'

def t_ANY_error(t):
    print('Illegal character: %s', t.value[0])

#lexer = lex.lex()
#lexer = lex.lex(reflags=re.UNICODE) 
lexer = lex.lex(reflags=re.IGNORECASE) 