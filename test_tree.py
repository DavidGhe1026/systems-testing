import unittest

from tree import Tree


class TestTreeFind(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        for value in [3, 4, 0, 8, 2]:
            self.tree.add(value)

    def test__find_returns_matching_node_when_value_exists(self):
        node = self.tree._find(2, self.tree.getRoot())

        self.assertIsNotNone(node)
        self.assertEqual(2, node.data)

    def test__find_returns_none_when_value_is_missing(self):
        node = self.tree._find(7, self.tree.getRoot())

        self.assertIsNone(node)


if __name__ == "__main__":
    unittest.main()