import unittest
import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calc.add(10, 6)
        self.assertEqual(result, 16)

    def test_divide(self):
        result = calc.divide(10, 6)
        self.assertEqual(result, 1.666666667)
        self.assertRaises(ValueError, calc.divide, 10, 0)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
