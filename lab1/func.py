
from automat import NonDeterministicAutomat, DeterministicAutomat
from typing import Dict, List, Tuple
epsilon = 'epsilon'

priorities = {
    ';': 0,
    '#': 1,
    ',': 1,
    '*': 2,
    '+': 2,
    '?': 2
    }

binary = [';', '#', ',']
unary = ['*', '+', '?']


def combine_automat(automat1, automat2):   # Объединяем два недетерминированных автомата в один автомат
    #Объединяю ключи таблиц переходов
    keys = set(list(automat1.table.keys()) + list(automat2.table.keys()))
    #список состояний-результатов для объединенного автомата
    result = [state + automat1.num_states() for state in automat2.result_states]
    result.extend(automat1.result_states)
    new_table = {}
    '''
    Для каждого ключа нового множества: если ключ есть в таблице перехода автомата1,добавляем его переходы в новый список,
      иначе- пустые переходы для каждого состояния автомата1.
      Если ключ есть в таблице переходов автомата2, добавляем его переходы в новый список,
      прибавляя значение состояний автомата 1 к переходам, иначе- добавляем пустые переходы для каждого состояния автомата2
    '''
    for k in keys:
        new_row = []
        if k in automat1.table:
            new_row.extend(automat1.table[k])
        else:
            new_row.extend([[] for _ in range(automat1.num_states())])
        if k in automat2.table:
            new_row.extend([[s + automat1.num_states() for s in states] for states in automat2.table[k]])
        else:
            new_row.extend([[] for _ in range(automat2.num_states())])
        new_table[k] = new_row
    table = new_table
    result_states = result
    merged_automat = NonDeterministicAutomat(table, result_states)
    return merged_automat

#ход работы с операторами

def matching(automat1, automat2):                 # оператором ,
    merged = combine_automat(automat1, automat2)
    for start in automat1.result_states:
        merged.set_trans(start, epsilon, automat1.num_states())
    merged.result_states = [s + automat1.num_states() for s in automat2.result_states]
    return merged


def next(automat1, automat2):                   # оператором ;
    merged = combine_automat(automat1, automat2)
    shifted_finals = [f + 1 for f in merged.result_states]
    shifted_table = {}
    for char, state_list in merged.table.items():
        shifted_table[char] = [[]] + [[state + 1 for state in states] for states in state_list] + [[]]
    new = NonDeterministicAutomat(table=shifted_table, result_states=[])
    new.set_trans(0, epsilon, 1)
    new.set_trans(0, epsilon, automat1.num_states() + 1)
    for f in shifted_finals:
        new.set_trans(f, epsilon, new.num_states() - 1)
    new.result_states = [new.num_states() - 1]
    result_next = new
    return result_next


def multiplication(automat1):                                 # оператором *
    shifted_finals = [f + 1 for f in automat1.result_states]
    shifted_table = {}
    for char, state_list in automat1.table.items():
        shifted_table[char] = [[]] + [[state + 1 for state in states] for states in state_list] + [[]]
    new = NonDeterministicAutomat(table=shifted_table, result_states=[])
    for f in shifted_finals:
        new.set_trans(f, epsilon, 1)
        new.set_trans(f, epsilon, new.num_states() - 1)
    new.set_trans(0, epsilon, 1)
    new.set_trans(0, epsilon, new.num_states() - 1)
    new.result_states = [new.num_states() - 1]
    result_mult = new
    return result_mult


def merged(automat1):                                           # оператором +
    return matching(automat1, multiplication(automat1))


def generalized_iteration(automat1, automat2):                  # оператором #
    return matching(automat1, multiplication(matching(automat2, automat1)))


# прием пустой строки
def optional(automat1):
    automat1_copy = automat1.copy()
    for f in automat1_copy.result_states:
        automat1_copy.set_trans(0, epsilon, f)
    return automat1_copy


def primitive_fnda(actual_string):         # создание недетерминированного автомата
    table: Dict[str, List[List[int]]] = {}
    for i, c in enumerate(actual_string):
        if c not in table:
            table[c] = [[] for _ in range(len(actual_string) + 1)]
        table[c][i].append(i + 1)
    table=table
    result_states=[len(actual_string)]
    return NonDeterministicAutomat(table,result_states)


operations = {
    '*': multiplication,
    '+': merged,
    ';': next,
    ',': matching,
    '#': generalized_iteration,
    '?': optional
    }


def is_character(c):
    return c not in {*operations.keys(), '(', ')'}


def regex_p(regexp):     # преобразование регулярки
    if len(regexp) == 0:
        return ''
    new = []
    last = None
    for c in regexp:
        if last is None:
            last = c
            new.append(c)
            continue
        if last in unary and c == '(' \
                or last in unary and is_character(c) \
                or is_character(last) and is_character(c) \
                or last == ')' and is_character(c) \
                or is_character(last) and c == '(':
            new.append(',')
        new.append(c)
        last = c
    return ''.join(new)



