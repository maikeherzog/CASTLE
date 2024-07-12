import math
import unittest

from src.Castle import Castle
from src.Cluster import Cluster
from src.Tupel import Tuple
from src.hierarchy_tree import education_tree_easy

class TestCastle(unittest.TestCase):
    def test_calculate_tuple_distance(self):
        castle = Castle(None, 6, 5, 2, "easy_data")
        tuple1 = Tuple(0, 0, (26, 'Masters'), ())
        tuple2 = Tuple(1, 1, (28, 'Bachelors'), ())
        erg = castle.calculate_tuple_distance(tuple1, tuple2)

        self.assertEqual(erg, -math.sqrt(5))

    def test_is_in_interval(self):
        castle = Castle(None, 6, 5, 2, "easy_data")
        self.assertTrue(castle.is_in_interval(26, [18, 28]))
        self.assertTrue(castle.is_in_interval(18, [18, 28]))
        self.assertTrue(castle.is_in_interval(28, [18, 28]))
        self.assertFalse(castle.is_in_interval(29, [18, 28]))
        self.assertFalse(castle.is_in_interval(17, [18, 28]))

    def test_add_unique_string_to_list(self):
        castle = Castle(None, 6, 5, 2, "easy_data")
        self.assertEqual(castle.add_unique_string_to_list('Masters', ['Bachelors']), ['Bachelors', 'Masters'])
        self.assertEqual(castle.add_unique_string_to_list('Masters', ['Masters']), ['Masters'])
        self.assertEqual(castle.add_unique_string_to_list('Masters', []), ['Masters'])

    def test_adjust_interval(self):
        castle = Castle(None, 6, 5, 2, "easy_data")
        self.assertEqual(castle.adjust_interval(26, [18, 28]), [18, 28])
        self.assertEqual(castle.adjust_interval(18, [18, 28]), [18, 28])
        self.assertEqual(castle.adjust_interval(28, [18, 28]), [18, 28])
        self.assertEqual(castle.adjust_interval(29, [18, 28]), [18, 29])
        self.assertEqual(castle.adjust_interval(17, [18, 28]), [17, 28])
        self.assertEqual(castle.adjust_interval([17,18], [18, 28]), [17, 28])
        self.assertEqual(castle.adjust_interval([17, 30], [18, 28]), [17, 30])
        self.assertEqual(castle.adjust_interval([27, 30], [18, 28]), [18, 30])
        self.assertEqual(castle.adjust_interval([17, 27], 18), [17, 27])
        self.assertEqual(castle.adjust_interval([17, 30], 18), [17, 30])
        self.assertEqual(castle.adjust_interval([27, 30], 18), [18, 30])

    def test_add_tuple(self):
        castle = Castle(None, 6, 5, 2, "easy_data")
        tuple1 = Tuple(0, 0, (26, 'Masters'), ())
        cluster = Cluster(tuple1, "easy_data")
        tuple2 = Tuple(1, 1, (28, 'Bachelors'), ())
        cluster.add_tupel(tuple2)
        self.assertEqual(cluster.data, [tuple1, tuple2])
        self.assertEqual(cluster.t, ([26, 28], ['Masters', 'Bachelors']))

