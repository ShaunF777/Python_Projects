# chain method calls together, whatever is entered will become lowercase
s = input("Do you agree?").lower()


if s in ["y", "yes"]:
    print("Agreed")
elif s in ["n", "no"]:
    print("Not agreed")

# methods are built into data types now. instead of library functions as in c
# docs.python.org/3/library/stdtypes.html#string-methods