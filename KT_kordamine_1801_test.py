import unittest


from KT_kordamine_1801 import timeformating
from KT_kordamine_1801 import countvowels
from KT_kordamine_1801 import longshortstring
from KT_kordamine_1801 import makeiteven
from KT_kordamine_1801 import speedticket
from KT_kordamine_1801 import findarea
from KT_kordamine_1801 import salesnight


class TestTimeformating(unittest.TestCase):

    def test_timeformating_negative(self):
        self.assertEqual("", timeformating(-23))

    def test_timeformating_zero(self):
        self.assertEqual("", timeformating(0))

    def test_timeformating_example1(self):
        self.assertEqual("2tundi 43minutit", timeformating(163))

    def test_timeformating_example2(self):
        self.assertEqual("3tundi", timeformating(180))

    def test_timeformating_example3(self):
        self.assertEqual("45minutit", timeformating(45))


class TestCountvowels(unittest.TestCase):

    def test_countvowels_empty(self):
        self.assertEqual(0, countvowels(""))

    def test_countvowels_estvowels(self):
        self.assertEqual(2, countvowels("ÕUN"))

    def test_countvowels_example1(self):
        self.assertEqual(16, countvowels("supercalifragilisticexpialidocious"))

    def test_countvowels_example2(self):
        self.assertEqual(0, countvowels("drpgnnn"))


class TestLongshortstring(unittest.TestCase):

    def test_longshortstring_example1(self):
        self.assertEqual("HIhelloHI", longshortstring("hi", "hello"))

    def test_longshortstring_example2(self):
        self.assertEqual("HIhelloHI", longshortstring("HEllo", "hI"))

    def test_longshortstring_example3(self):
        self.assertEqual("BaaaB", longshortstring("aaa", "b"))

    def test_longshortstring_example4(self):
        self.assertEqual("BEEBdibeepBEEB", longshortstring("beeb", "dibEEp"))


class TestMakeiteven(unittest.TestCase):

    def test_makeiteven_empty(self):
        self.assertEqual([], makeiteven([]))

    def test_makeiteven_nopair(self):
        self.assertEqual([], makeiteven([1, 1, 3, 9, 11, 21]))

    def test_makeiteven_example1(self):
        self.assertEqual([2, 8, 12, 6], makeiteven([1, 1, 2, 5, 8, 9, 12, 6]))

    def test_makeiteven_example2(self):
        self.assertEqual([2, 8, 10, 100, 50, 56, 12, 6],
                         makeiteven([2, 5, 8, 10, 100, 17, 27, 50, 56, 9, 12, 6]))


class TestSpeedticket(unittest.TestCase):

    def test_speedticket_example1(self):
        self.assertEqual(1, speedticket(65, False))

    def test_speedticket_example2(self):
        self.assertEqual(0, speedticket(65, True))

    def test_speedticket_example3(self):
        self.assertEqual(1, speedticket(84, True))

    def test_speedticket_example4(self):
        self.assertEqual(2, speedticket(84, False))


class TestFindarea(unittest.TestCase):

    def test_findare_square(self):
        self.assertEqual(16.0, findarea(0, 4, 4))

    def test_findare_square2(self):
        self.assertEqual(36.0, findarea(0, 6, 6))

    def test_findare_parallelogram(self):
        self.assertEqual(50.0, findarea(1, 10, 5))

    def test_findare_triangle(self):
        self.assertEqual(25.0, findarea(2, 10, 5))

    def test_findare_triangle2(self):
        self.assertEqual(13.5, findarea(2, 9, 3))

    def test_findare_cicrcle(self):
        self.assertEqual(50.27, findarea(3, 4, 0))

class TestSalesnight(unittest.TestCase):

    def test_salesnight_example1(self):
        self.assertEqual("40.0 €", salesnight(50,20,False))

    def test_salesnight_example2(self):
        self.assertEqual("40.0 €", salesnight(50,10,True))

    def test_speedticket_example3(self):
        self.assertEqual("20.0 €", salesnight(50,80,True))


if __name__ == '__main__':
    unittest.main()
