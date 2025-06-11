# Using sys module(library) you can exit the program
import sys # import all of sys

# If not correct arguments tell user
if len(sys.argv) != 2: # Specify function of sys needed  
    print("Missing command-line argument")
    sys.exit(1) # Exit the program with an exit status fault-finding

print(f"hello, {sys.argv[1]}") #
sys.exit(0) # Exit with status 0