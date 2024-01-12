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

    def test_to_list(self):
        """
        Проверяет работу методa to_list.
        """
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.ll.insert_beginning({'id': 0, 'username': 'serebro'})

        result = self.ll.to_list()

        self.assertEqual(str(result[0]), "{'id': 0, 'username': 'serebro'}")
        self.assertEqual(str(result[1]), "{'id': 1, 'username': 'lazzy508509'}")
        self.assertEqual(str(result[2]), "{'id': 2, 'username': 'mik.roz'}")
        self.assertEqual(str(result[3]), "{'id': 3, 'username': 'mosh_s'}")

    def test_get_data_by_id(self):
        """
        Проверяет работу методa get_data_by_id.
        """
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end({'id': 3, 'username': 'mosh_s'})

        self.assertEqual(self.ll.get_data_by_id(3), {'id': 3, 'username': 'mosh_s'})

    def test_typeerror_get_data_by_id(self):
        """
        Проверяет работу исключений в методе get_data_by_id.
        """
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end([1, 2, 3])
        self.assertRaises(TypeError, self.ll.get_data_by_id(2))
