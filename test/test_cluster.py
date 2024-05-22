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

    def test_fits_in_cluster(self):
        c = Cluster((18, 'Bachelors'))
        c.add_tupel((16, 'Masters'))
        c.add_tupel((17, 'Primary School'))

        self.assertTrue(c.fits_in_cluster((16, 'Masters')))
        self.assertTrue(c.fits_in_cluster((17, 'Primary School')))
        self.assertTrue(c.fits_in_cluster((17, 'Masters')))
        self.assertFalse(c.fits_in_cluster((12, 'Primary School')))
        self.assertFalse(c.fits_in_cluster((19, 'Ph.D')))
        self.assertFalse(c.fits_in_cluster((30, 'Bachelors')))


# Führe die TestSuite aus
if __name__ == '__main__':
    unittest.main()


