# Stefan Patch

import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        
        list1 = [0,1,2,3,4,5,6,7,8,9,10]    #ordered
        list2 = [0,1,2,3,6,4,5,7,1]         #unordered
        list3 = [0,0,0,0,0,0,0,0,0]         #all the same
        list4 = [0,1,1,2,3,4,5,5,6,7,7]     #many duplicates
        list5 = []                          #empty

        self.assertEqual(max_list_iter(list1), 10)
        self.assertEqual(max_list_iter(list2), 7)
        self.assertEqual(max_list_iter(list3), 0)
        self.assertEqual(max_list_iter(list4), 7)
        self.assertEqual(max_list_iter(list5), None)

    def test_reverse_rec(self):
        #check ValueError
        none_list = None
        with self.assertRaises(ValueError):
            reverse_rec(none_list)

        #check 3 and 4 list length
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1,2,3,4]),[4,3,2,1])
        
        #check reverses
        self.assertEqual(reverse_rec([4,3,2,1]),[1,2,3,4])
        self.assertEqual(reverse_rec([3,2,1]),[1,2,3])

    def test_bin_search(self):
        none_list = None
        with self.assertRaises(ValueError):
            bin_search(3, 0, 13, none_list)
        
        #odd
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)

        #even
        list_val =[0,1,2,3,4,7,8,9]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)

        #odd None
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(11, 0, len(list_val)-1, list_val), None)

        #even None
        list_val =[0,1,2,3,4,7,8,9]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), None)

        #odd max
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 8)
    
        #even max
        list_val =[0,1,2,3,4,7,8,9]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(9, 0, len(list_val)-1, list_val), 7)

        #min
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0)

        #empty
        list_val = []
        low = 0
        high = 0
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), None)

        #1 item
        list_val = [1]
        low = 0
        high = 0
        self.assertEqual(bin_search(1, 0, len(list_val)-1, list_val), 0)
        
        #2 items
        list_val = [1, 2]
        low = 0
        high = 1
        self.assertEqual(bin_search(1, 0, len(list_val)-1, list_val), 0)


if __name__ == "__main__":
        unittest.main()

    
