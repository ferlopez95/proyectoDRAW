
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'POINT PLUS MINUS TIMES DIVIDE LESS LESSEQUAL GREATER GREATEREQUAL EQUAL DEQUAL DISTINT SEMICOLON COMMA LPAREN RPAREN LBRACKET RBRACKET PERCENT AND OR ID CTE_I CTE_F IF ELSE INT FLOAT BOOLEAN DRAW ARRAY MAIN GLOBAL DEF END VOID WHILE FOR RETURN TRUE FALSE SETPOSITION SETCOLOR SPEED FORWARD LEFT RIGHT BACK HIDE SHOW CLEAR SQUARE CIRCLE PRINTprograma : init globales funciones programa_end\n    | init funciones programa_end init : empty  programa_end : empty funciones : funciones_2 mainfunciones_2 : funcion funciones_2\n    | emptyglobales : global_1 vars globales_2 globales_2 : global_1 vars globales_2\n    | empty  global_1 : GLOBAL bloque : estatuto bloque\n    | emptydata_type : INT\n    | FLOAT\n    | BOOLEANdata_type_func : INT\n    | FLOAT\n    | BOOLEANmain : main_1 bloque END main_1 : MAIN LPAREN RPARENestatuto : asignacion\n    | condicion\n    | ciclo\n    | accion\n    | vars\n    | llamada SEMICOLON\n    | print print : PRINT LPAREN super_exp RPAREN SEMICOLON asignacion : asignacion_id asignacion_2 SEMICOLONasignacion_id : ID asignacion_arrayasignacion_2 : asignacion_equal super_expasignacion_array : LBRACKET super_exp asignacion_3\n    | emptyasignacion_equal : EQUALasignacion_3 : RBRACKET\n    | COMMA super_exp RBRACKETvars : DRAW ID EQUAL DRAW LPAREN RPAREN SEMICOLON\n    | vars_id vars2\n    | vars_auxvars_id : data_type ID vars_aux : array vars3  array : ARRAY LESS data_type COMMA CTE_I array_2 GREATER ID array_2 : COMMA CTE_I\n    | empty vars2 : asignacion_equal super_exp SEMICOLON\n    | SEMICOLONvars3 : EQUAL def_array SEMICOLON\n    | SEMICOLONllamada : llamada_id llamada_2 llamada_id : ID LPARENllamada_2 : llamada_exp llamada_rparen\n    | llamada_rparenllamada_rparen : RPARENllamada_exp : llamada_super_exp llamada_exp2llamada_super_exp : super_expllamada_exp2 : COMMA llamada_exp\n    | emptydef_array : LBRACKET def_array_2 def_array_2 : def_array_cte RBRACKET\n    | RBRACKETdef_array_cte : super_exp def_array_cte_2def_array_cte_2 : COMMA def_array_cte\n    | emptysuper_exp : expresion super_exp_2super_exp_2 :  logicop super_exp\n    | emptyexpresion : exp expresion_2expresion_2 : relop exp\n    | emptyrelop : GREATER\n    | GREATEREQUAL\n    | LESS\n    | LESSEQUAL\n    | DEQUAL\n    | DISTINTexp : termino exp_2exp_2 : addop exp\n    | emptytermino : factor termino_2termino_2 : timesop termino\n    | emptyvar_cte : var_cte_1\n    | var_cte_i\n    | var_cte_f\n    | var_cte_b\n    | llamada var_cte_i : CTE_I\n    | MINUS CTE_I  var_cte_f : CTE_F  var_cte_b : TRUE\n    | FALSE  var_cte_1 : ID var_cte_2  var_cte_2 : var_cte_2_lbracket super_exp var_cte_3\n    | empty  var_cte_2_lbracket : LBRACKET var_cte_3 : RBRACKET\n    | COMMA super_exp RBRACKETfactor : lparen_factor super_exp rparen_factor\n    | addop var_cte\n    | var_ctelparen_factor : LPARENrparen_factor : RPARENcondicion : condicion_id LPAREN super_exp rparen_condicion bloque condicion_2 rparen_condicion : RPAREN condicion_id : IFcondicion_2 : condicion_end\n    | condicion_else  bloque condicion_end condicion_else : ELSE  condicion_end : END ciclo : for\n    | whileaccion : accion_id POINT accion_params SEMICOLON accion_id : ID  accion_params :  SETPOSITION LPAREN exp COMMA exp RPAREN\n    | CIRCLE LPAREN exp RPAREN\n    | RIGHT LPAREN exp RPAREN\n    | LEFT LPAREN exp RPAREN\n    | HIDE LPAREN RPAREN\n    | SQUARE LPAREN exp RPAREN\n    | CLEAR LPAREN RPAREN\n    | SHOW LPAREN RPAREN\n    | BACK LPAREN exp RPAREN\n    | SPEED LPAREN exp RPAREN\n    | FORWARD LPAREN exp RPAREN \n    | SETCOLOR LPAREN exp COMMA exp COMMA exp RPARENfor : for_init LPAREN for_exp COMMA for_exp COMMA for_exp2 for_rparen bloque for_endfor_exp : expfor_exp2 : expfor_rparen : RPAREN for_init : FOR  for_end : END while : while_init LPAREN super_exp rparen_while bloque while_end while_init : WHILE rparen_while : RPAREN while_end : END funcion :  DEF funcion_aux  funcion_aux : funcion_1 var_local bloque funcion_2\n        | funcion_void var_local bloque funcion_endfuncion_void :  VOID IDfuncion_1 :  data_type_func IDfuncion_2 : RETURN super_exp SEMICOLON END funcion_end : END var_local : LPAREN var_local_2 RPARENvar_local_2 : var_local_2_1 var_local_3\n    | emptyvar_local_2_1 : data_type ID var_local_3 : COMMA var_local_2\n    | emptyaddop : PLUS\n    | MINUStimesop : TIMES\n    | DIVIDE\n    | PERCENTlogicop : AND\n    | ORempty :'
    
