from src.Tupel import Tuple

class Data:
    """
    A class to represent a stream of tuples.
    """
    def __init__(self, data, qi_index, sa_index):
        """
        Constructor of the Data class.
        :param data:
        :param qi_index:
        :param sa_index:
        """
        self.data = self.data_from_stream(data, qi_index, sa_index)

    @staticmethod
    def data_from_stream(stream, qi_index, sa_index):
        """
        Converts a stream to a list of Tuples.

        Args:
        stream (list of tuples): the stream to convert
        qi_index (list of int): indices of the Quasi-identifier attributes in the stream tuple
        sa_index (list of int): indices of the sensitive attributes in the stream tuple

        Returns:
        list of `Tuple`: the converted list of tuples
        """

        list_of_tuples = []
        for item in stream:
            pid = item[0]
            time = item[1]

            qi = tuple(item[i] for i in range(qi_index[0], qi_index[1]))
            sa = []
            if sa_index != []:
                sa = tuple(item[i] for i in range(sa_index[0], sa_index[1]))

            my_tuple = Tuple(pid, time, qi, sa)
            list_of_tuples.append(my_tuple)

        return list_of_tuples