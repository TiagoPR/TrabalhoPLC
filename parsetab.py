
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "DIFF DO E ELSE EQUAL FALSE FRASE ID IF INF INFEQ INPUT INT NUM OU PRINT SUP SUPEQ THEN TRUE WHILE begin end returnPrograma : Vars Funcs CodEscrever : PRINT corpoescreve '.'corpoescreve : corpoescreve : alter corpoescrevealter : FRASEalter : exprVars : Vars : var VarsFuncs : Funcs : Funcs FuncFunc : ID begin Cod end return expr '.'Func : ID begin Cod end '.'Cod : var : INT ID '.'var : INT ID '=' expr '.'Cod : Linha CodLinha : EscreverLinha : atrLinha : ID '(' ')' '.'Linha : LerLinha : condLinha : SESE : IF cond THEN Cod ELSE Cod Ler : ID '=' INPUT FRASE '.'Linha : CicloCiclo : WHILE cond DO Cod end WHILE '.'atr : ID '=' expr '.'atr : ID '=' ID '(' ')' '.'bool : TRUEbool : FALSEcond : boolcond : exproprelacao : INFoprelacao : EQUALoprelacao : DIFFoprelacao : INFEQoprelacao : SUPoprelacao : SUPEQcond : expr oprelacao exprcond : cond E condcond : cond OU condexpr : expr '+' termoexpr : expr '-' termoexpr : termotermo : termo '*' fatortermo : termo '/' fatortermo : termo '%' fatortermo : fatorfator : NUMfator : IDfator : '(' expr ')'"
    
