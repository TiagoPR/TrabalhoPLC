import ply.yacc as yacc

from linguagem_lex import tokens

def p_Programa(p):
    "Programa : Vars Funcs Cod"
    parser.assembly = f'START\n{p[1]}{p[2]}{p[3]}STOP'

def p_Vars_Empty(p):
    "Vars : "

def p_Vars_Var(p):
    "Vars : Vars Var"
    p[0] = f'{p[1]}{p[2]}'

def p_Funcs_Empty(p):
    "Funcs : "

def p_Funcs_Func(p):
    "Funcs : Funcs Func"
    p[0] = f'{p[1]}{p[2]}'

def p_Func(p):
    "Func : PAL begin COD return Expr end"
    p[0] = f'FUNCTION {p[1]}()'

def p_Cod_linha(p):
    "Cod : Linha"

def p_Cod_linhas(p):
    "Cod : Linha Cod"

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
    "Linha : Se"
    p[0] = p[1]

def p_Linha_Ciclo(p):
    "Linha : Ciclo"
    p[0] = p[1]

def p_error(p):
    print('Syntax error!')
    parser.sucesso = False
    
#inicio do Parser e do Processamento
parser = yacc.yacc()

parser.sucesso = True
parser.assembly = ""