def construct_fnda(regexp):   # строим недетерминированный конечный автомат на основе регулярки
    data = '' 
    op_stack = []
    eval_stack = []

    # Функция для обработки операторов в соответствии с их приоритетами. Извлекаем операторы из стека операторов
    def process_operator(priority=-1):
        while len(op_stack) != 0 \
                and op_stack[-1] != '(' \
                and (op_stack[-1] not in operations.keys() or priorities[op_stack[-1]] > priority):
            op = op_stack[-1]
            if op in binary:
                eval_stack.append(operations[op](eval_stack[-2], eval_stack[-1]))
                eval_stack.pop(-2)
                eval_stack.pop(-2)
                op_stack.pop()
            elif op in unary:
                eval_stack.append(operations[op](eval_stack[-1]))
                eval_stack.pop(-2)
                op_stack.pop()
        if priority == -1 and len(op_stack) != 0 and op_stack[-1] == '(':
            op_stack.pop()
    regexp = regex_p(regexp)

    for c in regexp:
        if c in list(operations.keys()) + ['(', ')']:
            if data != '':
                eval_stack.append(primitive_fnda(data))
            data = ''
        if c in operations:
            if len(op_stack) == 0 or op_stack[-1] in ['(', ')'] or priorities[op_stack[-1]] < priorities[c]:
                op_stack.append(c)
            else:
                process_operator(priorities[c])
                op_stack.append(c)
        elif c == '(':
            op_stack.append('(')
        elif c == ')':
            process_operator()
        else:
            data += c

    if data != '':
        eval_stack.append(primitive_fnda(data))
    process_operator()
    return eval_stack[-1]


def convert_to_fda(fnda):                 #конвертация недерменированного автомата в детерменированный
    links = []
    # Множество новых состояний, начиная с эпсилон состояния 0
    newStates = [set(fnda.e_closure(0))]
    visitedStates = []
    keys = [x for x in list(fnda.table.keys()) if x != epsilon]
    while len(newStates) > 0:
        tmp = newStates.pop()
        # Если состояние уже посещено, пропускаем его
        if tmp in visitedStates:
            continue
        # Добавляем состояние в список посещенных
        visitedStates.append(tmp)
        # Получаем новое состояние после перехода по символу
        for char in keys:
            newTmp = set(fnda.step(tmp, char))
            if len(newTmp) != 0:
                newStates.append(newTmp)
                links.append((tmp, char, newTmp))
    formatted_links = []
    # Преобразование ссылок в индексы состояний
    for link in links:
        formatted_links.append((visitedStates.index(link[0]), link[1], visitedStates.index(link[2])))
    links = formatted_links
    old_final = set(fnda.result_states)
    # Индексы финальных состояний в полученном DFA
    result = [i for i, s in enumerate(visitedStates) if s.intersection(old_final)]
    new_table = {}
    for k in keys:
        new_table[k] = [None for _ in enumerate(visitedStates)]
    # Заполнение таблицы переходов
    for link in links:
        new_table[link[1]][link[0]] = link[2]
    table=new_table
    result_states=result
    return DeterministicAutomat(table, result_states)


def minimize_fda(fda):                             # минимизация детерминированного конечного автомата
    def split_set(target, splitter, split_char):
        setA = set()
        setB = set()
        for condition in target:
            if fda.table[split_char][condition] in splitter:
                setA.add(condition)
            else:
                setB.add(condition)
        return setA, setB

    # Инициализация списка классов эквивалентности
    sets = [{*fda.result_states}]
    non_final = {*list(range(fda.num_states()))}.difference(fda.result_states)
    if len(non_final) > 0:
        sets.append(non_final)
    queue = []
    # Формирование очереди разбиений классов эквивалентности
    for symbol in fda.keys():
        for classs in sets:
            queue.append((classs, symbol))
    # Построение классов эквивалентности
    while len(queue) > 0:
        splitter, char = queue.pop(0)
        for classs in sets:
            setA, setB = split_set(classs, splitter, char)
            if len(setA) > 0 and len(setB) > 0:
                sets.remove(classs)
                sets.extend([setA, setB])
                if (classs, char) in queue:
                    queue.remove((classs, char))
                    queue.append((setA, char))
                    queue.append((setB, char))
                else:
                    if len(setA) < len(setB):
                        queue.append((setA, char))
                    else:
                        queue.append((setB, char))

    # Перестановка классов эквивалентности так, чтобы первым был класс состояния 0
    first_state_index = [sets.index(classs) for classs in sets if 0 in classs][0]
    first_state = sets.pop(first_state_index)
    sets.insert(0, first_state)

    states = len(sets)
    new_table = {k: [None] * states for k in fda.keys()}
    # Формирование новой таблицы переходов
    for i, classs in enumerate(sets):
        for condition in classs:
            for symbol in fda.keys():
                new_indexes = [sets.index(classs) for classs in sets if fda.table[symbol][condition] in classs]
                new_table[symbol][i] = None if len(new_indexes) == 0 else new_indexes[0]

    # Формирование нового множества финальных состояний
    result = [sets.index(classs) for classs in sets if classs.intersection(fda.result_states)]
    table=new_table
    result_states=result
    return DeterministicAutomat(table, result_states)