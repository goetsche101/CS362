"""
"""

import unittest
from contrived_func import contrived_func


class TestStuff(unittest.TestCase):

    def test(self):
        self.assertTrue(contrived_func(102))

    def test1(self):
        self.assertFalse(contrived_func(6))

    def test2(self):
        self.assertTrue(contrived_func(7))

    def test3(self):
        self.assertTrue(contrived_func(80))

    def test4(self):
        self.assertTrue(contrived_func(75))

    def test5(self):
        self.assertFalse(contrived_func(151))


if __name__ == '__main__':
    unittest.main()
