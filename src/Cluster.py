import copy

from src.Tupel import Tuple
from src.edit_data import attribute_properties
from src.tree_functions import find_generalization


class Cluster:
  """
  Ein k-anonymisierter Cluster.

  Args:
    t: Der erste Datensatz des Clusters.
  """

  def __init__(self, t, name_dataset):
    self.t = t.qi
    self.data = [t]
    self.name_dataset = name_dataset

  def __len__(self):
    """
    Gibt die Anzahl der Datensätze in diesem Cluster zurück.
    """

    return len(self.data)

  def __str__(self):
    return str(self.t) + ', ' + ', '.join(str(t) for t in self.data[1:])


  def make_tuple_from_qi(self, qi):
    new_tuple = Tuple(0, 0, qi, ())
    return new_tuple

  # schaut, ob ein Tupel in das Cluster passt
  def fits_in_cluster(self, tuple_prime):
    # Implementierungsabhängig. Die aus der Beschreibung zu entnehmende Anforderung
    # ist, dass tuple_prime zu allen Tupeln in cluster.data passt.
    #print("Tuple:", tuple_prime, "Cluster:", self.t)
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
    Fügt einen Datensatz zum Cluster hinzu.

    Args:
      t: Der Datensatz.
    """

    self.data.append(t)
    cluster = list(self.t)
    for i in range(len(cluster)):
        if attribute_properties[self.name_dataset][i]['type'] == 'continuous':
          #print("Tuple:", t.qi[i], "Cluster:", cluster[i])
          cluster[i] = self.adjust_interval(t.qi[i], cluster[i])

        elif attribute_properties[self.name_dataset][i]['type'] == 'cathegorical':
            cluster[i] = self.add_unique_string_to_list(t.qi[i], cluster[i])
    self.t = tuple(cluster)

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

      if value <= lower_bound:
        lower_bound = value
      elif value > upper_bound:
        upper_bound = value

      return [lower_bound, upper_bound]

  def add_unique_string_to_list(self, value, value_list):
    # Falls value_list ein String ist, machen wir daraus eine Liste
    if isinstance(value_list, str):
      value_list = [value_list]

    # Wenn der Wert eine Liste ist, fügen wir jedes eindeutige Element hinzu
    if isinstance(value, list):
      for item in value:
        if item not in value_list:
          value_list.append(item)

    # Wenn der Wert ein String ist und nicht in der Liste ist, fügen wir ihn hinzu
    elif value not in value_list:
      value_list.append(value)

    return value_list

  def check_cluster_if_equal(self, cluster):
    if len(self.t) != len(cluster.t):
      return False

    for i in range(len(self.t)):
      if self.t[i] != cluster.t[i]:
        return False

    return True

  def is_k_anonymous(self, k):
    """
    Überprüft, ob der Cluster k-anonym ist.

    Args:
      k: Der Anonymisierungsgrad.
      δ: Der Datenschutzparameter.
      β: Der Genauigkeitsparameter.

    Returns:
      `True`, wenn der Cluster k-anonym ist, sonst `False`.
    """

    if len(self.data) < k or len(self.group_tuples_by_pid()) < k:
      return False
    else:
      return True

  def group_tuples_by_pid(self) -> dict:
      grouped_data = dict()
      for tupel in self.data:
          pid = tupel.pid
          if pid in grouped_data:
              grouped_data[pid].append(tupel)
          else:
              grouped_data[pid] = [tupel]
      return grouped_data


  def output_tuples(self) -> list:
      generalized_tupels = []
      for tupel in self.data:
        copied_tuple = copy.copy(tupel)
        qi_generalized = self.set_qi_generalized(self.t)
        copied_tuple.set_qi(qi_generalized)
        generalized_tupels.append(copied_tuple)
      return generalized_tupels

  def set_qi_generalized(self, qi):
    #print("QI:", qi)
    qi = list(qi)
    for pos in range(len(qi)):
      if attribute_properties[self.name_dataset][pos]['type'] == 'cathegorical':
        qi[pos] = find_generalization(attribute_properties[self.name_dataset][pos]['hierarchy_tree'], qi[pos])
    return tuple(qi)

  def update(self, tuples):
    for tuple in tuples:
      self.add_tupel(tuple)

  def check_if_tuple_is_in_cluster(self, tuple):
    for t in self.data:
      if t == tuple:
        return True
    return False