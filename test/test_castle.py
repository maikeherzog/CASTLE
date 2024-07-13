import math
import sys
import unittest

from src.Castle import Castle
from src.Cluster import Cluster
from src.Data import Data
from src.Tupel import Tuple
from src.hierarchy_tree import education_tree_easy
from src.tree_functions import find_generalization

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


class TestMergeCluster(unittest.TestCase):

    def setUp(self):
        self.castle = Castle(None, 6, 5, 2, 'easy_data')


    def test_merge_cluster(self):
        tuple0 = Tuple(0, 0, (18, 'Bachelors'), ())
        cluster1 = Cluster(tuple0, "easy_data")
        tuple1 = Tuple(1,1,(24, 'Bachelors'),())
        tuple2 = Tuple(2,2,(23, 'Masters'),())
        cluster1.add_tupel(tuple1)
        cluster1.add_tupel(tuple2)

        tuple3 = Tuple(3,3,(12, 'Bachelors'),())
        cluster2 = Cluster(tuple3, "easy_data")
        tuple4 = Tuple(5,4,(12, 'Bachelors'),())
        tuple5 = Tuple(6,5,(28, 'Masters'),())
        cluster2.add_tupel(tuple4)
        cluster2.add_tupel(tuple5)

        not_anonymized_clusters = {cluster2}
        self.castle.not_anonymized_clusters = not_anonymized_clusters
        # Aufrufen der zu testenden Funktion
        result = self.castle.merge_cluster(cluster1, not_anonymized_clusters)

        expected_cluster_data = [tuple0, tuple1, tuple2, tuple3, tuple4, tuple5]

        self.assertEqual(result.data, expected_cluster_data)
        self.assertEqual(result.t, ([12, 28], ['Bachelors', 'Masters']))



class TestSplitMethods(unittest.TestCase):
    def setUp(self):
        self.castle = Castle({(0, 18, 'Bachelors'), (1, 24, 'Bachelors'), (2, 23, 'Masters')}, 6, 5, 2, 'easy_data')


    def test_initialize_heap(self):

        tuple = Tuple(0, 0, (18, 'Bachelors'), ())
        H = self.castle.initialize_heap(tuple)

        self.assertEqual(len(H), 5)

        for element in H:
            self.assertEqual(element.dist, -1 * float('inf'))

    def test_split_cluster(self):
        tupel_liste = [(1, 1, 18, 'Bachelors'), (2, 2, 20, 'Masters'), (4, 3, 30, 'Ph.D.'), (5, 4, 24, 'Ph.D.'), (6, 5, 17, 'Bachelors'), (8, 7, 20, 'Bachelors')]
        data = Data(tupel_liste, [2, 4], [])
        castle = Castle(data.data, 3, 4, 3, 'easy_data')
        cluster = Cluster(Tuple(1, 1, (18, 'Bachelors'), ()), 'easy_data')

        cluster.add_tupel(Tuple(2, 2, (20, 'Masters'), ()))
        cluster.add_tupel(Tuple(4, 3, (30, 'Ph.D'), ()))
        cluster.add_tupel(Tuple(5, 4, (24, 'Ph.D'), ()))
        cluster.add_tupel(Tuple(6, 5, (17, 'Bachelors'), ()))
        cluster.add_tupel(Tuple(8, 7, (20, 'Bachelors'), ()))
        castle.not_anonymized_clusters = {cluster}
        result = castle.split(cluster)

        self.assertEqual(len(result), 2)

    def test_split_cluster(self):
        tupel_liste = [(1, 1, 18, 'Bachelors'), (2, 2, 20, 'Masters'), (3, 1, 18, 'Bachelors'), (5, 4, 24, 'Ph.D.'),
                       (6, 5, 17, 'Bachelors'), (8, 2, 20, 'Masters')]
        data = Data(tupel_liste, [2, 4], [])
        castle = Castle(data.data, 3, 4, 3, 'easy_data')
        cluster = Cluster(Tuple(1, 1, (18, 'Bachelors'), ()), 'easy_data')

        cluster.add_tupel(Tuple(2, 2, (20, 'Masters'), ()))
        cluster.add_tupel(Tuple(4, 1, (18, 'Bachelors'), ()))
        cluster.add_tupel(Tuple(5, 4, (24, 'Ph.D'), ()))
        cluster.add_tupel(Tuple(6, 5, (17, 'Bachelors'), ()))
        cluster.add_tupel(Tuple(8, 2, (20, 'Masters'), ()))

        castle.not_anonymized_clusters = {cluster}
        result = castle.split(cluster)

        self.assertEqual(len(result), 2)

class TestEnlargementAndBestSelection(unittest.TestCase):
    def setUp(self):
        self.castle = Castle(None, 6, 5, 2, "easy_data")
        self.tuple1 = Tuple(0, 0, (18, 'Primary School'), ())
        self.tuple2 = Tuple(1, 1, (22, 'Secondary School'), ())
        self.tuple3 = Tuple(2, 2, (26, 'Bachelors'), ())
        self.tuple4 = Tuple(3, 3, (28, 'Masters'), ())
        self.cluster1 = Cluster(self.tuple1, "easy_data")
        self.cluster1.add_tupel(self.tuple2)
        self.cluster2 = Cluster(self.tuple3, "easy_data")
        self.cluster2.add_tupel(self.tuple4)

        self.tuple5 = Tuple(1,5,(24, 'Bachelors'), ())


    """def test_Enlargement_Tuple_Tuple(self):

        erg = self.castle.Enlargement((18, 'Bachelors'), (24, 'Bachelors'))
        self.assertEqual(erg, 0.13480392156862744)"""

    def test_enlargement(self):
        # testcase 1
        expected_result1 = 0.3848
        result1 = self.castle.Enlargement(self.cluster1, self.tuple5)
        self.assertAlmostEqual(result1, expected_result1, places=3)

        self.cluster1.add_tupel(self.tuple5)
        result2 = self.castle.Enlargement(self.cluster1, self.tuple5)
        expected_result2 = 0.0
        self.assertAlmostEqual(result2, expected_result2, places=3)

        result3 = self.castle.Enlargement(self.cluster2, self.tuple5)
        expected_result3 = 0.01
        self.assertAlmostEqual(result3, expected_result3, places=3)

    def test_best_selection(self):
        self.castle.not_anonymized_clusters = {self.cluster1, self.cluster2}
        erg = self.castle.best_selection(self.tuple5)
        self.assertEqual(erg, self.cluster2)



