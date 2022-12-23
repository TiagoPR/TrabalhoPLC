import ply.yacc as yacc

from linguagem_lex import tokens

#Breno ----------------------------------------------------------------------------------------------------------------

## TEMA DE DISCUSSÃO ADICIONAR NOT NAS OPRELACAO ??????????????  , o Cond ta certo de fato ele retorna ?????????
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
    "alter : FRASE"
    p[0] = p[1:-1]

def p_alter_frase(p):
    "alter : expr"
    p[0] = f'p{1}'


def p_ciclo(p):
    "while : WHILE Cond DO Corpo "
    p[0] = f'l{p.parser.labels}c: NOP\n{p[2]}JZ l{p.parser.labels}f\n{p[4]}JUMP l{p.parser.labels}c\nl{p.parser.labels}f: NOP\n'
    p.parser.labels += 1
    
# Tiago ----------------------------------------------------------------------

def p_Programa(p):
    "Programa : Vars Funcs Cod"
    parser.assembly = f'START\n{p[1]}{p[2]}{p[3]}STOP'

def p_Vars_Empty(p):
    "Vars : "
    p[0] = f' '

def p_Vars_Var(p):
    "Vars : Vars Var"
    p[0] = f'{p[1]}{p[2]}'

def p_Funcs_Empty(p):
    "Funcs : "
    p[0] = f' '

def p_Funcs_Func(p):
    "Funcs : Funcs Func"
    p[0] = f'{p[1]}{p[2]}'

def p_Func(p):
    "Func : PAL begin Cod return Expr end"
    p[0] = f'{p[1]}:\n{p[2]}\nret'

def p_Cod_linha(p):
    "Cod : Linha"
    p[0] = f'{p[0]}'

def p_Cod_linhas(p):
    "Cod : Linha Cod"
    p[0] = f'{p[0]} {p[1]}'

def p_Linha_Escrever(p):
    "Linha : Escrever"
    p[0] = p[1]

def p_Linha_Atr(p):
    "Linha : Atr"
    p[0] = p[1]

def p_Linha_Ler(p):
    "Linha : Ler"
    p[0] = p[1]

def p_Linha_Se(p):
    "Linha : SE"
    p[0] = p[1]

def p_Linha_Ciclo(p):
    "Linha : Ciclo"
    p[0] = p[1]

def p_error(p):
    print('Syntax error!')
    parser.sucesso = False

#---------------------------------------------------- Tales

def p_SE(p):
    "SE : IF cond THEN Cod ELSE Cod"
    p[0] = f"PUSHI{p[2]} JZ p1{p.parser.labels}\n {p[3]} JUMP fim{p.parser.labels}\n p1{p.parser.labels}\n {p[5]} fim{p.parser.labels}"
    p.parser.labels += 1

def p_var_tipoID(p):
    "var : Tipo ID ."
    var = p[2]
    p.parser.table[var] = p[2]
    p[0] = "PUSHI 0"

def p_var_expr(p):
    "var : Tipo ID = expr ."
    var = p[2]
    p.parser.table[var] = p[4]

def p_expr_add(p):
    "expr : expr '+' termo"
    p[0] = p[1] + p[3] + "ADD\n"

def p_expr_sub(p):
    "expr : expr '-' termo"
    p[0] = p[1] + p[3] + "SUB\n"

def p_expr_termo(p):
    "expr : termo"
    p[0] = p[1]

def p_termo_mul(p):
    "termo : termo '*' fator"
    p[0] = p[1] + p[3] + "MUL\n"

def p_termo_div(p):
    "termo : termo '/' fator"
    p[0] = p[1] + p[3] + "DIV\n"

def fator_NUM(p):
    "fator : NUM"
    p[0] = f"PUSHI {p[1]}"

def fator_ID(p):
    "fator : ID"
    p[0] = p.parser.table[p[1]]

def fator_func(p):
    "fator : func"
    p[0] = p[1]

def fator_expr(p):
    "fator : '(' expr ')'"
    p[0] = p[2]

#inicio do Parser e do Processamento
parser = yacc.yacc()
parser.table = {}

parser.sucesso = True
parser.assembly = ""
parser.labels = 0
