import unittest

from src.Tupel import Tuple


class TestTuple(unittest.TestCase):
    def test_eq(self):
        tuple1 = Tuple(0, 0, (52, 'Secondary School'), ())
        tuple2 = Tuple(0, 0, (52, 'Secondary School'), ())
        tuple3 = Tuple(1, 0, (52, 'Secondary School'), ())

        # Assert that they are equal
        self.assertEqual(tuple1, tuple2)

        # Assert that they are not equal
        self.assertNotEqual(tuple1, tuple3)

    def test_len_qi(self):
        tuple1 = Tuple(0, 0, (52, 'Secondary School'), ())
        self.assertEqual(tuple1.len_qi(), 2)
        self.assertNotEqual(tuple1.len_qi(), 3)

    def test_set_qi(self):
        tuple1 = Tuple(0, 0, (52, 'Secondary School'), ())
        tuple1.set_qi(([50,55], 'Secondary School'))
        self.assertEqual(tuple1.qi, ([50,55], 'Secondary School'))
        self.assertNotEqual(tuple1.qi, (52, 'Primary School'))



# Ausführen der Test-Suite
if __name__ == "__main__":
    unittest.main()