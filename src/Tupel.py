class Tuple:
    """
    A class to represent a tuple.
    """

    def __init__(self, time, pid, qi, sensitive_attributes):
        """
        Constructor of the Tuple class.
        :param time:
        :param pid:
        :param qi:
        :param sensitive_attributes:
        """
        self.pid = pid
        self.time = time
        self.qi = qi
        self.sensitive_attributes = sensitive_attributes

    def __eq__(self, other):
        """
        Compares two tuples if equal.
        :param other:
        :return:
        """
        if isinstance(other, Tuple):
          return (self.pid == other.pid and
                  self.time == other.time and
                  self.qi == other.qi and
                  self.sensitive_attributes == other.sensitive_attributes)
        return False

    def len_qi(self):
        """
        Returns the number of Quasi-identifier attributes.
        :return:
        """
        return len(self.qi)

    def set_qi(self, qi):
        """
        Sets the Quasi-identifier attributes.
        :param qi:
        :return:
        """
        self.qi = qi


