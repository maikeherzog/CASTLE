from src.Castle import Castle
from src.Cluster import Cluster
from src.Data import Data
from src.Tupel import Tuple
from src.hierarchy_tree import education_tree_easy

def test_InfoLoss_cluster_test1(self):
    castle = Castle(None, 5, 5, 2, 'adult_castle')
    # ([38, 47], [65324, 410867], [14, 16], [0, 0], [0, 0], [40, 50])
    cluster1 = Cluster(Tuple(1, 1, (38, 65324, 14, 0, 0, 40), ()), 'adult_castle')
    cluster1.add_tupel(Tuple(2, 2, (47, 410867, 16, 0, 0, 50), ()))
    # ([35, 49], [29054, 113324], [9, 10], [0, 0], [0, 0], [40, 60])
    cluster2 = Cluster(Tuple(3, 3, (35, 29054, 9, 0, 0, 40), ()), 'adult_castle')
    cluster2.add_tupel(Tuple(4, 4, (49, 113324, 10, 0, 0, 60), ()))
    # ([35, 49], [63509, 96055], [9, 10], [0, 0], [0, 0], [40, 60])
    cluster3 = Cluster(Tuple(5, 5, (35, 63509, 9, 0, 0, 40), ()), 'adult_castle')
    cluster3.add_tupel(Tuple(6, 6, (49, 96055, 10, 0, 0, 60), ()))
    # ([18, 32], [193650, 219838], [7, 9], [0, 2580], [0, 0], [40, 40])
    cluster4 = Cluster(Tuple(7, 7, (18, 193650, 7, 0, 0, 40), ()), 'adult_castle')
    cluster4.add_tupel(Tuple(8, 8, (32, 219838, 9, 2580, 0, 40), ()))
    # ([17, 54], [173858, 234652], [1, 6], [0, 0], [0, 0], [35, 50])
    cluster5 = Cluster(Tuple(9, 9, (17, 173858, 1, 0, 0, 35), ()), 'adult_castle')
    cluster5.add_tupel(Tuple(10, 10, (54, 234652, 6, 0, 0, 50), ()))
    # ([32, 44], [158416, 180551], [9, 10], [0, 7298], [0, 0], [35, 40])
    cluster6 = Cluster(Tuple(11, 11, (32, 158416, 9, 0, 0, 35), ()), 'adult_castle')
    cluster6.add_tupel(Tuple(12, 12, (44, 180551, 10, 7298, 0, 40), ()))
    # ([32, 44], [139890, 157747], [9, 10], [0, 7298], [0, 0], [35, 40])
    cluster7 = Cluster(Tuple(13, 13, (32, 139890, 9, 0, 0, 35), ()), 'adult_castle')
    cluster7.add_tupel(Tuple(14, 14, (44, 157747, 10, 7298, 0, 40), ()))
    # ([24, 90], [122246, 156623], [4, 16], [0, 15831], [0, 4356], [1, 99])
    cluster8 = Cluster(Tuple(15, 15, (24, 122246, 4, 0, 0, 1), ()), 'adult_castle')
    cluster8.add_tupel(Tuple(16, 16, (90, 156623, 16, 15831, 4356, 99), ()))
    # ([19, 80], [180401, 185283], [4, 15], [0, 1055], [0, 1977], [6, 99])
    cluster9 = Cluster(Tuple(17, 17, (19, 180401, 4, 0, 0, 6), ()), 'adult_castle')
    cluster9.add_tupel(Tuple(18, 18, (80, 185283, 15, 1055, 1977, 99), ()))

    castle.anonymized_clusters = {cluster1, cluster2, cluster3, cluster4, cluster5, cluster6, cluster7, cluster8,
                                  cluster9}
    erg = castle.InfoLoss_anonymized_cluster(castle.anonymized_clusters)

    self.assertEqual(erg, 0)


