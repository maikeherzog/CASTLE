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

  def add_tupel(self, t):
    """
    Fügt einen Datensatz zum Cluster hinzu.

    Args:
      t: Der Datensatz.
    """

    self.data.append(t)

  def __len__(self):
    """
    Gibt die Anzahl der Datensätze in diesem Cluster zurück.
    """

    return len(self.data)

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