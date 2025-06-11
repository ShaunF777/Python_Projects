# Import the get_int function from the cs50 library
from cs50 import get_int

# Prompt the user to input an integer value for x
x = get_int("What's x? ")

# Prompt the user to input an integer value for y
y = get_int("What's y? ")

# Check if x is less than y
if x < y:
    # If x is less than y, print "x is less than y"
    print("x is less than y")
# Check if x is greater than y
elif x > y:
    # If x is greater than y, print "x is greater than y"
    print("x is greater than y")
# If neither of the above conditions are true, x must be equal to y
else:
    # Print "x is equal to y"
    print("x is equal to y")