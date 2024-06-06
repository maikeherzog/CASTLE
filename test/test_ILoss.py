import unittest

from src.Castle import Castle
from src.Cluster import Cluster
from src.Tupel import Tuple

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

    def test_enlargement1(self):
        castle = Castle(None, 6, 5, 2)
        # testcase 1
        """#cluster1 = ([26, 28], ['Masters', 'Bachelors'])
        cluster1 = Cluster(Tuple(0,0,(26, 'Masters'),()))
        cluster1.add_tupel(Tuple(1,1,(28, 'Bachelors'),()))
        #tupel1 = (24, 'Bachelors')
        tuple1 = Tuple(2,2,(24, 'Bachelors'), ())
        expected_result1 = 0.13480392156862744
        result1 = castle.Enlargement(cluster1, tuple1)
        self.assertAlmostEqual(result1, expected_result1, places=3)"""

    def test_enlargement2(self):
        castle = Castle(None, 6, 5, 2)
        # testcase 2
        #cluster2 = ([18,22], ['Primary School', 'Bachelors'])
        cluster2 = Cluster(Tuple(0,0,([18,22], ['Primary School', 'Bachelors']),()))
        #tupel2 = (24, 'Bachelors')
        tupel2 = Tuple(0,0,(24, 'Bachelors'), ())
        expected_result2 = 0.38480392156862747
        result2 = castle.Enlargement(cluster2, tupel2)
        self.assertAlmostEqual(result2, expected_result2, places=3)

    def test_enlargement3(self):
        castle = Castle(None, 6, 5, 2)
        # testcase 3
        #cluster1 = ([24, 28], ['Masters', 'Bachelors'])
        cluster3 = Cluster(Tuple(0,0,([26, 28], ['Masters', 'Bachelors']),()))
        #tupel1 = (24, 'Bachelors')
        tupel3 = Tuple(0,0,(24, 'Bachelors'), ())
        expected_result3 = 0.135
        result3 = castle.Enlargement(cluster3, tupel3)
        self.assertAlmostEqual(result3, expected_result3, places=3)

    def test_enlargement4(self):
        castle = Castle(None, 6, 5, 2)
        # testcase 4
        cluster4 = Cluster(Tuple(0,0,(52, 'Secondary School'),()))
        tupel4 = Tuple(0,0,(51, 'Bachelors'), ())
        expected_result4 = 0.50490196
        result4 = castle.Enlargement(cluster4, tupel4)
        self.assertAlmostEqual(result4, expected_result4, places=3)


    def test_enlargement5(self):
        castle = Castle(None, 6, 5, 2)
        # testcase 5
        cluster5 = Cluster(Tuple(0,0,(52, 'Secondary School'),()))
        tupel5 = Tuple(0,0,(52, 'Secondary School'), ())
        expected_result5 = 0
        result5 = castle.Enlargement(cluster5, tupel5)
        self.assertAlmostEqual(result5, expected_result5, places=3)

    def test_enlargement6(self):
        castle = Castle(None, 6, 5, 2)
        # testcase 6
        cluster6 = Cluster(Tuple(0,0,(52, 'Secondary School'),()))
        tupel6 = Tuple(0,0,(53, 'Masters'), ())
        expected_result6 = 0.50490196
        result6 = castle.Enlargement(cluster6, tupel6)
        self.assertAlmostEqual(result6, expected_result6, places=3)

if __name__ == '__main__':
    unittest.main()
