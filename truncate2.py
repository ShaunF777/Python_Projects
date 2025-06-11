x = int(input("x: "))
y = int(input("y: "))

z = x / y
print(f"{z:.50f}") # use format to allow a float of 50decimals
# Notice floating point inprecision is still present
# Many 3rd party libraries exsist to help with scientific or financial purposes