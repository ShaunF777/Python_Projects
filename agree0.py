# Prompt the user to input a response to the question "Do you agree?"
s = input("Do you agree?")

# Convert the user's input to lowercase to ensure case-insensitivity
s = s.lower()

# Check if the user's input is either "y" or "yes"
if s in ["y", "yes"]:
    # If the input is "y" or "yes", print "Agreed"
    print("Agreed")
# Check if the user's input is either "n" or "no"
elif s in ["n", "no"]:
    # If the input is "n" or "no", print "Not agreed"
    print("Not agreed")