#from cs50 import get_int
def get_int(prompt):
    while True:
        try: # If try fail, it'll do except
            n = int(input(prompt)) # Convert to int
            if n > 0 and n < 100: # Check int limits
                # print(f"Valid input: {n}") # Feedbank
                return n # Return the checked int
            else: # Handling non-positive integers
                pass # print("Please enter a positive integer.")
        except ValueError: # Non-integer input error handling
            pass # print("Not an integer")

scores = []

for i in range(3):
    score = get_int("Score: ")
    # scores.append(score) appends new values like linked lists in c 
    scores = scores + [score] # Concatenate scores with itself by adding 2 lists

average = sum(scores) / len(scores)
print(f"Average: {average}")

# docs.python.org/3/lebrary/stdtypes.html#sequence-types-list-tuple-range
# docs.python.org/3/library/functions.html#len