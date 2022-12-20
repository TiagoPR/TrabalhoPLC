import ply.yacc as yacc

from linguagem_lex import tokens
## TEMA DE DISCUSSÃO ADICIONAR NOT NAS OPRELACAO ??????????????
def p_bool_true(p):
    "bool : TRUE"
    p[0] = f'1'

def p_bool_false(p):
    "bool : FALSE"
    p[0] = f'0'
    
def p_cond_bool(p):
    "cond : bool"
    p[0] = f'pushi{p[1]}\npushi 0\n sup\n'

def p_cond_expr(p):
    "cond : expr"
    p[0] = f'pushi{p[1]}\npushi 0\n sup\n'

def p_oprelacao_inf(p):
    "oprelacao : INF"
    p[0] = 'inf'

def p_oprelacao_infeq(p):
    "oprelacao : INFEQ"
    p[0] = 'infeq'

def p_oprelacao_sup(p):
    "oprelacao : SUP"
    p[0] = 'sup'

def p_oprelacao_supeq(p):
    "oprelacao : SUPEQ"
    p[0] = 'supeq'

def p_cond_oprelacao(p):
    "cond : expr oprelacao expr"
    p[0] = f'pushi {p[1]}\npushi {p[3]}\np[1]'

def p_cond_e(p):
    "cond : cond E cond"
    p[0] = f'pushi{p[1]}\npushi{p[3]}\nadd\npushi 2\nequal\n'

def p_cond_ou(p):
    "cond : cond OU cond"
    p[0] = f'pushi{p[1]}\npushi{p[3]}\nadd\npushi 0\nsup\n'

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



