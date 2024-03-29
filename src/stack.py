class Node:
    """Класс для узла стека."""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node.

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека."""

    def __init__(self):
        """Конструктор класса Stack."""
        self.top = None

    def __str__(self):
        return f'Это экземпляр класса {self.__class__.__name__}.'

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека.

        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения.

        :return: данные удаленного элемента
        """
        if self.top is None:
            return None

        removed_node = self.top
        self.top = self.top.next_node
        return removed_node.data
