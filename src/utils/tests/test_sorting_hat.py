import unittest

from utils.sorters.sorting_hat import SortingError, SortingHat


class SortingHatTest(unittest.TestCase):
    def test_raises_errors(self):
        test_sorter_raises = SortingHat()
        self.assertRaises(
            SortingError, test_sorter_raises.insertion_sort, [1,"w",3], 3,
        )
        self.assertRaises(
            SortingError, test_sorter_raises.insertion_sort, [1,{},3], 3
        )
        self.assertRaises(
            SortingError, test_sorter_raises.insertion_sort, [1,[],3], 3
        )
        self.assertRaises(
            SortingError, test_sorter_raises.insertion_sort, [1,None,3], 3
        )
        self.assertRaises(
            SortingError, test_sorter_raises.insertion_sort, [1,(1, 3),3], 3
        )
        self.assertRaises(
            SortingError, test_sorter_raises.insertion_sort, [1,[1,1],3], 3
        )
