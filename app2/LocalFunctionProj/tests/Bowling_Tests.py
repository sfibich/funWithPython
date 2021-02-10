import unittest
import bowling


class Testing(unittest.TestCase):
    """
    12345123451234512345
    always hitting pins without getting spares or strikes, a total score of 60

    XXXXXXXXXXXX
    a perfect game, 12 strikes, giving a score of 300

    9-9-9-9-9-9-9-9-9-9-
    heartbreak - 9 pins down each round, giving a score of 90

    5/5/5/5/5/5/5/5/5/5/5
    a spare every round, giving a score of 150
    """

    def test_canary(self):
        a = 1
        b = 1
        self.assertEqual(a, b)

    def test_compute_12345123451234512345(self):
        expected = 60
        result = bowling.computeScore("12345123451234512345")
        self.assertEqual(expected, result)

    def test_compute_XXXXXXXXXXXX(self):
        expected = 300
        result = bowling.computeScore("XXXXXXXXXXXX")
        self.assertEqual(expected, result)

    def test_compute_9hearbreak(self):
        expected = 90
        result = bowling.computeScore("9-9-9-9-9-9-9-9-9-9-")
        self.assertEqual(expected, result)

    def test_compute_5spare(self):
        expected = 155
        result = bowling.computeScore("5/5/5/5/5/5/5/5/5/5/5")
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
