import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_str(self):
        """
        Проверяет работу метода __str__.
        """
        self.assertEqual(str(self.queue), "")

    def test_enqueue(self):
        """
        Проверка функции enqueue() из класса Queue.
        """
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')
        self.assertEqual(self.queue.head.data, 'data1')
        self.assertEqual(self.queue.head.next_node.data, 'data2')
        self.assertEqual(self.queue.tail.data, 'data3')
        self.assertEqual(self.queue.tail.next_node, None)

    def test_dequeue(self):
        """
        Проверка функции dequeue() из класса Queue.
        """
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')
        self.assertEqual(self.queue.dequeue(), 'data1')
        self.assertEqual(self.queue.dequeue(), 'data2')
        self.assertEqual(self.queue.dequeue(), 'data3')
        self.assertEqual(self.queue.dequeue(), None)
