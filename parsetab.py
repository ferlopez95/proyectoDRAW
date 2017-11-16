
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'POINT PLUS MINUS TIMES DIVIDE LESS LESSEQUAL GREATER GREATEREQUAL EQUAL DEQUAL DISTINT SEMICOLON COMMA LPAREN RPAREN LBRACKET RBRACKET PERCENT AND OR ID CTE_I CTE_F IF ELSE INT FLOAT BOOLEAN DRAW ARRAY MAIN GLOBAL DEF END VOID WHILE FOR RETURN TRUE FALSE SETPOSITION SETCOLOR SPEED FORWARD LEFT RIGHT BACK HIDE SHOW CLEAR SQUARE CIRCLE NEWDRAW PRINTprograma : init globales funciones programa_end\n    | init funciones programa_end init : empty  programa_end : empty funciones : funciones_2 mainfunciones_2 : funcion funciones_2\n    | emptyglobales : global_1 vars globales_2 globales_2 : global_1 vars globales_2\n    | empty  global_1 : GLOBAL bloque : estatuto bloque\n    | emptydata_type : INT\n    | FLOAT\n    | BOOLEANdata_type_func : INT\n    | FLOAT\n    | BOOLEANmain : main_1 bloque END main_1 : MAIN LPAREN RPARENestatuto : asignacion\n    | condicion\n    | ciclo\n    | accion\n    | vars\n    | llamada SEMICOLON\n    | print print : PRINT LPAREN super_exp RPAREN SEMICOLON asignacion : asignacion_id asignacion_2 SEMICOLONasignacion_id : IDasignacion_2 : asignacion_equal super_exp\n    | LBRACKET exp asignacion_3 EQUAL super_expasignacion_equal : EQUALasignacion_3 : RBRACKET\n    | COMMA exp RBRACKETvars : DRAW ID EQUAL NEWDRAW LPAREN RPAREN SEMICOLON\n    | vars_id vars2\n    | vars_auxvars_id : data_type ID vars_aux : array vars3  array : ARRAY LESS data_type COMMA CTE_I array_2 GREATER ID array_2 : COMMA CTE_I\n    | empty vars2 : asignacion_equal super_exp SEMICOLON\n    | SEMICOLONvars3 : EQUAL def_array SEMICOLON\n    | SEMICOLONllamada : llamada_id llamada_2 llamada_id : ID LPARENllamada_2 : llamada_exp llamada_rparen\n    | llamada_rparenllamada_rparen : RPARENllamada_exp : llamada_super_exp llamada_exp2llamada_super_exp : super_expllamada_exp2 : llamada_comma llamada_exp\n    | emptyllamada_comma : COMMAdef_array : LBRACKET def_array_2 def_array_2 : def_array_cte RBRACKET\n    | RBRACKETdef_array_cte : super_exp def_array_cte_2def_array_cte_2 : COMMA def_array_cte\n    | emptysuper_exp : expresion super_exp_2super_exp_2 :  logicop super_exp\n    | emptyexpresion : exp expresion_2expresion_2 : relop exp\n    | emptyrelop : GREATER\n    | GREATEREQUAL\n    | LESS\n    | LESSEQUAL\n    | DEQUAL\n    | DISTINTexp : termino exp_2exp_2 : addop exp\n    | emptytermino : factor termino_2termino_2 : timesop termino\n    | emptyvar_cte : var_cte_1\n    | var_cte_i\n    | var_cte_f\n    | var_cte_b\n    | llamada var_cte_i : CTE_I  var_cte_f : CTE_F  var_cte_b : TRUE\n    | FALSE  var_cte_1 : ID var_cte_2  var_cte_2 : LBRACKET super_exp var_cte_3\n    | empty var_cte_3 : RBRACKET\n    | COMMA super_exp RBRACKETfactor : lparen_factor super_exp rparen_factor\n    | addop var_cte\n    | var_ctelparen_factor : LPARENrparen_factor : RPARENcondicion : condicion_id LPAREN super_exp rparen_condicion bloque condicion_2 rparen_condicion : RPAREN condicion_id : IFcondicion_2 : condicion_end\n    | condicion_else  bloque condicion_end condicion_else : ELSE  condicion_end : END ciclo : for\n    | whileaccion : ID POINT accion_nombre accion_params SEMICOLON accion_params : LPAREN accion_params_2  accion_params_2 : accion_params_cte RPAREN\n    | RPAREN  accion_params_cte : var_cte accion_params_cte_2 accion_params_cte_2 : COMMA accion_params_cte\n    | empty  accion_nombre :  SETPOSITION\n    | CIRCLE\n    | RIGHT\n    | LEFT\n    | HIDE\n    | SQUARE\n    | CLEAR\n    | SHOW\n    | BACK\n    | SPEED\n    | FORWARD\n    | SETCOLOR for : for_init LPAREN for_exp COMMA for_exp COMMA for_exp2 for_rparen bloque for_endfor_exp : expfor_exp2 : expfor_rparen : RPAREN for_init : FOR  for_end : END while : while_init LPAREN super_exp rparen_while bloque while_end while_init : WHILE rparen_while : RPAREN while_end : END funcion :  DEF funcion_aux  funcion_aux : funcion_1 var_local bloque funcion_2\n        | funcion_void var_local bloque funcion_endfuncion_void :  VOID IDfuncion_1 :  data_type_func IDfuncion_2 : RETURN super_exp SEMICOLON END funcion_end : END var_local : LPAREN var_local_2 RPARENvar_local_2 : var_local_2_1 var_local_3\n    | emptyvar_local_2_1 : data_type ID var_local_3 : COMMA var_local_2\n    | emptyaddop : PLUS\n    | MINUStimesop : TIMES\n    | DIVIDE\n    | PERCENTlogicop : AND\n    | ORempty :'
    
