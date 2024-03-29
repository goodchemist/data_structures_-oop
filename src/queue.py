class Node:
    """Класс для узла очереди."""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node.

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди."""

    def __init__(self):
        """Конструктор класса Queue."""

        self.head = None
        self.tail = None
        self.all = []

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь.

        :param data: данные, которые будут добавлены в очередь
        """
        new_item = Node(data)

        if self.head is None:
            self.head = new_item
            self.tail = new_item
            self.all.append(data)
        else:
            self.tail.next_node = new_item
            self.tail = new_item
            self.all.append(data)

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента.

        :return: данные удаленного элемента
        """
        if not self.all:
            return None

        else:
            removed_data = self.all.pop(0)

            if len(self.all) > 0:
                self.head.data = self.head.next_node.data
                self.head.next_node.data = self.tail.data
                self.tail.data = None

            else:
                self.head.data = None

            return removed_data

    def __str__(self):
        """Магический метод для строкового представления объекта."""

        return '\n'.join(self.all)
