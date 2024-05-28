import sys
import unittest

from src.Castle import Castle
from src.Cluster import Cluster


class TestMergeCluster(unittest.TestCase):

    castle = Castle({(0, 18, 'Bachelors'), (1, 24, 'Bachelors'), (2, 23, 'Masters')}, 6, 5, 2)

    def test_merge_cluster(self):
        castle = Castle(None, 6, 5, 2)
        # Erzeugung der Eingabedaten
        cluster1 = Cluster((18, 'Bachelors'))
        cluster1.add_tupel((24, 'Bachelors'))
        cluster1.add_tupel((23, 'Masters'))

        cluster2 = Cluster((18, 'Bachelors'))
        cluster2.add_tupel((12, 'Bachelors'))
        cluster2.add_tupel((28, 'Masters'))

        not_anonymized_clusters = {cluster2}
        castle.set_not_anonymized_clusters(not_anonymized_clusters)
        # Aufrufen der zu testenden Funktion
        result = castle.merge_cluster(cluster1, not_anonymized_clusters)

        expected_cluster = [(18, 'Bachelors'), (24, 'Bachelors'),
                            (23, 'Masters'), (18, 'Bachelors'),
                            (12, 'Bachelors'), (28, 'Masters')]
        self.assertEqual(result.data, expected_cluster)
        self.assertEqual(result.t, ([12, 28], ['Bachelors', 'Masters']))

    def test_average_loss(self):
        castle = Castle({(0, 18, 'Bachelors'), (1, 24, 'Bachelors'), (2, 23, 'Masters') }, 6, 5, 2)
        castle.anonymized_clusters_InfoLoss= [0.1, 0.2, 0.3]
        self.assertEqual(castle.average_Loss(), 0.2)

    def test_average_loss_no_anonymized_cluster(self):
        castle = Castle({(0, 18, 'Bachelors'), (1, 24, 'Bachelors'), (2, 23, 'Masters') }, 6, 5, 2)
        self.assertEqual(castle.average_Loss(), 0.0)


class TestSplitMethods(unittest.TestCase):

    def test_initialize_heap(self):
        castle = Castle({(0, 18, 'Bachelors'), (1, 24, 'Bachelors'), (2, 23, 'Masters') }, 5, 5, 2)

        H = castle.initialize_heap(
            "Dummy Tuple")  # es spielt keine Rolle, was wir hier passieren, da die Distanzen unabhängig von diesem Wert auf Unendlichkeit gesetzt werden

        # Es sollte k - 1 = 4 Knoten im Heap geben
        self.assertEqual(len(H), 4)

        # Jeder Knoten sollte eine "unendliche" Distanz haben, die sich durch float('inf') darstellen lässt
        for (index,distanze) in H:
            self.assertEqual((index, distanze),(index, -1 * float('inf')))

class TestEnlargement(unittest.TestCase):
    def test_Enlargement_Tuple_Tuple(self):

        castle = Castle({(0, 18, 'Bachelors'), (1, 24, 'Bachelors'), (2, 23, 'Masters')}, 5, 5, 2)
        castle.Enlargement((18, 'Bachelors'), (24, 'Bachelors'))
        self.assertEqual(castle.Enlargement((18, 'Bachelors'), (24, 'Bachelors')), 0.13480392156862744)

# Ausführen der Test-Suite
if __name__ == "__main__":
    unittest.main()
