import unittest

from coltab import Table


class Tests(unittest.TestCase):
    def print_table(self, t, on=None):
        print('----------')
        print(t.asstring(on=on))
        print('----------')

    def test_tests(self):
        self.assertEqual(1, 1)

    def test_1(self):
        t = Table()
        self.assertEqual(t.asstring(), '')

    def test_2(self):
        t = Table()
        t.add(0, 0, 'hello')
        self.assertEqual(t.asstring(), 'hello')

    def test_3(self):
        t = Table()
        t.add(0, 0, 'x')
        t.add(1, 1, 'hello')
        self.print_table(t, on='red')
        # self.assertEqual(str(t), 'hello')
