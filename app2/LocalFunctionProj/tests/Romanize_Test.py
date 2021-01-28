import unittest
import romanize

class Testing(unittest.TestCase):

    def test_canary(self):
        a=1
        b=1
        self.assertEqual(a,b)

    def test_I(self):
        expected_result='I'
        result = romanize.romanize(1)
        self.assertEqual(expected_result,result)

    def test_V(self):
        expected_result='V'
        result = romanize.romanize(5)
        self.assertEqual(expected_result,result)

    def test_X(self):
        expected_result='X'
        result = romanize.romanize(10)
        self.assertEqual(expected_result,result)

    def test_II(self):
        expected_result='II'
        result = romanize.romanize(2)
        self.assertEqual(expected_result,result)

    def test_III(self):
        expected_result='III'
        result = romanize.romanize(3)
        self.assertEqual(expected_result,result)

    def test_IV(self):
        expected_result='IV'
        result = romanize.romanize(4)
        self.assertEqual(expected_result,result)

    def test_VI(self):
        expected_result='VI'
        result = romanize.romanize(6)
        self.assertEqual(expected_result,result)

    def test_VII(self):
        expected_result='VII'
        result = romanize.romanize(7)
        self.assertEqual(expected_result,result)

    def test_VIII(self):
        expected_result='VIII'
        result = romanize.romanize(8)
        self.assertEqual(expected_result,result)

    def test_IX(self):
        expected_result='IX'
        result = romanize.romanize(9)
        self.assertEqual(expected_result,result)

    def test_XI(self):
        expected_result='XI'
        result = romanize.romanize(11)
        self.assertEqual(expected_result,result)

    def test_XII(self):
        expected_result='XII'
        result = romanize.romanize(12)
        self.assertEqual(expected_result,result)

    def test_XIII(self):
        expected_result='XIII'
        result = romanize.romanize(13)
        self.assertEqual(expected_result,result)

    def test_XIV(self):
        expected_result='XIV'
        result = romanize.romanize(14)
        self.assertEqual(expected_result,result)

    def test_XV(self):
        expected_result='XV'
        result = romanize.romanize(15)
        self.assertEqual(expected_result,result)

    def test_XIX(self):
        expected_result='XIX'
        result = romanize.romanize(19)
        self.assertEqual(expected_result,result)

    def test_XX(self):
        expected_result='XX'
        result = romanize.romanize(20)
        self.assertEqual(expected_result,result)

    def test_XXI(self):
        expected_result='XXI'
        result = romanize.romanize(21)
        self.assertEqual(expected_result,result)

    def test_XXIII(self):
        expected_result='XXIII'
        result = romanize.romanize(23)
        self.assertEqual(expected_result,result)

    def test_XL(self):
        expected_result='XL'
        result = romanize.romanize(40)
        self.assertEqual(expected_result,result)

    def test_XLIX(self):
        expected_result='XLIX'
        result = romanize.romanize(49)
        self.assertEqual(expected_result,result)

    def test_L(self):
        expected_result='L'
        result = romanize.romanize(50)
        self.assertEqual(expected_result,result)

    def test_LX(self):
        expected_result='LX'
        result = romanize.romanize(60)
        self.assertEqual(expected_result,result)

    def test_XC(self):
        expected_result='XC'
        result = romanize.romanize(90)
        self.assertEqual(expected_result,result)

    def test_C(self):
        expected_result='C'
        result = romanize.romanize(100)
        self.assertEqual(expected_result,result)

    def test_CC(self):
        expected_result='CC'
        result = romanize.romanize(200)
        self.assertEqual(expected_result,result)

    def test_CD(self):
        expected_result='CD'
        result = romanize.romanize(400)
        self.assertEqual(expected_result,result)

    def test_D(self):
        expected_result='D'
        result = romanize.romanize(500)
        self.assertEqual(expected_result,result)

    def test_DC(self):
        expected_result='DC'
        result = romanize.romanize(600)
        self.assertEqual(expected_result,result)

    def test_CM(self):
        expected_result='CM'
        result = romanize.romanize(900)
        self.assertEqual(expected_result,result)

    def test_M(self):
        expected_result='M'
        result = romanize.romanize(1000)
        self.assertEqual(expected_result,result)

    def test_MC(self):
        expected_result='MC'
        result = romanize.romanize(1100)
        self.assertEqual(expected_result,result)

    def test_MI(self):
        expected_result='MI'
        result = romanize.romanize(1001)
        self.assertEqual(expected_result,result)

    def test_MCM(self):
        expected_result='MCM'
        result = romanize.romanize(1900)
        self.assertEqual(expected_result,result)

    def test_MM(self):
        expected_result='MM'
        result = romanize.romanize(2000)
        self.assertEqual(expected_result,result)

    def test_MMMM(self):
        expected_result='MMMM'
        result = romanize.romanize(4000)
        self.assertEqual(expected_result,result)

if __name__ == "__main__":
    unittest.main()
