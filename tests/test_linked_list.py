import unittest
from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_str(self):
        """
        Проверяет работу метода __str__.
        """
        self.assertEqual(str(self.ll), "None")
        self.ll.insert_beginning({'id': 1})
        self.assertEqual(str(self.ll), "{'id': 1} -> None")

    def test_insert_beginning_end(self):
        """
        Проверяет работу методов insert_beginning и insert_at_end.
        """
        self.ll.insert_beginning({'id': 1})
        self.ll.insert_at_end({'id': 2})
        self.ll.insert_at_end({'id': 3})
        self.ll.insert_beginning({'id': 0})
        self.assertEqual(self.ll.head.data, {'id': 0})
        self.assertEqual(self.ll.head.next_node.data, {'id': 1})
        self.assertEqual(self.ll.tail, None)
