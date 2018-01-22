import unittest
import hashlib

from coltab import Table, Cell, Line, HALF, Fr, RIGHT, CENTER, LEFT


def sha1(s):
    m = hashlib.sha1()
    m.update(s.encode())
    return m.hexdigest()


class Tests(unittest.TestCase):
    def print_table(self, t, bg=None, fg=None, styles=None):
        s = t.asstring(bg=bg, fg=fg, styles=styles)
        print('----------')
        print(s)
        print('----------')
        print(sha1(s))
        print('----------')

    def test_tests(self):
        self.assertEqual(1, 1)

    def test_1(self):
        t = Table()
        self.assertEqual(t.asstring(), '')

    def test_2(self):
        t = Table()
        t.add(0, 0, 'hello')

        self.print_table(t)
        self.assertEqual(
            sha1(t.asstring()),
            'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d'
        )

    def test_3(self):
        t = Table()
        t.add(0, 0, 'x')
        t.add(1, 1, 'hello')

        self.print_table(t)
        self.assertEqual(
            sha1(t.asstring()),
            '07495f79f42dcdfc56c686c263a84e65786fe041'
        )

    def test_4(self):
        t = Table(styles='bold')
        t.add(0, 0, Cell('abc'))
        t.add(0, 2, Cell('x'))
        t.add(1, 1, Cell('hello'))
        t.add(1, 2, Cell('***'))
        t.add(2, 1, Cell('xxxxxxxx'))

        self.print_table(t)
        self.assertEqual(
            sha1(t.asstring()),
            '0121fa60d456dc3dbba4231a656d500aa61a89fe'
        )

    def test_5(self):
        t = Table(styles='bold', bg='yellow', rowsepstyle=HALF)
        t.add(0, 0, Cell('abc'))
        t.add(0, 2, Cell('x'))
        t.add(1, 1, Cell('hello', bg='blue'))
        t.add(1, 2, Cell('***', padding=(0, 1)))
        t.add(2, 1, Cell('xxxxxxxx'))

        self.print_table(t, bg='white')
        self.assertEqual(
            sha1(t.asstring(bg='white')),
            'cff1e0a83abbb941b8169f31d54a3db79899cf16'
        )

    def test_6(self):
        t1 = Table(styles='bold', bg='yellow', rowsepstyle=HALF)
        t1.add(0, 0, Cell('abc'))
        t1.add(0, 2, Cell('x'))
        t1.add(1, 1, Cell('hello', bg='blue'))
        t1.add(1, 2, Cell('***', padding=(0, 1)))
        t1.add(2, 1, Cell('xxxxxxxx'))

        t = Table(rowsepstyle=HALF)
        t.add(0, 0, Cell('hello', bg='green'))
        c = Cell('tab:', bg='cyan')
        c.add(t1)
        t.add(1, 1, c)
        t.add(0, 2, '012345')
        t.add(1, 2, Cell('0123456789', padding=(0, 2, 0, 0)))

        self.print_table(t, bg='magenta')
        self.assertEqual(
            sha1(t.asstring(bg='magenta')),
            'b87344ab9d346d56e2b3fec43604de1883b81719'
        )

    def test_7(self):
        t1 = Table(styles='bold', bg='yellow', rowsepstyle=HALF)
        t1.add(0, 0, Cell('abc'))
        t1.add(0, 2, Cell('x'))
        t1.add(1, 1, Cell('hello', bg='blue'))
        t1.add(1, 2, Cell('***', padding=(0, 1)))
        t1.add(2, 1, Cell('xxxxxxxx'))

        t = Table(rowsepstyle=HALF)
        t.add(0, 0, Cell('hello', bg='green'))
        c = Cell('tab:', bg='cyan')
        c.add(Cell('(this is a simple line)', padding=(0, 1, 0, 0)))
        c.add(t1)
        t.add(1, 1, c)
        t.add(0, 2, Cell('0123456789', padding=1))
        t.add(1, 2, Cell('012345', padding=(0, 2, 0, 0)))
        t.add(0, 4, 'far')

        l = Line('0')
        t1.add(1, 3, l)
        l.add(Fr('0', fg='black'))

        self.print_table(t, bg='magenta')
        self.assertEqual(
            sha1(t.asstring(bg='magenta')),
            '9ae4f999b1bdf49ed45f92860b90c3b2fdadbfea'
        )

    def test_8(self):
        t1 = Table(styles='bold', bg='yellow', rowsepstyle=HALF)
        t1.add(0, 0, Cell('abc'))
        t1.add(0, 2, Cell('x'))
        t1.add(1, 1, Cell('hello', bg='blue'))
        t1.add(1, 2, Cell('***', padding=(0, 1)))
        t1.add(2, 1, Cell('xxxxxxxx'))

        t = Table(rowsepstyle=HALF)
        t.add(0, 0, Cell('hello', bg='green'))
        c = Cell('tab:', bg='cyan')
        c.add(Cell('(this is a simple line)', padding=(0, 1, 0, 0)))
        c.add(t1)
        t.add(1, 1, c)
        t.add(0, 2, Cell('0123456789', padding=1))
        t.add(1, 2, Cell('012345', padding=(0, 2, 0, 0)))
        t.add(0, 4, 'far')

        l = Line('0')
        t1.add(1, 3, l)
        l.add(Fr('0', fg='black'))

        self.print_table(t)
        self.assertEqual(
            sha1(t.asstring()),
            'd4d3c980e0c96761b311ffb8c96c6ce0d1092e6e'
        )

    def test_9(self):
        t1 = Table(styles='bold', bg='yellow', rowsepstyle=HALF)
        t1.add(0, 0, Cell('abc'))
        t1.add(0, 2, Cell('x'))
        t1.add(1, 1, Cell('hello', bg='blue'))
        t1.add(1, 2, Cell('***', padding=(0, 1)))
        t1.add(2, 1, Cell('xxxxxxxx'))

        t = Table()
        t.add(0, 0, Cell('hello', bg='green'))
        c = Cell('tab:', bg='cyan')
        c.add(Cell('(this is a simple line)', padding=(0, 1, 0, 0)))
        c.add(t1)
        t.add(1, 1, c)
        t.add(0, 2, Cell('0123456789', padding=1))
        t.add(1, 2, Cell('012345', padding=(0, 2, 0, 0)))
        t.add(0, 4, 'far')

        l = Line('0')
        t1.add(1, 3, l)
        l.add(Fr('0', fg='black'))
        l.add(Fr('1111111111', styles='normal'))

        self.print_table(t, bg='magenta')
        self.assertEqual(
            sha1(t.asstring(bg='magenta')),
            '1b746534d00d56a6eb1907232c3c1ad129354628'
        )

    def test_a(self):
        t1 = Table(styles='bold', bg='yellow', rowsepstyle=HALF)
        t1.add(0, 0, Cell('abc'))
        t1.add(0, 2, Cell('x'))
        t1.add(1, 1, Cell('hello', bg='blue'))
        t1.add(1, 2, Cell('***', padding=(0, 1)))
        t1.add(2, 1, Cell('xxxxxxxx'))

        t = Table()
        t.add(0, 0, Cell('hello', bg='green'))
        c = Cell('vvv', bg='cyan', align=CENTER)
        c.add('this is a line to strech the cell')
        c.add(t1)
        c.add(Cell('what', align=RIGHT))
        t.add(1, 1, c)
        t.add(0, 2, Cell('0123456789', padding=1))
        t.add(1, 2, Cell('012345', padding=(0, 2, 0, 0)))
        t.add(0, 4, 'far')

        self.print_table(t, bg='magenta')
        self.assertEqual(
            sha1(t.asstring(bg='magenta')),
            '8b720f4b8b96a0c875b0ae1cdca333a12f3bfaf4'
        )

    def test_b(self):
        t = Table()
        c = Cell(
            Line('*************************'),
            Line('************************'),
            Line('***************************'),
            bg='green'
        )

        sub1 = Cell(
            Line('11'),
            Line('111'),
            align=RIGHT,
            bg='yellow'
        )
        c.add(sub1)

        sub2 = Cell(
            Line('222222'),
            Line('22222'),
            bg='red',
            align=CENTER
        )

        t.add(0, 0, c)
        sub1.add(sub2)
        sub1.add('1111111111111')

        self.print_table(t)
        self.assertEqual(
            sha1(t.asstring()),
            '838e8b571e13bdc20e22acb79107a41d5fd1b0fd'
        )
