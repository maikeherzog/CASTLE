from src.Cluster import Cluster
import unittest
from io import StringIO
from contextlib import redirect_stdout

class TestCluster(unittest.TestCase):

    def test_output_tuples(self):
        c = Cluster((18, 'Bachelors'))
        c.add_tupel((16, 'Bachelors'))
        c.add_tupel((17, 'Bachelors'))

        with StringIO() as buf, redirect_stdout(buf):
            c.output_tuples()
            output = buf.getvalue()

        expected_output = "Output: (18, 'Bachelors')\nOutput: (16, 'Bachelors')\nOutput: (17, 'Bachelors')\n"
        self.assertEqual(output, expected_output)

# Führe die TestSuite aus
if __name__ == '__main__':
    unittest.main()


