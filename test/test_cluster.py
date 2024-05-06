from src.Cluster import Cluster
import unittest
from io import StringIO
from contextlib import redirect_stdout

class TestCluster(unittest.TestCase):

    def test_output_tuples_intervall(self):
        c = Cluster((18, 'Bachelors'))
        c.add_tupel((16, 'Bachelors'))
        c.add_tupel((17, 'Bachelors'))

        with StringIO() as buf, redirect_stdout(buf):
            c.output_tuples()
            output = buf.getvalue()

        expected_output = "Output: ([16, 18], ['Bachelors'])\nOutput: ([16, 18], ['Bachelors'])\nOutput: ([16, 18], ['Bachelors'])\n"
        self.assertEqual(output, expected_output)

    def test_output_tuples(self):
        c = Cluster((18, 'Bachelors'))
        c.add_tupel((16, 'Masters'))
        c.add_tupel((17, 'Primary School'))

        with StringIO() as buf, redirect_stdout(buf):
            c.output_tuples()
            output = buf.getvalue()

        expected_output = "Output: ([16, 18], ['Bachelors', 'Masters', 'Primary School'])\nOutput: ([16, 18], ['Bachelors', 'Masters', 'Primary School'])\nOutput: ([16, 18], ['Bachelors', 'Masters', 'Primary School'])\n"
        self.assertEqual(output, expected_output)


# Führe die TestSuite aus
if __name__ == '__main__':
    unittest.main()


