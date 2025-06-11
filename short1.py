# Key Function differences going over from C to Python

# Functions work the same, but prefix "def" and don't need data types on the 
# return types nor on the parameters 
# main is not needed, the interpreter reads from top to bottom!
# If main is a must have to run functions in a specific order, you must use
# if __name__ == "__main__": # at the very last line
#    main()

# Examples
def cube(x):
    x = x ** 3 # same as x * x, ** is pythons exponentiation operator
    return x
# or using convoluted ways like
def square(x):
    result = 0
    for i in range(0, x):
        result += x
    return result
# doesnt realy matter as long as 
print(cube(4)) # prints out 64
print(square(5)) # prints out 25