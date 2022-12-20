import ply.yacc as yacc

from linguagem_lex import tokens

def p_cond_bool(p):
    "cond : BOOL"
    p[0] = f'pushi{p[1]}\npushi 0\n sup\n'

def p_cond_expr(p):
    "cond : expr"
    p[0] = f'pushi{p[1]}\npushi 0\n sup\n'


def p_cond_oprelacao(p):
    "cond : expr oprelacao expr"
    p[0] = f'pushi {p[1]}\npushi {p[3]}\np[1]'

def p_cond_oplogico(p):
    "cond : cond oplogico cond"

def p_ler(p):
    "ler : INPUT FRASE"
    p[0] = f"pushs {p[2]}\nread\natoi"

def p_escreva(p):
    "escreva : PRINT corpoescreve"
    p[0] = f"pushs {p[2]}"
def p_corpoescreve_alter(p):
    "corpoescreve : alter corpoescreve"
    p[0] = f'{p[0]} {p[1]}'
def p_corpoescreve_null(p):
    "corpoescreve : "
    p[0] = f' '

def p_alter_frase(p):
    "alter : frase"
    p[0] = p[1:-1]

def p_alter_frase(p):
    "alter : expr"
    p[0] = f'p{1}'



