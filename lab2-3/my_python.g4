grammar my_python;


/// типы данных
expression  : '(' expression ')' | expression SIGN expression | INT  | REAL | BOOL | NEGATIVE | STRING | DICT | LIST;

INT  : [0-9]+;
REAL  : INT '.' INT;
STRING : [a-z_]+;
SIGN  : '<'|'>'|'=='|'!='|'='|'<='|'>='|'**'|'*'|'/'|'+'|'-'|'%';
BOOL : 'True' | 'False';
NEGATIVE : '-' INT ;
INDEX : INT | NEGATIVE;
DICT  : '{'(NOT_LAST_PAIR)*LAST_PAIR '}';
NOT_LAST_PAIR  :  (BOOL | INT | REAL | STRING) ':' (BOOL | INT | REAL | STRING) ',';
LAST_PAIR  :  (BOOL | INT | REAL | STRING) ':' (BOOL | INT | REAL | STRING);
LIST_ELEMENT : INT | REAL | STRING | BOOL;
LIST :  '[' LIST_ELEMENT ']';
SPACES : [ \t\n]+ -> skip ;