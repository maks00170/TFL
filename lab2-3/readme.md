# 2 и 3 задание по курсу формальных языков "my_Python"

## Запуск
[Инструкция](https://evogeek.ru/articles/27474/) для установки и сборки проекта.
 


## Доступные методы:
1. INT : [0-9]+
2. REAL : INT'.'INT 
3. STRING :  [a-z_]
4. SIGN : < | > | == | != | = | <= | >= | ** | * | / | + | - | %
5. BOOL : True | False 
6. NEGATIVE : -INT
7. INDEX : INT | NEGATIVE
8. DICT : {(NOT_LAST_PAIR)*LAST_PAIR}  #здесь скобки не символы алфавита 
9. NOT_LAST_PAIR : (BOOL|INT|REAL|STRING):(BOOL|INT|REAL|STRING), #здесь скобки не символы алфавита
10.	LAST_PAIR : (BOOL|INT|REAL|STRING):(BOOL|INT|REAL|STRING) 
11. LIST_ELEMENT: : INT | DOUBLE | STRING | BOOL;
12. LIST  : '[' LIST_ELEMENT ']';