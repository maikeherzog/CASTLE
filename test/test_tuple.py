import unittest

from src.Tupel import Tuple


class TestTuple(unittest.TestCase):
    def test_eq(self):
        # Erstellen Sie zwei Tuple, die im Sinne Ihrer __eq__ Methode gleich sein sollten
        tuple1 = Tuple(0, 0, (52, 'Secondary School'), ())
        tuple2 = Tuple(0, 0, (52, 'Secondary School'), ())
        # Assert that they are equal
        self.assertEqual(tuple1, tuple2)

        # Erstellen Sie zwei Tuple, die unterschiedlich sind
        tuple3 = Tuple(1, 0, (52, 'Secondary School'), ())
        # Assert that they are not equal
        self.assertNotEqual(tuple1, tuple3)


# Ausführen der Test-Suite
if __name__ == "__main__":
    unittest.main()