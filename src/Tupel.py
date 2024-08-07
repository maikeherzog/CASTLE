class Tuple:
    """
    A class to represent a tuple.
    """

    def __init__(self, time, pid, qi, sensitive_attributes):
        """
        Constructor of the Tuple class.
        :param time (int): the arrival time of the tuple
        :param pid (int): the person-ID of the tuple
        :param qi (tuple): the Quasi-identifier attributes of the tuple
        :param sensitive_attributes (tuple): the sensitive attributes of the tuple
        """
        self.pid = pid
        self.time = time
        self.qi = qi
        self.sensitive_attributes = sensitive_attributes

    def __eq__(self, other):
        """
        Compares two tuples if equal.
        :param other (Tuple): other tuple
        :return: True if self is equal to other, False otherwise
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
        :return: the number of Quasi-identifier attributes
        """
        return len(self.qi)

    def set_qi(self, qi):
        """
        Sets the Quasi-identifier attributes.
        :param qi (tuple): the Quasi-identifier attributes
        """
        self.qi = qi


