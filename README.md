# PE9-whileTrue-loops

# Python Loops: The "While True" Pattern

## Overview
In this homework, you will practice using **Post-Conditional Loops**. Python does not have a `do-while` loop, so we simulate it using `while True` combined with `if` and `break`.

This pattern is useful when **you must perform an action at least once** (like asking for input) before checking if you should stop.

## How to Run Your Code
1. Open `PE9exercises.py` in your IDE.
2. Edit the functions at the top of the file.
3. Run the file normally (e.g., `python PE9exercises.py`).
4. The **Autotests** at the bottom of the file will run automatically and tell you if your code is correct.

---

## Tasks

### Task 1: `get_positive_number()`
You need to force the user to give you good data.
* **Goal:** Loop until the user provides a positive integer.
* **Logic:**
    1.  Ask for input.
    2.  Check if it is a digit and greater than 0.
    3.  If yes -> `break` (or return).
    4.  If no -> print error and loop again.

### Task 2: `robot_menu()`
Create a controller for a robot.
* **Goal:** Keep the program running until the "Stop" command is given.
* **Commands:**
    * `M` -> Print "Moving forward..."
    * `T` -> Print "Turning right..."
    * `S` -> Print "Stopping..." and stop the loop.
    * Anything else -> Print "Unknown command."

### Task 3: `authenticate_user(password, max_tries)`
Simulate a login screen.
* **Goal:** Allow the user to try entering a password, but lock them out if they fail too many times.
* **Logic:**
    * Use a variable to count attempts.
    * If the input matches the password -> return `True`.
    * If the count reaches `max_tries` -> print "Locked out" and return `False`.

### Task 4: `calculate_average()`
Calculate the average of an unknown list of numbers.
* **Goal:** Ask for numbers until the user types 'q'.
* **Logic:**
    * Loop forever.
    * Ask for input.
    * If input is 'q', break.
    * If input is a number, add it to a total.
    * If input is junk (like "hello"), ignore it.
    * Finally, return `total / count`.
