import sys

# ==============================================================================
#  STUDENT EXERCISES (Edit these functions)
# ==============================================================================

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
#  TEST RUNNER (Do not modify below this line)
# ==============================================================================
import io
import builtins

class TestRunner:
    def __init__(self):
        self.failed_checks = 0
        self.total_checks = 0

    def mock_input_output(self, inputs, func, args=None):
        """Helper to simulate inputs and capture prints safely"""
        original_input = builtins.input
        original_stdout = sys.stdout
        
        input_iterator = iter(inputs)
        captured_output = io.StringIO()
        
        def mock_input(prompt=""):
            try:
                return next(input_iterator)
            except StopIteration:
                return ""
        
        builtins.input = mock_input
        sys.stdout = captured_output

        result = None
        try:
            if args:
                result = func(*args)
            else:
                result = func()
        except Exception as e:
            # We catch crashes but don't stop the whole suite
            result = None
            print(f"    [CRASH] Your code crashed: {e}")
        finally:
            builtins.input = original_input
            sys.stdout = original_stdout
            
        return result, captured_output.getvalue()

    def check(self, description, condition, failure_msg):
        self.total_checks += 1
        if condition:
            print(f"  [\033[92mOK\033[0m] {description}")
        else:
            print(f"  [\033[91mFAIL\033[0m] {description}")
            print(f"         -> {failure_msg}")
            self.failed_checks += 1

    def summary(self):
        print("\n" + "="*40)
        print(f"SUMMARY: {self.total_checks - self.failed_checks}/{self.total_checks} Checks Passed")
        print("="*40)
        # Only exit with error code at the very end
        if self.failed_checks > 0:
            sys.exit(1)

def run_tests():
    t = TestRunner()
    print("\nRunning Tests...\n")

    # --- Test Task 1 ---
    print("--- Checking Task 1: Positive Number ---")
    try:
        res, out = t.mock_input_output(['-5', 'abc', '10'], get_positive_number)
        t.check("Return Value is 10", res == 10, f"Expected return 10, got {res}")
        t.check("Prints error message", "Invalid input" in out, "Did not print 'Invalid input.' on bad data")
    except Exception as e:
        print(f"  [CRASH] Task 1 crashed: {e}")
        t.failed_checks += 1
    print("")

    # --- Test Task 2 ---
    print("--- Checking Task 2: Robot Menu ---")
    try:
        res, out = t.mock_input_output(['m', 'X', 's'], robot_menu)
        out = out.lower() if out else ""
        t.check("Responds to 'm'", "moving forward" in out, "Input 'm' did not print 'Moving forward...'")
        t.check("Responds to unknown", "unknown command" in out, "Input 'X' did not print 'Unknown command.'")
        t.check("Responds to 's'", "stopping" in out, "Input 's' did not print 'Stopping...'")
    except Exception as e:
        print(f"  [CRASH] Task 2 crashed: {e}")
        t.failed_checks += 1
    print("")

    # --- Test Task 3 ---
    print("--- Checking Task 3: Authentication ---")
    try:
        # Case A: Success
        res, out = t.mock_input_output(['wrong', 'secret'], authenticate_user, ["secret", 3])
        t.check("Correct password returns True", res is True, f"Expected True, got {res}")
        
        # Case B: Failure
        res, out = t.mock_input_output(['wrong', 'wrong', 'wrong'], authenticate_user, ["secret", 3])
        t.check("Max attempts returns False", res is False, f"Expected False, got {res}")
        t.check("Prints lockout message", "Locked out" in (out if out else ""), "Did not print 'Locked out'")
    except Exception as e:
        print(f"  [CRASH] Task 3 crashed: {e}")
        t.failed_checks += 1
    print("")

    # --- Test Task 4 ---
    print("--- Checking Task 4: Average ---")
    try:
        res, out = t.mock_input_output(['10', 'bad', '20', 'q'], calculate_average)
        out = out if out else ""
        # Handle None return gracefully
        is_correct = False
        if isinstance(res, (int, float)):
            is_correct = abs(res - 15.0) < 0.01
        
        t.check("Calculates average (10, 20)", is_correct, f"Expected 15.0, got {res}")
        t.check("Handles invalid input", "Not a number" in out, "Did not print 'Not a number' for text input")
    except Exception as e:
        print(f"  [CRASH] Task 4 crashed: {e}")
        t.failed_checks += 1

    t.summary()

if __name__ == "__main__":
    run_tests()
