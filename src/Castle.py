import heapq
import math
import random
import sys

from src.Cluster import Cluster
from src.edit_data import attribute_properties_test
from src.tree_functions import count_all_leaves, find_generalization, get_subtree


class Castle:
    def __init__(self, stream, k, delta, beta):
        self.not_anonymized_clusters = set()
        self.anonymized_clusters = set()
        self.tao = 0
        self.beta = beta
        self.k = k
        self.stream = stream
        self.pos_stream = 0
        self.delta = delta
        self.anonymized_clusters_InfoLoss = []

    def set_anonymized_clusters(self, anonymized_clusters):
        self.anonymized_clusters = anonymized_clusters

    def set_not_anonymized_clusters(self, not_anonymized_clusters):
        self.not_anonymized_clusters = not_anonymized_clusters

    def set_pos_stream(self, pos_stream):
        self.pos_stream = pos_stream

    def castle_algo(self, S):
        while self.S:
            next_tupel = self.S.pop()  # Get the next tupel from S
            pos_stream = next_tupel[0]
            print("pos:", pos_stream)
            best_cluster = self.best_selection(next_tupel)
            if best_cluster is None:
                new_cluster = Cluster(next_tupel)
                self.not_anonymized_clusters.add(new_cluster)
                best_cluster = new_cluster
                print("new cluster added to not_anonymized_clusters")
            else:
                best_cluster.add_tupel(next_tupel)
                print("tupel added to cluster")
                print("best cluster:", best_cluster.t)

            if next_tupel[0] - self.delta < 0:
                tuple_prime = None
            else:
                tuple_prime = S[next_tupel[0] - self.delta]
            if tuple_prime not in self.anonymized_clusters:
                self.delay_constraint(tuple_prime, best_cluster)

    def delay_constraint(self, tuple_prime, best_cluster):
        # ich übergebe das bestpasssende cluster, dann muss ich es nicht erst neu berechnen
        if len(best_cluster) >= self.k:
            self.output_cluster(best_cluster)
        else:
            KC_set = {cluster for cluster in self.anonymized_cluster if cluster.fits_in_cluster(tuple_prime)}
            # prüfen ob KC_set nicht leer ist
            if KC_set:
                KC = random.choice(KC_set)
                self.output_cluster(KC)
                return
            m = 0
            for cluster in self.not_anonymized_clusters:
                if len(best_cluster)<len(cluster):
                    m = m+1
            if m > (len(self.not_anonymized_clusters)/2):
                # suppress tuple prime
                self.suppress_tuple(tuple_prime)
                return
            if sum(len(cluster) for cluster in self.not_anonymized_clusters) < self.k:
                # suppress tuple prime
                self.suppress_tuple(tuple_prime)
                return
            # entfernt das beste Cluster aus den nicht anonymisierten Clustern um dann die merge Funktion aufrufen zu können
            clusters_without_best_cluster = self.not_anonymized_clusters.copy()
            clusters_without_best_cluster.discard(best_cluster)
            MC = self.merge_cluster(best_cluster, clusters_without_best_cluster)
            self.output_cluster(MC)


    def suppress_tuple(self, tuple):
        # TODO: nochmal prüfen
        self.stream.remove(tuple)



    def output_cluster(self, cluster):
        if len(cluster) >= 2 * self.k:
            split_cluster = self.split(cluster)
        else:
            split_cluster = {cluster}
        for cluster in split_cluster:
            cluster.output_tuples()
            self.tao = self.average_Loss()
            if self.InfoLoss(cluster.t) >= self.tao:
                self.anonymized_clusters.add(cluster, self.pos_stream)
                Info_Loss_anonymized_cluster = self.InfoLoss(cluster.t)
                self.anonymized_clusters_InfoLoss.append(Info_Loss_anonymized_cluster)
                # Muss das noch aus den nicht anonymisierten Clustern entfernt werden? Bzw. Müssen die Tuple entfernt werden?
                # not_anonymized_clusters.remove(cluster)
            else:
                # TODO: stimmt das hier so, dass das da entfern werden soll?
                del cluster
                # not_anonymized_clusters.remove(cluster)
            self.not_anonymized_clusters.remove(cluster)

    def split(self, cluster):
        split_cluster = set()
        BS = self.group_tuples_by_pid(cluster.data)
        while len(BS) >= self.k:
            selected_bucket = random.choice(list(BS.keys()))
            selected_tuple = random.choice(BS[selected_bucket])
            new_cluster = Cluster(selected_tuple)
            if not selected_bucket:
                del(selected_bucket)
            # H is heap with k-1 nodes
            H = self.initialize_heap(selected_tuple)
            for bucket in [b for b in BS if b != selected_bucket]:         # Führe Aktionen auf jedem "bucket" aus, der nicht "selected_bucket" ist.
                # Zufälligen Tupel aus Bucket auswählen
                tuple_from_bucket = random.choice(BS[bucket])

                # Distanz berechnen
                t_dist = self.calculate_tuple_distance(tuple_from_bucket, selected_tuple)

                # Distanz von t ist kleiner als die Distanz des Wurzelelements von H
                if t_dist < H[0][1]:
                    # Ersetze Wurzelelement mit t
                    heapq.heapreplace(H, (tuple_from_bucket, t_dist))
            for node in H:
                tuple_in_node = node[0]
                new_cluster.add_tupel(tuple_in_node)
                for bucket in BS:
                    if tuple_in_node in BS[bucket]:
                        BS[bucket].remove(tuple_in_node)
                        # Wenn Bucket leer ist, entfernen
                        if not BS[bucket]:
                            del BS[bucket]
                        break
            split_cluster.add(new_cluster)
        for bucket in BS.keys():
            ti = random.choice(BS[bucket])
            nearest_cluster = min(split_cluster, key=lambda cluster: self.Enlargement(cluster, t))
            nearest_cluster.update(BS[bucket])
            del BS[bucket]
        return split_cluster

    import heapq
    import sys

    def initialize_heap(self, tuple):
        H = []

        # Füge k-1 Knoten hinzu, jedes mit unendlicher Distanz zu selected_tuple
        for _ in range(self.k - 1):
            # Annahme: Der Knoten ist hier nur repräsentiert als Index (z.B. die Knoten könnten anschließend als 'Knoten 1', 'Knoten 2', etc. behandelt werden)
            # Du könntest stattdessen eigene Knotenobjekte o.ä. hinzufügen
            node = len(H)

            # Mit 'sys.maxsize' setzen wir die Distanz initial auf 'unendlich'
            distance = float('inf')

            # Die heapq-Bibliothek erlaubt es nur Min-Heap zu bauen,
            # deswegen nehmen wir -1*distance, um einen Max-Heap zu simulieren, da es nach der Beschreibung aussieht, dass du einen Max-Heap willst
            H.append((node, -1 * distance))

        # Heapfify ist eine Funktion, die eine Liste in-place in einen Heap umwandelt.
        heapq.heapify(H)

        return H

    def group_tuples_by_pid(self, cluster_data):
        grouped_data = dict()
        for tupel in cluster_data:
            pid = tupel.pid
            if pid in grouped_data:
                grouped_data[pid].append(tupel)
            else:
                grouped_data[pid] = [tupel]
        return grouped_data

    def merge_cluster(self, cluster, set_of_clusters):
        # set_of clusters besteht aus non_anonymized_clusters
        leng = len(cluster)
        while len(cluster) < self.k:
            min_enlargement = float('inf')

            for c in set_of_clusters:
                # berechnung der potentiellen Größe des gemergeden Clusters
                merged_size = len(cluster) + len(c)

                # berechnung des Enlargement
                enlargement = self.Enlargement(cluster.t, c.t)

                if enlargement < min_enlargement:
                    min_enlargement = enlargement
                    min_enlargement_cluster = c

            # fügt die Tupel des min_enlargement_cluster zu cluster hinzu
            for tupel in min_enlargement_cluster.data:
                cluster.add_tupel(tupel)
            # not_anonymized_clusters.remove(min_enlargement_cluster)
        return cluster

    def best_selection(self, tuple):
        enlargements = set()
        if not self.not_anonymized_clusters:
            return None
        # Möglichkeit mit List-Comprehension darstellen:
        # enlargements = set([Enlargement(cluster, tuple) for cluster in not_anonymized_clusters])
        for cluster in self.not_anonymized_clusters:
            enlargement = self.Enlargement(cluster.t, tuple)
            enlargements.add(enlargement)
        min_enlargement = min(enlargements)

        # Set of clusters C' in not_anonymized_clusters with Enlargement(C', tupel) = min
        set_cluster_min = [C for C in self.not_anonymized_clusters if self.Enlargement(C.t, tuple) == min_enlargement]
        set_c_ok = set()
        for cluster in set_cluster_min:
            IL_cluster = self.InfoLoss(cluster.t)
            if IL_cluster >= self.tao:
                set_c_ok.add(cluster)
        if not set_c_ok:
            if len(self.not_anonymized_clusters) >= self.beta:
                return min(set_cluster_min, key=lambda cluster: len(cluster.data))
            else:
                return None
        else:
            return min(set_c_ok, key=lambda cluster: len(cluster.data))

    def Enlargement(self, cluster, tupel):
        """
          This function calculates the enlargement of a cluster C with respect to a tuple t.

          Args:
              cluster: A cluster represented as a list of tuples.
              tupel: A tuple.

          Returns:
              A number representing the enlargement of a cluster with respect to t.
          """
        n = len(cluster)  # Assuming all tuples in C have the same length
        enlarged_cluster = self.add_tupel(cluster, tupel)
        sum_iloss_cluster = 0
        sum_iloss_enlarged_cluster = 0

        # Calculate VInfoLoss for each attribute
        for i in range(n):
            info_loss_cluster = self.VInfoLoss_cluster(cluster[i], i)
            sum_iloss_cluster += info_loss_cluster
            info_loss_together = self.VInfoLoss(enlarged_cluster[i], i)
            sum_iloss_enlarged_cluster += info_loss_together

        return 1 / n * sum_iloss_enlarged_cluster - 1 / n * sum_iloss_cluster

    def InfoLoss(self, tupel):
        n = len(tupel)
        sum = 0
        for att_pos in range(n):
            sum += self.VInfoLoss_cluster(tupel[att_pos], att_pos)
        return 1 / n * sum

    def InfoLoss_tupel(self, tupel):
        n = len(tupel)
        sum = 0
        for att_pos in range(n):
            sum += self.VInfoLoss(tupel[att_pos], att_pos)
        return 1 / n * sum


    def add_tupel(self, cluster, tupel):
        new_cluster = list(cluster)
        for i in range(len(cluster) - 1):
            if attribute_properties_test[i]['type'] == 'continuous':
                new_cluster[i] = self.adjust_interval(tupel[i], cluster[i])

            elif attribute_properties_test[i]['type'] == 'cathegorical':
                new_cluster[i] = self.add_unique_string_to_list(tupel[i], cluster[i])

        return tuple(new_cluster)

    def adjust_interval(self, value, interval):
        # wenn beides Intervalle sind
        if isinstance(value, (list, tuple)) and isinstance(interval, (list, tuple)):
            return [min(value[0], interval[0]), max(value[1], interval[1])]

        # Wenn das Intervall nur eine einzelne Zahl enthält
        if isinstance(interval, int):
            if value < interval:
                return [value, interval]
            else:
                return [interval, value]

        # Wenn das Intervall ein normaler Bereich ist
        else:
            lower_bound, upper_bound = interval

            if value < lower_bound:
                lower_bound = value
            elif value > upper_bound:
                upper_bound = value

            return [lower_bound, upper_bound]

    def add_unique_string_to_list(self, value, value_list):
        if value not in value_list:
            value_list.append(value)

    def is_in_interval(self, value, interval):
        lower_bound, upper_bound = interval
        return lower_bound <= value <= upper_bound

    def VInfoLoss(self, attribut, pos) -> int:
        info_loss = 0
        if attribute_properties_test[pos]['type'] == 'continuous':
            info_loss = self.VInfoLoss_continuos(attribut, attribute_properties_test[pos]['interval'])
        elif attribute_properties_test[pos]['type'] == 'cathegorical':
            info_loss = self.VInfoLoss_cathegorical(attribut, attribute_properties_test[pos]['hierarchy_tree'])
        return info_loss

    def VInfoLoss_cluster(self, attribut, pos) -> int:
        info_loss = 0
        if attribute_properties_test[pos]['type'] == 'continuous':
            info_loss = self.VInfoLoss_continuos(attribut, attribute_properties_test[pos]['interval'])
        elif attribute_properties_test[pos]['type'] == 'cathegorical':
            info_loss = self.VInfoLoss_cathegorical_cluster(attribut, attribute_properties_test[pos]['hierarchy_tree'])
        return info_loss

    def VInfoLoss_continuos(self, attribut_range, domain_range):
        if len(attribut_range) == 1:
            # TODO: hier nochmal schauen ob das stimmt
            return (attribut_range[0]) / (domain_range[1] - domain_range[0])
        return (attribut_range[1] - attribut_range[0]) / (domain_range[1] - domain_range[0])

    def VInfoLoss_cathegorical(self, attribut_range, domain_tree):
        domain_range = count_all_leaves(domain_tree)
        attribute_range_generalized = find_generalization(domain_tree, attribut_range)
        generalized_range = count_all_leaves(get_subtree(domain_tree, attribute_range_generalized))
        erg = (generalized_range - 1) / (domain_range - 1)
        return erg

    def VInfoLoss_cathegorical_cluster(self, attribut_range, domain_tree):
        domain_range = count_all_leaves(domain_tree)
        generalized_range = len(attribut_range)
        erg = (generalized_range - 1) / (domain_range - 1)
        return erg

    def average_Loss(self):
        if len(self.anonymized_clusters_InfoLoss) == 0:
            return 0
        else:
            return 1/len(self.anonymized_clusters_InfoLoss) * sum(self.anonymized_clusters_InfoLoss)

    def calculate_tuple_distance(self, tuple1, tuple2) -> float:
        num_diff = abs(tuple1[0] - tuple2[0])
        str_diff = 0 if tuple1[1] == tuple2[1] else 1
        return math.sqrt(num_diff ** 2 + str_diff ** 2)

