import copy
import heapq
import math
import random
import logging

from src.Cluster import Cluster
from src.HeapElement import HeapElement
from src.edit_data import attribute_properties
from src.tree_functions import count_all_leaves, find_generalization, get_subtree, is_leaf_node, get_leaf_nodes

# config for logger
logging.basicConfig(filename='castle_algo_ILoss_qi_2-10__32000__10000_50_adult_mix_reverse.log', level=logging.INFO)
logger = logging.getLogger()
class Castle:
    """
    A class to represent the Castle algorithm.
    """
    def __init__(self, stream, k, delta, beta, name_dataset):
        """
        Constructor of the Castle class.
        :param stream (list of Tuple): the stream of tuples
        :param k (int): the k-anonymity parameter
        :param delta (int): the delay constraint
        :param beta (int): Threshold for non-annonymous clusters
        :param name_dataset (str): the name of the dataset

        :return: list of anonymized tuples
        """
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
        self.all_cluster_Iloss = []
        self.anonymized_clusters_InfoLoss_only_cluster = []


    def set_pos_stream(self, pos_stream):
        """
        Sets the position of the stream.
        :param pos_stream (int): the position of the stream
        """
        self.pos_stream = pos_stream

    def castle_algo(self, S):
        """
        The Castle algorithm.
        :param S (list of Tuple): the stream of tuples
        :return: None
        """
        # logging before
        logger.info(f'Starte Castle Algorithmus mit k={self.k}, delta={self.delta}, beta={self.beta}, name_dataset={self.name_dataset}, len_qi={len(S[0].qi)}, example_qi = {S[0].qi}, Anzahl anonyme CLuster: {len(self.anonymized_clusters)}, Anzahl nicht anonyme Cluster: {len(self.not_anonymized_clusters)}, Anzahl alle Cluster:{self.num_cluster}')
        while self.stream and self.pos_stream < len(self.stream):
            print("pos_stream", self.pos_stream)
            next_tupel = self.stream[self.pos_stream]  # Get the next tupel from S

            # Find the best matching cluster for the current tuple
            best_cluster = self.best_selection(next_tupel)
            if best_cluster is None:
                # If no suitable cluster is found, create a new cluster for this tuple
                new_cluster = Cluster(next_tupel, self.name_dataset)
                self.not_anonymized_clusters.add(new_cluster)
                best_cluster = new_cluster
            else:
                # If a suitable cluster is found, add the tuple to this cluster
                best_cluster.add_tupel(next_tupel)

            # Handle delay constraint: check if the tuple at (current position - delta) should be processed
            if self.pos_stream - self.delta < 0:
                tuple_prime = None
            else:
                tuple_prime = S[self.pos_stream - self.delta]

            # If the tuple_prime exists and hasn't been output yet, apply the delay constraint
            if tuple_prime not in self.output and tuple_prime is not None:
                self.delay_constraint(tuple_prime)

            # Move to the next position in the stream
            self.pos_stream += 1
        #logging after
        logger.info(f'Castle Algorithmus beendet, Anzahl anonymisierte Cluster: {len(self.anonymized_clusters)}, Anzahl alle Cluster: {self.num_cluster}, kompletter Durchschnitt ILoss: {self.average_Loss_all()}, Durchschnittlicher ILoss letzte Cluster: {self.average_Loss()}, Durchschnittlicher ILoss über Cluster:{self.average_loss_all_clusters()}, InfoLoss anonymisierte Cluster: {self.average_Loss_all_ano_cluster()}')
        return self.output_anonym

    def delay_constraint(self, tuple_prime):
        """
        The delay constraint.
        :param tuple_prime (Tuple): the tuple to check
        """
        #find tuple prime in not_anonymized_clusters
        cluster_of_tuple_prime = next(cluster for cluster in self.not_anonymized_clusters if cluster.check_if_tuple_is_in_cluster(tuple_prime))

        # If the cluster containing tuple_prime is k-anonymous, output this cluster
        if cluster_of_tuple_prime.is_k_anonymous(self.k):
            self.output_cluster(cluster_of_tuple_prime)
        elif self.get_num_of_all_pids() < self.k:
            # If the number of all PIDs is less than k, suppress the tuple
            self.suppress_tuple(tuple_prime)
            return
        else:
            # Find all anonymized clusters that the tuple can fit into based on its QIs
            KC_set = {cluster for cluster in self.anonymized_clusters if cluster.fits_in_cluster(tuple_prime.qi)}
            # check whether KC_set is not empty
            if KC_set:
                KC = random.choice(list(KC_set))
                self.output_anonymized_cluster(KC, tuple_prime)
                logger.info(f'Tuple Prime {tuple_prime.qi} in anonymisiertes Cluster {KC.t} eingefügt')
                return
            m = 0
            for cluster in self.not_anonymized_clusters:
                if len(cluster_of_tuple_prime)<len(cluster):
                    m = m+1
            if m > (len(self.not_anonymized_clusters)/2):
                # suppress tuple prime
                self.suppress_tuple(tuple_prime)
                return
            if sum(len(cluster) for cluster in self.not_anonymized_clusters) < self.k:
                # suppress tuple prime
                self.suppress_tuple(tuple_prime)
                return
            # removes the best cluster from the non-anonymised clusters in order to be able to call the merge function
            clusters_without_best_cluster = copy.deepcopy(self.not_anonymized_clusters)

            for i in clusters_without_best_cluster:
                if i.check_cluster_if_equal(cluster_of_tuple_prime):
                    clusters_without_best_cluster.remove(i)
                    break

            # Merge the remaining non-anonymized clusters with the cluster containing tuple_prime
            MC = self.merge_cluster(cluster_of_tuple_prime, clusters_without_best_cluster)
            self.output_cluster(MC)


    def suppress_tuple(self, tuple):
        """
        Suppresses a tuple.
        :param tuple (Tuple): the tuple to suppress
        """
        self.stream.remove(tuple)
        self.pos_stream -= 1

    def get_num_of_all_pids(self):
        """
        Get the amount of all person-IDs in the stream.
        :return: the number of all person-IDs in the stream
        """
        pids = set()
        for cluster in self.not_anonymized_clusters:
            for tupel in cluster.data:
                pids.add(tupel.pid)
        return len(pids)

    def output_anonymized_cluster(self, cluster, tuple):
        """
        Outputs a tuple from an anonymized cluster.
        :param cluster (Cluster): cluster for tuple
        :param tuple (Tuple): the tuple to output
        """
        output = cluster.output_single_tuple(tuple)
        self.output.append(tuple)
        self.anonymized_clusters_InfoLoss.append(self.InfoLoss(output.qi))

    def output_cluster(self, cluster):
        """
        Outputs a cluster.
        :param cluster (Cluster): the cluster to output
        """
        # Get the number of unique PIDs in the cluster
        num_pids = len(cluster.group_tuples_by_pid())

        # Check if the cluster size and number of PIDs meet the threshold to potentially split the cluster
        if len(cluster) >= 2 * self.k  and num_pids >= 2*self.k:
            split_cluster = self.split(cluster)
            # Add the resulting clusters to the set of non-anonymized clusters
            for elem in split_cluster:
                self.not_anonymized_clusters.add(elem)
        else:
            # If the conditions for splitting are not met, treat the cluster as a single unit
            split_cluster = {cluster}

        # Process and output each cluster in the split_clusters set
        for c in split_cluster:
            output_tuples = c.output_tuples()
            self.output.extend(c.data)
            self.num_cluster += 1
            for tuple in output_tuples:
                self.output_anonym.append(tuple.qi)
                self.anonymized_clusters_InfoLoss.append(self.InfoLoss(tuple.qi))

            logger.info(f'Cluster veröffentlicht, Nummer Cluster: {self.num_cluster}, aktuelles pos_stream: {self.pos_stream}, Anzahl anonymisierte Cluster: {len(self.anonymized_clusters)}, Clustermuster: {c.t}, kompletter Durchschnittlicher ILoss: {self.average_Loss_all()}, Anzahl Tupel in Cluster:{len(c.data)} Durchschnittlicher ILoss letzte Cluster: {self.average_Loss()}, InfoLoss Clustermuster:{self.InfoLoss(c.t)} ')
            self.all_cluster_Iloss.append(self.InfoLoss(c.t))

            # Update the average information loss and check if the current cluster's information loss is less than the average
            self.tao = self.average_Loss()
            if self.InfoLoss(c.t) < self.tao:
                self.anonymized_clusters.add(c)

                Info_Loss_anonymized_cluster = self.InfoLoss(c.t)
                """for _ in range(len(cluster.data)):
                    self.anonymized_clusters_InfoLoss.append(Info_Loss_anonymized_cluster)"""
                self.anonymized_clusters_InfoLoss_only_cluster.append(self.InfoLoss(c.t))
                logger.info(f'neues anonymisiertes Cluster: {c.t}')
            else:
                pass
            self.not_anonymized_clusters.remove(c)

        # Ensure the cluster is removed from the non-anonymized clusters set
        if (cluster in self.not_anonymized_clusters):
            self.not_anonymized_clusters.remove(cluster)


    def split(self, cluster):
        """
        Splits a cluster.
        :param cluster (Cluster): the cluster to split
        :return: list of split clusters
        """
        split_cluster = set()

        # Group the tuples in the cluster by their PID (personal identifier)
        BS = cluster.group_tuples_by_pid()

        # While there are enough tuples in BS to potentially form new clusters
        while len(BS) >= self.k:
            # Randomly select a bucket (PID group) and a tuple from it
            selected_bucket = random.choice(list(BS.keys()))
            selected_tuple = random.choice(BS[selected_bucket])
            # Create a new cluster with the selected tuple
            new_cluster = Cluster(selected_tuple, self.name_dataset)

            BS[selected_bucket].remove(selected_tuple)
            if not BS[selected_bucket]:
                del BS[selected_bucket]

            # Create a heap to find the nearest tuples to the selected tuple
            heap = []
            for bucket in [b for b in BS if b != selected_bucket]:
                tuple_from_bucket = random.choice(BS[bucket])
                t_dist = self.calculate_tuple_distance(tuple_from_bucket, selected_tuple)
                heapq.heappush(heap, (t_dist, random.random(), tuple_from_bucket))
                while len(heap) > self.k - 1:
                    heapq.heappop(heap)

            # Add the tuples from the heap to the new cluster
            for _,_, heap_element in heap:
                new_cluster.add_tupel(heap_element)
                BS[heap_element.pid].remove(heap_element)
                if not BS[heap_element.pid]:
                    del BS[heap_element.pid]
            # Add the newly formed cluster to the set of split clusters
            split_cluster.add(new_cluster)

        for tup in sum(BS.values(), []):
            closest_cluster = min(split_cluster, key=lambda cluster: self.Enlargement(cluster, tup))
            closest_cluster.add_tupel(tup)
            BS[tup.pid].remove(tup)
        return split_cluster

    def initialize_heap(self, tuple):
        """
        Initializes the heap.
        :param tuple (Tuple): the tuple to initialize the heap
        :return: the heap
        """
        H = []
        for _ in range(self.k - 1):
            node = len(H)
            distance = float('inf')
            H.append(HeapElement(distance * (-1), node))
        heapq.heapify(H)
        return H

    def merge_cluster(self, cluster, set_of_clusters):
        """
        Merges a cluster with another cluster.
        :param cluster (Cluster): the cluster to merge
        :param set_of_clusters (set of Cluster): the set of other clusters for merge options
        :return: the merged cluster
        """
        # Check if the given cluster is already k-anonymous
        is_cluster_k_ano = cluster.is_k_anonymous(self.k)

        # Continue merging until the cluster is k-anonymous
        while not is_cluster_k_ano:
            min_enlargement = float('inf')
            # Iterate through the set of clusters to find the best cluster to merge with
            for c in set_of_clusters:
                # Calculation of the potential size of the merged cluster
                merged_size = len(cluster) + len(c)

                enlargement = self.Enlargement(cluster, c.make_tuple_from_qi(c.t))

                # Update the minimum enlargement and corresponding cluster if a better option is found
                if enlargement < min_enlargement:
                    min_enlargement = enlargement
                    min_enlargement_cluster = c
            # adds the tuples of the min_enlargement_cluster to cluster
            for tupel in min_enlargement_cluster.data:
                cluster.add_tupel(tupel)

            # Remove the merged cluster from the set of non-anonymized clusters
            for i in self.not_anonymized_clusters:
                if i.check_cluster_if_equal(min_enlargement_cluster):
                    self.not_anonymized_clusters.remove(i)
                    break

            for i in set_of_clusters:
                if i.check_cluster_if_equal(min_enlargement_cluster):
                    set_of_clusters.remove(i)
                    break

            is_cluster_k_ano = cluster.is_k_anonymous(self.k)
        return cluster

    def best_selection(self, tuple)-> Cluster:
        """
        Selects the best cluster for a tuple.
        :param tuple (Tuple): the tuple to select the best cluster
        :return: the best cluster
        """
        enlargements = set()

        # If there are no non-anonymized clusters, return None
        if not self.not_anonymized_clusters:
            return None

        # Calculate the enlargement for each non-anonymized cluster
        for cluster in self.not_anonymized_clusters:
            enlargement = self.Enlargement(cluster, tuple)
            enlargements.add(enlargement)

        # Find the minimum enlargement value
        min_enlargement = min(enlargements)
        # Find clusters that have the minimum enlargement value
        set_cluster_min = [C for C in self.not_anonymized_clusters if self.Enlargement(C, tuple) == min_enlargement]
        set_c_ok = set()
        for cluster in set_cluster_min:
            IL_cluster = self.Enlargement(cluster, tuple)
            if IL_cluster <= self.tao:
                set_c_ok.add(cluster)

        # If no cluster meets the InfoLoss criteria, select the cluster with the smallest size if there are enough clusters
        if not set_c_ok:
            if len(self.not_anonymized_clusters) >= self.beta:
                return min(set_cluster_min, key=lambda cluster: len(cluster))
            else:
                return None
        else:
            return min(set_c_ok, key=lambda cluster: len(cluster))

    def Enlargement(self, cluster, tupel):
        """
        Calculates the enlargement of a cluster.
        :param cluster (Cluster): the cluster to calculate the enlargement
        :param tupel (Tuple): the tuple to be inserted
        :return: the enlargement of the cluster
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
        """
        Calculates the InfoLoss of a cluster.
        :param cluster (Cluster): the cluster to calculate the InfoLoss
        :return: the InfoLoss of the cluster
        """
        n = len(cluster)
        sum = 0
        for att_pos in range(n):
            sum += self.VInfoLoss(cluster[att_pos], att_pos)
        return 1 / n * sum

    def InfoLoss_tupel(self, tupel):
        """
        Calculates the InfoLoss of a tuple.
        :param tupel (Tuple): the tuple to calculate the InfoLoss
        :return: the InfoLoss of the tuple
        """
        n = len(tupel)
        sum = 0
        for att_pos in range(n):
            sum += self.VInfoLoss(tupel[att_pos], att_pos)
        return 1 / n * sum

    def InfoLoss_anonymized_cluster(self, clusters):
        """
        Calculates the InfoLoss of an anonymized cluster.
        :param clusters (set of Cluster): the cluster to calculate the InfoLoss
        :return: the InfoLoss of the cluster
        """
        for cluster in clusters:
            n = len(cluster.t)
            sum = 0
            for att_pos in range(n):
                sum += self.VInfoLoss(cluster.t[att_pos], att_pos)
            return 1 / n * sum



    def add_tupel(self, cluster, tupel):
        """
        Adds a tuple to a cluster.
        :param cluster (Cluster): the cluster to add the tuple
        :param tupel (Tuple): the tuple to add
        """
        new_cluster = list(cluster)
        for i in range(len(cluster) - 1):
            if attribute_properties[self.name_dataset][i]['type'] == 'continuous':
                new_cluster[i] = self.adjust_interval(tupel[i], cluster[i])

            elif attribute_properties[self.name_dataset][i]['type'] == 'categorical':
                new_cluster[i] = self.add_unique_string_to_list(tupel[i], cluster[i])

        return tuple(new_cluster)

    def adjust_interval(self, value, interval):
        """
        Adjusts an interval.
        :param value (int or list or tuple): the value to adjust
        :param interval (int or list or tuple): the interval to adjust
        :return: the adjusted interval
        """
        # If value is an interval and interval is a number
        if isinstance(value, (list, tuple)) and isinstance(interval, int):
            if value[0] > interval:
                return [interval, value[1]]
            elif value[1] < interval:
                return [value[0], interval]
            else:
                return value

        # if both are intervals
        if isinstance(value, (list, tuple)) and isinstance(interval, (list, tuple)):
            return [min(value[0], interval[0]), max(value[1], interval[1])]

        # If the interval only contains a single number
        if isinstance(interval, int) and isinstance(value, int):
            if value < interval:
                return [value, interval]
            else:
                return [interval, value]

        # If the interval is a normal range
        else:
            lower_bound, upper_bound = interval

            if value < lower_bound:
                lower_bound = value
            elif value > upper_bound:
                upper_bound = value

            return [lower_bound, upper_bound]

    def add_unique_string_to_list(self, value, value_list):
        """
        Adds a unique string to a list.
        :param value (str): the value to add
        :param value_list (list): the list to add the value
        :return: the list with the added value
        """
        if value not in value_list:
            value_list.append(value)
        return value_list

    def is_in_interval(self, value, interval):
        """
        Checks if a value is in an interval.
        :param value (int): the value to check
        :param interval (list or tuple): the interval to check
        :return: True if the value is in the interval, False otherwise
        """
        lower_bound, upper_bound = interval
        return lower_bound <= value <= upper_bound

    def VInfoLoss(self, attribut, pos):
        """
        Calculates the VInfoLoss of an attribute.
        :param attribut: attribute to calculate the VInfoLoss
        :param pos (int): the position of the attribute
        :return: the VInfoLoss of the attribute
        """
        info_loss = 0
        if attribute_properties[self.name_dataset][pos]['type'] == 'continuous':
            info_loss = self.VInfoLoss_continuos(attribut, attribute_properties[self.name_dataset][pos]['interval'])
        elif attribute_properties[self.name_dataset][pos]['type'] == 'categorical':
            info_loss = self.VInfoLoss_categorical(attribut, attribute_properties[self.name_dataset][pos]['hierarchy_tree'])
        return info_loss



    def VInfoLoss_continuos(self, attribut_range, domain_range):
        """
        Calculates the VInfoLoss of a continuous attribute.
        :param attribut_range (int or list): the range of the attribute
        :param domain_range (list): the range of the domain
        :return: the VInfoLoss of the continuous attribute
        """
        if isinstance(attribut_range, int):
            return 0
        if len(attribut_range) == 1:
            return 0
        return (attribut_range[1] - attribut_range[0]) / (domain_range[1] - domain_range[0])

    def VInfoLoss_categorical(self, attribut_range, domain_tree):
        """
        Calculates the VInfoLoss of a categorical attribute.
        :param attribut_range (str or list): the range of the attribute
        :param domain_tree (dict): the domain tree
        :return: the VInfoLoss of the categorical attribute
        """
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
        """
        Calculates the average loss.
        :return: the average loss over the last clusters
        """
        if len(self.anonymized_clusters_InfoLoss) == 0:
            return 0
        else:
            start_index = max(0, len(self.anonymized_clusters_InfoLoss) - self.mu)
            recent_elements = self.anonymized_clusters_InfoLoss[start_index:]

            return (1 / len(recent_elements)) * sum(recent_elements)


    def average_Loss_all(self):
        """
        Calculates the average loss over all anonymized clusters.
        :return: the average loss
        """
        if len(self.anonymized_clusters_InfoLoss) == 0:
            return 0
        else:
            return (1/len(self.anonymized_clusters_InfoLoss)) * sum(self.anonymized_clusters_InfoLoss)

    def average_loss_all_clusters(self):
        """
        Calculates the average loss over all clusters.
        :return: the average loss
        """
        if len(self.all_cluster_Iloss) == 0:
            return 0
        else:
            return (1/len(self.all_cluster_Iloss)) * sum(self.all_cluster_Iloss)
    def calculate_tuple_distance(self, tuple1, tuple2):
        """
        Calculates the distance between two tuples.
        :param tuple1 (Tuple): the first tuple
        :param tuple2 (Tuple): the second tuple
        :return: the distance between the two tuples
        """
        num_diff = 0
        str_diff = 0
        for i in range(len(tuple1.qi)):
            if isinstance(tuple1.qi[i], int):
                num_diff += abs(tuple1.qi[i] - tuple2.qi[i])
            else:
                str_diff += 0 if tuple1.qi[i] == tuple2.qi[i] else 1
        return math.sqrt(num_diff ** 2 + str_diff ** 2) * (-1)

    def get_recent_InfoLoss(self):
        """
        Gets the recent InfoLoss.
        :return: the recent InfoLoss
        """
        start_index = max(0, len(self.anonymized_clusters_InfoLoss) - self.mu)
        recent_info_loss = self.anonymized_clusters_InfoLoss[start_index:]
        return recent_info_loss

    def average_Loss_all_ano_cluster(self):
        """
        Calculates the average loss over all anonymized clusters.
        :return: the average loss over all anonymized clusters
        """
        if len(self.anonymized_clusters_InfoLoss_only_cluster) == 0:
            return 0
        else:
            return (1/len(self.anonymized_clusters_InfoLoss_only_cluster)) * sum(self.anonymized_clusters_InfoLoss_only_cluster)


