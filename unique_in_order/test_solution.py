import unittest
from unique_in_order_one_line import unique_in_order

class TestUniqueInOrder(unittest.TestCase):
    def test_empty_sequence(self):
        self.assertEqual(unique_in_order(""), [])
        self.assertEqual(unique_in_order([]), [])
        self.assertEqual(unique_in_order(()), [])

    def test_single_element_sequence(self):
        self.assertEqual(unique_in_order("A"), ["A"])
        self.assertEqual(unique_in_order(["A"]), ["A"])
        self.assertEqual(unique_in_order(("A",)), ["A"])

    def test_reduce_duplicates(self):
        self.assertEqual(unique_in_order("AA"), ["A"])
        self.assertEqual(unique_in_order("AAAABBBCCDAABBB"), ["A", "B", "C", "D", "A", "B"])

    def test_case_sensitive(self):
        self.assertEqual(unique_in_order("ABBCcA"), ["A", "B", "C", "c", "A"])

    def test_different_element_types(self):
        self.assertEqual(unique_in_order([1, 2, 3, 3, -1]), [1, 2, 3, -1])
        self.assertEqual(unique_in_order(["a", "b", "b", "a"]), ["a", "b", "a"])

if __name__ == "__main__":
    unittest.main()
