import calculator
import unittest


class CalcTest(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(calculator.add(9, 4), 13)

    def testPow(self):
        self.assertEqual(calculator.pow(3, -1), 0.333)

    def testMul(self):
        self.assertEqual(calculator.mul(0, -3), 0)

    def testDiv(self):
        self.assertEqual(calculator.div(12, 0), 'На ноль делить нельзя!')

    def testSub(self):
        self.assertEqual(calculator.sub(12, 6), 6)

    def testCheckOperation(self):
        self.assertEqual(calculator.checkOperations(')'), 'Такой операции не существует!')


if __name__ == '__main__':
    unittest.main()