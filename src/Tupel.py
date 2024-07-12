from src.edit_data import attribute_properties
from src.tree_functions import find_generalization


class Tuple:
  """
  Ein Datensatz.

  Args:


  """

  def __init__(self, time, pid, qi, sensitive_attributes):
    self.pid = pid
    self.time = time
    self.qi = qi
    self.sensitive_attributes = sensitive_attributes

  def __eq__(self, other):
    if isinstance(other, Tuple):
      return (self.pid == other.pid and
              self.time == other.time and
              self.qi == other.qi and
              self.sensitive_attributes == other.sensitive_attributes)
    return False

  def __ne__(self, other):
    return not self.__eq__(other)
  def len_qi(self):
    return len(self.qi)

  def set_qi(self, qi):
    self.qi = qi