_lr_action_items = {'GLOBAL':([0,2,3,15,18,42,44,47,49,80,135,168,272,],[-157,8,-3,8,-40,-39,-47,-42,-49,8,-46,-48,-38,]),'DEF':([0,2,3,4,9,15,18,29,39,40,42,44,47,49,80,133,135,168,199,206,207,272,294,],[-157,11,-3,11,11,-157,-40,-137,-8,-10,-39,-47,-42,-49,-157,-9,-46,-48,-138,-139,-143,-38,-142,]),'MAIN':([0,2,3,4,7,9,10,15,18,28,29,39,40,42,44,47,49,80,133,135,168,199,206,207,272,294,],[-157,-157,-3,-157,27,-157,-7,-157,-40,-6,-137,-8,-10,-39,-47,-42,-49,-157,-9,-46,-48,-138,-139,-143,-38,-142,]),'$end':([1,5,12,13,14,25,37,106,],[0,-157,-157,-2,-4,-5,-1,-20,]),'DRAW':([6,8,18,26,38,42,44,47,49,52,54,55,56,57,58,60,63,64,75,77,81,108,126,135,168,174,201,221,222,223,242,243,268,272,276,277,278,279,280,292,293,302,305,306,310,311,],[16,-11,-40,16,16,-39,-47,-42,-49,16,-22,-23,-24,-25,-26,-28,-111,-112,16,16,134,-27,-21,-46,-48,-30,-144,16,-105,-113,16,-135,-29,-38,-104,-107,16,-110,-109,-133,-136,-108,16,-130,-127,-132,]),'INT':([6,8,11,18,26,38,42,44,47,49,50,52,54,55,56,57,58,60,63,64,75,76,77,108,126,135,168,174,201,203,221,222,223,242,243,268,272,276,277,278,279,280,292,293,302,305,306,310,311,],[21,-11,34,-40,21,21,-39,-47,-42,-49,21,21,-22,-23,-24,-25,-26,-28,-111,-112,21,21,21,-27,-21,-46,-48,-30,-144,21,21,-105,-113,21,-135,-29,-38,-104,-107,21,-110,-109,-133,-136,-108,21,-130,-127,-132,]),'FLOAT':([6,8,11,18,26,38,42,44,47,49,50,52,54,55,56,57,58,60,63,64,75,76,77,108,126,135,168,174,201,203,221,222,223,242,243,268,272,276,277,278,279,280,292,293,302,305,306,310,311,],[22,-11,35,-40,22,22,-39,-47,-42,-49,22,22,-22,-23,-24,-25,-26,-28,-111,-112,22,22,22,-27,-21,-46,-48,-30,-144,22,22,-105,-113,22,-135,-29,-38,-104,-107,22,-110,-109,-133,-136,-108,22,-130,-127,-132,]),'BOOLEAN':([6,8,11,18,26,38,42,44,47,49,50,52,54,55,56,57,58,60,63,64,75,76,77,108,126,135,168,174,201,203,221,222,223,242,243,268,272,276,277,278,279,280,292,293,302,305,306,310,311,],[23,-11,36,-40,23,23,-39,-47,-42,-49,23,23,-22,-23,-24,-25,-26,-28,-111,-112,23,23,23,-27,-21,-46,-48,-30,-144,23,23,-105,-113,23,-135,-29,-38,-104,-107,23,-110,-109,-133,-136,-108,23,-130,-127,-132,]),'ARRAY':([6,8,18,26,38,42,44,47,49,52,54,55,56,57,58,60,63,64,75,77,108,126,135,168,174,201,221,222,223,242,243,268,272,276,277,278,279,280,292,293,302,305,306,310,311,],[24,-11,-40,24,24,-39,-47,-42,-49,24,-22,-23,-24,-25,-26,-28,-111,-112,24,24,-27,-21,-46,-48,-30,-144,24,-105,-113,24,-135,-29,-38,-104,-107,24,-110,-109,-133,-136,-108,24,-130,-127,-132,]),'VOID':([11,],[33,]),'ID':([16,18,19,21,22,23,26,32,33,34,35,36,42,43,44,45,47,49,52,54,55,56,57,58,60,63,64,67,75,77,87,88,90,91,92,104,108,110,111,114,115,123,124,125,126,131,135,137,139,140,142,144,145,146,147,148,149,151,153,155,157,158,159,165,167,168,174,193,200,201,218,221,222,223,224,225,226,227,229,232,233,234,235,238,241,242,243,249,268,272,275,276,277,278,279,280,281,289,291,292,293,302,304,305,306,310,311,],[41,-40,46,-14,-15,-16,66,78,79,-17,-18,-19,-39,98,-47,-35,-42,-49,66,-22,-23,-24,-25,-26,-28,-111,-112,98,66,66,98,98,-102,-150,-151,98,-27,98,98,-51,98,98,98,98,-21,205,-46,98,-155,-156,98,-71,-72,-73,-74,-75,-76,98,-151,98,-152,-153,-154,98,-96,-48,-30,98,98,-144,98,66,-105,-113,98,98,98,98,98,98,98,98,98,98,98,66,-135,98,-29,-38,296,-104,-107,66,-110,-109,98,98,98,-133,-136,-108,98,66,-130,-127,-132,]),'SEMICOLON':([17,20,46,59,82,83,84,85,86,89,93,94,95,96,97,98,99,100,101,102,103,109,117,119,121,136,138,141,143,150,152,154,156,161,163,164,166,169,171,175,177,191,209,210,211,212,213,214,216,240,244,246,247,248,259,261,262,282,283,284,285,286,287,288,295,296,303,309,],[44,49,-41,108,135,-157,-157,-157,-157,-101,-83,-84,-85,-86,-87,-157,-88,-90,-91,-92,168,174,-50,-53,-54,-65,-67,-68,-70,-77,-79,-80,-82,-100,-89,-93,-95,-59,-61,-32,223,-52,-66,-69,-78,-81,-99,-103,-60,268,271,272,-94,-97,-119,-121,-122,-116,-117,-118,-120,-123,-124,-125,-98,-43,-115,-126,]),'EQUAL':([17,20,41,46,61,66,113,116,236,237,290,296,],[45,48,81,-41,45,-157,-31,-34,-33,-36,-37,-43,]),'PRINT':([18,26,42,44,47,49,52,54,55,56,57,58,60,63,64,75,77,108,126,135,168,174,201,221,222,223,242,243,268,272,276,277,278,279,280,292,293,302,305,306,310,311,],[-40,68,-39,-47,-42,-49,68,-22,-23,-24,-25,-26,-28,-111,-112,68,68,-27,-21,-46,-48,-30,-144,68,-105,-113,68,-135,-29,-38,-104,-107,68,-110,-109,-133,-136,-108,68,-130,-127,-132,]),'IF':([18,26,42,44,47,49,52,54,55,56,57,58,60,63,64,75,77,108,126,135,168,174,201,221,222,223,242,243,268,272,276,277,278,279,280,292,293,302,305,306,310,311,],[-40,69,-39,-47,-42,-49,69,-22,-23,-24,-25,-26,-28,-111,-112,69,69,-27,-21,-46,-48,-30,-144,69,-105,-113,69,-135,-29,-38,-104,-107,69,-110,-109,-133,-136,-108,69,-130,-127,-132,]),'FOR':([18,26,42,44,47,49,52,54,55,56,57,58,60,63,64,75,77,108,126,135,168,174,201,221,222,223,242,243,268,272,276,277,278,279,280,292,293,302,305,306,310,311,],[-40,72,-39,-47,-42,-49,72,-22,-23,-24,-25,-26,-28,-111,-112,72,72,-27,-21,-46,-48,-30,-144,72,-105,-113,72,-135,-29,-38,-104,-107,72,-110,-109,-133,-136,-108,72,-130,-127,-132,]),'WHILE':([18,26,42,44,47,49,52,54,55,56,57,58,60,63,64,75,77,108,126,135,168,174,201,221,222,223,242,243,268,272,276,277,278,279,280,292,293,302,305,306,310,311,],[-40,73,-39,-47,-42,-49,73,-22,-23,-24,-25,-26,-28,-111,-112,73,73,-27,-21,-46,-48,-30,-144,73,-105,-113,73,-135,-29,-38,-104,-107,73,-110,-109,-133,-136,-108,73,-130,-127,-132,]),'END':([18,26,42,44,47,49,51,52,53,54,55,56,57,58,60,63,64,77,107,108,126,132,135,168,174,201,221,222,223,242,243,254,268,270,271,272,276,277,278,279,280,292,293,297,302,305,306,308,310,311,],[-40,-157,-39,-47,-42,-49,106,-157,-13,-22,-23,-24,-25,-26,-28,-111,-112,-157,-12,-27,-21,207,-46,-48,-30,-144,-157,-105,-113,-157,-135,279,-29,293,294,-38,-104,-107,-157,-110,-109,-133,-136,279,-108,-157,-130,311,-127,-132,]),'RETURN':([18,42,44,47,49,52,53,54,55,56,57,58,60,63,64,75,107,108,127,135,168,174,201,223,268,272,276,277,279,292,293,302,310,311,],[-40,-39,-47,-42,-49,-157,-13,-22,-23,-24,-25,-26,-28,-111,-112,-157,-12,-27,200,-46,-48,-30,-144,-113,-29,-38,-104,-107,-110,-133,-136,-108,-127,-132,]),'ELSE':([18,42,44,47,49,52,53,54,55,56,57,58,60,63,64,107,108,135,168,174,221,222,223,254,268,272,276,277,279,292,293,302,310,311,],[-40,-39,-47,-42,-49,-157,-13,-22,-23,-24,-25,-26,-28,-111,-112,-12,-27,-46,-48,-30,-157,-105,-113,280,-29,-38,-104,-107,-110,-133,-136,-108,-127,-132,]),'COMMA':([21,22,23,83,84,85,86,89,93,94,95,96,97,98,99,100,101,102,105,117,119,120,121,122,129,136,138,141,143,150,152,154,156,161,163,164,166,172,190,191,196,197,205,209,210,211,212,213,214,215,220,247,248,255,266,269,295,299,],[-14,-15,-16,-157,-157,-157,-157,-101,-83,-84,-85,-86,-87,-157,-88,-90,-91,-92,173,-50,-53,193,-54,-56,203,-65,-67,-68,-70,-77,-79,-80,-82,-100,-89,-93,-95,218,238,-52,241,-128,-147,-66,-69,-78,-81,-99,-103,249,251,-94,-97,281,289,291,-98,304,]),'LESS':([24,84,85,86,89,93,94,95,96,97,98,99,100,101,102,117,119,121,150,152,154,156,161,163,164,166,191,211,212,213,214,247,248,295,],[50,146,-157,-157,-101,-83,-84,-85,-86,-87,-157,-88,-90,-91,-92,-50,-53,-54,-77,-79,-80,-82,-100,-89,-93,-95,-52,-78,-81,-99,-103,-94,-97,-98,]),'LPAREN':([27,30,31,43,45,62,66,67,68,69,70,71,72,73,78,79,87,90,91,98,104,110,111,114,115,123,124,125,134,137,139,140,142,144,145,146,147,148,149,151,153,155,157,158,159,165,167,178,179,180,181,182,183,184,185,186,187,188,189,193,200,218,224,225,226,227,229,232,233,234,235,238,241,249,281,289,291,304,],[74,76,76,90,-35,111,114,90,123,-106,124,125,-131,-134,-141,-140,90,-102,-150,114,90,90,90,-51,90,90,90,90,208,90,-155,-156,90,-71,-72,-73,-74,-75,-76,90,-151,90,-152,-153,-154,90,-96,224,225,226,227,228,229,230,231,232,233,234,235,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,]),'PLUS':([43,45,67,85,86,87,89,90,91,93,94,95,96,97,98,99,100,101,102,104,110,111,114,115,117,119,121,123,124,125,137,139,140,142,144,145,146,147,148,149,151,153,154,155,156,157,158,159,161,163,164,165,166,167,191,193,200,212,213,214,218,224,225,226,227,229,232,233,234,235,238,241,247,248,249,281,289,291,295,304,],[91,-35,91,91,-157,91,-101,-102,-150,-83,-84,-85,-86,-87,-157,-88,-90,-91,-92,91,91,91,-51,91,-50,-53,-54,91,91,91,91,-155,-156,91,-71,-72,-73,-74,-75,-76,91,-151,-80,91,-82,-152,-153,-154,-100,-89,-93,91,-95,-96,-52,91,91,-81,-99,-103,91,91,91,91,91,91,91,91,91,91,91,91,-94,-97,91,91,91,91,-98,91,]),'MINUS':([43,45,67,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,110,111,114,115,117,119,121,123,124,125,137,139,140,142,144,145,146,147,148,149,151,153,154,155,156,157,158,159,161,163,164,165,166,167,191,193,200,212,213,214,218,224,225,226,227,229,232,233,234,235,238,241,247,248,249,281,289,291,295,304,],[92,-35,92,153,-157,92,162,-101,-102,-150,-151,-83,-84,-85,-86,-87,-157,-88,-90,-91,-92,92,92,92,-51,92,-50,-53,-54,92,92,92,92,-155,-156,92,-71,-72,-73,-74,-75,-76,92,-151,-80,92,-82,-152,-153,-154,-100,-89,-93,92,-95,-96,-52,92,92,-81,-99,-103,92,92,92,92,92,92,92,92,92,92,92,92,-94,-97,92,92,92,92,-98,92,]),'CTE_I':([43,45,67,87,88,90,91,92,104,110,111,114,115,123,124,125,137,139,140,142,144,145,146,147,148,149,151,153,155,157,158,159,162,165,167,173,193,200,218,224,225,226,227,229,232,233,234,235,238,241,249,251,281,289,291,304,],[99,-35,99,99,99,-102,-150,163,99,99,99,-51,99,99,99,99,99,-155,-156,99,-71,-72,-73,-74,-75,-76,99,-151,99,-152,-153,-154,163,99,-96,220,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,274,99,99,99,99,]),'CTE_F':([43,45,67,87,88,90,91,92,104,110,111,114,115,123,124,125,137,139,140,142,144,145,146,147,148,149,151,153,155,157,158,159,165,167,193,200,218,224,225,226,227,229,232,233,234,235,238,241,249,281,289,291,304,],[100,-35,100,100,100,-102,-150,-151,100,100,100,-51,100,100,100,100,100,-155,-156,100,-71,-72,-73,-74,-75,-76,100,-151,100,-152,-153,-154,100,-96,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,]),'TRUE':([43,45,67,87,88,90,91,92,104,110,111,114,115,123,124,125,137,139,140,142,144,145,146,147,148,149,151,153,155,157,158,159,165,167,193,200,218,224,225,226,227,229,232,233,234,235,238,241,249,281,289,291,304,],[101,-35,101,101,101,-102,-150,-151,101,101,101,-51,101,101,101,101,101,-155,-156,101,-71,-72,-73,-74,-75,-76,101,-151,101,-152,-153,-154,101,-96,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,]),'FALSE':([43,45,67,87,88,90,91,92,104,110,111,114,115,123,124,125,137,139,140,142,144,145,146,147,148,149,151,153,155,157,158,159,165,167,193,200,218,224,225,226,227,229,232,233,234,235,238,241,249,281,289,291,304,],[102,-35,102,102,102,-102,-150,-151,102,102,102,-51,102,102,102,102,102,-155,-156,102,-71,-72,-73,-74,-75,-76,102,-151,102,-152,-153,-154,102,-96,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,]),'LBRACKET':([48,66,98,],[104,115,167,]),'POINT':([65,66,],[112,-114,]),'RPAREN':([67,74,76,83,84,85,86,89,93,94,95,96,97,98,99,100,101,102,114,117,118,119,120,121,122,128,129,130,136,138,141,143,150,152,154,156,160,161,163,164,166,176,191,192,194,195,198,202,203,204,205,208,209,210,211,212,213,214,228,230,231,239,245,247,248,256,257,258,260,263,264,265,295,298,300,301,307,],[121,126,-157,-157,-157,-157,-157,-101,-83,-84,-85,-86,-87,-157,-88,-90,-91,-92,-51,-50,121,-53,-157,-54,-56,201,-157,-146,-65,-67,-68,-70,-77,-79,-80,-82,214,-100,-89,-93,-95,222,-52,-55,-58,240,243,-145,-157,-149,-147,246,-66,-69,-78,-81,-99,-103,259,261,262,-57,-148,-94,-97,282,283,284,285,286,287,288,-98,303,306,-129,309,]),'AND':([83,84,85,86,89,93,94,95,96,97,98,99,100,101,102,117,119,121,141,143,150,152,154,156,161,163,164,166,191,210,211,212,213,214,247,248,295,],[139,-157,-157,-157,-101,-83,-84,-85,-86,-87,-157,-88,-90,-91,-92,-50,-53,-54,-68,-70,-77,-79,-80,-82,-100,-89,-93,-95,-52,-69,-78,-81,-99,-103,-94,-97,-98,]),'OR':([83,84,85,86,89,93,94,95,96,97,98,99,100,101,102,117,119,121,141,143,150,152,154,156,161,163,164,166,191,210,211,212,213,214,247,248,295,],[140,-157,-157,-157,-101,-83,-84,-85,-86,-87,-157,-88,-90,-91,-92,-50,-53,-54,-68,-70,-77,-79,-80,-82,-100,-89,-93,-95,-52,-69,-78,-81,-99,-103,-94,-97,-98,]),'RBRACKET':([83,84,85,86,89,93,94,95,96,97,98,99,100,101,102,104,117,119,121,136,138,141,143,150,152,154,156,161,163,164,166,170,172,190,191,209,210,211,212,213,214,215,217,219,247,248,250,267,273,295,],[-157,-157,-157,-157,-101,-83,-84,-85,-86,-87,-157,-88,-90,-91,-92,171,-50,-53,-54,-65,-67,-68,-70,-77,-79,-80,-82,-100,-89,-93,-95,216,-157,237,-52,-66,-69,-78,-81,-99,-103,248,-62,-64,-94,-97,-63,290,295,-98,]),'GREATER':([84,85,86,89,93,94,95,96,97,98,99,100,101,102,117,119,121,150,152,154,156,161,163,164,166,191,211,212,213,214,220,247,248,252,253,274,295,],[144,-157,-157,-101,-83,-84,-85,-86,-87,-157,-88,-90,-91,-92,-50,-53,-54,-77,-79,-80,-82,-100,-89,-93,-95,-52,-78,-81,-99,-103,-157,-94,-97,275,-45,-44,-98,]),'GREATEREQUAL':([84,85,86,89,93,94,95,96,97,98,99,100,101,102,117,119,121,150,152,154,156,161,163,164,166,191,211,212,213,214,247,248,295,],[145,-157,-157,-101,-83,-84,-85,-86,-87,-157,-88,-90,-91,-92,-50,-53,-54,-77,-79,-80,-82,-100,-89,-93,-95,-52,-78,-81,-99,-103,-94,-97,-98,]),'LESSEQUAL':([84,85,86,89,93,94,95,96,97,98,99,100,101,102,117,119,121,150,152,154,156,161,163,164,166,191,211,212,213,214,247,248,295,],[147,-157,-157,-101,-83,-84,-85,-86,-87,-157,-88,-90,-91,-92,-50,-53,-54,-77,-79,-80,-82,-100,-89,-93,-95,-52,-78,-81,-99,-103,-94,-97,-98,]),'DEQUAL':([84,85,86,89,93,94,95,96,97,98,99,100,101,102,117,119,121,150,152,154,156,161,163,164,166,191,211,212,213,214,247,248,295,],[148,-157,-157,-101,-83,-84,-85,-86,-87,-157,-88,-90,-91,-92,-50,-53,-54,-77,-79,-80,-82,-100,-89,-93,-95,-52,-78,-81,-99,-103,-94,-97,-98,]),'DISTINT':([84,85,86,89,93,94,95,96,97,98,99,100,101,102,117,119,121,150,152,154,156,161,163,164,166,191,211,212,213,214,247,248,295,],[149,-157,-157,-101,-83,-84,-85,-86,-87,-157,-88,-90,-91,-92,-50,-53,-54,-77,-79,-80,-82,-100,-89,-93,-95,-52,-78,-81,-99,-103,-94,-97,-98,]),'TIMES':([86,89,93,94,95,96,97,98,99,100,101,102,117,119,121,161,163,164,166,191,213,214,247,248,295,],[157,-101,-83,-84,-85,-86,-87,-157,-88,-90,-91,-92,-50,-53,-54,-100,-89,-93,-95,-52,-99,-103,-94,-97,-98,]),'DIVIDE':([86,89,93,94,95,96,97,98,99,100,101,102,117,119,121,161,163,164,166,191,213,214,247,248,295,],[158,-101,-83,-84,-85,-86,-87,-157,-88,-90,-91,-92,-50,-53,-54,-100,-89,-93,-95,-52,-99,-103,-94,-97,-98,]),'PERCENT':([86,89,93,94,95,96,97,98,99,100,101,102,117,119,121,161,163,164,166,191,213,214,247,248,295,],[159,-101,-83,-84,-85,-86,-87,-157,-88,-90,-91,-92,-50,-53,-54,-100,-89,-93,-95,-52,-99,-103,-94,-97,-98,]),'SETPOSITION':([112,],[178,]),'CIRCLE':([112,],[179,]),'RIGHT':([112,],[180,]),'LEFT':([112,],[181,]),'HIDE':([112,],[182,]),'SQUARE':([112,],[183,]),'CLEAR':([112,],[184,]),'SHOW':([112,],[185,]),'BACK':([112,],[186,]),'SPEED':([112,],[187,]),'FORWARD':([112,],[188,]),'SETCOLOR':([112,],[189,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'init':([0,],[2,]),'empty':([0,2,4,5,9,12,15,26,52,66,75,76,77,80,83,84,85,86,98,120,129,172,203,220,221,242,278,305,],[3,10,10,14,10,14,40,53,53,116,53,130,53,40,138,143,152,156,166,194,204,219,130,253,53,53,53,53,]),'globales':([2,],[4,]),'funciones':([2,4,],[5,12,]),'global_1':([2,15,80,],[6,38,38,]),'funciones_2':([2,4,9,],[7,7,28,]),'funcion':([2,4,9,],[9,9,9,]),'programa_end':([5,12,],[13,37,]),'vars':([6,26,38,52,75,77,221,242,278,305,],[15,58,80,58,58,58,58,58,58,58,]),'vars_id':([6,26,38,52,75,77,221,242,278,305,],[17,17,17,17,17,17,17,17,17,17,]),'vars_aux':([6,26,38,52,75,77,221,242,278,305,],[18,18,18,18,18,18,18,18,18,18,]),'data_type':([6,26,38,50,52,75,76,77,203,221,242,278,305,],[19,19,19,105,19,19,131,19,131,19,19,19,19,]),'array':([6,26,38,52,75,77,221,242,278,305,],[20,20,20,20,20,20,20,20,20,20,]),'main':([7,],[25,]),'main_1':([7,],[26,]),'funcion_aux':([11,],[29,]),'funcion_1':([11,],[30,]),'funcion_void':([11,],[31,]),'data_type_func':([11,],[32,]),'globales_2':([15,80,],[39,133,]),'vars2':([17,],[42,]),'asignacion_equal':([17,61,],[43,110,]),'vars3':([20,],[47,]),'bloque':([26,52,75,77,221,242,278,305,],[51,107,127,132,254,270,297,308,]),'estatuto':([26,52,75,77,221,242,278,305,],[52,52,52,52,52,52,52,52,]),'asignacion':([26,52,75,77,221,242,278,305,],[54,54,54,54,54,54,54,54,]),'condicion':([26,52,75,77,221,242,278,305,],[55,55,55,55,55,55,55,55,]),'ciclo':([26,52,75,77,221,242,278,305,],[56,56,56,56,56,56,56,56,]),'accion':([26,52,75,77,221,242,278,305,],[57,57,57,57,57,57,57,57,]),'llamada':([26,43,52,67,75,77,87,88,104,110,111,115,123,124,125,137,142,151,155,165,193,200,218,221,224,225,226,227,229,232,233,234,235,238,241,242,249,278,281,289,291,304,305,],[59,97,59,97,59,59,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,59,97,97,97,97,97,97,97,97,97,97,97,59,97,59,97,97,97,97,59,]),'print':([26,52,75,77,221,242,278,305,],[60,60,60,60,60,60,60,60,]),'asignacion_id':([26,52,75,77,221,242,278,305,],[61,61,61,61,61,61,61,61,]),'condicion_id':([26,52,75,77,221,242,278,305,],[62,62,62,62,62,62,62,62,]),'for':([26,52,75,77,221,242,278,305,],[63,63,63,63,63,63,63,63,]),'while':([26,52,75,77,221,242,278,305,],[64,64,64,64,64,64,64,64,]),'accion_id':([26,52,75,77,221,242,278,305,],[65,65,65,65,65,65,65,65,]),'llamada_id':([26,43,52,67,75,77,87,88,104,110,111,115,123,124,125,137,142,151,155,165,193,200,218,221,224,225,226,227,229,232,233,234,235,238,241,242,249,278,281,289,291,304,305,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'for_init':([26,52,75,77,221,242,278,305,],[70,70,70,70,70,70,70,70,]),'while_init':([26,52,75,77,221,242,278,305,],[71,71,71,71,71,71,71,71,]),'var_local':([30,31,],[75,77,]),'super_exp':([43,67,87,104,110,111,115,123,125,137,165,193,200,218,238,249,],[82,122,160,172,175,176,190,195,198,209,215,122,244,172,267,273,]),'expresion':([43,67,87,104,110,111,115,123,125,137,165,193,200,218,238,249,],[83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,]),'exp':([43,67,87,104,110,111,115,123,124,125,137,142,151,165,193,200,218,224,225,226,227,229,232,233,234,235,238,241,249,281,289,291,304,],[84,84,84,84,84,84,84,84,197,84,84,210,211,84,84,84,84,255,256,257,258,260,263,264,265,266,84,197,84,298,299,301,307,]),'termino':([43,67,87,104,110,111,115,123,124,125,137,142,151,155,165,193,200,218,224,225,226,227,229,232,233,234,235,238,241,249,281,289,291,304,],[85,85,85,85,85,85,85,85,85,85,85,85,85,212,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,]),'factor':([43,67,87,104,110,111,115,123,124,125,137,142,151,155,165,193,200,218,224,225,226,227,229,232,233,234,235,238,241,249,281,289,291,304,],[86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,]),'lparen_factor':([43,67,87,104,110,111,115,123,124,125,137,142,151,155,165,193,200,218,224,225,226,227,229,232,233,234,235,238,241,249,281,289,291,304,],[87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,]),'addop':([43,67,85,87,104,110,111,115,123,124,125,137,142,151,155,165,193,200,218,224,225,226,227,229,232,233,234,235,238,241,249,281,289,291,304,],[88,88,151,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,]),'var_cte':([43,67,87,88,104,110,111,115,123,124,125,137,142,151,155,165,193,200,218,224,225,226,227,229,232,233,234,235,238,241,249,281,289,291,304,],[89,89,89,161,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,]),'var_cte_1':([43,67,87,88,104,110,111,115,123,124,125,137,142,151,155,165,193,200,218,224,225,226,227,229,232,233,234,235,238,241,249,281,289,291,304,],[93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,]),'var_cte_i':([43,67,87,88,104,110,111,115,123,124,125,137,142,151,155,165,193,200,218,224,225,226,227,229,232,233,234,235,238,241,249,281,289,291,304,],[94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,]),'var_cte_f':([43,67,87,88,104,110,111,115,123,124,125,137,142,151,155,165,193,200,218,224,225,226,227,229,232,233,234,235,238,241,249,281,289,291,304,],[95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,]),'var_cte_b':([43,67,87,88,104,110,111,115,123,124,125,137,142,151,155,165,193,200,218,224,225,226,227,229,232,233,234,235,238,241,249,281,289,291,304,],[96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,]),'def_array':([48,],[103,]),'asignacion_2':([61,],[109,]),'asignacion_array':([66,],[113,]),'llamada_2':([67,],[117,]),'llamada_exp':([67,193,],[118,239,]),'llamada_rparen':([67,118,],[119,191,]),'llamada_super_exp':([67,193,],[120,120,]),'var_local_2':([76,203,],[128,245,]),'var_local_2_1':([76,203,],[129,129,]),'super_exp_2':([83,],[136,]),'logicop':([83,],[137,]),'expresion_2':([84,],[141,]),'relop':([84,],[142,]),'exp_2':([85,],[150,]),'termino_2':([86,],[154,]),'timesop':([86,],[155,]),'var_cte_2':([98,],[164,]),'var_cte_2_lbracket':([98,],[165,]),'def_array_2':([104,],[169,]),'def_array_cte':([104,218,],[170,250,]),'accion_params':([112,],[177,]),'llamada_exp2':([120,],[192,]),'for_exp':([124,241,],[196,269,]),'funcion_2':([127,],[199,]),'var_local_3':([129,],[202,]),'funcion_end':([132,],[206,]),'rparen_factor':([160,],[213,]),'def_array_cte_2':([172,],[217,]),'rparen_condicion':([176,],[221,]),'asignacion_3':([190,],[236,]),'rparen_while':([198,],[242,]),'var_cte_3':([215,],[247,]),'array_2':([220,],[252,]),'condicion_2':([254,],[276,]),'condicion_end':([254,297,],[277,302,]),'condicion_else':([254,],[278,]),'while_end':([270,],[292,]),'for_exp2':([291,],[300,]),'for_rparen':([300,],[305,]),'for_end':([308,],[310,]),}

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
  ('asignacion_id -> ID asignacion_array','asignacion_id',2,'p_asignacion_id','c_parser.py',101),
  ('asignacion_2 -> asignacion_equal super_exp','asignacion_2',2,'p_asignacion_2','c_parser.py',140),
  ('asignacion_array -> LBRACKET super_exp asignacion_3','asignacion_array',3,'p_asignacion_array','c_parser.py',157),
  ('asignacion_array -> empty','asignacion_array',1,'p_asignacion_array','c_parser.py',158),
  ('asignacion_equal -> EQUAL','asignacion_equal',1,'p_asignacion_equal','c_parser.py',165),
  ('asignacion_3 -> RBRACKET','asignacion_3',1,'p_asignacion_3','c_parser.py',169),
  ('asignacion_3 -> COMMA super_exp RBRACKET','asignacion_3',3,'p_asignacion_3','c_parser.py',170),
  ('vars -> DRAW ID EQUAL DRAW LPAREN RPAREN SEMICOLON','vars',7,'p_vars','c_parser.py',177),
  ('vars -> vars_id vars2','vars',2,'p_vars','c_parser.py',178),
  ('vars -> vars_aux','vars',1,'p_vars','c_parser.py',179),
  ('vars_id -> data_type ID','vars_id',2,'p_vars_id','c_parser.py',191),
  ('vars_aux -> array vars3','vars_aux',2,'p_vars_aux','c_parser.py',203),
  ('array -> ARRAY LESS data_type COMMA CTE_I array_2 GREATER ID','array',8,'p_array','c_parser.py',215),
  ('array_2 -> COMMA CTE_I','array_2',2,'p_array_2','c_parser.py',239),
  ('array_2 -> empty','array_2',1,'p_array_2','c_parser.py',240),
  ('vars2 -> asignacion_equal super_exp SEMICOLON','vars2',3,'p_vars_2','c_parser.py',247),
  ('vars2 -> SEMICOLON','vars2',1,'p_vars_2','c_parser.py',248),
  ('vars3 -> EQUAL def_array SEMICOLON','vars3',3,'p_vars_3','c_parser.py',268),
  ('vars3 -> SEMICOLON','vars3',1,'p_vars_3','c_parser.py',269),
  ('llamada -> llamada_id llamada_2','llamada',2,'p_llamada','c_parser.py',276),
  ('llamada_id -> ID LPAREN','llamada_id',2,'p_llamada_id','c_parser.py',290),
  ('llamada_2 -> llamada_exp llamada_rparen','llamada_2',2,'p_llamada_2','c_parser.py',304),
  ('llamada_2 -> llamada_rparen','llamada_2',1,'p_llamada_2','c_parser.py',305),
  ('llamada_rparen -> RPAREN','llamada_rparen',1,'p_llamada_rparen','c_parser.py',309),
  ('llamada_exp -> llamada_super_exp llamada_exp2','llamada_exp',2,'p_llamada_exp','c_parser.py',317),
  ('llamada_super_exp -> super_exp','llamada_super_exp',1,'p_llamada_super_exp','c_parser.py',321),
  ('llamada_exp2 -> COMMA llamada_exp','llamada_exp2',2,'p_llamada_exp_2','c_parser.py',339),
  ('llamada_exp2 -> empty','llamada_exp2',1,'p_llamada_exp_2','c_parser.py',340),
  ('def_array -> LBRACKET def_array_2','def_array',2,'p_def_array','c_parser.py',344),
  ('def_array_2 -> def_array_cte RBRACKET','def_array_2',2,'p_def_array_2','c_parser.py',348),
  ('def_array_2 -> RBRACKET','def_array_2',1,'p_def_array_2','c_parser.py',349),
  ('def_array_cte -> super_exp def_array_cte_2','def_array_cte',2,'p_def_array_cte','c_parser.py',353),
  ('def_array_cte_2 -> COMMA def_array_cte','def_array_cte_2',2,'p_def_array_cte_2','c_parser.py',357),
  ('def_array_cte_2 -> empty','def_array_cte_2',1,'p_def_array_cte_2','c_parser.py',358),
  ('super_exp -> expresion super_exp_2','super_exp',2,'p_super_exp','c_parser.py',362),
  ('super_exp_2 -> logicop super_exp','super_exp_2',2,'p_super_exp_2','c_parser.py',366),
  ('super_exp_2 -> empty','super_exp_2',1,'p_super_exp_2','c_parser.py',367),
  ('expresion -> exp expresion_2','expresion',2,'p_expresion','c_parser.py',370),
  ('expresion_2 -> relop exp','expresion_2',2,'p_expresion_2','c_parser.py',390),
  ('expresion_2 -> empty','expresion_2',1,'p_expresion_2','c_parser.py',391),
  ('relop -> GREATER','relop',1,'p_relop','c_parser.py',395),
  ('relop -> GREATEREQUAL','relop',1,'p_relop','c_parser.py',396),
  ('relop -> LESS','relop',1,'p_relop','c_parser.py',397),
  ('relop -> LESSEQUAL','relop',1,'p_relop','c_parser.py',398),
  ('relop -> DEQUAL','relop',1,'p_relop','c_parser.py',399),
  ('relop -> DISTINT','relop',1,'p_relop','c_parser.py',400),
  ('exp -> termino exp_2','exp',2,'p_exp','c_parser.py',404),
  ('exp_2 -> addop exp','exp_2',2,'p_exp_2','c_parser.py',425),
  ('exp_2 -> empty','exp_2',1,'p_exp_2','c_parser.py',426),
  ('termino -> factor termino_2','termino',2,'p_termino','c_parser.py',430),
  ('termino_2 -> timesop termino','termino_2',2,'p_termino_2','c_parser.py',450),
  ('termino_2 -> empty','termino_2',1,'p_termino_2','c_parser.py',451),
  ('var_cte -> var_cte_1','var_cte',1,'p_var_cte','c_parser.py',455),
  ('var_cte -> var_cte_i','var_cte',1,'p_var_cte','c_parser.py',456),
  ('var_cte -> var_cte_f','var_cte',1,'p_var_cte','c_parser.py',457),
  ('var_cte -> var_cte_b','var_cte',1,'p_var_cte','c_parser.py',458),
  ('var_cte -> llamada','var_cte',1,'p_var_cte','c_parser.py',459),
  ('var_cte_i -> CTE_I','var_cte_i',1,'p_var_cte_i','c_parser.py',463),
  ('var_cte_i -> MINUS CTE_I','var_cte_i',2,'p_var_cte_i','c_parser.py',464),
  ('var_cte_f -> CTE_F','var_cte_f',1,'p_var_cte_f','c_parser.py',473),
  ('var_cte_b -> TRUE','var_cte_b',1,'p_var_cte_b','c_parser.py',479),
  ('var_cte_b -> FALSE','var_cte_b',1,'p_var_cte_b','c_parser.py',480),
  ('var_cte_1 -> ID var_cte_2','var_cte_1',2,'p_var_cte_1','c_parser.py',486),
  ('var_cte_2 -> var_cte_2_lbracket super_exp var_cte_3','var_cte_2',3,'p_var_cte_2','c_parser.py',525),
  ('var_cte_2 -> empty','var_cte_2',1,'p_var_cte_2','c_parser.py',526),
  ('var_cte_2_lbracket -> LBRACKET','var_cte_2_lbracket',1,'p_var_cte_2_lbracket','c_parser.py',533),
  ('var_cte_3 -> RBRACKET','var_cte_3',1,'p_var_cte_3','c_parser.py',537),
  ('var_cte_3 -> COMMA super_exp RBRACKET','var_cte_3',3,'p_var_cte_3','c_parser.py',538),
  ('factor -> lparen_factor super_exp rparen_factor','factor',3,'p_factor','c_parser.py',546),
  ('factor -> addop var_cte','factor',2,'p_factor','c_parser.py',547),
  ('factor -> var_cte','factor',1,'p_factor','c_parser.py',548),
  ('lparen_factor -> LPAREN','lparen_factor',1,'p_lparen_factor','c_parser.py',569),
  ('rparen_factor -> RPAREN','rparen_factor',1,'p_rparen_factor','c_parser.py',573),
  ('condicion -> condicion_id LPAREN super_exp rparen_condicion bloque condicion_2','condicion',6,'p_condicion','c_parser.py',577),
  ('rparen_condicion -> RPAREN','rparen_condicion',1,'p_rparen_condicion','c_parser.py',581),
  ('condicion_id -> IF','condicion_id',1,'p_condicion_id','c_parser.py',594),
  ('condicion_2 -> condicion_end','condicion_2',1,'p_condicion_2','c_parser.py',598),
  ('condicion_2 -> condicion_else bloque condicion_end','condicion_2',3,'p_condicion_2','c_parser.py',599),
  ('condicion_else -> ELSE','condicion_else',1,'p_condicion_else','c_parser.py',603),
  ('condicion_end -> END','condicion_end',1,'p_condicion_end','c_parser.py',610),
  ('ciclo -> for','ciclo',1,'p_ciclo','c_parser.py',616),
  ('ciclo -> while','ciclo',1,'p_ciclo','c_parser.py',617),
  ('accion -> accion_id POINT accion_params SEMICOLON','accion',4,'p_accion','c_parser.py',621),
  ('accion_id -> ID','accion_id',1,'p_accion_id','c_parser.py',630),
  ('accion_params -> SETPOSITION LPAREN exp COMMA exp RPAREN','accion_params',6,'p_accion_params','c_parser.py',643),
  ('accion_params -> CIRCLE LPAREN exp RPAREN','accion_params',4,'p_accion_params','c_parser.py',644),
  ('accion_params -> RIGHT LPAREN exp RPAREN','accion_params',4,'p_accion_params','c_parser.py',645),
  ('accion_params -> LEFT LPAREN exp RPAREN','accion_params',4,'p_accion_params','c_parser.py',646),
  ('accion_params -> HIDE LPAREN RPAREN','accion_params',3,'p_accion_params','c_parser.py',647),
  ('accion_params -> SQUARE LPAREN exp RPAREN','accion_params',4,'p_accion_params','c_parser.py',648),
  ('accion_params -> CLEAR LPAREN RPAREN','accion_params',3,'p_accion_params','c_parser.py',649),
  ('accion_params -> SHOW LPAREN RPAREN','accion_params',3,'p_accion_params','c_parser.py',650),
  ('accion_params -> BACK LPAREN exp RPAREN','accion_params',4,'p_accion_params','c_parser.py',651),
  ('accion_params -> SPEED LPAREN exp RPAREN','accion_params',4,'p_accion_params','c_parser.py',652),
  ('accion_params -> FORWARD LPAREN exp RPAREN','accion_params',4,'p_accion_params','c_parser.py',653),
  ('accion_params -> SETCOLOR LPAREN exp COMMA exp COMMA exp RPAREN','accion_params',8,'p_accion_params','c_parser.py',654),
  ('for -> for_init LPAREN for_exp COMMA for_exp COMMA for_exp2 for_rparen bloque for_end','for',10,'p_for','c_parser.py',677),
  ('for_exp -> exp','for_exp',1,'p_for_exp','c_parser.py',681),
  ('for_exp2 -> exp','for_exp2',1,'p_for_exp2','c_parser.py',688),
  ('for_rparen -> RPAREN','for_rparen',1,'p_for_rparen','c_parser.py',708),
  ('for_init -> FOR','for_init',1,'p_for_init','c_parser.py',722),
  ('for_end -> END','for_end',1,'p_for_end','c_parser.py',726),
  ('while -> while_init LPAREN super_exp rparen_while bloque while_end','while',6,'p_while','c_parser.py',741),
  ('while_init -> WHILE','while_init',1,'p_while_init','c_parser.py',745),
  ('rparen_while -> RPAREN','rparen_while',1,'p_rparen_while','c_parser.py',750),
  ('while_end -> END','while_end',1,'p_while_end','c_parser.py',762),
  ('funcion -> DEF funcion_aux','funcion',2,'p_funcion','c_parser.py',770),
  ('funcion_aux -> funcion_1 var_local bloque funcion_2','funcion_aux',4,'p_funcion_aux','c_parser.py',775),
  ('funcion_aux -> funcion_void var_local bloque funcion_end','funcion_aux',4,'p_funcion_aux','c_parser.py',776),
  ('funcion_void -> VOID ID','funcion_void',2,'p_funcion_void','c_parser.py',780),
  ('funcion_1 -> data_type_func ID','funcion_1',2,'p_funcion_1','c_parser.py',790),
  ('funcion_2 -> RETURN super_exp SEMICOLON END','funcion_2',4,'p_funcion_2','c_parser.py',801),
  ('funcion_end -> END','funcion_end',1,'p_funcion_end','c_parser.py',814),
  ('var_local -> LPAREN var_local_2 RPAREN','var_local',3,'p_var_local','c_parser.py',818),
  ('var_local_2 -> var_local_2_1 var_local_3','var_local_2',2,'p_var_local_2','c_parser.py',822),
  ('var_local_2 -> empty','var_local_2',1,'p_var_local_2','c_parser.py',823),
  ('var_local_2_1 -> data_type ID','var_local_2_1',2,'p_var_local_2_1','c_parser.py',827),
  ('var_local_3 -> COMMA var_local_2','var_local_3',2,'p_var_local_3','c_parser.py',838),
  ('var_local_3 -> empty','var_local_3',1,'p_var_local_3','c_parser.py',839),
  ('addop -> PLUS','addop',1,'p_addop','c_parser.py',843),
  ('addop -> MINUS','addop',1,'p_addop','c_parser.py',844),
  ('timesop -> TIMES','timesop',1,'p_timesop','c_parser.py',848),
  ('timesop -> DIVIDE','timesop',1,'p_timesop','c_parser.py',849),
  ('timesop -> PERCENT','timesop',1,'p_timesop','c_parser.py',850),
  ('logicop -> AND','logicop',1,'p_logicop','c_parser.py',854),
  ('logicop -> OR','logicop',1,'p_logicop','c_parser.py',855),
  ('empty -> <empty>','empty',0,'p_empty','c_parser.py',859),
]
