class Tuple:
  """
  Ein Datensatz.

  Args:


  """

  def __init__(self, pid, time, qi, sensitive_attributes):
    self.pid = pid
    self.time = time
    self.qi = qi
    self.sensitive_attributes = sensitive_attributes

  def len_qi(self):
    return len(self.qi)

  def set_qi(self, qi):
    self.qi = qi