def test_Infoloss_cluster_test2(self):
    castle = Castle(None, 5, 5, 2, 'adult_castle')
    # ([36, 43], [202683, 365739], [10, 10], [0, 0])
    cluster1 = Cluster(Tuple(1, 1, (36, 202683, 10, 0), ()), 'adult_castle')
    cluster1.add_tupel(Tuple(2, 2, (43, 365739, 10, 0), ()))
    # ([43, 90], [142717, 160625], [4, 16], [0, 15024])
    cluster2 = Cluster(Tuple(3, 3, (43, 142717, 4, 0), ()), 'adult_castle')
    cluster2.add_tupel(Tuple(4, 4, (90, 160625, 16, 15024), ()))
    # ([26, 41], [83893, 116358], [10, 12], [0, 0])
    cluster3 = Cluster(Tuple(5, 5, (26, 83893, 10, 0), ()), 'adult_castle')
    cluster3.add_tupel(Tuple(6, 6, (41, 116358, 12, 0), ()))
    # ([17, 30], [267034, 309178], [5, 9], [0, 0])
    cluster4 = Cluster(Tuple(7, 7, (17, 267034, 5, 0), ()), 'adult_castle')
    cluster4.add_tupel(Tuple(8, 8, (30, 309178, 9, 0), ()))
    # ([17, 30], [19752, 57067], [5, 9], [0, 594])
    cluster5 = Cluster(Tuple(9, 9, (17, 19752, 5, 0), ()), 'adult_castle')
    cluster5.add_tupel(Tuple(10, 10, (30, 57067, 9, 594), ()))
    # ([33, 42], [73296, 114678], [9, 9], [0, 5455])
    cluster6 = Cluster(Tuple(11, 11, (33, 73296, 9, 0), ()), 'adult_castle')
    cluster6.add_tupel(Tuple(12, 12, (42, 114678, 9, 5455), ()))
    # ([24, 45], [106169, 157240], [13, 16], [0, 15024])
    cluster7 = Cluster(Tuple(13, 13, (24, 106169, 13, 0), ()), 'adult_castle')
    cluster7.add_tupel(Tuple(14, 14, (45, 157240, 16, 15024), ()))
    # ([33, 42], [188391, 215646], [9, 9], [0, 7298])
    cluster8 = Cluster(Tuple(15, 15, (33, 188391, 9, 0), ()), 'adult_castle')
    cluster8.add_tupel(Tuple(16, 16, (42, 215646, 9, 7298), ()))
    # ([43, 82], [145493, 152540], [4, 16], [0, 2414])
    cluster9 = Cluster(Tuple(17, 17, (43, 145493, 4, 0), ()), 'adult_castle')
    cluster9.add_tupel(Tuple(18, 18, (82, 152540, 16, 2414), ()))
    # ([17, 30], [205188, 216814], [5, 9], [0, 0])
    cluster10 = Cluster(Tuple(19, 19, (17, 205188, 5, 0), ()), 'adult_castle')
    cluster10.add_tupel(Tuple(20, 20, (30, 216814, 9, 0), ()))
    # ([32, 90], [39643, 58898], [4, 16], [0, 9386])
    cluster11 = Cluster(Tuple(21, 21, (32, 39643, 4, 0), ()), 'adult_castle')
    cluster11.add_tupel(Tuple(22, 22, (90, 58898, 16, 9386), ()))
    # ([33, 42], [36270, 67317], [9, 9], [0, 7298])
    cluster12 = Cluster(Tuple(23, 23, (33, 36270, 9, 0), ()), 'adult_castle')
    cluster12.add_tupel(Tuple(24, 24, (42, 67317, 9, 7298), ()))
    # ([26, 41], [130589, 146243], [10, 12], [0, 0])
    cluster13 = Cluster(Tuple(25, 25, (26, 130589, 10, 0), ()), 'adult_castle')
    cluster13.add_tupel(Tuple(26, 26, (41, 146243, 12, 0), ()))

    castle.anonymized_clusters = {cluster1, cluster2, cluster3, cluster4, cluster5, cluster6, cluster7, cluster8,
                                  cluster9, cluster10, cluster11, cluster12, cluster13}
    erg = castle.InfoLoss_anonymized_cluster(castle.anonymized_clusters)

    self.assertEqual(erg, 0)
