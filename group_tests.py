import unittest
import group
from tokenize import group

from group import groups_of_3


class MyTestCase(unittest.TestCase):
    def test_groups_of3(self):
        values = [1,2,3,5,1,8,10,22,46]
        results = groups_of_3(values)
        expected = [[1,2,3],[5,1,8],[10,22,46]]
        self.assertEqual(results, expected)  # add assertion here
    def test_groups_of_3_2(self):
        values = [67,3,52,1,70,87,60,13]
        results = groups_of_3(values)
        expected = [[67,3,52],[1,70,87],[60,13]]

if __name__ == '__main__':
    unittest.main()
