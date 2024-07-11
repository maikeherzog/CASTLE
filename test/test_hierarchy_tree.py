import unittest

from src.Castle import Castle
from src.hierarchy_tree import education_tree_easy
from src.tree_functions import *


class TestCastle(unittest.TestCase):
    def test_generalization(self):
        erg1 = find_generalization(education_tree_easy, ['Bachelors'])
        erg2 = find_generalization(education_tree_easy, ['Bachelors', 'Masters'])
        erg3 = find_generalization(education_tree_easy, ['Bachelors', 'Masters', 'Primary School'])

        self.assertEqual(erg1, 'Bachelors')
        self.assertEqual(erg2, 'University')
        self.assertEqual(erg3, 'Any Education')

    def test_get_leaf_nodes(self):
        erg1 = get_leaf_nodes(education_tree_easy)
        erg2 = get_leaf_nodes(get_subtree(education_tree_easy, 'University'))
        erg3 = get_leaf_nodes(get_subtree(education_tree_easy, 'Any Education'))
        erg4 = get_leaf_nodes(get_subtree(education_tree_easy, 'Bachelors'))

        self.assertEqual(erg1, ['Primary School', 'Secondary School', 'Bachelors', 'Masters', 'Ph.D'])
        self.assertEqual(erg2, ['Bachelors', 'Masters', 'Ph.D'])
        self.assertEqual(erg3, ['Primary School', 'Secondary School', 'Bachelors', 'Masters', 'Ph.D'])
        self.assertEqual(erg4, ['Bachelors'])

    def test_is_leaf_node(self):
        erg1 = is_leaf_node(education_tree_easy, 'Bachelors')
        erg2 = is_leaf_node(education_tree_easy, 'University')

        self.assertTrue(erg1)
        self.assertFalse(erg2)

    def test_get_subtree(self):
        erg1 = get_subtree(education_tree_easy, 'Bachelors')
        erg2 = get_subtree(education_tree_easy, 'University')
        erg3 = get_subtree(education_tree_easy, 'Any Education')

        self.assertEqual(erg1, {'name': 'Bachelors'})
        self.assertEqual(erg2, {'name': 'University', 'children': [{'name': 'Bachelors'}, {'name': 'Masters'}, {'name': 'Ph.D'}]})
        self.assertEqual(erg3, education_tree_easy)

    def test_count_all_leaves(self):
        erg1 = count_all_leaves(education_tree_easy)
        erg2 = count_all_leaves(get_subtree(education_tree_easy, 'University'))
        erg3 = count_all_leaves(get_subtree(education_tree_easy, 'Any Education'))
        erg4 = count_all_leaves(get_subtree(education_tree_easy, 'Bachelors'))

        self.assertEqual(erg1, 5)
        self.assertEqual(erg2, 3)
        self.assertEqual(erg3, 5)
        self.assertEqual(erg4, 1)


if __name__ == '__main__':
    unittest.main()