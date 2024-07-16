import copy
import heapq
import math
import random
import logging

import sys

from src.Cluster import Cluster
from src.HeapElement import HeapElement
from src.edit_data import attribute_properties
from src.tree_functions import count_all_leaves, find_generalization, get_subtree, is_leaf_node, get_leaf_nodes

logging.basicConfig(filename='castle_algo_ILoss_k_20-50-100-200_32000__10000_50_current.log', level=logging.INFO)
logger = logging.getLogger()
class Castle:
    def __init__(self, stream, k, delta, beta, name_dataset):
        self.not_anonymized_clusters = set()
        self.anonymized_clusters = set()
        self.tao = 0
        self.beta = beta
        self.k = k
        self.stream = stream
        self.pos_stream = 0
        self.delta = delta
        self.anonymized_clusters_InfoLoss = []
        self.output = []
        self.name_dataset = name_dataset
        self.mu = 100
        self.output_anonym = []
        self.num_cluster= 0


    def set_pos_stream(self, pos_stream):
        self.pos_stream = pos_stream

    def castle_algo(self, S):
        logger.info(f'Starte Castle Algorithmus mit k={self.k}, delta={self.delta}, beta={self.beta}, name_dataset={self.name_dataset}, len_qi={len(S[0].qi)}, example_qi = {S[0].qi}, Anzahl anonyme CLuster: {len(self.anonymized_clusters)}, Anzahl nicht anonyme Cluster: {len(self.not_anonymized_clusters)}, Anzahl alle Cluster:{self.num_cluster}')
        while self.stream and self.pos_stream < len(self.stream):
            print("pos_stream", self.pos_stream)
            next_tupel = self.stream[self.pos_stream]  # Get the next tupel from S
            #print("____________________________________________________________________________________________________")
            #print("Tuple", next_tupel.qi)
            best_cluster = self.best_selection(next_tupel)
            if best_cluster is None:
                #print(f"best_cluster for {next_tupel.qi} is None")
                new_cluster = Cluster(next_tupel, self.name_dataset)
                self.not_anonymized_clusters.add(new_cluster)
                best_cluster = new_cluster
                #print(f"new cluster {new_cluster.t} added to not_anonymized_clusters")
            else:
                best_cluster.add_tupel(next_tupel)
                #print(f"tupel {next_tupel.qi} added to cluster {best_cluster.t}")

            if self.pos_stream - self.delta < 0:
                tuple_prime = None
            else:
                #print("Tuple_prime:", S[self.pos_stream - self.delta].qi)
                tuple_prime = S[self.pos_stream - self.delta]

            if tuple_prime not in self.output and tuple_prime is not None: #hier prüfen, ob es schon ausgegeben wurde
                self.delay_constraint(tuple_prime)

            self.pos_stream += 1
        logger.info(f'Castle Algorithmus beendet, Anzahl anonymisierte Cluster: {len(self.anonymized_clusters)}, Anzahl alle Cluster: {self.num_cluster}, kompletter Durchschnitt ILoss: {self.average_Loss_all()}, Durchschnittlicher ILoss letzte Cluster: {self.average_Loss()}')

    def delay_constraint(self, tuple_prime):
        #print('delay_constraint')
        #find tuple prime in not_anonymized_clusters
        cluster_of_tuple_prime = next(cluster for cluster in self.not_anonymized_clusters if cluster.check_if_tuple_is_in_cluster(tuple_prime))
        #if len(cluster_of_tuple_prime) >= self.k:
        if cluster_of_tuple_prime.is_k_anonymous(self.k):
            self.output_cluster(cluster_of_tuple_prime)
        elif self.get_num_of_all_pids() < self.k:
            self.suppress_tuple(tuple_prime)
            return
        else:
            KC_set = {cluster for cluster in self.anonymized_clusters if cluster.fits_in_cluster(tuple_prime.qi)}
            # prüfen ob KC_set nicht leer ist
            if KC_set:
                KC = random.choice(list(KC_set))
                self.output_anonymized_cluster(KC, tuple_prime)
                return
            m = 0
            for cluster in self.not_anonymized_clusters:
                if len(cluster_of_tuple_prime)<len(cluster):
                    m = m+1
            if m > (len(self.not_anonymized_clusters)/2):
                # suppress tuple prime
                #print("Suppress Tuple")
                self.suppress_tuple(tuple_prime)
                return
            if sum(len(cluster) for cluster in self.not_anonymized_clusters) < self.k:
                # suppress tuple prime
                self.suppress_tuple(tuple_prime)
                return
            # entfernt das beste Cluster aus den nicht anonymisierten Clustern um dann die merge Funktion aufrufen zu können
            clusters_without_best_cluster = copy.deepcopy(self.not_anonymized_clusters)

            for i in clusters_without_best_cluster:
                if i.check_cluster_if_equal(cluster_of_tuple_prime):
                    clusters_without_best_cluster.remove(i)
                    break
            MC = self.merge_cluster(cluster_of_tuple_prime, clusters_without_best_cluster)
            self.output_cluster(MC)


    def suppress_tuple(self, tuple):
        #print("Suppress Tuple", tuple.qi)
        self.stream.remove(tuple)
        self.pos_stream -= 1

    def get_num_of_all_pids(self):
        pids = set()
        for cluster in self.not_anonymized_clusters:
            for tupel in cluster.data:
                pids.add(tupel.pid)
        return len(pids)

    def output_anonymized_cluster(self, cluster, tuple):
        output = cluster.output_single_tuple(tuple)
        self.output.append(tuple)
        self.anonymized_clusters_InfoLoss.append(self.InfoLoss(output.qi))

    def output_cluster(self, cluster):
        #print("Output Cluster Funktion")
        num_pids = len(cluster.group_tuples_by_pid())
        if len(cluster) >= 2 * self.k  and num_pids >= 2*self.k:
            split_cluster = self.split(cluster)
            #self.not_anonymized_clusters.remove(cluster)
            for elem in split_cluster:
                self.not_anonymized_clusters.add(elem)
        else:
            split_cluster = {cluster}
        for c in split_cluster:
            output_tuples = c.output_tuples()
            self.output.extend(c.data)
            self.num_cluster += 1
            for tuple in output_tuples:
                self.output_anonym.append(tuple.qi)
                self.anonymized_clusters_InfoLoss.append(self.InfoLoss(tuple.qi))

            logger.info(f'Cluster veröffentlicht, Nummer Cluster: {self.num_cluster}, aktuelles pos_stream: {self.pos_stream}, Anzahl anonymisierte Cluster: {len(self.anonymized_clusters)}, Clustermuster: {c.t}, kompletter Durchschnittlicher ILoss: {self.average_Loss_all()}, Anzahl Tupel in Cluster:{len(c.data)} Durchschnittlicher ILoss letzte Cluster: {self.average_Loss()}, InfoLoss Clustermuster:{self.InfoLoss(c.t)} ')

            self.tao = self.average_Loss()
            if self.InfoLoss(c.t) < self.tao:
                self.anonymized_clusters.add(c)

                Info_Loss_anonymized_cluster = self.InfoLoss(c.t)
                """for _ in range(len(cluster.data)):
                    self.anonymized_clusters_InfoLoss.append(Info_Loss_anonymized_cluster)"""
                #self.anonymized_clusters_InfoLoss.append(Info_Loss_anonymized_cluster)
                logger.info(f'neues anonymisiertes Cluster: {c.t}')
            else:
                pass
            self.not_anonymized_clusters.remove(c)
        if (cluster in self.not_anonymized_clusters):
            self.not_anonymized_clusters.remove(cluster)


    def split(self, cluster):
        split_cluster = set()
        BS = cluster.group_tuples_by_pid()
        while len(BS) >= self.k:
            selected_bucket = random.choice(list(BS.keys()))
            selected_tuple = random.choice(BS[selected_bucket])
            new_cluster = Cluster(selected_tuple, self.name_dataset)

            # Lösche das ausgewählte Tupel aus BS
            BS[selected_bucket].remove(selected_tuple)
            if not BS[selected_bucket]:
                del BS[selected_bucket]

            heap = []
            for bucket in [b for b in BS if b != selected_bucket]:
                tuple_from_bucket = random.choice(BS[bucket])
                t_dist = self.calculate_tuple_distance(tuple_from_bucket, selected_tuple)
                heapq.heappush(heap, (t_dist, random.random(), tuple_from_bucket))
                while len(heap) > self.k - 1:
                    heapq.heappop(heap)
            for _,_, heap_element in heap:
                new_cluster.add_tupel(heap_element)
                BS[heap_element.pid].remove(heap_element)
                if not BS[heap_element.pid]:
                    del BS[heap_element.pid]
            split_cluster.add(new_cluster)
        for tup in sum(BS.values(), []):
            closest_cluster = min(split_cluster, key=lambda cluster: self.Enlargement(cluster, tup))
            closest_cluster.add_tupel(tup)
            BS[tup.pid].remove(tup)
        return split_cluster

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
            H.append(HeapElement(distance * (-1), node))

        # Heapfify ist eine Funktion, die eine Liste in-place in einen Heap umwandelt.
        heapq.heapify(H)

        return H

    def merge_cluster(self, cluster, set_of_clusters):
        #print("merge Cluster Funktion")
        # set_of clusters besteht aus non_anonymized_clusters
        #while len(cluster) < self.k or len(cluster.group_tuples_by_pid()) < self.k:
        is_cluster_k_ano = cluster.is_k_anonymous(self.k)
        while not is_cluster_k_ano:
            min_enlargement = float('inf')

            for c in set_of_clusters:
                # berechnung der potentiellen Größe des gemergeden Clusters
                merged_size = len(cluster) + len(c)

                # berechnung des Enlargement
                enlargement = self.Enlargement(cluster, c.make_tuple_from_qi(c.t))

                if enlargement < min_enlargement:
                    min_enlargement = enlargement
                    min_enlargement_cluster = c
            # fügt die Tupel des min_enlargement_cluster zu cluster hinzu
            for tupel in min_enlargement_cluster.data:
                cluster.add_tupel(tupel)

            for i in self.not_anonymized_clusters:
                if i.check_cluster_if_equal(min_enlargement_cluster):
                    self.not_anonymized_clusters.remove(i)
                    break

            for i in set_of_clusters:
                if i.check_cluster_if_equal(min_enlargement_cluster):
                    set_of_clusters.remove(i)
                    break

            is_cluster_k_ano = cluster.is_k_anonymous(self.k)
        self.not_anonymized_clusters.add(cluster)
        return cluster

    def best_selection(self, tuple)-> Cluster:
        #print("best selection Funktion")
        enlargements = set()
        if not self.not_anonymized_clusters:
            return None
        # Möglichkeit mit List-Comprehension darstellen:
        # enlargements = set([Enlargement(cluster, tuple) for cluster in not_anonymized_clusters])
        for cluster in self.not_anonymized_clusters:
            enlargement = self.Enlargement(cluster, tuple)
            enlargements.add(enlargement)
        min_enlargement = min(enlargements)

        # Set of clusters C' in not_anonymized_clusters with Enlargement(C', tupel) = min
        set_cluster_min = [C for C in self.not_anonymized_clusters if self.Enlargement(C, tuple) == min_enlargement]
        set_c_ok = set()
        for cluster in set_cluster_min:
            #IL_cluster = self.InfoLoss(cluster.t)
            IL_cluster = self.Enlargement(cluster, tuple)
            if IL_cluster <= self.tao:
                set_c_ok.add(cluster)
        if not set_c_ok:
            if len(self.not_anonymized_clusters) >= self.beta:
                return min(set_cluster_min, key=lambda cluster: len(cluster))
            else:
                return None
        else:
            return min(set_c_ok, key=lambda cluster: len(cluster))

    def Enlargement(self, cluster, tupel) -> float:
        """
          This function calculates the enlargement of a cluster C with respect to a tuple t.

          Args:
              cluster: A cluster represented as a list of tuples.
              tupel: A tuple.

          Returns:
              A number representing the enlargement of a cluster with respect to t.
          """
        n = len(cluster.t)  # Assuming all tuples in C have the same length
        enlarged_cluster = copy.deepcopy(cluster)
        enlarged_cluster.add_tupel(tupel)
        sum_iloss_cluster = 0
        sum_iloss_enlarged_cluster = 0

        # Calculate VInfoLoss for each attribute
        for i in range(n):
            info_loss_cluster = self.VInfoLoss(cluster.t[i], i)
            sum_iloss_cluster += info_loss_cluster
            info_loss_together = self.VInfoLoss(enlarged_cluster.t[i], i)
            sum_iloss_enlarged_cluster += info_loss_together

        return 1 / n * sum_iloss_enlarged_cluster - 1 / n * sum_iloss_cluster

    def InfoLoss(self, cluster):
        n = len(cluster)
        sum = 0
        for att_pos in range(n):
            sum += self.VInfoLoss(cluster[att_pos], att_pos)
        return 1 / n * sum

    def InfoLoss_tupel(self, tupel):
        n = len(tupel)
        sum = 0
        for att_pos in range(n):
            sum += self.VInfoLoss(tupel[att_pos], att_pos)
        return 1 / n * sum

    def InfoLoss_anonymized_cluster(self, clusters):
        for cluster in clusters:
            n = len(cluster.t)
            sum = 0
            for att_pos in range(n):
                sum += self.VInfoLoss(cluster.t[att_pos], att_pos)
            return 1 / n * sum



    def add_tupel(self, cluster, tupel):
        new_cluster = list(cluster)
        for i in range(len(cluster) - 1):
            if attribute_properties[self.name_dataset][i]['type'] == 'continuous':
                new_cluster[i] = self.adjust_interval(tupel[i], cluster[i])

            elif attribute_properties[self.name_dataset][i]['type'] == 'cathegorical':
                new_cluster[i] = self.add_unique_string_to_list(tupel[i], cluster[i])

        return tuple(new_cluster)

    def adjust_interval(self, value, interval):

        # Wenn value ein Intervall ist und Intervall nur eine Zahl (kann bei merge Cluster vorkommen
        if isinstance(value, (list, tuple)) and isinstance(interval, int):
            if value[0] > interval:
                return [interval, value[1]]
            elif value[1] < interval:
                return [value[0], interval]
            else:
                return value

        # wenn beides Intervalle sind
        if isinstance(value, (list, tuple)) and isinstance(interval, (list, tuple)):
            return [min(value[0], interval[0]), max(value[1], interval[1])]

        # Wenn das Intervall nur eine einzelne Zahl enthält
        if isinstance(interval, int) and isinstance(value, int):
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
        return value_list

    def is_in_interval(self, value, interval):
        lower_bound, upper_bound = interval
        return lower_bound <= value <= upper_bound

    def VInfoLoss(self, attribut, pos) -> int:
        info_loss = 0
        if attribute_properties[self.name_dataset][pos]['type'] == 'continuous':
            info_loss = self.VInfoLoss_continuos(attribut, attribute_properties[self.name_dataset][pos]['interval'])
        elif attribute_properties[self.name_dataset][pos]['type'] == 'cathegorical':
            info_loss = self.VInfoLoss_cathegorical(attribut, attribute_properties[self.name_dataset][pos]['hierarchy_tree'])
        return info_loss



    def VInfoLoss_continuos(self, attribut_range, domain_range):
        if isinstance(attribut_range, int):
            #return attribut_range / (domain_range[1] - domain_range[0])
            return 0
        if len(attribut_range) == 1:
            return 0
        return (attribut_range[1] - attribut_range[0]) / (domain_range[1] - domain_range[0])

    def VInfoLoss_cathegorical(self, attribut_range, domain_tree):
        domain_range = count_all_leaves(domain_tree)

        if isinstance(attribut_range, str):
            subtree = get_subtree(domain_tree, attribut_range)
            subtree_leaf = get_leaf_nodes(subtree)
            generalized_range = len(subtree_leaf)
            return (generalized_range - 1) / (domain_range - 1)
        else:
            attribute_range_generalized = find_generalization(domain_tree, attribut_range)
            generalized_range = count_all_leaves(get_subtree(domain_tree, attribute_range_generalized))
            erg = (generalized_range - 1) / (domain_range - 1)
            return erg


    def average_Loss(self):
        if len(self.anonymized_clusters_InfoLoss) == 0:
            return 0
        else:
            start_index = max(0, len(self.anonymized_clusters_InfoLoss) - self.mu)
            recent_elements = self.anonymized_clusters_InfoLoss[start_index:]

            return (1 / len(recent_elements)) * sum(recent_elements)


    def average_Loss_all(self):
        if len(self.anonymized_clusters_InfoLoss) == 0:
            return 0
        else:
            return (1/len(self.anonymized_clusters_InfoLoss)) * sum(self.anonymized_clusters_InfoLoss)
    def calculate_tuple_distance(self, tuple1, tuple2) -> float:
        num_diff = 0
        str_diff = 0
        for i in range(len(tuple1.qi)):
            if isinstance(tuple1.qi[i], int):
                num_diff += abs(tuple1.qi[i] - tuple2.qi[i])
            else:
                str_diff += 0 if tuple1.qi[i] == tuple2.qi[i] else 1
        return math.sqrt(num_diff ** 2 + str_diff ** 2) * (-1)

    def get_recent_InfoLoss(self):
        start_index = max(0, len(self.anonymized_clusters_InfoLoss) - self.mu)
        recent_info_loss = self.anonymized_clusters_InfoLoss[start_index:]
        return recent_info_loss


