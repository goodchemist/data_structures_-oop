import ast


class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node

    def __str__(self):
        """
        Вывод данных в строковом представлении.
        :return:
        """
        return f'{self.data}'

    def __getitem__(self, item):
        """
        Получение значения по ключу item.
        """
        return self.data[item]


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.all = []

    def insert_beginning(self, data_: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data_)

        new_node.next_node = self.head
        self.head = new_node

        self.all.append(new_node)

    def insert_at_end(self, data_: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data_)

        previous = self.all[-1]

        previous.next_node = new_node
        self.all.append(new_node)

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self):
        """
        Возвращает список с данными, содержащимися в односвязном списке `LinkedList`.
        :return: список с данными
        """
        sorted_list = sorted(self.all, key=lambda x: x['id'])

        return sorted_list

    def get_data_by_id(self, key_):
        """
        Возвращает первый найденный в `LinkedList` словарь с ключом 'id',
        значение которого равно переданному в метод значению.
        :return: словарь с ключом 'key_'
        """
        for item in self.all:

            try:

                if item['id'] == key_:
                    result_str = str(item)
                    result_dict = ast.literal_eval(result_str)
                    return result_dict

            except TypeError:
                print('Данные не являются словарем или в словаре нет id.')
