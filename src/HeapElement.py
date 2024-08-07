class HeapElement:
    """
    Class to represent an element in the heap
    """
    def __init__(self, dist, tuple):
        """
        Constructor of the HeapElement class.
        :param dist: specifies the distance of the tuple to another element
        :param tuple: tuple for which the distance is calculated
        """
        self.dist = dist
        self.tuple = tuple

    def __lt__(self, other):
        """
        Compares two HeapElements if smaller.
        :param other: other HeapElement
        :return: True if self is smaller than other, False otherwise
        """
        return self.dist < other.dist
