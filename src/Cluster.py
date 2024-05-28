from src.edit_data import attribute_properties_test


class Cluster:
  """
  Ein k-anonymisierter Cluster.

  Args:
    t: Der erste Datensatz des Clusters.
  """

  def __init__(self, t):
    self.t = t
    self.data = [t]

  def __len__(self):
    """
    Gibt die Anzahl der Datensätze in diesem Cluster zurück.
    """

    return len(self.data)

  def __str__(self):
    return str(self.t) + ', ' + ', '.join(str(t) for t in self.data[1:])


  # schaut, ob ein Tupel in das Cluster passt
  def fits_in_cluster(self, tuple_prime):
    # Implementierungsabhängig. Die aus der Beschreibung zu entnehmende Anforderung
    # ist, dass tuple_prime zu allen Tupeln in cluster.data passt.
    for i in range(len(self.t)):
      if attribute_properties_test[i]['type'] == 'continuous':
        if tuple_prime[i] < self.t[i][0] or tuple_prime[i] > self.t[i][1]:
          return False

      elif attribute_properties_test[i]['type'] == 'cathegorical':
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
    for i in range(len(self.t)):
        if attribute_properties_test[i]['type'] == 'continuous':
            cluster[i] = self.adjust_interval(t[i], cluster[i])

        elif attribute_properties_test[i]['type'] == 'cathegorical':
            cluster[i] = self.add_unique_string_to_list(t[i], cluster[i])
    self.t = tuple(cluster)

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
    # Falls value_list ein String ist, machen wir daraus eine Liste
    if isinstance(value_list, str):
      value_list = [value_list]

    if value not in value_list:
      value_list.append(value)
    return value_list


  def is_k_anonymous(self, k, δ, β):
    """
    Überprüft, ob der Cluster k-anonym ist.

    Args:
      k: Der Anonymisierungsgrad.
      δ: Der Datenschutzparameter.
      β: Der Genauigkeitsparameter.

    Returns:
      `True`, wenn der Cluster k-anonym ist, sonst `False`.
    """

    # TODO: Implementieren Sie die Prüfung der k-Anonymität

    return True

  def can_add(self, t):
    """
    Überprüft, ob der Datensatz `t` zum Cluster hinzugefügt werden kann.

    Args:
      t: Der Datensatz.

    Returns:
      `True`, wenn der Datensatz hinzugefügt werden kann, sonst `False`.
    """

    # TODO: Implementieren Sie die Prüfung, ob der Datensatz hinzugefügt werden kann

    return True

  def output_tuples(self):
    for tupel in self.data:
      # Erstelle ein neues Tupel, beginnend mit den generalisierten Werten
      generalized_tupel = [x for x in self.t[:len(tupel)]]

      # Wenn das Originaltupel länger ist als t, füge die zusätzlichen Werte hinzu
      if len(tupel) > len(self.t):
        for extra in tupel[len(self.t):]:
          generalized_tupel.append(extra)

      # Umwandlung in Tupel und Ausgaben
      print("Output:", tuple(generalized_tupel))
      """for tupel in self.data:
          generalized_tupel = (self.t[0], [edu for edu in self.t[1] if edu == tupel[1]])
          print("Output:", generalized_tupel)"""

  """
  def tuple_enlargement(self, tupel, global_ranges: Dict[str, Range]) -> float:
    Calculates the enlargement value for adding <item> into this cluster

    Args:
        item: The tuple to calculate enlargement based on
        global_ranges: The globally known ranges for each attribute

    Returns: The information loss if we added item into this cluster

    
    given = self.information_loss_given_t(tuple, global_ranges)
    current = self.information_loss(global_ranges)

    return (given - current) / len(self.ranges)
"""

  def update(self, tuples):
    for tuple in tuples:
      self.add_tupel(tuple)