class TestIloss(unittest.TestCase):

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

    def test_Iloss_cluster(self):
        castle = Castle({(1, 0, 18, 'Bachelors'), (2, 1, 24, 'Bachelors'), (3, 2, 23, 'Masters')}, 5, 5, 2, 'easy_data')
        cluster = Cluster(Tuple(1, 1, (18, 'Bachelors'), ()), 'easy_data')

        cluster.add_tupel(Tuple(2, 2, (20, 'Masters'), ()))
        cluster.add_tupel(Tuple(4, 1, (18, 'Bachelors'), ()))
        cluster.add_tupel(Tuple(5, 4, (24, 'Ph.D'), ()))
        cluster.add_tupel(Tuple(6, 5, (17, 'Bachelors'), ()))
        cluster.add_tupel(Tuple(8, 2, (20, 'Masters'), ()))

        iloss = castle.InfoLoss(cluster.t)
        self.assertEqual(iloss, 0.28431372549019607)

        cluster_2 = Cluster(Tuple(8, 2, (20, 'Masters'), ()), 'easy_data')
        cluster_2.add_tupel(Tuple(6, 5, (17, 'Bachelors'), ()))
        cluster_2.add_tupel(Tuple(4, 1, (18, 'Bachelors'), ()))

        iloss_2 = castle.InfoLoss(cluster_2.t)
        self.assertEqual(iloss_2, 0.2647058823529412)

        cluster_3 = Cluster(Tuple(1, 1, (18, 'Bachelors'), ()), 'easy_data')
        cluster_3.add_tupel(Tuple(2, 2, (20, 'Masters'), ()))
        cluster_3.add_tupel(Tuple(5, 4, (24, 'Ph.D'), ()))

        iloss_3 = castle.InfoLoss(cluster_3.t)
        self.assertEqual(iloss_3, 0.27941176470588236)

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


class TestOutput(unittest.TestCase):

    def setUp(self):
        self.castle = Castle({(0, 18, 'Bachelors'), (1, 24, 'Bachelors'), (2, 23, 'Masters')}, 6, 5, 2, 'easy_data')
        self.castle2 = Castle({(0, 18, 'Bachelors'), (1, 24, 'Bachelors'), (2, 23, 'Masters')}, 2, 5, 2, 'easy_data')


    def test_output_anonymized_cluster(self):
        cluster = Cluster(Tuple(1, 1, (26, 'Bachelors'), ()), 'easy_data')
        cluster.add_tupel(Tuple(2, 2, (28, 'Masters'), ()))

        self.castle.output_anonymized_cluster(cluster, Tuple(1, 1, (18, 'Bachelors'), ()))
        self.assertAlmostEqual(self.castle.anonymized_clusters_InfoLoss[0], 0.2598, places=3)

    def test_output_cluster(self):
        cluster = Cluster(Tuple(1, 1, (21, 'Bachelors'), ()), 'easy_data')
        cluster.add_tupel(Tuple(2, 2, (20, 'Masters'), ()))
        cluster.add_tupel(Tuple(4, 1, (19, 'Bachelors'), ()))
        cluster.add_tupel(Tuple(5, 2, (21, 'Masters'), ()))
        cluster.add_tupel(Tuple(2, 3, (20, 'Masters'), ()))
        cluster.add_tupel(Tuple(4, 4, (18, 'Bachelors'), ()))


        self.castle2.not_anonymized_clusters = {cluster}

        output = self.castle2.output_cluster(cluster)

        self.assertEqual(len(self.castle2.anonymized_clusters_InfoLoss), 6)

    def test_get_num_of_all_pids(self):
        castle = Castle(None, 6, 5, 2, 'easy_data')
        cluster = Cluster(Tuple(1, 1, (21, 'Bachelors'), ()), 'easy_data')
        cluster.add_tupel(Tuple(2, 2, (20, 'Masters'), ()))
        cluster.add_tupel(Tuple(4, 1, (19, 'Bachelors'), ()))
        cluster.add_tupel(Tuple(5, 2, (21, 'Masters'), ()))
        cluster.add_tupel(Tuple(2, 3, (20, 'Masters'), ()))
        cluster.add_tupel(Tuple(4, 4, (18, 'Bachelors'), ()))

        castle.not_anonymized_clusters = {cluster}
        self.assertEqual(castle.get_num_of_all_pids(), 4)

class TestCastleSet(unittest.TestCase):
    def test_set_pos_stream(self):
        castle = Castle(None, 6, 5, 2, 'easy_data')
        castle.set_pos_stream(5)
        self.assertEqual(castle.pos_stream, 5)




# Ausführen der Test-Suite
if __name__ == "__main__":
    unittest.main()