_lr_action_items = {'ID':([0,2,3,4,5,6,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,37,38,39,40,41,42,43,44,46,47,48,50,51,52,55,56,57,64,65,66,67,68,69,70,72,73,74,75,76,77,79,81,85,86,88,89,92,93,95,96,],[-7,-9,-7,7,11,-8,-10,32,-50,-32,-17,-18,46,-20,-21,-22,-25,46,-31,46,46,-29,-30,-44,-48,-49,-14,46,-16,-50,32,61,46,46,46,-33,-34,-35,-36,-37,-38,-50,46,46,46,-5,-6,46,46,46,-39,-42,-43,-51,-40,-41,-2,32,32,-45,-46,-47,-15,-19,-27,46,-12,-24,32,-28,-23,-11,-26,]),'PRINT':([0,2,3,5,6,9,10,11,12,13,14,16,17,18,19,21,24,25,26,27,28,29,31,32,33,46,64,65,66,67,68,69,70,72,73,74,75,76,77,79,81,86,88,89,92,93,95,96,],[-7,-9,-7,20,-8,-10,20,-50,-32,-17,-18,-20,-21,-22,-25,-31,-29,-30,-44,-48,-49,-14,-16,-50,20,-50,-39,-42,-43,-51,-40,-41,-2,20,20,-45,-46,-47,-15,-19,-27,-12,-24,20,-28,-23,-11,-26,]),'IF':([0,2,3,5,6,9,10,11,12,13,14,16,17,18,19,21,24,25,26,27,28,29,31,32,33,46,64,65,66,67,68,69,70,72,73,74,75,76,77,79,81,86,88,89,92,93,95,96,],[-7,-9,-7,22,-8,-10,22,-50,-32,-17,-18,-20,-21,-22,-25,-31,-29,-30,-44,-48,-49,-14,-16,-50,22,-50,-39,-42,-43,-51,-40,-41,-2,22,22,-45,-46,-47,-15,-19,-27,-12,-24,22,-28,-23,-11,-26,]),'WHILE':([0,2,3,5,6,9,10,11,12,13,14,16,17,18,19,21,24,25,26,27,28,29,31,32,33,46,64,65,66,67,68,69,70,72,73,74,75,76,77,79,81,86,88,89,90,92,93,95,96,],[-7,-9,-7,23,-8,-10,23,-50,-32,-17,-18,-20,-21,-22,-25,-31,-29,-30,-44,-48,-49,-14,-16,-50,23,-50,-39,-42,-43,-51,-40,-41,-2,23,23,-45,-46,-47,-15,-19,-27,-12,-24,23,94,-28,-23,-11,-26,]),'TRUE':([0,2,3,5,6,9,10,11,12,13,14,16,17,18,19,21,22,23,24,25,26,27,28,29,31,32,33,46,47,48,64,65,66,67,68,69,70,72,73,74,75,76,77,79,81,86,88,89,92,93,95,96,],[-7,-9,-7,24,-8,-10,24,-50,-32,-17,-18,-20,-21,-22,-25,-31,24,24,-29,-30,-44,-48,-49,-14,-16,-50,24,-50,24,24,-39,-42,-43,-51,-40,-41,-2,24,24,-45,-46,-47,-15,-19,-27,-12,-24,24,-28,-23,-11,-26,]),'FALSE':([0,2,3,5,6,9,10,11,12,13,14,16,17,18,19,21,22,23,24,25,26,27,28,29,31,32,33,46,47,48,64,65,66,67,68,69,70,72,73,74,75,76,77,79,81,86,88,89,92,93,95,96,],[-7,-9,-7,25,-8,-10,25,-50,-32,-17,-18,-20,-21,-22,-25,-31,25,25,-29,-30,-44,-48,-49,-14,-16,-50,25,-50,25,25,-39,-42,-43,-51,-40,-41,-2,25,25,-45,-46,-47,-15,-19,-27,-12,-24,25,-28,-23,-11,-26,]),'NUM':([0,2,3,5,6,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,37,38,39,40,41,42,43,44,46,47,48,50,51,52,55,56,57,64,65,66,67,68,69,70,72,73,74,75,76,77,79,81,85,86,88,89,92,93,95,96,],[-7,-9,-7,28,-8,-10,28,-50,-32,-17,-18,28,-20,-21,-22,-25,28,-31,28,28,-29,-30,-44,-48,-49,-14,28,-16,-50,28,28,28,28,28,-33,-34,-35,-36,-37,-38,-50,28,28,28,-5,-6,28,28,28,-39,-42,-43,-51,-40,-41,-2,28,28,-45,-46,-47,-15,-19,-27,28,-12,-24,28,-28,-23,-11,-26,]),'(':([0,2,3,5,6,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,37,38,39,40,41,42,43,44,46,47,48,50,51,52,55,56,57,61,64,65,66,67,68,69,70,72,73,74,75,76,77,79,81,85,86,88,89,92,93,95,96,],[-7,-9,-7,15,-8,-10,15,34,-32,-17,-18,15,-20,-21,-22,-25,15,-31,15,15,-29,-30,-44,-48,-49,-14,15,-16,34,15,15,15,15,15,-33,-34,-35,-36,-37,-38,-50,15,15,15,-5,-6,15,15,15,80,-39,-42,-43,-51,-40,-41,-2,15,15,-45,-46,-47,-15,-19,-27,15,-12,-24,15,-28,-23,-11,-26,]),'$end':([0,1,2,3,5,6,8,9,10,11,12,13,14,16,17,18,19,21,24,25,26,27,28,29,31,32,46,64,65,66,67,68,69,70,74,75,76,77,79,81,86,88,89,92,93,95,96,],[-7,0,-9,-7,-13,-8,-1,-10,-13,-50,-32,-17,-18,-20,-21,-22,-25,-31,-29,-30,-44,-48,-49,-14,-16,-50,-50,-39,-42,-43,-51,-40,-41,-2,-45,-46,-47,-15,-19,-27,-12,-24,-13,-28,-23,-11,-26,]),'INT':([0,3,29,77,],[4,4,-14,-15,]),'.':([7,20,26,27,28,46,49,50,51,52,58,60,61,62,65,66,67,71,74,75,76,78,82,87,91,94,],[29,-3,-44,-48,-49,-50,70,-3,-5,-6,77,79,-50,81,-42,-43,-51,-4,-45,-46,-47,86,88,92,95,96,]),'=':([7,11,32,],[30,35,35,]),'end':([10,12,13,14,16,17,18,19,21,24,25,26,27,28,31,32,33,46,59,64,65,66,67,68,69,70,73,74,75,76,79,81,84,88,89,92,93,96,],[-13,-32,-17,-18,-20,-21,-22,-25,-31,-29,-30,-44,-48,-49,-16,-50,-13,-50,78,-39,-42,-43,-51,-40,-41,-2,-13,-45,-46,-47,-19,-27,90,-24,-13,-28,-23,-26,]),'ELSE':([10,12,13,14,16,17,18,19,21,24,25,26,27,28,31,32,46,64,65,66,67,68,69,70,72,74,75,76,79,81,83,88,89,92,93,96,],[-13,-32,-17,-18,-20,-21,-22,-25,-31,-29,-30,-44,-48,-49,-16,-50,-50,-39,-42,-43,-51,-40,-41,-2,-13,-45,-46,-47,-19,-27,89,-24,-13,-28,-23,-26,]),'begin':([11,],[33,]),'*':([11,26,27,28,32,46,61,65,66,67,74,75,76,],[-50,55,-48,-49,-50,-50,-50,55,55,-51,-45,-46,-47,]),'/':([11,26,27,28,32,46,61,65,66,67,74,75,76,],[-50,56,-48,-49,-50,-50,-50,56,56,-51,-45,-46,-47,]),'%':([11,26,27,28,32,46,61,65,66,67,74,75,76,],[-50,57,-48,-49,-50,-50,-50,57,57,-51,-45,-46,-47,]),'+':([11,12,26,27,28,32,45,46,52,58,61,62,64,65,66,67,74,75,76,91,],[-50,37,-44,-48,-49,-50,37,-50,37,37,-50,37,37,-42,-43,-51,-45,-46,-47,37,]),'-':([11,12,26,27,28,32,45,46,52,58,61,62,64,65,66,67,74,75,76,91,],[-50,38,-44,-48,-49,-50,38,-50,38,38,-50,38,38,-42,-43,-51,-45,-46,-47,38,]),'INF':([11,12,26,27,28,32,46,65,66,67,74,75,76,],[-50,39,-44,-48,-49,-50,-50,-42,-43,-51,-45,-46,-47,]),'EQUAL':([11,12,26,27,28,32,46,65,66,67,74,75,76,],[-50,40,-44,-48,-49,-50,-50,-42,-43,-51,-45,-46,-47,]),'DIFF':([11,12,26,27,28,32,46,65,66,67,74,75,76,],[-50,41,-44,-48,-49,-50,-50,-42,-43,-51,-45,-46,-47,]),'INFEQ':([11,12,26,27,28,32,46,65,66,67,74,75,76,],[-50,42,-44,-48,-49,-50,-50,-42,-43,-51,-45,-46,-47,]),'SUP':([11,12,26,27,28,32,46,65,66,67,74,75,76,],[-50,43,-44,-48,-49,-50,-50,-42,-43,-51,-45,-46,-47,]),'SUPEQ':([11,12,26,27,28,32,46,65,66,67,74,75,76,],[-50,44,-44,-48,-49,-50,-50,-42,-43,-51,-45,-46,-47,]),'E':([11,12,17,21,24,25,26,27,28,32,46,53,54,64,65,66,67,68,69,74,75,76,],[-50,-32,47,-31,-29,-30,-44,-48,-49,-50,-50,47,47,-39,-42,-43,-51,47,47,-45,-46,-47,]),'OU':([11,12,17,21,24,25,26,27,28,32,46,53,54,64,65,66,67,68,69,74,75,76,],[-50,-32,48,-31,-29,-30,-44,-48,-49,-50,-50,48,48,-39,-42,-43,-51,48,48,-45,-46,-47,]),'THEN':([12,21,24,25,26,27,28,46,53,64,65,66,67,68,69,74,75,76,],[-32,-31,-29,-30,-44,-48,-49,-50,72,-39,-42,-43,-51,-40,-41,-45,-46,-47,]),'DO':([12,21,24,25,26,27,28,46,54,64,65,66,67,68,69,74,75,76,],[-32,-31,-29,-30,-44,-48,-49,-50,73,-39,-42,-43,-51,-40,-41,-45,-46,-47,]),'FRASE':([20,26,27,28,46,50,51,52,63,65,66,67,74,75,76,],[51,-44,-48,-49,-50,51,-5,-6,82,-42,-43,-51,-45,-46,-47,]),')':([26,27,28,34,45,46,65,66,67,74,75,76,80,],[-44,-48,-49,60,67,-50,-42,-43,-51,-45,-46,-47,87,]),'INPUT':([35,],[63,]),'return':([78,],[85,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Programa':([0,],[1,]),'Vars':([0,3,],[2,6,]),'var':([0,3,],[3,3,]),'Funcs':([2,],[5,]),'Cod':([5,10,33,72,73,89,],[8,31,59,83,84,93,]),'Func':([5,],[9,]),'Linha':([5,10,33,72,73,89,],[10,10,10,10,10,10,]),'expr':([5,10,15,20,22,23,30,33,35,36,47,48,50,72,73,85,89,],[12,12,45,52,12,12,58,12,62,64,12,12,52,12,12,91,12,]),'Escrever':([5,10,33,72,73,89,],[13,13,13,13,13,13,]),'atr':([5,10,33,72,73,89,],[14,14,14,14,14,14,]),'Ler':([5,10,33,72,73,89,],[16,16,16,16,16,16,]),'cond':([5,10,22,23,33,47,48,72,73,89,],[17,17,53,54,17,68,69,17,17,17,]),'SE':([5,10,33,72,73,89,],[18,18,18,18,18,18,]),'Ciclo':([5,10,33,72,73,89,],[19,19,19,19,19,19,]),'bool':([5,10,22,23,33,47,48,72,73,89,],[21,21,21,21,21,21,21,21,21,21,]),'termo':([5,10,15,20,22,23,30,33,35,36,37,38,47,48,50,72,73,85,89,],[26,26,26,26,26,26,26,26,26,26,65,66,26,26,26,26,26,26,26,]),'fator':([5,10,15,20,22,23,30,33,35,36,37,38,47,48,50,55,56,57,72,73,85,89,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,74,75,76,27,27,27,27,]),'oprelacao':([12,],[36,]),'corpoescreve':([20,50,],[49,71,]),'alter':([20,50,],[50,50,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Programa","S'",1,None,None,None),
  ('Programa -> Vars Funcs Cod','Programa',3,'p_Programa','linguagem_yacc.py',7),
  ('Escrever -> PRINT corpoescreve .','Escrever',3,'p_Escrever','linguagem_yacc.py',11),
  ('corpoescreve -> <empty>','corpoescreve',0,'p_corpoescreve_null','linguagem_yacc.py',15),
  ('corpoescreve -> alter corpoescreve','corpoescreve',2,'p_corpoescreve_alter','linguagem_yacc.py',19),
  ('alter -> FRASE','alter',1,'p_alter_frase','linguagem_yacc.py',23),
  ('alter -> expr','alter',1,'p_alter_expr','linguagem_yacc.py',28),
  ('Vars -> <empty>','Vars',0,'p_Vars_Empty','linguagem_yacc.py',33),
  ('Vars -> var Vars','Vars',2,'p_Vars_Var','linguagem_yacc.py',37),
  ('Funcs -> <empty>','Funcs',0,'p_Funcs_Empty','linguagem_yacc.py',41),
  ('Funcs -> Funcs Func','Funcs',2,'p_Funcs_Func','linguagem_yacc.py',45),
  ('Func -> ID begin Cod end return expr .','Func',7,'p_Func_comRETURN','linguagem_yacc.py',49),
  ('Func -> ID begin Cod end .','Func',5,'p_Func','linguagem_yacc.py',53),
  ('Cod -> <empty>','Cod',0,'p_Cod_Empty','linguagem_yacc.py',57),
  ('var -> INT ID .','var',3,'p_var_tipoID','linguagem_yacc.py',61),
  ('var -> INT ID = expr .','var',5,'p_var_atribuicao','linguagem_yacc.py',69),
  ('Cod -> Linha Cod','Cod',2,'p_Cod_linhas','linguagem_yacc.py',76),
  ('Linha -> Escrever','Linha',1,'p_Linha_Escrever','linguagem_yacc.py',80),
  ('Linha -> atr','Linha',1,'p_Linha_atr','linguagem_yacc.py',84),
  ('Linha -> ID ( ) .','Linha',4,'p_linha_func','linguagem_yacc.py',88),
  ('Linha -> Ler','Linha',1,'p_Linha_Ler','linguagem_yacc.py',92),
  ('Linha -> cond','Linha',1,'p_Linha_Cond','linguagem_yacc.py',96),
  ('Linha -> SE','Linha',1,'p_Linha_Se','linguagem_yacc.py',100),
  ('SE -> IF cond THEN Cod ELSE Cod','SE',6,'p_se_else','linguagem_yacc.py',104),
  ('Ler -> ID = INPUT FRASE .','Ler',5,'p_ler','linguagem_yacc.py',114),
  ('Linha -> Ciclo','Linha',1,'p_Linha_Ciclo','linguagem_yacc.py',118),
  ('Ciclo -> WHILE cond DO Cod end WHILE .','Ciclo',7,'p_ciclo','linguagem_yacc.py',122),
  ('atr -> ID = expr .','atr',4,'p_atr','linguagem_yacc.py',127),
  ('atr -> ID = ID ( ) .','atr',6,'p_atr_func','linguagem_yacc.py',131),
  ('bool -> TRUE','bool',1,'p_bool_true','linguagem_yacc.py',135),
  ('bool -> FALSE','bool',1,'p_bool_false','linguagem_yacc.py',139),
  ('cond -> bool','cond',1,'p_cond_bool','linguagem_yacc.py',143),
  ('cond -> expr','cond',1,'p_cond_expr','linguagem_yacc.py',147),
  ('oprelacao -> INF','oprelacao',1,'p_oprelacao_inf','linguagem_yacc.py',151),
  ('oprelacao -> EQUAL','oprelacao',1,'p_oprelacao_EQUALS','linguagem_yacc.py',155),
  ('oprelacao -> DIFF','oprelacao',1,'p_oprelacao_DIFF','linguagem_yacc.py',159),
  ('oprelacao -> INFEQ','oprelacao',1,'p_oprelacao_infeq','linguagem_yacc.py',163),
  ('oprelacao -> SUP','oprelacao',1,'p_oprelacao_sup','linguagem_yacc.py',167),
  ('oprelacao -> SUPEQ','oprelacao',1,'p_oprelacao_supeq','linguagem_yacc.py',171),
  ('cond -> expr oprelacao expr','cond',3,'p_cond_oprelacao','linguagem_yacc.py',175),
  ('cond -> cond E cond','cond',3,'p_cond_e','linguagem_yacc.py',179),
  ('cond -> cond OU cond','cond',3,'p_cond_ou','linguagem_yacc.py',183),
  ('expr -> expr + termo','expr',3,'p_expr_add','linguagem_yacc.py',187),
  ('expr -> expr - termo','expr',3,'p_expr_sub','linguagem_yacc.py',191),
  ('expr -> termo','expr',1,'p_expr_termo','linguagem_yacc.py',195),
  ('termo -> termo * fator','termo',3,'p_termo_mul','linguagem_yacc.py',199),
  ('termo -> termo / fator','termo',3,'p_termo_div','linguagem_yacc.py',203),
  ('termo -> termo % fator','termo',3,'p_termo_mod','linguagem_yacc.py',207),
  ('termo -> fator','termo',1,'p_termo_fator','linguagem_yacc.py',211),
  ('fator -> NUM','fator',1,'p_fator_NUM','linguagem_yacc.py',215),
  ('fator -> ID','fator',1,'p_fator_ID','linguagem_yacc.py',220),
  ('fator -> ( expr )','fator',3,'p_fator_expr','linguagem_yacc.py',225),
]
