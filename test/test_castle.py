import sys
import unittest

from src.Castle import Castle
from src.Cluster import Cluster
from src.Tupel import Tuple


class TestMergeCluster(unittest.TestCase):

    def setUp(self):
        self.castle = Castle({(0, 18, 'Bachelors'), (1, 24, 'Bachelors'), (2, 23, 'Masters')}, 6, 5, 2)


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
        self.castle = Castle({(0, 18, 'Bachelors'), (1, 24, 'Bachelors'), (2, 23, 'Masters')}, 6, 5, 2)


    def test_initialize_heap(self):
        #castle = Castle({(0, 18, 'Bachelors'), (1, 24, 'Bachelors'), (2, 23, 'Masters') }, 5, 5, 2)

        H = self.castle.initialize_heap(
            "Dummy Tuple")  # es spielt keine Rolle, was wir hier passieren, da die Distanzen unabhängig von diesem Wert auf Unendlichkeit gesetzt werden

        # Es sollte k - 1 = 4 Knoten im Heap geben
        self.assertEqual(len(H), 4)

        # Jeder Knoten sollte eine "unendliche" Distanz haben, die sich durch float('inf') darstellen lässt
        for (index,distanze) in H:
            self.assertEqual((index, distanze),(index, -1 * float('inf')))

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

# Ausführen der Test-Suite
if __name__ == "__main__":
    unittest.main()