class TestILossFunction(unittest.TestCase):
    def test_VInfoLoss_continuos(self):
        castle = Castle(None, 6, 5, 2, "easy_data")
        iLoss1 = castle.VInfoLoss_continuos(26, [18,120])
        iLoss2 = castle.VInfoLoss_continuos([26,28], [18,120])
        iLoss3 = castle.VInfoLoss_continuos([26], [18,28])
        iLoss4 = castle.VInfoLoss_continuos([18,24], [18,120])


        self.assertEqual(iLoss1, 0.0)
        self.assertEqual(iLoss2, 2/102)
        self.assertEqual(iLoss3, 0.0)
        self.assertEqual(iLoss4, 6/102)

    def test_VInfoLoss_cathegorical(self):
        castle = Castle(None, 6, 5, 2, "easy_data")
        iLoss1 = castle.VInfoLoss_cathegorical(['Masters'], education_tree_easy)
        iLoss2 = castle.VInfoLoss_cathegorical(['Masters', 'Bachelors'], education_tree_easy)
        iLoss3 = castle.VInfoLoss_cathegorical(['Bachelors', 'Masters', 'Primary School'], education_tree_easy)
        iLoss4 = castle.VInfoLoss_cathegorical('University', education_tree_easy)
        iLoss5 = castle.VInfoLoss_cathegorical('Bachelors', education_tree_easy)

        self.assertEqual(iLoss1, 0.0)
        self.assertEqual(iLoss2, 0.5)
        self.assertEqual(iLoss3, 1.0)
        self.assertEqual(iLoss4, 0.5)
        self.assertEqual(iLoss5, 0.0)

    def test_average_Loss(self):
        castle = Castle(None, 6, 5, 2, "easy_data")
        castle.mu = 3
        castle.anonymized_clusters_InfoLoss = [0.1, 0.2, 0.3]
        self.assertEqual(castle.average_Loss(), 0.2)

        castle.anonymized_clusters_InfoLoss = [0.1, 0.2, 0.3, 0.2]
        self.assertEqual(castle.average_Loss(), 0.7/3)

    def test_average_Loss_all(self):
        castle = Castle(None, 6, 5, 2, "easy_data")
        castle.mu = 3
        castle.anonymized_clusters_InfoLoss = [0.1, 0.2, 0.3]
        self.assertEqual(castle.average_Loss_all(), 0.2)

        castle.anonymized_clusters_InfoLoss = [0.1, 0.2, 0.3, 0.2]
        self.assertEqual(castle.average_Loss_all(), 0.8/4)

    def test_get_recent_InfoLoss(self):
        castle = Castle(None, 6, 5, 2, "easy_data")
        castle.mu = 3
        castle.anonymized_clusters_InfoLoss = [0.1, 0.2, 0.3]
        self.assertEqual(castle.get_recent_InfoLoss(), [0.1, 0.2, 0.3])

        castle.anonymized_clusters_InfoLoss = [0.1, 0.2, 0.3, 0.2]
        self.assertEqual(castle.get_recent_InfoLoss(), [0.2, 0.3, 0.2])

    def test_InfoLoss(self):
        castle = Castle(None, 6, 5, 2, "easy_data")
        tuple1 = Tuple(0, 0, (26, 'Masters'), ())
        cluster = Cluster(tuple1, "easy_data")
        erg1 = castle.InfoLoss(cluster.t)

        self.assertEqual(erg1, 0.0)

        tuple2 = Tuple(1, 1, (28, 'Bachelors'), ())
        cluster.add_tupel(tuple2)
        erg2 = castle.InfoLoss(cluster.t)

        self.assertAlmostEqual(erg2, 0.2598, places=4)

    def test_InfoLoss_tupel(self):
        castle = Castle(None, 6, 5, 2, "easy_data")
        tuple1 = Tuple(0, 0, (26, 'Masters'), ())
        tuple2 = Tuple(1, 1, ([26,28], 'Bachelors'), ())
        erg1 = castle.InfoLoss_tupel(tuple1.qi)
        erg2 = castle.InfoLoss_tupel(tuple2.qi)

        self.assertAlmostEqual(erg1, 0.0, places=4)
        self.assertAlmostEqual(erg2, 1/102, places=5)

class TestEnlargementFunction(unittest.TestCase):

    def test_enlargement1(self):
        castle = Castle(None, 6, 5, 2, "easy_data")
        tuple1 = Tuple(0, 0, (18, 'Primary School'), ())
        cluster = Cluster(tuple1, "easy_data")
        expected_result1 = 0.13480392156862744
        result1 = castle.Enlargement(cluster, Tuple(2, 2, (24, 'Bachelors'), ()))
        self.assertAlmostEqual(result1, expected_result1, places=3)
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
