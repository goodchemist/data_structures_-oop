import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):
    stack = Stack()

    def test_push(self):
        """
        Проверка функции push() из класса Stack
        """
        self.stack.push('test1')
        self.stack.push('test2')
        self.stack.push('test3')
        self.assertEqual(self.stack.top.data, 'test3')
        self.assertEqual(self.stack.top.next_node.data, 'test2')
        self.assertEqual(self.stack.top.next_node.next_node.data, 'test1')
        self.assertEqual(self.stack.top.next_node.next_node.next_node, None)

    def test_pop(self):
        """
        Проверка функции pop() из класса Stack
        """
        self.stack.push('test1')
        self.assertEqual(self.stack.pop(), 'test1')
        self.assertEqual(self.stack.pop(), None)
