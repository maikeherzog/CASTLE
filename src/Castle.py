from src.Cluster import Cluster
from src.edit_data import attribute_properties_test
from src.tree_functions import count_all_leaves, find_generalization, get_subtree


class Castle:
    def __init__(self, S, k, delta, beta):
        self.not_anonymized_clusters = set()
        self.anonymized_clusters = set()
        self.tao = 0
        self.beta = beta
        self.k = k
        self.S = S
        self.delta = delta

    def castle_algo(self):
        while self.S:
            next_tupel = self.S.pop()  # Get the next tupel from S
            print("pos:", next_tupel[0])
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

            """if next_tupel[0] - delta < 0:
                tuple_prime = None
            else:
                tuple_prime = S[next_tupel[0] - delta]
            if tuple_prime not in anonymized_clusters:
                delay_constraint(tuple_prime, best_cluster, k)"""

    def delay_constraint(self, tuple_prime, best_cluster):
        # ich übergebe das bestpasssende cluster, dann muss ich es nicht erst neu berechnen
        if len(best_cluster) < self.k:
            return
        pass

    def output_cluster(self, cluster):
        if len(cluster) >= 2 * self.k:
            split_cluster = self.split(cluster)
        else:
            split_cluster = {cluster}
        for cluster in split_cluster:
            cluster.output_tuples()
            # TODO: was soll ich hier übergeben?
            # tao = average_Loss()
            if self.InfoLoss(cluster.t) >= self.tao:
                self.anonymized_clusters.add(cluster)
                # Muss das noch aus den nicht anonymisierten Clustern entfernt werden? Bzw. Müssen die Tuple entfernt werden?
                # not_anonymized_clusters.remove(cluster)
            else:
                # TODO: stimmt das hier so, dass das da entfern werden soll?
                del cluster
                # not_anonymized_clusters.remove(cluster)
            self.not_anonymized_clusters.remove(cluster)

    def split(self, cluster):
        split_cluster = set()
        # TODO: implementieren

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

    def average_Loss(self, stream, position):
        sum = 0
        for tuple in stream and tuple[0] < position:
            sum += self.InfoLoss(tuple)
        return 1 / position * sum