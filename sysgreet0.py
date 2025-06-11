# Greet people using command line arguments
from sys import argv # argv is inside sys module

if len(argv) == 2: # The command "python3" will be ignored in terminal
    print(f"hello, {argv[1]}") # Whatever is at location 1
else:
    print("hello, world")
# docs.python.org/3/library/sys.html