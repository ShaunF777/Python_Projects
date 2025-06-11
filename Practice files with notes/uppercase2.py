# Typically c would have to go through char for char
# Python funtions = docs.python.org/3/library/functions.html
before = input("Before: ")

# after = before.upper() could first make the variable to be printed
# But this is the py way for small format changes 
print(f"After:  {before.upper()}") # Put short bits code inside format string