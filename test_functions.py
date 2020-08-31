import unittest
from unittest.mock import patch
import mastermind
import sys
from io import StringIO

class test_mastermind(unittest.TestCase):

    def test_create_code(self):
        j = 0
        while j != 100:

            code = set(mastermind.create_code())


            self.assertEqual(len(code), 4)                 
            j += 1
    def test_check_correctness(self):     
        orig_stdout = sys.stdout
        new_string = StringIO()
        sys.stdout = new_string 
        #sys.stdout = orig_stdout
        for correct_digits_and_position in range(5):
            correctness = mastermind.check_correctness(0, correct_digits_and_position)
            if correct_digits_and_position == 4:
                self.assertTrue(correctness)
            else:
                self.assertFalse(correctness)
        sys.stdout = orig_stdout



    @patch("sys.stdin",StringIO("123\n12345\n1234\n"))
    def test_get_answer_input(self):   
        orig_stdout = sys.stdout

        new_string = StringIO()
        sys.stdout = new_string #redirecting sys output to new string
        answer = mastermind.get_input()
        out = new_string.getvalue()
        
        self.assertEqual("Input 4 digit code: Please enter exactly 4 digits.\nInput 4 digit code: Please enter exactly 4 digits.\nInput 4 digit code: ",out)
        sys.stdout = orig_stdout


    @patch("sys.stdin",StringIO("3517\n6573\n6473\n6483\n6482\n"))
    def test_take_turn(self):
        self.assertEqual(mastermind.take_turn([6,4,8,2]),(0,0))
        self.assertEqual(mastermind.take_turn([6,4,8,2]),(0,1))
        self.assertEqual(mastermind.take_turn([6,4,8,2]),(0,2))
        self.assertEqual(mastermind.take_turn([6,4,8,2]),(0,3))
        self.assertEqual(mastermind.take_turn([6,4,8,2]),(0,4))




                
            

if __name__ == '__main__':
    unittest.main()


  