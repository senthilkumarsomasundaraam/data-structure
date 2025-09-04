import unittest
from friends import Friends
# Trying with possible test cases with help of unitest module.
# Autor: Senthil Kumar Somasundaram
# Date: 2024-06-10
# Purpose: Test the Friends iterator class to return pairs of friends       
#-----------------------------------------------------------------------
class TestFriendsIterator(unittest.TestCase):

    def test_basic_case(self):
        friends_dir = {
            "x": {"y", "z"},
            "y": {"x", "z"},
            "z": {"x", "y"}
        }
        result = list(Friends(friends_dir))
        expected = [("x", "z"), ("x", "y"), ("y", "z")]
        self.assertEqual(result, expected)


    def test_empty_directory(self):
        friends_dir = {}
        result = list(Friends(friends_dir))
        self.assertEqual(result, [])

    def test_single_person(self):
        friends_dir = {"x": set()}
        result = list(Friends(friends_dir))
        self.assertEqual(result, [])

    def test_no_duplicate_pairs(self):
        friends_dir = {
            "x": {"y"},
            "y": {"x"}
        }
        result = list(Friends(friends_dir))
        expected = [("x", "y")]
        self.assertEqual(result, expected)

    def test_ordering(self):
        friends_dir = {
            "z": {"x", "y"},
            "y": {"x"},
            "x": {"z"}
        }
        result = list(Friends(friends_dir))
        expected = [("x", "z")]
        self.assertEqual(result, expected)

## For this testing needed possible expected values  3 x 2 = 6 
   ## def test_large_network(self):
    #     friends_dir = {
    #        "x": {"y", "z"},
    #        "y": {"x", "z"},
    #        "z": {"x", "y"}
    #    }
    #    result = list(Friends(friends_dir))
    #    expected1 = [("x", "y"), ("x", "z"), ("y", "z")]
    #    expected2 = [("x", "z"), ("x", "z"), ("y", "z")]
    #    self.assertEqual(result, expected1) or self.assertEqual(result, expected2)
   #

if __name__ == '__main__':
    unittest.main()