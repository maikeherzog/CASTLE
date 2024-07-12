from src.Cluster import Cluster
import unittest
from io import StringIO
from contextlib import redirect_stdout

from src.Tupel import Tuple


class TestCluster(unittest.TestCase):

    def setUp(self):
        #self.castle = Castle({(0, 18, 'Bachelors'), (1, 24, 'Bachelors'), (2, 23, 'Masters')}, 6, 5, 2)
        self.t = Tuple(0, 0, (52, 'Secondary School'),())
        self.c = Cluster(self.t, "easy_data")

    def test_len(self):
        self.assertEqual(len(self.c), 1)

        self.c.add_tupel(Tuple(1, 1, (51, 'Bachelors'), ()))
        self.assertEqual(len(self.c), 2)

        self.c.add_tupel(Tuple(2, 2, (53, 'Masters'), ()))
        self.assertEqual(len(self.c), 3)

    def test_make_tuple_from_qi(self):
        self.assertTrue(self.c.make_tuple_from_qi((52, 'Secondary School')).__eq__(Tuple(0, 0, (52, 'Secondary School'), ())))
        self.assertFalse(self.c.make_tuple_from_qi((51, 'Bachelors')).__eq__(Tuple(0, 0, (50, 'Bachelors'), ())))
        self.assertFalse(self.c.make_tuple_from_qi((52, 'Secondary School')).__eq__(Tuple(0, 0, (52, 'Primary School'), ())))
        self.assertTrue(self.c.make_tuple_from_qi((52, 'Secondary School')).__eq__(Tuple(0, 0, (52, 'Secondary School'), ())))

    def test_add_tupel(self):
        t = Tuple(0, 0, (52, 'Secondary School'),())
        c = Cluster(t, "easy_data")
        tuple1 = Tuple(1, 1, (51, 'Bachelors'), ())
        c.add_tupel(tuple1)

        self.assertEqual(c.data, [t, tuple1])
        self.assertEqual(c.t, ([51, 52], ['Secondary School', 'Bachelors']))

        tuple2 = Tuple(2, 2, (53, 'Masters'), ())
        c.add_tupel(tuple2)

        self.assertEqual(c.data, [t, tuple1, tuple2])
        self.assertEqual(c.t, ([51, 53], ['Secondary School', 'Bachelors', 'Masters']))


    def test_output_tuples_intervall(self):
        t = Tuple(0, 0, (18, 'Bachelors'),())
        c = Cluster(t, "easy_data")
        c.add_tupel(Tuple(1, 1, (16, 'Bachelors'), ()))
        c.add_tupel(Tuple(2, 2, (17, 'Bachelors'), ()))

        with StringIO() as buf, redirect_stdout(buf):
            c.output_tuples()
            output = buf.getvalue()

        expected_output = "Output: ([16, 18], ['Bachelors'])\nOutput: ([16, 18], ['Bachelors'])\nOutput: ([16, 18], ['Bachelors'])\n"
        self.assertEqual(output, expected_output)

    def test_output_tuples(self):
        t = Tuple(0, 0, (18, 'Bachelors'), ())
        c = Cluster(t, "easy_data")
        c.add_tupel(Tuple(1, 1, (16, 'Masters'), ()))
        c.add_tupel(Tuple(2, 2, (17, 'Primary School'), ()))

        with StringIO() as buf, redirect_stdout(buf):
            c.output_tuples()
            output = buf.getvalue()

        expected_output = "Output: ([16, 18], ['Bachelors', 'Masters', 'Primary School'])\nOutput: ([16, 18], ['Bachelors', 'Masters', 'Primary School'])\nOutput: ([16, 18], ['Bachelors', 'Masters', 'Primary School'])\n"
        self.assertEqual(output, expected_output)

    def test_fits_in_cluster(self):
        tuple = Tuple(0, 0, (18, 'Bachelors'),())
        c = Cluster(tuple, "easy_data")
        c.add_tupel(Tuple(1,1,(16, 'Masters'), ()))
        c.add_tupel(Tuple(2,2,(17, 'Primary School'), ()))

        self.assertTrue(c.fits_in_cluster((16, 'Masters')))
        self.assertTrue(c.fits_in_cluster((17, 'Primary School')))
        self.assertTrue(c.fits_in_cluster((17, 'Masters')))
        self.assertFalse(c.fits_in_cluster((12, 'Primary School')))
        self.assertFalse(c.fits_in_cluster((19, 'Ph.D')))
        self.assertFalse(c.fits_in_cluster((30, 'Bachelors')))

    def test_add_unique_string_to_list(self):
        self.assertEqual(self.c.add_unique_string_to_list('Masters', ['Bachelors']), ['Bachelors', 'Masters'])
        self.assertEqual(self.c.add_unique_string_to_list('Bachelors', ['Bachelors']), ['Bachelors'])
        self.assertEqual(self.c.add_unique_string_to_list('Masters', ['Bachelors', 'Masters']), ['Bachelors', 'Masters'])
        self.assertEqual(self.c.add_unique_string_to_list('Bachelors', ['Bachelors', 'Masters']), ['Bachelors', 'Masters'])
        self.assertEqual(self.c.add_unique_string_to_list(['Ph.D', 'Bachelors'], ['Bachelors', 'Masters']), ['Bachelors', 'Masters', 'Ph.D'])

    def test_adjust_interval(self):
        self.assertEqual(self.c.adjust_interval(51, [52, 53]), [51, 53])
        self.assertEqual(self.c.adjust_interval(54, [52, 53]), [52, 54])
        self.assertEqual(self.c.adjust_interval(51, [52, 54]), [51, 54])
        self.assertEqual(self.c.adjust_interval(51, [52, 55]), [51, 55])
        self.assertEqual(self.c.adjust_interval(51, [51, 53]), [51, 53])
        self.assertEqual(self.c.adjust_interval(51, 52), [51, 52])
        self.assertEqual(self.c.adjust_interval(51, 51), [51, 51])
        self.assertEqual(self.c.adjust_interval(51, 50), [50, 51])
        self.assertEqual(self.c.adjust_interval([20,23], 12), [12, 23])
        self.assertEqual(self.c.adjust_interval([20,23], 40), [20, 40])
        self.assertEqual(self.c.adjust_interval([20,23], 21), [20,23])

    def test_output_tuples(self):
        tuple1 = Tuple(1, 1, (52, 'Secondary School'), ())
        c = Cluster(tuple1, "easy_data")
        tuple2 = Tuple(2, 2, (53, 'Masters'), ())
        tuple3 = Tuple(3, 3, (54, 'Ph.D'), ())

        c.add_tupel(tuple2)
        c.add_tupel(tuple3)

        tuple1.set_qi(c.t)
        tuple2.set_qi(c.t)
        tuple3.set_qi(c.t)
        erg = c.output_tuples()

        self.assertEqual(erg, [tuple1, tuple2, tuple3])

    def test_if_cluster_is_equal(self):
        tuple1= Tuple(1, 1, (18, 'Bachelors'), ())
        c1 = Cluster(tuple1, "easy_data")
        self.assertFalse(self.c.check_cluster_if_equal(c1))

        tuple2 = Tuple(1, 1, (52, 'Secondary School'), ())
        c2 = Cluster(tuple2, "easy_data")
        self.assertTrue(self.c.check_cluster_if_equal(c2))

    def test_check_if_tuple_is_in_cluster(self):
        tuple1 = Tuple(1, 1, (18, 'Bachelors'), ())
        c1 = Cluster(tuple1, "easy_data")
        self.assertTrue(c1.check_if_tuple_is_in_cluster(tuple1))

        tuple2 = Tuple(1, 1, (52, 'Secondary School'), ())
        c2 = Cluster(tuple1, "easy_data")
        self.assertFalse(c2.check_if_tuple_is_in_cluster(tuple2))

    def test_is_k_anonymous(self):
        tuple1 = Tuple(1, 1, (18, 'Bachelors'), ())
        c1 = Cluster(tuple1, "easy_data")
        tuple2 = Tuple(2, 2, (52, 'Secondary School'), ())
        tuple3 = Tuple(3, 2, (53, 'Secondary School'), ())
        c1.add_tupel(tuple2)
        c1.add_tupel(tuple3)

        self.assertFalse(c1.is_k_anonymous(3))

        c2 = Cluster(tuple1, "easy_data")
        tuple4 = Tuple(2, 3, (52, 'Secondary School'), ())
        tuple5 = Tuple(3, 4, (53, 'Secondary School'), ())
        c2.add_tupel(tuple4)
        c2.add_tupel(tuple5)

        self.assertTrue(c2.is_k_anonymous(3))

    def test_group_tuples_by_pid(self):
        tuple1 = Tuple(1, 1, (18, 'Bachelors'), ())
        c1 = Cluster(tuple1, "easy_data")
        tuple2 = Tuple(2, 1, (52, 'Secondary School'), ())
        c1.add_tupel(tuple2)

        self.assertEqual(c1.group_tuples_by_pid(), {1: [tuple1, tuple2]})

        c2 = Cluster(tuple1, "easy_data")
        tuple3 = Tuple(3, 2, (52, 'Secondary School'), ())
        c2.add_tupel(tuple3)

        self.assertEqual(c2.group_tuples_by_pid(), {1: [tuple1], 2: [tuple3]})

    def test_set_qi_generalized(self):
        tuple1 = Tuple(1, 1, (18, 'Bachelors'), ())
        c1 = Cluster(tuple1, "easy_data")
        tuple2 = Tuple(1, 2, (52, 'Secondary School'), ())
        c1.add_tupel(tuple2)

        self.assertEqual(c1.set_qi_generalized(([18, 52], ['Bachelors', 'Secondary School'])), ([18,52], 'Any Education') )


# Führe die TestSuite aus
if __name__ == '__main__':
    unittest.main()