_lr_action_items = {'GLOBAL':([0,2,3,15,18,42,44,47,49,79,132,161,249,],[-160,8,-3,8,-39,-38,-46,-41,-48,8,-45,-47,-37,]),'DEF':([0,2,3,4,9,15,18,29,39,40,42,44,47,49,79,130,132,161,193,200,201,249,267,],[-160,11,-3,11,11,-160,-39,-140,-8,-10,-38,-46,-41,-48,-160,-9,-45,-47,-141,-142,-146,-37,-145,]),'MAIN':([0,2,3,4,7,9,10,15,18,28,29,39,40,42,44,47,49,79,130,132,161,193,200,201,249,267,],[-160,-160,-3,-160,27,-160,-7,-160,-39,-6,-140,-8,-10,-38,-46,-41,-48,-160,-9,-45,-47,-141,-142,-146,-37,-145,]),'$end':([1,5,12,13,14,25,37,105,],[0,-160,-160,-2,-4,-5,-1,-20,]),'DRAW':([6,8,18,26,38,42,44,47,49,52,54,55,56,57,58,60,63,64,74,76,107,123,132,161,167,195,218,219,225,226,240,245,249,255,256,257,258,259,265,266,274,275,276,278,279,],[16,-11,-39,16,16,-38,-46,-41,-48,16,-22,-23,-24,-25,-26,-28,-109,-110,16,16,-27,-21,-45,-47,-30,-147,16,-103,16,-138,-111,-29,-37,-102,-105,16,-108,-107,-136,-139,-106,16,-133,-130,-135,]),'INT':([6,8,11,18,26,38,42,44,47,49,50,52,54,55,56,57,58,60,63,64,74,75,76,107,123,132,161,167,195,197,218,219,225,226,240,245,249,255,256,257,258,259,265,266,274,275,276,278,279,],[21,-11,34,-39,21,21,-38,-46,-41,-48,21,21,-22,-23,-24,-25,-26,-28,-109,-110,21,21,21,-27,-21,-45,-47,-30,-147,21,21,-103,21,-138,-111,-29,-37,-102,-105,21,-108,-107,-136,-139,-106,21,-133,-130,-135,]),'FLOAT':([6,8,11,18,26,38,42,44,47,49,50,52,54,55,56,57,58,60,63,64,74,75,76,107,123,132,161,167,195,197,218,219,225,226,240,245,249,255,256,257,258,259,265,266,274,275,276,278,279,],[22,-11,35,-39,22,22,-38,-46,-41,-48,22,22,-22,-23,-24,-25,-26,-28,-109,-110,22,22,22,-27,-21,-45,-47,-30,-147,22,22,-103,22,-138,-111,-29,-37,-102,-105,22,-108,-107,-136,-139,-106,22,-133,-130,-135,]),'BOOLEAN':([6,8,11,18,26,38,42,44,47,49,50,52,54,55,56,57,58,60,63,64,74,75,76,107,123,132,161,167,195,197,218,219,225,226,240,245,249,255,256,257,258,259,265,266,274,275,276,278,279,],[23,-11,36,-39,23,23,-38,-46,-41,-48,23,23,-22,-23,-24,-25,-26,-28,-109,-110,23,23,23,-27,-21,-45,-47,-30,-147,23,23,-103,23,-138,-111,-29,-37,-102,-105,23,-108,-107,-136,-139,-106,23,-133,-130,-135,]),'ARRAY':([6,8,18,26,38,42,44,47,49,52,54,55,56,57,58,60,63,64,74,76,107,123,132,161,167,195,218,219,225,226,240,245,249,255,256,257,258,259,265,266,274,275,276,278,279,],[24,-11,-39,24,24,-38,-46,-41,-48,24,-22,-23,-24,-25,-26,-28,-109,-110,24,24,-27,-21,-45,-47,-30,-147,24,-103,24,-138,-111,-29,-37,-102,-105,24,-108,-107,-136,-139,-106,24,-133,-130,-135,]),'VOID':([11,],[33,]),'ID':([16,18,19,21,22,23,26,32,33,34,35,36,42,43,44,45,47,49,52,54,55,56,57,58,60,63,64,66,74,76,86,87,89,90,91,103,107,109,110,111,113,120,121,122,123,128,132,134,136,137,139,141,142,143,144,145,146,148,151,153,154,155,159,161,167,186,188,194,195,212,217,218,219,221,224,225,226,232,237,240,245,249,252,255,256,257,258,259,262,264,265,266,274,275,276,278,279,],[41,-39,46,-14,-15,-16,65,77,78,-17,-18,-19,-38,97,-46,-34,-41,-48,65,-22,-23,-24,-25,-26,-28,-109,-110,97,65,65,97,97,-100,-153,-154,97,-27,97,97,97,-50,97,97,97,-21,199,-45,97,-158,-159,97,-71,-72,-73,-74,-75,-76,97,97,-155,-156,-157,97,-47,-30,97,-58,97,-147,97,97,65,-103,97,97,65,-138,97,97,-111,-29,-37,269,-102,-105,65,-108,-107,97,97,-136,-139,-106,65,-133,-130,-135,]),'SEMICOLON':([17,20,46,59,81,82,83,84,85,88,92,93,94,95,96,97,98,99,100,101,102,108,114,116,118,133,135,138,140,147,149,150,152,157,158,160,162,164,168,184,203,204,205,206,207,208,210,220,223,227,229,230,231,241,243,253,260,268,269,],[44,49,-40,107,132,-160,-160,-160,-160,-99,-83,-84,-85,-86,-87,-160,-88,-89,-90,-91,161,167,-49,-52,-53,-65,-67,-68,-70,-77,-79,-80,-82,-98,-92,-94,-59,-61,-32,-51,-66,-69,-78,-81,-97,-101,-60,240,245,248,249,-93,-95,-112,-114,-33,-113,-96,-42,]),'EQUAL':([17,20,41,46,61,65,215,216,254,269,],[45,48,80,-40,45,-31,237,-35,-36,-42,]),'PRINT':([18,26,42,44,47,49,52,54,55,56,57,58,60,63,64,74,76,107,123,132,161,167,195,218,219,225,226,240,245,249,255,256,257,258,259,265,266,274,275,276,278,279,],[-39,67,-38,-46,-41,-48,67,-22,-23,-24,-25,-26,-28,-109,-110,67,67,-27,-21,-45,-47,-30,-147,67,-103,67,-138,-111,-29,-37,-102,-105,67,-108,-107,-136,-139,-106,67,-133,-130,-135,]),'IF':([18,26,42,44,47,49,52,54,55,56,57,58,60,63,64,74,76,107,123,132,161,167,195,218,219,225,226,240,245,249,255,256,257,258,259,265,266,274,275,276,278,279,],[-39,68,-38,-46,-41,-48,68,-22,-23,-24,-25,-26,-28,-109,-110,68,68,-27,-21,-45,-47,-30,-147,68,-103,68,-138,-111,-29,-37,-102,-105,68,-108,-107,-136,-139,-106,68,-133,-130,-135,]),'FOR':([18,26,42,44,47,49,52,54,55,56,57,58,60,63,64,74,76,107,123,132,161,167,195,218,219,225,226,240,245,249,255,256,257,258,259,265,266,274,275,276,278,279,],[-39,71,-38,-46,-41,-48,71,-22,-23,-24,-25,-26,-28,-109,-110,71,71,-27,-21,-45,-47,-30,-147,71,-103,71,-138,-111,-29,-37,-102,-105,71,-108,-107,-136,-139,-106,71,-133,-130,-135,]),'WHILE':([18,26,42,44,47,49,52,54,55,56,57,58,60,63,64,74,76,107,123,132,161,167,195,218,219,225,226,240,245,249,255,256,257,258,259,265,266,274,275,276,278,279,],[-39,72,-38,-46,-41,-48,72,-22,-23,-24,-25,-26,-28,-109,-110,72,72,-27,-21,-45,-47,-30,-147,72,-103,72,-138,-111,-29,-37,-102,-105,72,-108,-107,-136,-139,-106,72,-133,-130,-135,]),'END':([18,26,42,44,47,49,51,52,53,54,55,56,57,58,60,63,64,76,106,107,123,129,132,161,167,195,218,219,225,226,239,240,245,247,248,249,255,256,257,258,259,265,266,270,274,275,276,277,278,279,],[-39,-160,-38,-46,-41,-48,105,-160,-13,-22,-23,-24,-25,-26,-28,-109,-110,-160,-12,-27,-21,201,-45,-47,-30,-147,-160,-103,-160,-138,258,-111,-29,266,267,-37,-102,-105,-160,-108,-107,-136,-139,258,-106,-160,-133,279,-130,-135,]),'RETURN':([18,42,44,47,49,52,53,54,55,56,57,58,60,63,64,74,106,107,124,132,161,167,195,240,245,249,255,256,258,265,266,274,278,279,],[-39,-38,-46,-41,-48,-160,-13,-22,-23,-24,-25,-26,-28,-109,-110,-160,-12,-27,194,-45,-47,-30,-147,-111,-29,-37,-102,-105,-108,-136,-139,-106,-130,-135,]),'ELSE':([18,42,44,47,49,52,53,54,55,56,57,58,60,63,64,106,107,132,161,167,218,219,239,240,245,249,255,256,258,265,266,274,278,279,],[-39,-38,-46,-41,-48,-160,-13,-22,-23,-24,-25,-26,-28,-109,-110,-12,-27,-45,-47,-30,-160,-103,259,-111,-29,-37,-102,-105,-108,-136,-139,-106,-130,-135,]),'COMMA':([21,22,23,82,83,84,85,88,92,93,94,95,96,97,98,99,100,101,104,114,116,117,118,119,126,133,135,138,140,147,149,150,152,157,158,160,165,169,184,190,191,199,203,204,205,206,207,208,209,214,230,231,244,246,268,],[-14,-15,-16,-160,-160,-160,-160,-99,-83,-84,-85,-86,-87,-160,-88,-89,-90,-91,166,-49,-52,188,-53,-55,197,-65,-67,-68,-70,-77,-79,-80,-82,-98,-92,-94,212,217,-51,224,-131,-150,-66,-69,-78,-81,-97,-101,232,234,-93,-95,262,264,-96,]),'LESS':([24,83,84,85,88,92,93,94,95,96,97,98,99,100,101,114,116,118,147,149,150,152,157,158,160,184,205,206,207,208,230,231,268,],[50,143,-160,-160,-99,-83,-84,-85,-86,-87,-160,-88,-89,-90,-91,-49,-52,-53,-77,-79,-80,-82,-98,-92,-94,-51,-78,-81,-97,-101,-93,-95,-96,]),'LPAREN':([27,30,31,43,45,62,65,66,67,68,69,70,71,72,77,78,86,89,90,91,97,103,109,110,111,113,120,121,122,131,134,136,137,139,141,142,143,144,145,146,148,151,153,154,155,159,171,172,173,174,175,176,177,178,179,180,181,182,183,186,188,194,212,217,224,232,237,264,],[73,75,75,89,-34,111,113,89,120,-104,121,122,-134,-137,-144,-143,89,-100,-153,-154,113,89,89,89,89,-50,89,89,89,202,89,-158,-159,89,-71,-72,-73,-74,-75,-76,89,89,-155,-156,-157,89,221,-118,-119,-120,-121,-122,-123,-124,-125,-126,-127,-128,-129,89,-58,89,89,89,89,89,89,89,]),'PLUS':([43,45,66,84,85,86,88,89,90,91,92,93,94,95,96,97,98,99,100,101,103,109,110,111,113,114,116,118,120,121,122,134,136,137,139,141,142,143,144,145,146,148,150,151,152,153,154,155,157,158,159,160,184,186,188,194,206,207,208,212,217,224,230,231,232,237,264,268,],[90,-34,90,90,-160,90,-99,-100,-153,-154,-83,-84,-85,-86,-87,-160,-88,-89,-90,-91,90,90,90,90,-50,-49,-52,-53,90,90,90,90,-158,-159,90,-71,-72,-73,-74,-75,-76,90,-80,90,-82,-155,-156,-157,-98,-92,90,-94,-51,90,-58,90,-81,-97,-101,90,90,90,-93,-95,90,90,90,-96,]),'MINUS':([43,45,66,84,85,86,88,89,90,91,92,93,94,95,96,97,98,99,100,101,103,109,110,111,113,114,116,118,120,121,122,134,136,137,139,141,142,143,144,145,146,148,150,151,152,153,154,155,157,158,159,160,184,186,188,194,206,207,208,212,217,224,230,231,232,237,264,268,],[91,-34,91,91,-160,91,-99,-100,-153,-154,-83,-84,-85,-86,-87,-160,-88,-89,-90,-91,91,91,91,91,-50,-49,-52,-53,91,91,91,91,-158,-159,91,-71,-72,-73,-74,-75,-76,91,-80,91,-82,-155,-156,-157,-98,-92,91,-94,-51,91,-58,91,-81,-97,-101,91,91,91,-93,-95,91,91,91,-96,]),'CTE_I':([43,45,66,86,87,89,90,91,103,109,110,111,113,120,121,122,134,136,137,139,141,142,143,144,145,146,148,151,153,154,155,159,166,186,188,194,212,217,221,224,232,234,237,262,264,],[98,-34,98,98,98,-100,-153,-154,98,98,98,98,-50,98,98,98,98,-158,-159,98,-71,-72,-73,-74,-75,-76,98,98,-155,-156,-157,98,214,98,-58,98,98,98,98,98,98,251,98,98,98,]),'CTE_F':([43,45,66,86,87,89,90,91,103,109,110,111,113,120,121,122,134,136,137,139,141,142,143,144,145,146,148,151,153,154,155,159,186,188,194,212,217,221,224,232,237,262,264,],[99,-34,99,99,99,-100,-153,-154,99,99,99,99,-50,99,99,99,99,-158,-159,99,-71,-72,-73,-74,-75,-76,99,99,-155,-156,-157,99,99,-58,99,99,99,99,99,99,99,99,99,]),'TRUE':([43,45,66,86,87,89,90,91,103,109,110,111,113,120,121,122,134,136,137,139,141,142,143,144,145,146,148,151,153,154,155,159,186,188,194,212,217,221,224,232,237,262,264,],[100,-34,100,100,100,-100,-153,-154,100,100,100,100,-50,100,100,100,100,-158,-159,100,-71,-72,-73,-74,-75,-76,100,100,-155,-156,-157,100,100,-58,100,100,100,100,100,100,100,100,100,]),'FALSE':([43,45,66,86,87,89,90,91,103,109,110,111,113,120,121,122,134,136,137,139,141,142,143,144,145,146,148,151,153,154,155,159,186,188,194,212,217,221,224,232,237,262,264,],[101,-34,101,101,101,-100,-153,-154,101,101,101,101,-50,101,101,101,101,-158,-159,101,-71,-72,-73,-74,-75,-76,101,101,-155,-156,-157,101,101,-58,101,101,101,101,101,101,101,101,101,]),'LBRACKET':([48,61,65,97,],[103,110,-31,159,]),'POINT':([65,],[112,]),'RPAREN':([66,73,75,82,83,84,85,88,92,93,94,95,96,97,98,99,100,101,113,114,115,116,117,118,119,125,126,127,133,135,138,140,147,149,150,152,156,157,158,160,170,184,185,187,189,192,196,197,198,199,202,203,204,205,206,207,208,221,222,228,230,231,242,244,261,263,268,271,272,273,],[118,123,-160,-160,-160,-160,-160,-99,-83,-84,-85,-86,-87,-160,-88,-89,-90,-91,-50,-49,118,-52,-160,-53,-55,195,-160,-149,-65,-67,-68,-70,-77,-79,-80,-82,208,-98,-92,-94,219,-51,-54,-57,223,226,-148,-160,-152,-150,229,-66,-69,-78,-81,-97,-101,243,-56,-151,-93,-95,260,-160,-115,-117,-96,-116,276,-132,]),'NEWDRAW':([80,],[131,]),'AND':([82,83,84,85,88,92,93,94,95,96,97,98,99,100,101,114,116,118,138,140,147,149,150,152,157,158,160,184,204,205,206,207,208,230,231,268,],[136,-160,-160,-160,-99,-83,-84,-85,-86,-87,-160,-88,-89,-90,-91,-49,-52,-53,-68,-70,-77,-79,-80,-82,-98,-92,-94,-51,-69,-78,-81,-97,-101,-93,-95,-96,]),'OR':([82,83,84,85,88,92,93,94,95,96,97,98,99,100,101,114,116,118,138,140,147,149,150,152,157,158,160,184,204,205,206,207,208,230,231,268,],[137,-160,-160,-160,-99,-83,-84,-85,-86,-87,-160,-88,-89,-90,-91,-49,-52,-53,-68,-70,-77,-79,-80,-82,-98,-92,-94,-51,-69,-78,-81,-97,-101,-93,-95,-96,]),'RBRACKET':([82,83,84,85,88,92,93,94,95,96,97,98,99,100,101,103,114,116,118,133,135,138,140,147,149,150,152,157,158,160,163,165,169,184,203,204,205,206,207,208,209,211,213,230,231,233,238,250,268,],[-160,-160,-160,-160,-99,-83,-84,-85,-86,-87,-160,-88,-89,-90,-91,164,-49,-52,-53,-65,-67,-68,-70,-77,-79,-80,-82,-98,-92,-94,210,-160,216,-51,-66,-69,-78,-81,-97,-101,231,-62,-64,-93,-95,-63,254,268,-96,]),'GREATER':([83,84,85,88,92,93,94,95,96,97,98,99,100,101,114,116,118,147,149,150,152,157,158,160,184,205,206,207,208,214,230,231,235,236,251,268,],[141,-160,-160,-99,-83,-84,-85,-86,-87,-160,-88,-89,-90,-91,-49,-52,-53,-77,-79,-80,-82,-98,-92,-94,-51,-78,-81,-97,-101,-160,-93,-95,252,-44,-43,-96,]),'GREATEREQUAL':([83,84,85,88,92,93,94,95,96,97,98,99,100,101,114,116,118,147,149,150,152,157,158,160,184,205,206,207,208,230,231,268,],[142,-160,-160,-99,-83,-84,-85,-86,-87,-160,-88,-89,-90,-91,-49,-52,-53,-77,-79,-80,-82,-98,-92,-94,-51,-78,-81,-97,-101,-93,-95,-96,]),'LESSEQUAL':([83,84,85,88,92,93,94,95,96,97,98,99,100,101,114,116,118,147,149,150,152,157,158,160,184,205,206,207,208,230,231,268,],[144,-160,-160,-99,-83,-84,-85,-86,-87,-160,-88,-89,-90,-91,-49,-52,-53,-77,-79,-80,-82,-98,-92,-94,-51,-78,-81,-97,-101,-93,-95,-96,]),'DEQUAL':([83,84,85,88,92,93,94,95,96,97,98,99,100,101,114,116,118,147,149,150,152,157,158,160,184,205,206,207,208,230,231,268,],[145,-160,-160,-99,-83,-84,-85,-86,-87,-160,-88,-89,-90,-91,-49,-52,-53,-77,-79,-80,-82,-98,-92,-94,-51,-78,-81,-97,-101,-93,-95,-96,]),'DISTINT':([83,84,85,88,92,93,94,95,96,97,98,99,100,101,114,116,118,147,149,150,152,157,158,160,184,205,206,207,208,230,231,268,],[146,-160,-160,-99,-83,-84,-85,-86,-87,-160,-88,-89,-90,-91,-49,-52,-53,-77,-79,-80,-82,-98,-92,-94,-51,-78,-81,-97,-101,-93,-95,-96,]),'TIMES':([85,88,92,93,94,95,96,97,98,99,100,101,114,116,118,157,158,160,184,207,208,230,231,268,],[153,-99,-83,-84,-85,-86,-87,-160,-88,-89,-90,-91,-49,-52,-53,-98,-92,-94,-51,-97,-101,-93,-95,-96,]),'DIVIDE':([85,88,92,93,94,95,96,97,98,99,100,101,114,116,118,157,158,160,184,207,208,230,231,268,],[154,-99,-83,-84,-85,-86,-87,-160,-88,-89,-90,-91,-49,-52,-53,-98,-92,-94,-51,-97,-101,-93,-95,-96,]),'PERCENT':([85,88,92,93,94,95,96,97,98,99,100,101,114,116,118,157,158,160,184,207,208,230,231,268,],[155,-99,-83,-84,-85,-86,-87,-160,-88,-89,-90,-91,-49,-52,-53,-98,-92,-94,-51,-97,-101,-93,-95,-96,]),'SETPOSITION':([112,],[172,]),'CIRCLE':([112,],[173,]),'RIGHT':([112,],[174,]),'LEFT':([112,],[175,]),'HIDE':([112,],[176,]),'SQUARE':([112,],[177,]),'CLEAR':([112,],[178,]),'SHOW':([112,],[179,]),'BACK':([112,],[180,]),'SPEED':([112,],[181,]),'FORWARD':([112,],[182,]),'SETCOLOR':([112,],[183,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'init':([0,],[2,]),'empty':([0,2,4,5,9,12,15,26,52,74,75,76,79,82,83,84,85,97,117,126,165,197,214,218,225,244,257,275,],[3,10,10,14,10,14,40,53,53,53,127,53,40,135,140,149,152,160,187,198,213,127,236,53,53,263,53,53,]),'globales':([2,],[4,]),'funciones':([2,4,],[5,12,]),'global_1':([2,15,79,],[6,38,38,]),'funciones_2':([2,4,9,],[7,7,28,]),'funcion':([2,4,9,],[9,9,9,]),'programa_end':([5,12,],[13,37,]),'vars':([6,26,38,52,74,76,218,225,257,275,],[15,58,79,58,58,58,58,58,58,58,]),'vars_id':([6,26,38,52,74,76,218,225,257,275,],[17,17,17,17,17,17,17,17,17,17,]),'vars_aux':([6,26,38,52,74,76,218,225,257,275,],[18,18,18,18,18,18,18,18,18,18,]),'data_type':([6,26,38,50,52,74,75,76,197,218,225,257,275,],[19,19,19,104,19,19,128,19,128,19,19,19,19,]),'array':([6,26,38,52,74,76,218,225,257,275,],[20,20,20,20,20,20,20,20,20,20,]),'main':([7,],[25,]),'main_1':([7,],[26,]),'funcion_aux':([11,],[29,]),'funcion_1':([11,],[30,]),'funcion_void':([11,],[31,]),'data_type_func':([11,],[32,]),'globales_2':([15,79,],[39,130,]),'vars2':([17,],[42,]),'asignacion_equal':([17,61,],[43,109,]),'vars3':([20,],[47,]),'bloque':([26,52,74,76,218,225,257,275,],[51,106,124,129,239,247,270,277,]),'estatuto':([26,52,74,76,218,225,257,275,],[52,52,52,52,52,52,52,52,]),'asignacion':([26,52,74,76,218,225,257,275,],[54,54,54,54,54,54,54,54,]),'condicion':([26,52,74,76,218,225,257,275,],[55,55,55,55,55,55,55,55,]),'ciclo':([26,52,74,76,218,225,257,275,],[56,56,56,56,56,56,56,56,]),'accion':([26,52,74,76,218,225,257,275,],[57,57,57,57,57,57,57,57,]),'llamada':([26,43,52,66,74,76,86,87,103,109,110,111,120,121,122,134,139,148,151,159,186,194,212,217,218,221,224,225,232,237,257,262,264,275,],[59,96,59,96,59,59,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,59,96,96,59,96,96,59,96,96,59,]),'print':([26,52,74,76,218,225,257,275,],[60,60,60,60,60,60,60,60,]),'asignacion_id':([26,52,74,76,218,225,257,275,],[61,61,61,61,61,61,61,61,]),'condicion_id':([26,52,74,76,218,225,257,275,],[62,62,62,62,62,62,62,62,]),'for':([26,52,74,76,218,225,257,275,],[63,63,63,63,63,63,63,63,]),'while':([26,52,74,76,218,225,257,275,],[64,64,64,64,64,64,64,64,]),'llamada_id':([26,43,52,66,74,76,86,87,103,109,110,111,120,121,122,134,139,148,151,159,186,194,212,217,218,221,224,225,232,237,257,262,264,275,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'for_init':([26,52,74,76,218,225,257,275,],[69,69,69,69,69,69,69,69,]),'while_init':([26,52,74,76,218,225,257,275,],[70,70,70,70,70,70,70,70,]),'var_local':([30,31,],[74,76,]),'super_exp':([43,66,86,103,109,111,120,122,134,159,186,194,212,232,237,],[81,119,156,165,168,170,189,192,203,209,119,227,165,250,253,]),'expresion':([43,66,86,103,109,111,120,122,134,159,186,194,212,232,237,],[82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,]),'exp':([43,66,86,103,109,110,111,120,121,122,134,139,148,159,186,194,212,217,224,232,237,264,],[83,83,83,83,83,169,83,83,191,83,83,204,205,83,83,83,83,238,191,83,83,273,]),'termino':([43,66,86,103,109,110,111,120,121,122,134,139,148,151,159,186,194,212,217,224,232,237,264,],[84,84,84,84,84,84,84,84,84,84,84,84,84,206,84,84,84,84,84,84,84,84,84,]),'factor':([43,66,86,103,109,110,111,120,121,122,134,139,148,151,159,186,194,212,217,224,232,237,264,],[85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,]),'lparen_factor':([43,66,86,103,109,110,111,120,121,122,134,139,148,151,159,186,194,212,217,224,232,237,264,],[86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,]),'addop':([43,66,84,86,103,109,110,111,120,121,122,134,139,148,151,159,186,194,212,217,224,232,237,264,],[87,87,148,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,]),'var_cte':([43,66,86,87,103,109,110,111,120,121,122,134,139,148,151,159,186,194,212,217,221,224,232,237,262,264,],[88,88,88,157,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,244,88,88,88,244,88,]),'var_cte_1':([43,66,86,87,103,109,110,111,120,121,122,134,139,148,151,159,186,194,212,217,221,224,232,237,262,264,],[92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,]),'var_cte_i':([43,66,86,87,103,109,110,111,120,121,122,134,139,148,151,159,186,194,212,217,221,224,232,237,262,264,],[93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,]),'var_cte_f':([43,66,86,87,103,109,110,111,120,121,122,134,139,148,151,159,186,194,212,217,221,224,232,237,262,264,],[94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,]),'var_cte_b':([43,66,86,87,103,109,110,111,120,121,122,134,139,148,151,159,186,194,212,217,221,224,232,237,262,264,],[95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,]),'def_array':([48,],[102,]),'asignacion_2':([61,],[108,]),'llamada_2':([66,],[114,]),'llamada_exp':([66,186,],[115,222,]),'llamada_rparen':([66,115,],[116,184,]),'llamada_super_exp':([66,186,],[117,117,]),'var_local_2':([75,197,],[125,228,]),'var_local_2_1':([75,197,],[126,126,]),'super_exp_2':([82,],[133,]),'logicop':([82,],[134,]),'expresion_2':([83,],[138,]),'relop':([83,],[139,]),'exp_2':([84,],[147,]),'termino_2':([85,],[150,]),'timesop':([85,],[151,]),'var_cte_2':([97,],[158,]),'def_array_2':([103,],[162,]),'def_array_cte':([103,212,],[163,233,]),'accion_nombre':([112,],[171,]),'llamada_exp2':([117,],[185,]),'llamada_comma':([117,],[186,]),'for_exp':([121,224,],[190,246,]),'funcion_2':([124,],[193,]),'var_local_3':([126,],[196,]),'funcion_end':([129,],[200,]),'rparen_factor':([156,],[207,]),'def_array_cte_2':([165,],[211,]),'asignacion_3':([169,],[215,]),'rparen_condicion':([170,],[218,]),'accion_params':([171,],[220,]),'rparen_while':([192,],[225,]),'var_cte_3':([209,],[230,]),'array_2':([214,],[235,]),'accion_params_2':([221,],[241,]),'accion_params_cte':([221,262,],[242,271,]),'condicion_2':([239,],[255,]),'condicion_end':([239,270,],[256,274,]),'condicion_else':([239,],[257,]),'accion_params_cte_2':([244,],[261,]),'while_end':([247,],[265,]),'for_exp2':([264,],[272,]),'for_rparen':([272,],[275,]),'for_end':([277,],[278,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> init globales funciones programa_end','programa',4,'p_programa','c_parser.py',18),
  ('programa -> init funciones programa_end','programa',3,'p_programa','c_parser.py',19),
  ('init -> empty','init',1,'p_init','c_parser.py',22),
  ('programa_end -> empty','programa_end',1,'p_programa_end','c_parser.py',27),
  ('funciones -> funciones_2 main','funciones',2,'p_funciones','c_parser.py',31),
  ('funciones_2 -> funcion funciones_2','funciones_2',2,'p_funciones_2','c_parser.py',35),
  ('funciones_2 -> empty','funciones_2',1,'p_funciones_2','c_parser.py',36),
  ('globales -> global_1 vars globales_2','globales',3,'p_globales','c_parser.py',40),
  ('globales_2 -> global_1 vars globales_2','globales_2',3,'p_globales_2','c_parser.py',44),
  ('globales_2 -> empty','globales_2',1,'p_globales_2','c_parser.py',45),
  ('global_1 -> GLOBAL','global_1',1,'p_global_1','c_parser.py',49),
  ('bloque -> estatuto bloque','bloque',2,'p_bloque','c_parser.py',53),
  ('bloque -> empty','bloque',1,'p_bloque','c_parser.py',54),
  ('data_type -> INT','data_type',1,'p_data_type','c_parser.py',58),
  ('data_type -> FLOAT','data_type',1,'p_data_type','c_parser.py',59),
  ('data_type -> BOOLEAN','data_type',1,'p_data_type','c_parser.py',60),
  ('data_type_func -> INT','data_type_func',1,'p_data_type_func','c_parser.py',64),
  ('data_type_func -> FLOAT','data_type_func',1,'p_data_type_func','c_parser.py',65),
  ('data_type_func -> BOOLEAN','data_type_func',1,'p_data_type_func','c_parser.py',66),
  ('main -> main_1 bloque END','main',3,'p_main','c_parser.py',70),
  ('main_1 -> MAIN LPAREN RPAREN','main_1',3,'p_main_1','c_parser.py',74),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','c_parser.py',81),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','c_parser.py',82),
  ('estatuto -> ciclo','estatuto',1,'p_estatuto','c_parser.py',83),
  ('estatuto -> accion','estatuto',1,'p_estatuto','c_parser.py',84),
  ('estatuto -> vars','estatuto',1,'p_estatuto','c_parser.py',85),
  ('estatuto -> llamada SEMICOLON','estatuto',2,'p_estatuto','c_parser.py',86),
  ('estatuto -> print','estatuto',1,'p_estatuto','c_parser.py',87),
  ('print -> PRINT LPAREN super_exp RPAREN SEMICOLON','print',5,'p_print','c_parser.py',91),
  ('asignacion -> asignacion_id asignacion_2 SEMICOLON','asignacion',3,'p_asignacion','c_parser.py',97),
  ('asignacion_id -> ID','asignacion_id',1,'p_asignacion_id','c_parser.py',101),
  ('asignacion_2 -> asignacion_equal super_exp','asignacion_2',2,'p_asignacion_2','c_parser.py',112),
  ('asignacion_2 -> LBRACKET exp asignacion_3 EQUAL super_exp','asignacion_2',5,'p_asignacion_2','c_parser.py',113),
  ('asignacion_equal -> EQUAL','asignacion_equal',1,'p_asignacion_equal','c_parser.py',130),
  ('asignacion_3 -> RBRACKET','asignacion_3',1,'p_asignacion_3','c_parser.py',134),
  ('asignacion_3 -> COMMA exp RBRACKET','asignacion_3',3,'p_asignacion_3','c_parser.py',135),
  ('vars -> DRAW ID EQUAL NEWDRAW LPAREN RPAREN SEMICOLON','vars',7,'p_vars','c_parser.py',139),
  ('vars -> vars_id vars2','vars',2,'p_vars','c_parser.py',140),
  ('vars -> vars_aux','vars',1,'p_vars','c_parser.py',141),
  ('vars_id -> data_type ID','vars_id',2,'p_vars_id','c_parser.py',151),
  ('vars_aux -> array vars3','vars_aux',2,'p_vars_aux','c_parser.py',163),
  ('array -> ARRAY LESS data_type COMMA CTE_I array_2 GREATER ID','array',8,'p_array','c_parser.py',175),
  ('array_2 -> COMMA CTE_I','array_2',2,'p_array_2','c_parser.py',199),
  ('array_2 -> empty','array_2',1,'p_array_2','c_parser.py',200),
  ('vars2 -> asignacion_equal super_exp SEMICOLON','vars2',3,'p_vars_2','c_parser.py',207),
  ('vars2 -> SEMICOLON','vars2',1,'p_vars_2','c_parser.py',208),
  ('vars3 -> EQUAL def_array SEMICOLON','vars3',3,'p_vars_3','c_parser.py',228),
  ('vars3 -> SEMICOLON','vars3',1,'p_vars_3','c_parser.py',229),
  ('llamada -> llamada_id llamada_2','llamada',2,'p_llamada','c_parser.py',236),
  ('llamada_id -> ID LPAREN','llamada_id',2,'p_llamada_id','c_parser.py',246),
  ('llamada_2 -> llamada_exp llamada_rparen','llamada_2',2,'p_llamada_2','c_parser.py',258),
  ('llamada_2 -> llamada_rparen','llamada_2',1,'p_llamada_2','c_parser.py',259),
  ('llamada_rparen -> RPAREN','llamada_rparen',1,'p_llamada_rparen','c_parser.py',263),
  ('llamada_exp -> llamada_super_exp llamada_exp2','llamada_exp',2,'p_llamada_exp','c_parser.py',270),
  ('llamada_super_exp -> super_exp','llamada_super_exp',1,'p_llamada_super_exp','c_parser.py',274),
  ('llamada_exp2 -> llamada_comma llamada_exp','llamada_exp2',2,'p_llamada_exp_2','c_parser.py',285),
  ('llamada_exp2 -> empty','llamada_exp2',1,'p_llamada_exp_2','c_parser.py',286),
  ('llamada_comma -> COMMA','llamada_comma',1,'p_llamada_comma','c_parser.py',290),
  ('def_array -> LBRACKET def_array_2','def_array',2,'p_def_array','c_parser.py',294),
  ('def_array_2 -> def_array_cte RBRACKET','def_array_2',2,'p_def_array_2','c_parser.py',298),
  ('def_array_2 -> RBRACKET','def_array_2',1,'p_def_array_2','c_parser.py',299),
  ('def_array_cte -> super_exp def_array_cte_2','def_array_cte',2,'p_def_array_cte','c_parser.py',303),
  ('def_array_cte_2 -> COMMA def_array_cte','def_array_cte_2',2,'p_def_array_cte_2','c_parser.py',307),
  ('def_array_cte_2 -> empty','def_array_cte_2',1,'p_def_array_cte_2','c_parser.py',308),
  ('super_exp -> expresion super_exp_2','super_exp',2,'p_super_exp','c_parser.py',312),
  ('super_exp_2 -> logicop super_exp','super_exp_2',2,'p_super_exp_2','c_parser.py',316),
  ('super_exp_2 -> empty','super_exp_2',1,'p_super_exp_2','c_parser.py',317),
  ('expresion -> exp expresion_2','expresion',2,'p_expresion','c_parser.py',320),
  ('expresion_2 -> relop exp','expresion_2',2,'p_expresion_2','c_parser.py',340),
  ('expresion_2 -> empty','expresion_2',1,'p_expresion_2','c_parser.py',341),
  ('relop -> GREATER','relop',1,'p_relop','c_parser.py',345),
  ('relop -> GREATEREQUAL','relop',1,'p_relop','c_parser.py',346),
  ('relop -> LESS','relop',1,'p_relop','c_parser.py',347),
  ('relop -> LESSEQUAL','relop',1,'p_relop','c_parser.py',348),
  ('relop -> DEQUAL','relop',1,'p_relop','c_parser.py',349),
  ('relop -> DISTINT','relop',1,'p_relop','c_parser.py',350),
  ('exp -> termino exp_2','exp',2,'p_exp','c_parser.py',354),
  ('exp_2 -> addop exp','exp_2',2,'p_exp_2','c_parser.py',374),
  ('exp_2 -> empty','exp_2',1,'p_exp_2','c_parser.py',375),
  ('termino -> factor termino_2','termino',2,'p_termino','c_parser.py',379),
  ('termino_2 -> timesop termino','termino_2',2,'p_termino_2','c_parser.py',399),
  ('termino_2 -> empty','termino_2',1,'p_termino_2','c_parser.py',400),
  ('var_cte -> var_cte_1','var_cte',1,'p_var_cte','c_parser.py',404),
  ('var_cte -> var_cte_i','var_cte',1,'p_var_cte','c_parser.py',405),
  ('var_cte -> var_cte_f','var_cte',1,'p_var_cte','c_parser.py',406),
  ('var_cte -> var_cte_b','var_cte',1,'p_var_cte','c_parser.py',407),
  ('var_cte -> llamada','var_cte',1,'p_var_cte','c_parser.py',408),
  ('var_cte_i -> CTE_I','var_cte_i',1,'p_var_cte_i','c_parser.py',412),
  ('var_cte_f -> CTE_F','var_cte_f',1,'p_var_cte_f','c_parser.py',418),
  ('var_cte_b -> TRUE','var_cte_b',1,'p_var_cte_b','c_parser.py',424),
  ('var_cte_b -> FALSE','var_cte_b',1,'p_var_cte_b','c_parser.py',425),
  ('var_cte_1 -> ID var_cte_2','var_cte_1',2,'p_var_cte_1','c_parser.py',431),
  ('var_cte_2 -> LBRACKET super_exp var_cte_3','var_cte_2',3,'p_var_cte_2','c_parser.py',466),
  ('var_cte_2 -> empty','var_cte_2',1,'p_var_cte_2','c_parser.py',467),
  ('var_cte_3 -> RBRACKET','var_cte_3',1,'p_var_cte_3','c_parser.py',474),
  ('var_cte_3 -> COMMA super_exp RBRACKET','var_cte_3',3,'p_var_cte_3','c_parser.py',475),
  ('factor -> lparen_factor super_exp rparen_factor','factor',3,'p_factor','c_parser.py',482),
  ('factor -> addop var_cte','factor',2,'p_factor','c_parser.py',483),
  ('factor -> var_cte','factor',1,'p_factor','c_parser.py',484),
  ('lparen_factor -> LPAREN','lparen_factor',1,'p_lparen_factor','c_parser.py',505),
  ('rparen_factor -> RPAREN','rparen_factor',1,'p_rparen_factor','c_parser.py',509),
  ('condicion -> condicion_id LPAREN super_exp rparen_condicion bloque condicion_2','condicion',6,'p_condicion','c_parser.py',513),
  ('rparen_condicion -> RPAREN','rparen_condicion',1,'p_rparen_condicion','c_parser.py',517),
  ('condicion_id -> IF','condicion_id',1,'p_condicion_id','c_parser.py',530),
  ('condicion_2 -> condicion_end','condicion_2',1,'p_condicion_2','c_parser.py',534),
  ('condicion_2 -> condicion_else bloque condicion_end','condicion_2',3,'p_condicion_2','c_parser.py',535),
  ('condicion_else -> ELSE','condicion_else',1,'p_condicion_else','c_parser.py',539),
  ('condicion_end -> END','condicion_end',1,'p_condicion_end','c_parser.py',546),
  ('ciclo -> for','ciclo',1,'p_ciclo','c_parser.py',552),
  ('ciclo -> while','ciclo',1,'p_ciclo','c_parser.py',553),
  ('accion -> ID POINT accion_nombre accion_params SEMICOLON','accion',5,'p_accion','c_parser.py',557),
  ('accion_params -> LPAREN accion_params_2','accion_params',2,'p_accion_params','c_parser.py',561),
  ('accion_params_2 -> accion_params_cte RPAREN','accion_params_2',2,'p_accion_params_2','c_parser.py',565),
  ('accion_params_2 -> RPAREN','accion_params_2',1,'p_accion_params_2','c_parser.py',566),
  ('accion_params_cte -> var_cte accion_params_cte_2','accion_params_cte',2,'p_accion_params_cte','c_parser.py',570),
  ('accion_params_cte_2 -> COMMA accion_params_cte','accion_params_cte_2',2,'p_accion_params_cte_2','c_parser.py',574),
  ('accion_params_cte_2 -> empty','accion_params_cte_2',1,'p_accion_params_cte_2','c_parser.py',575),
  ('accion_nombre -> SETPOSITION','accion_nombre',1,'p_accion_llamada','c_parser.py',579),
  ('accion_nombre -> CIRCLE','accion_nombre',1,'p_accion_llamada','c_parser.py',580),
  ('accion_nombre -> RIGHT','accion_nombre',1,'p_accion_llamada','c_parser.py',581),
  ('accion_nombre -> LEFT','accion_nombre',1,'p_accion_llamada','c_parser.py',582),
  ('accion_nombre -> HIDE','accion_nombre',1,'p_accion_llamada','c_parser.py',583),
  ('accion_nombre -> SQUARE','accion_nombre',1,'p_accion_llamada','c_parser.py',584),
  ('accion_nombre -> CLEAR','accion_nombre',1,'p_accion_llamada','c_parser.py',585),
  ('accion_nombre -> SHOW','accion_nombre',1,'p_accion_llamada','c_parser.py',586),
  ('accion_nombre -> BACK','accion_nombre',1,'p_accion_llamada','c_parser.py',587),
  ('accion_nombre -> SPEED','accion_nombre',1,'p_accion_llamada','c_parser.py',588),
  ('accion_nombre -> FORWARD','accion_nombre',1,'p_accion_llamada','c_parser.py',589),
  ('accion_nombre -> SETCOLOR','accion_nombre',1,'p_accion_llamada','c_parser.py',590),
  ('for -> for_init LPAREN for_exp COMMA for_exp COMMA for_exp2 for_rparen bloque for_end','for',10,'p_for','c_parser.py',594),
  ('for_exp -> exp','for_exp',1,'p_for_exp','c_parser.py',598),
  ('for_exp2 -> exp','for_exp2',1,'p_for_exp2','c_parser.py',605),
  ('for_rparen -> RPAREN','for_rparen',1,'p_for_rparen','c_parser.py',625),
  ('for_init -> FOR','for_init',1,'p_for_init','c_parser.py',639),
  ('for_end -> END','for_end',1,'p_for_end','c_parser.py',643),
  ('while -> while_init LPAREN super_exp rparen_while bloque while_end','while',6,'p_while','c_parser.py',658),
  ('while_init -> WHILE','while_init',1,'p_while_init','c_parser.py',662),
  ('rparen_while -> RPAREN','rparen_while',1,'p_rparen_while','c_parser.py',667),
  ('while_end -> END','while_end',1,'p_while_end','c_parser.py',679),
  ('funcion -> DEF funcion_aux','funcion',2,'p_funcion','c_parser.py',687),
  ('funcion_aux -> funcion_1 var_local bloque funcion_2','funcion_aux',4,'p_funcion_aux','c_parser.py',691),
  ('funcion_aux -> funcion_void var_local bloque funcion_end','funcion_aux',4,'p_funcion_aux','c_parser.py',692),
  ('funcion_void -> VOID ID','funcion_void',2,'p_funcion_void','c_parser.py',696),
  ('funcion_1 -> data_type_func ID','funcion_1',2,'p_funcion_1','c_parser.py',706),
  ('funcion_2 -> RETURN super_exp SEMICOLON END','funcion_2',4,'p_funcion_2','c_parser.py',717),
  ('funcion_end -> END','funcion_end',1,'p_funcion_end','c_parser.py',731),
  ('var_local -> LPAREN var_local_2 RPAREN','var_local',3,'p_var_local','c_parser.py',736),
  ('var_local_2 -> var_local_2_1 var_local_3','var_local_2',2,'p_var_local_2','c_parser.py',740),
  ('var_local_2 -> empty','var_local_2',1,'p_var_local_2','c_parser.py',741),
  ('var_local_2_1 -> data_type ID','var_local_2_1',2,'p_var_local_2_1','c_parser.py',745),
  ('var_local_3 -> COMMA var_local_2','var_local_3',2,'p_var_local_3','c_parser.py',756),
  ('var_local_3 -> empty','var_local_3',1,'p_var_local_3','c_parser.py',757),
  ('addop -> PLUS','addop',1,'p_addop','c_parser.py',761),
  ('addop -> MINUS','addop',1,'p_addop','c_parser.py',762),
  ('timesop -> TIMES','timesop',1,'p_timesop','c_parser.py',766),
  ('timesop -> DIVIDE','timesop',1,'p_timesop','c_parser.py',767),
  ('timesop -> PERCENT','timesop',1,'p_timesop','c_parser.py',768),
  ('logicop -> AND','logicop',1,'p_logicop','c_parser.py',772),
  ('logicop -> OR','logicop',1,'p_logicop','c_parser.py',773),
  ('empty -> <empty>','empty',0,'p_empty','c_parser.py',777),
]
