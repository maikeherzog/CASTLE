import unittest

from src.Castle import Castle

education_tree_test = {
    'name': 'Any Education',
    'children': [
        {
            'name': 'Secondary',
            'children': [
                {'name': 'Primary School'},
                {'name': 'Secondary School'}
            ]
        },
        {
            'name': 'University',
            'children': [
                {'name': 'Bachelors'},
                {'name': 'Masters'},
                {'name': 'Ph.D'}
            ]
        }
    ]
}

attribute_properties_test = {
    0: {'name': 'age', 'type': 'continuous', 'interval': (18, 120)},
    1: {'name': 'education', 'type': 'cathegorical', 'hierarchy_tree': education_tree_test}
}

class TestEnlargementFunction(unittest.TestCase):

    def test_enlargement(self):
        castle = Castle(None, 6, 5, 2)
        # testcase 1
        cluster1 = ([26, 28], ['Masters', 'Bachelors'])
        tupel1 = (24, 'Bachelors')
        expected_result1 = 0.13480392156862744
        result1 = castle.Enlargement(cluster1, tupel1)
        self.assertAlmostEqual(result1, expected_result1, places=3)

        # testcase 2
        cluster2 = ([18,22], ['Primary School', 'Bachelors'])
        tupel2 = (24, 'Bachelors')
        expected_result2 = 0.38480392156862747
        result2 = castle.Enlargement(cluster2, tupel2)
        self.assertAlmostEqual(result2, expected_result2, places=3)

        # testcase 3
        cluster1 = ([24, 28], ['Masters', 'Bachelors'])
        tupel1 = (24, 'Bachelors')
        expected_result1 = 0.125
        result1 = castle.Enlargement(cluster1, tupel1)
        self.assertAlmostEqual(result1, expected_result1, places=3)


if __name__ == '__main__':
    unittest.main()
