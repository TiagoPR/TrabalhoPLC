import ply.yacc as yacc
import sys

from linguagem_lex import tokens

def p_Programa(p):
    "Programa : Vars Funcs Cod"
    parser.assembly = f'START\n{p[1]}{p[3]}STOP\n{p[2]}'

def p_Escrever(p):
    "Escrever : PRINT corpoescreve '.'"
    p[0] = f"{p[2]}"

def p_corpoescreve_null(p):
    "corpoescreve : "
    p[0] = f''

def p_corpoescreve_alter(p):
    "corpoescreve : alter corpoescreve"
    p[0] = f'{p[1]}\n{p[2]}'

def p_alter_frase(p):
    "alter : FRASE"
    p[0] = f'pushs {p[1]}\nWRITES'


def p_alter_expr(p):
    "alter : expr"
    p[0] = f'{p[1]}WRITEI'


def p_Vars_Empty(p):
    "Vars : "
    p[0] = f''

def p_Vars_Var(p):
    "Vars : var Vars"
    p[0] = f'{p[1]}{p[2]}'

def p_Funcs_Empty(p):
    "Funcs : "
    p[0] = f''

def p_Funcs_Func(p):
    "Funcs : Funcs Func"
    p[0] = f'{p[1]}\n{p[2]}'

def p_Func_comRETURN(p):
    "Func : ID begin Cod end return expr '.'"
    p[0] = f'{p[1]}:\n{p[3]}\n{p[6]}return\n'

def p_Func(p):
    "Func : ID begin Cod end '.'"
    p[0] = f'{p[1]}:\n{p[3]}\nreturn\n'

def p_Cod_Empty(p):
    "Cod : "
    p[0] = f''

def p_var_tipoID(p):
    "var : INT ID '.'"
    var = p[2]
    p.parser.table[var] = parser.pc
    parser.pc += 1
    p[0] = "PUSHI 0\n"


def p_var_atribuicao(p):
    "var : INT ID '=' expr '.'"
    var = p[2]
    p.parser.table[var] = parser.pc
    parser.pc += 1
    p[0] = f"{p[4]}"

def p_Cod_linhas(p):
    "Cod : Linha Cod"
    p[0] = f'{p[1]} {p[2]}'

def p_Linha_Escrever(p):
    "Linha : Escrever"
    p[0] = p[1]

def p_Linha_atr(p):
    "Linha : atr"
    p[0] = p[1]

def p_linha_func(p):
    "Linha : ID '(' ')' '.'"
    p[0] = f'pusha {p[1]}\nCALL\n'

def p_Linha_Ler(p):
    "Linha : Ler"
    p[0] = p[1]

def p_Linha_Cond(p):
    "Linha : cond"
    p[0] = f'{p[1]}\n'

def p_Linha_Se(p):
    'Linha : SE'
    p[0] = p[1]

def p_se_else(p):
    'SE : IF cond THEN Cod ELSE Cod '
    p[0] = f'{p[2]}JZ l{p.parser.labels}\n{p[4]}JUMP l{p.parser.labels}f\nl{p.parser.labels}: NOP\n{p[6]}l{p.parser.labels}f: NOP\n'
    p.parser.labels += 1

#def p_se_then(p):
   # 'SE : IF cond THEN Cod '
   # p[0] = f'{p[2]}JZ l{p.parser.labels}\n{p[4]}JUMP l{p.parser.labels}f\nl{p.parser.labels}: NOP\n{p[6]}l{p.parser.labels}f: NOP\n'
   # p.parser.labels += 1

def p_ler(p):
    "Ler : ID '=' INPUT FRASE '.'"
    p[0] = f"pushs {p[4]}\nWRITES\nread\natoi\nstoreg {parser.table[p[1]]}\n"

def p_Linha_Ciclo(p):
    "Linha : Ciclo"
    p[0] = p[1]

def p_ciclo(p):
    "Ciclo : WHILE cond DO Cod end WHILE '.'"
    p[0] = f'comeco{p.parser.labels}: \n{p[2]}\nJZ terminar{p.parser.labels}\n{p[4]}JUMP comeco{p.parser.labels}\nterminar{p.parser.labels}: \n'
    p.parser.labels += 1

def p_atr(p):
    "atr : ID '=' expr '.'"
    p[0] = f'{p[3]}storeg {parser.table[p[1]]}\n'

def p_atr_func(p):
    "atr : ID '=' ID '(' ')' '.'"
    p[0] = f'pusha {p[3]}\nCALL\nstoreg {parser.table[p[1]]}\n'

def p_bool_true(p):
    "bool : TRUE"
    p[0] = f'PUSHI 1'

def p_bool_false(p):
    "bool : FALSE"
    p[0] = f'PUSHI 0'

def p_cond_bool(p):
    "cond : bool"
    p[0] = f'{p[1]}'

def p_cond_expr(p):
    "cond : expr"
    p[0] = f'{p[1]}pushi 0\nsup'

def p_oprelacao_inf(p):
    "oprelacao : INF"
    p[0] = 'inf'

def p_oprelacao_EQUALS(p):
    "oprelacao : EQUAL"
    p[0] = 'EQUAL\n'

def p_oprelacao_DIFF(p):
    "oprelacao : DIFF"
    p[0] = 'EQUAL\nNOT\n'

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
    p[0] = f'{p[1]}{p[3]}{p[2]}'

def p_cond_e(p):
    "cond : cond E cond"
    p[0] = f'{p[1]}\n{p[3]}\nadd\npushi 2\nequal'

def p_cond_ou(p):
    "cond : cond OU cond"
    p[0] = f'{p[1]}\n{p[3]}\nadd\npushi 0\nsup'

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

def p_termo_mod(p):
    "termo : termo '%' fator"
    p[0] = p[1] + p[3] + "MOD\n"

def p_termo_fator(p):
    "termo : fator"
    p[0] = p[1]

def p_fator_NUM(p):
    "fator : NUM"
    p[0] = f"PUSHI {p[1]}\n"


def p_fator_ID(p):
    "fator : ID"
    p[0] = f'PUSHG {parser.table[p[1]]}\n'


def p_fator_expr(p):
    "fator : '(' expr ')'"
    p[0] = p[2]

def p_error(p):
    print("Syntax error:", p)
    parser.sucesso = False

#inicio do Parser e do Processamento
parser = yacc.yacc()
parser.table = {}
parser.pc = 0

parser.sucesso = True
parser.assembly = ""
parser.labels = 0

fonte = ""
for linha in sys.stdin:
    fonte += linha

parser.parse(fonte)

print(parser.table)
print(parser.assembly)
