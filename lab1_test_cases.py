import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        
        list1 = [0,1,2,3,4,5,6,7,8,9,10]
        list2 = [0,1,2,3,6,4,5,7,1]
        list3 = [0,0,0,0,0,0,0,0,0]
        list4 = [0,1,1,2,3,4,5,5,6,7,7]
        list5 = []

        self.assertEqual(max_list_iter(list1), 10)
        self.assertEqual(max_list_iter(list2), 7)
        self.assertEqual(max_list_iter(list3), 0)
        self.assertEqual(max_list_iter(list4), 7)
        self.assertEqual(max_list_iter(list5), None)

    def test_reverse_rec(self):
        none_list = None
        with self.assertRaises(ValueError):
            reverse_rec(none_list)

        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1,2,3,4]),[4,3,2,1])
        self.assertEqual(reverse_rec([4,3,2,1]),[1,2,3,4])
        self.assertEqual(reverse_rec([3,2,1]),[1,2,3])
        self.assertEqual(reverse_rec([]),[])

    def test_bin_search(self):
        none_list = None
        with self.assertRaises(ValueError):
            bin_search(3, 0, 13, none_list)
    
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)

        list_val =[0,1,2,3,4,7,8,9]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)

        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(11, 0, len(list_val)-1, list_val), None)

        list_val =[0,1,2,3,4,7,8,9]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), None)


if __name__ == "__main__":
        unittest.main()

    
