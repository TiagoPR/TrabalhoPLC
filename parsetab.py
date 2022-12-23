
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "DO E ELSE FALSE FRASE ID IF INF INFEQ INPUT INT NUM OU PRINT SUP SUPEQ THEN TRUE WHILEPrograma : Vars CodVars : Vars : var VarsCod : var : INT ID '.'var : INT ID '=' expr '.'expr : expr '+' termoexpr : expr '-' termoexpr : termotermo : termo '*' fatortermo : termo '/' fatortermo : fatorfator : NUMfator : IDfator : '(' expr ')'"
    
_lr_action_items = {'$end':([0,1,2,3,5,6,8,16,],[-2,0,-4,-2,-1,-3,-5,-6,]),'INT':([0,3,8,16,],[4,4,-5,-6,]),'ID':([4,9,15,17,18,19,20,],[7,10,10,10,10,10,10,]),'.':([7,10,11,12,13,14,22,23,24,25,26,],[8,-14,16,-9,-12,-13,-7,-8,-10,-11,-15,]),'=':([7,],[9,]),'NUM':([9,15,17,18,19,20,],[14,14,14,14,14,14,]),'(':([9,15,17,18,19,20,],[15,15,15,15,15,15,]),'*':([10,12,13,14,22,23,24,25,26,],[-14,19,-12,-13,19,19,-10,-11,-15,]),'/':([10,12,13,14,22,23,24,25,26,],[-14,20,-12,-13,20,20,-10,-11,-15,]),'+':([10,11,12,13,14,21,22,23,24,25,26,],[-14,17,-9,-12,-13,17,-7,-8,-10,-11,-15,]),'-':([10,11,12,13,14,21,22,23,24,25,26,],[-14,18,-9,-12,-13,18,-7,-8,-10,-11,-15,]),')':([10,12,13,14,21,22,23,24,25,26,],[-14,-9,-12,-13,26,-7,-8,-10,-11,-15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Programa':([0,],[1,]),'Vars':([0,3,],[2,6,]),'var':([0,3,],[3,3,]),'Cod':([2,],[5,]),'expr':([9,15,],[11,21,]),'termo':([9,15,17,18,],[12,12,22,23,]),'fator':([9,15,17,18,19,20,],[13,13,13,13,24,25,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Programa","S'",1,None,None,None),
  ('Programa -> Vars Cod','Programa',2,'p_Programa','linguagem_yacc.py',86),
  ('Vars -> <empty>','Vars',0,'p_Vars_Empty','linguagem_yacc.py',91),
  ('Vars -> var Vars','Vars',2,'p_Vars_Var','linguagem_yacc.py',95),
  ('Cod -> <empty>','Cod',0,'p_Cod_Empty','linguagem_yacc.py',115),
  ('var -> INT ID .','var',3,'p_var_tipoID','linguagem_yacc.py',119),
  ('var -> INT ID = expr .','var',5,'p_var_atribuicao','linguagem_yacc.py',127),
  ('expr -> expr + termo','expr',3,'p_expr_add','linguagem_yacc.py',177),
  ('expr -> expr - termo','expr',3,'p_expr_sub','linguagem_yacc.py',181),
  ('expr -> termo','expr',1,'p_expr_termo','linguagem_yacc.py',185),
  ('termo -> termo * fator','termo',3,'p_termo_mul','linguagem_yacc.py',189),
  ('termo -> termo / fator','termo',3,'p_termo_div','linguagem_yacc.py',193),
  ('termo -> fator','termo',1,'p_termo_fator','linguagem_yacc.py',197),
  ('fator -> NUM','fator',1,'p_fator_NUM','linguagem_yacc.py',201),
  ('fator -> ID','fator',1,'p_fator_ID','linguagem_yacc.py',205),
  ('fator -> ( expr )','fator',3,'p_fator_expr','linguagem_yacc.py',213),
]
