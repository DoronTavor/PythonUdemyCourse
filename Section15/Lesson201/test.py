import unittest
import main


class TestGame(unittest.TestCase):
    def test_input(self):
        test_guess=5
        test_num=5
        result= main.run_guess(test_guess,test_num)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        test_guess = 7
        test_num = 5
        result = main.run_guess(test_guess, test_num)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        test_guess = 11
        test_num = 5
        result = main.run_guess(test_guess, test_num)
        self.assertFalse(result)
    def test_input_wrong_type(self):
        test_guess = 11
        test_num = "5"
        result = main.run_guess(test_guess, test_num)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
