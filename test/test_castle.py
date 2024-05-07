import unittest

from src.Castle import merge_cluster
from src.Cluster import Cluster


class TestMergeCluster(unittest.TestCase):
    def test_merge_cluster(self):
        # Erzeugung der Eingabedaten
        cluster1 = Cluster((18, 'Bachelors'))
        cluster1.add_tupel((24, 'Bachelors'))
        cluster1.add_tupel((23, 'Masters'))

        cluster2 = Cluster((18, 'Bachelors'))
        cluster2.add_tupel((12, 'Bachelors'))
        cluster2.add_tupel((28, 'Masters'))

        not_anonymized_clusters = {cluster2}

        # Aufrufen der zu testenden Funktion
        result = merge_cluster(cluster1, not_anonymized_clusters, 5)

        expected_cluster = [(18, 'Bachelors'), (24, 'Bachelors'),
                            (23, 'Masters'), (18, 'Bachelors'),
                            (12, 'Bachelors'), (28, 'Masters')]
        self.assertEqual(result.data, expected_cluster)
        self.assertEqual(result.t, ([12, 28], ['Bachelors', 'Masters']))


# Ausführen der Test-Suite
if __name__ == "__main__":
    unittest.main()
