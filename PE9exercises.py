import sys

def get_positive_number():
    """
    Task 1: Input Validation
    Continuously asks the user for a number.
    - Prompt: "Enter a positive number: "
    - If the input is not a number or is <= 0, print "Invalid input."
    - If the input is valid, return the number (as an integer).
    """
    # TODO: Delete 'pass' and write your 'while True' loop here
    pass

def robot_menu():
    """
    Task 2: Interactive Menu
    Runs a menu loop until the user chooses to stop.
    - Options: [M]ove, [T]urn, [S]top
    - Prompt: "Command: "
    - If 'm' or 'M': print "Moving forward..."
    - If 't' or 'T': print "Turning right..."
    - If 's' or 'S': print "Stopping..." and break the loop.
    - Any other input: print "Unknown command."
    """
    # TODO: Delete 'pass' and write your 'while True' loop here
    pass

def authenticate_user(correct_password, max_attempts):
    """
    Task 3: Retry Limit
    Asks the user for a password with a limited number of attempts.
    - Prompt: "Enter password: "
    - If input matches 'correct_password': print "Access Granted" and return True.
    - If input is wrong: print "Wrong password".
    - If attempts reach 'max_attempts': print "Locked out" and return False.
    """
    # TODO: Delete 'pass' and write your 'while True' loop here
    pass

def calculate_average():
    """
    Task 4: The Sentinel Value
    Continuously asks for numbers to calculate an average.
    - Prompt: "Enter number (or 'q' to quit): "
    - If input is 'q' or 'Q': break the loop.
    - If input is a valid number: add to total and count.
    - If input is invalid: print "Not a number".
    - Return the average (float). Return 0 if no numbers were entered.
    """
    # TODO: Delete 'pass' and write your 'while True' loop here
    pass


# ==============================================================================
#  DO NOT EDIT BELOW THIS LINE
#  The code below automatically tests your functions when you run this file.
# ==============================================================================

import unittest
from unittest.mock import patch
from io import StringIO

class TestPostConditionalLoops(unittest.TestCase):

    @patch('builtins.input', side_effect=['-5', 'abc', '0', '10'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1_get_positive_number(self, mock_stdout, mock_input):
        result = get_positive_number()
        output = mock_stdout.getvalue()
        
        self.assertEqual(result, 10, "Task 1: Should return the first valid positive integer (10).")
        self.assertIn("Invalid input", output, "Task 1: Should print 'Invalid input.' on bad data.")
        self.assertGreaterEqual(output.count("Invalid input"), 3, "Task 1: Should complain for every bad input (-5, abc, 0).")

    @patch('builtins.input', side_effect=['m', 'X', 'T', 's'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_2_robot_menu(self, mock_stdout, mock_input):
        robot_menu()
        output = mock_stdout.getvalue().lower()
        
        self.assertIn("moving forward", output, "Task 2: 'm' should print 'Moving forward...'")
        self.assertIn("unknown command", output, "Task 2: 'X' should print 'Unknown command.'")
        self.assertIn("turning right", output, "Task 2: 'T' should print 'Turning right...'")
        self.assertIn("stopping", output, "Task 2: 's' should print 'Stopping...'")

    @patch('builtins.input', side_effect=['wrong1', 'wrong2', 'secret'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_3a_authenticate_success(self, mock_stdout, mock_input):
        result = authenticate_user("secret", 3)
        output = mock_stdout.getvalue()
        
        self.assertTrue(result, "Task 3: Should return True if password is correct within limit.")
        self.assertIn("Access Granted", output, "Task 3: Should print 'Access Granted'.")

    @patch('builtins.input', side_effect=['wrong', 'wrong', 'wrong'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_3b_authenticate_fail(self, mock_stdout, mock_input):
        result = authenticate_user("secret", 3)
        output = mock_stdout.getvalue()
        
        self.assertFalse(result, "Task 3: Should return False if attempts run out.")
        self.assertIn("Locked out", output, "Task 3: Should print 'Locked out'.")

    @patch('builtins.input', side_effect=['10', '20', '30', 'q'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_4a_calculate_average(self, mock_stdout, mock_input):
        result = calculate_average()
        self.assertAlmostEqual(result, 20.0, places=2, msg="Task 4: Average of 10, 20, 30 should be 20.0")

    @patch('builtins.input', side_effect=['bad', '10', 'q'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_4b_calculate_average_validation(self, mock_stdout, mock_input):
        result = calculate_average()
        output = mock_stdout.getvalue()
        self.assertAlmostEqual(result, 10.0, msg="Task 4: Should ignore bad inputs and calculate average of valid ones.")
        self.assertIn("Not a number", output, "Task 4: Should warn on invalid input.")

if __name__ == '__main__':
    print("\nRunning Autotests...\n")
    unittest.main(verbosity=2, exit=False)
