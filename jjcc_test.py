#coding=utf-8
import unittest
from jjcccount import heheda

class Test(unittest.TestCase):

    def test_jia(self):
        self.assertEqual(3, heheda('1+2').jia())
        pass

    def test_jian(self):
        self.assertEqual(-1, heheda('2-3').jian())
        pass

    def test_chen(self):
        self.assertEqual(6, heheda('2*3').cheng())
        pass
    def test_chu(self):
        self.assertEqual(1, heheda('3/3').chu())
        pass
    def test_jisuan(self):
        self.assertEqual(-6, heheda('3/3/1+3*3*3-2-1*2*2*2').jisuan())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()