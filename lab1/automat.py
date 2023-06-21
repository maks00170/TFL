from typing import Dict, List, Set
import copy

epsilon = 'epsilon'

class NonDeterministicAutomat():        # недетерминированный автомат.
    def __init__(self, table, result_states):
        self.table = table
        self.result_states = result_states
        self.states = None

    #Получение следующего состояния автомата при переходе из заданного состояния по символу
    def nextState(self, state, char):
      if char not in self.table:
        raise ValueError("Символ не может быть принят")
      return self.table[char][state] if char in self.table else None

    #Установка перехода из одного состояния в другое по заданному символу
    def set_trans(self, start, char, finish):
        if char not in self.table:
            self.table[char] = [[] for _ in range(self.num_states())]
        self.table[char][start].append(finish)

    #Выполнение перехода из набора состояний по заданному символу
    def step(self, old_state, char):
      let_step = set()
      for state in old_state:
        let_step.update(self.nextState(state, char))
        if epsilon in self.table.keys():
            let_step.update(sum([self.e_closure(s) for s in let_step], []))
      return list(let_step) if let_step else []


    def copy(self):
      new_table = copy.deepcopy(self.table)
      result = copy.deepcopy(self.result_states)
      copied_instance = NonDeterministicAutomat(new_table, result)
      return copied_instance

    #Вычисление эпсилон-замыкания
    def e_closure(self, state):
        if epsilon not in self.table.keys():
            return [state]
        visited = []
        active = [state]
        while len(active) != 0:
            new_active = []
            for s in active:
                new_active.extend(self.table[epsilon][s])
            visited = list(set(visited + active))
            active = list(set(new_active).difference(visited))
        return visited


    def accept(self, input_string):
        self.states = self.e_closure(0)
        try:
            for c in input_string:
                self.states = self.step(self.states, c)
            for state in self.states:
                if set(self.e_closure(state)).intersection(self.result_states):
                    return True
            return False
        except ValueError:
            return False


    def num_states(self):
        return len(list(self.table.values())[0])


    def keys(self):
        return list(self.table.keys())
    


class DeterministicAutomat():   # детерминированный автомат.
    def __init__(self, table, result_states):
        self.table = table
        self.result_states = result_states
        proxy_table = {}
        for char, states in table.items():
            proxy_table[char] = [[state] if state is not None else [] for state in states]
        self.proxy = NonDeterministicAutomat(proxy_table, result_states)


    def accept(self, input_string):
        return self.proxy.accept(input_string)


    def num_states(self):
        return self.proxy.num_states()


    def keys(self):
        return self.proxy.keys()