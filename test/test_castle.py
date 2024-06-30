import sys
import unittest

from src.Castle import Castle
from src.Cluster import Cluster
from src.Data import Data
from src.Tupel import Tuple


class TestMergeCluster(unittest.TestCase):

    def setUp(self):
        self.castle = Castle({(0, 18, 'Bachelors'), (1, 24, 'Bachelors'), (2, 23, 'Masters')}, 6, 5, 2, 'easy_data')


    def test_merge_cluster(self):
        #castle = Castle(None, 6, 5, 2)
        # Erzeugung der Eingabedaten
        tuple0 = Tuple(0, 0, (18, 'Bachelors'), ())
        cluster1 = Cluster(tuple0)
        tuple1 = Tuple(1,1,(24, 'Bachelors'),())
        tuple2 = Tuple(2,2,(23, 'Masters'),())
        cluster1.add_tupel(tuple1)
        cluster1.add_tupel(tuple2)

        cluster2 = Cluster(tuple0)
        tuple3 = Tuple(1,1,(12, 'Bachelors'),())
        tuple4 = Tuple(2,2,(28, 'Masters'),())
        cluster2.add_tupel(tuple3)
        cluster2.add_tupel(tuple4)

        not_anonymized_clusters = {cluster2}
        self.castle.set_not_anonymized_clusters(not_anonymized_clusters)
        # Aufrufen der zu testenden Funktion
        result = self.castle.merge_cluster(cluster1, not_anonymized_clusters)

        expected_cluster_data = [tuple0, tuple1, tuple2, tuple0, tuple3, tuple4]

        self.assertEqual(result.data, expected_cluster_data)
        self.assertEqual(result.t, ([12, 28], ['Bachelors', 'Masters']))

    def test_average_loss(self):
        #castle = Castle({(0, 18, 'Bachelors'), (1, 24, 'Bachelors'), (2, 23, 'Masters') }, 6, 5, 2)
        self.castle.anonymized_clusters_InfoLoss= [0.1, 0.2, 0.3]
        self.assertEqual(self.castle.average_Loss(), 0.2)

    def test_average_loss_no_anonymized_cluster(self):
        #castle = Castle({(0, 18, 'Bachelors'), (1, 24, 'Bachelors'), (2, 23, 'Masters') }, 6, 5, 2)
        self.assertEqual(self.castle.average_Loss(), 0.0)


class TestSplitMethods(unittest.TestCase):
    def setUp(self):
        self.castle = Castle({(0, 18, 'Bachelors'), (1, 24, 'Bachelors'), (2, 23, 'Masters')}, 6, 5, 2, 'easy_data')


    def test_initialize_heap(self):
        #castle = Castle({(0, 18, 'Bachelors'), (1, 24, 'Bachelors'), (2, 23, 'Masters') }, 5, 5, 2)

        H = self.castle.initialize_heap(
            "Dummy Tuple")  # es spielt keine Rolle, was wir hier passieren, da die Distanzen unabhängig von diesem Wert auf Unendlichkeit gesetzt werden

        # Es sollte k - 1 = 4 Knoten im Heap geben
        self.assertEqual(len(H), 4)

        # Jeder Knoten sollte eine "unendliche" Distanz haben, die sich durch float('inf') darstellen lässt
        for (index,distanze) in H:
            self.assertEqual((index, distanze),(index, -1 * float('inf')))

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
        result = castle.split_2(cluster)

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
        result = castle.split_2(cluster)

        self.assertEqual(len(result), 2)

class TestEnlargement(unittest.TestCase):
    def setUp(self):
        self.castle = Castle({(0, 18, 'Bachelors'), (1, 24, 'Bachelors'), (2, 23, 'Masters')}, 6, 5, 2)

    def test_Enlargement_Tuple_Tuple(self):

        #castle = Castle({(0, 18, 'Bachelors'), (1, 24, 'Bachelors'), (2, 23, 'Masters')}, 5, 5, 2)
        self.castle.Enlargement((18, 'Bachelors'), (24, 'Bachelors'))
        self.assertEqual(self.castle.Enlargement((18, 'Bachelors'), (24, 'Bachelors')), 0.13480392156862744)

    def test_enlargement(self):
        # testcase 1
        #cluster1 = ([26, 28], ['Masters', 'Bachelors'])
        cluster1 = Cluster(Tuple(0,0,(26, 'Masters'),()))
        cluster1.add_tupel(Tuple(1,1,(28, 'Bachelors'),()))
        #tupel1 = (24, 'Bachelors')
        tuple1 = Tuple(2,2,(24, 'Bachelors'), ())
        expected_result1 = 0.13480392156862744
        result1 = self.castle.Enlargement(cluster1, tuple1)
        self.assertAlmostEqual(result1, expected_result1, places=3)

    def test_delay_constraint(self):
        castle = Castle({(0,0, 52, 'Secondary School'), (1,1, 51, 'Bachelors'), (2,2, 61, 'Ph.D'), (3,3,51,'Bachelors')}, 3, 3, 3)
        tuple1 = Tuple(0,0, 52, 'Secondary School')
        tuple2 = Tuple(1,1, 51, 'Bachelors')
        tuple3 = Tuple(2,2, 61, 'Ph.D')
        tuple4 = Tuple(3,3, 51, 'Bachelors')
        cluster1 = Cluster(tuple1)
        cluster2 = Cluster(tuple2)
        cluster3 = Cluster(tuple3)
        castle.not_anonymized_clusters = {cluster1, cluster2, cluster3}
        castle.delay_constraint(tuple1)

class TestIloss(unittest.TestCase):
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
        self.assertEqual(iloss_2, 0.13970588235294118)

        cluster_3 = Cluster(Tuple(1, 1, (18, 'Bachelors'), ()), 'easy_data')
        cluster_3.add_tupel(Tuple(2, 2, (20, 'Masters'), ()))
        cluster_3.add_tupel(Tuple(5, 4, (24, 'Ph.D'), ()))

        iloss_3 = castle.InfoLoss(cluster_3.t)
        self.assertEqual(iloss_3, 0.27941176470588236)

# Ausführen der Test-Suite
if __name__ == "__main__":
    unittest.main()
