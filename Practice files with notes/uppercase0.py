# Typically c would have to go through char for char
# Python funtions = docs.python.org/3/library/functions.html
before = input("Before: ")
print("After:  ", end="")# overide \n python gives by default
for c in before:
    print(c.upper(), end="")
print()
# Looping is not required because of string methodssee uppercase1.py