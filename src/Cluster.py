import copy

from src.Tupel import Tuple
from src.edit_data import attribute_properties
from src.tree_functions import find_generalization


class Cluster:
    """
    A class to represent a cluster of tuples.
    """
    def __init__(self, t, name_dataset):
        """
        Constructor of the Cluster class.
        :param t (tuple): the tuple representing the cluster  (cluster pattern)
        :param t (Tuple): tuple used to create the cluster
        :param name_dataset (str): name of the dataset
        """
        self.t = t.qi
        self.data = [t]
        self.name_dataset = name_dataset

    def __len__(self):
        """
        Returns the number of tuples in the cluster.
        :return: the number of tuples in the cluster
        """
        return len(self.data)

    def make_tuple_from_qi(self, qi):
      """
      Creates a tuple from the quasi-identifiers.
      :param qi (tuple): the quasi-identifiers
      :return: the tuple
      """
      new_tuple = Tuple(0, 0, qi, ())
      return new_tuple

    def fits_in_cluster(self, tuple_prime):
        """
        Checks if the tuple fits in the cluster.
        :param tuple_prime (Tuple): the tuple to check
        :return: True if the tuple fits in the cluster, False otherwise
        """
        for i in range(len(self.t)):
          if attribute_properties[self.name_dataset][i]['type'] == 'continuous':
            if tuple_prime[i] < self.t[i][0] or tuple_prime[i] > self.t[i][1]:
              return False

          elif attribute_properties[self.name_dataset][i]['type'] == 'cathegorical':
            if tuple_prime[i] not in self.t[i]:
              return False

        return True
    def add_tupel(self, t):
        """
        Adds a tuple to the cluster.
        :param t (Tuple): the tuple to add
        :return: None
        """
        self.data.append(t)
        cluster = list(self.t)
        for i in range(len(cluster)):
            if attribute_properties[self.name_dataset][i]['type'] == 'continuous':
              cluster[i] = self.adjust_interval(t.qi[i], cluster[i])

            elif attribute_properties[self.name_dataset][i]['type'] == 'cathegorical':
                cluster[i] = self.add_unique_string_to_list(t.qi[i], cluster[i])
        self.t = tuple(cluster)

    def adjust_interval(self, value, interval):
        """
        Adjusts the interval to include the value.
        :param value (int or list or tuple): the value to include
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

        # both are intervals
        if isinstance(value, (list, tuple)) and isinstance(interval, (list, tuple)):
          return [min(value[0], interval[0]), max(value[1], interval[1])]

        # Interval only contains a single number
        if isinstance(interval, int) and isinstance(value, int):
          if value < interval:
            return [value, interval]
          else:
            return [interval, value]

        # If the interval is a normal range
        else:
          lower_bound, upper_bound = interval

          if value <= lower_bound:
            lower_bound = value
          elif value > upper_bound:
            upper_bound = value

          return [lower_bound, upper_bound]

    def add_unique_string_to_list(self, value, value_list):
        """
        Adds a unique string to a list.
        :param value (str or list): the value to add
        :param value_list (str or list): the list to add the value to
        :return: the list with the added value
        """
        # If value_list is a string, we turn it into a list
        if isinstance(value_list, str):
            value_list = [value_list]

        # If the value is a list, we add each unique element
        if isinstance(value, list):
            for item in value:
              if item not in value_list:
                value_list.append(item)

        # If the value is a string and is not in the list, we add it
        elif value not in value_list:
            value_list.append(value)

        return value_list

    def check_cluster_if_equal(self, cluster):
        """
        Checks if two clusters are equal.
        :param cluster (Cluster): the cluster to compare with
        :return: True if the clusters are equal, False otherwise
        """
        if len(self.t) != len(cluster.t):
            return False

        for i in range(len(self.t)):
            if self.t[i] != cluster.t[i]:
              return False

        return True

    def is_k_anonymous(self, k):
        """
        Checks if the cluster is k-anonymous.
        :param k (int): the value of k
        :return: True if the cluster is k-anonymous, False otherwise
        """
        if len(self.data) < k or len(self.group_tuples_by_pid()) < k:
            return False
        else:
            return True

    def group_tuples_by_pid(self):
        """
        Groups the tuples in the cluster by their person-ID.
        :return: a dictionary with the person-ID as key and the list of tuples as value
        """
        grouped_data = dict()
        for tupel in self.data:
            pid = tupel.pid
            if pid in grouped_data:
                grouped_data[pid].append(tupel)
            else:
                grouped_data[pid] = [tupel]
        return grouped_data


    def output_tuples(self):
        """
        Outputs the tuples in the cluster.
        :return: a generalized list of tuples from the cluster
        """
        generalized_tupels = []
        for tupel in self.data:
          copied_tuple = copy.copy(tupel)
          qi_generalized = self.set_qi_generalized(self.t)
          copied_tuple.set_qi(qi_generalized)
          generalized_tupels.append(copied_tuple)
        return generalized_tupels

    def output_single_tuple(self, tuple):
        """
        Outputs a single tuple from the cluster.
        :param tuple:
        :return: a generalized tuple from the cluster
        """
        copied_tuple = copy.copy(tuple)
        qi_generalized = self.set_qi_generalized(self.t)
        copied_tuple.set_qi(qi_generalized)
        return copied_tuple

    def set_qi_generalized(self, qi):
        """
        Generalizes the quasi-identifiers.
        :param qi (tuple): the quasi-identifiers
        :return: the generalized quasi-identifiers
        """
        qi = list(qi)
        for pos in range(len(qi)):
            if attribute_properties[self.name_dataset][pos]['type'] == 'cathegorical':
              qi[pos] = find_generalization(attribute_properties[self.name_dataset][pos]['hierarchy_tree'], qi[pos])
        return tuple(qi)

    def check_if_tuple_is_in_cluster(self, tuple):
        """
        Checks if a tuple is in the cluster.
        :param tuple (Tuple): the tuple to check
        :return: True if the tuple is in the cluster, False otherwise
        """
        for t in self.data:
            if t == tuple:
              return True
        return False