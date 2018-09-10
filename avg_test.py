#coding=utf-8
import unittest
from avgcount import  avg1

class Test(unittest.TestCase):


    def test_Avg(self):
        self.assertEqual(20, avg1(10,20,30))
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()