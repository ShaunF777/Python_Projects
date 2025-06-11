# Key differences going over from C to Python
# Only from 10minutes theres more Syntax Suger

for x in range(100): # Normal for loop
    print(x)

for x in range(0, 100, 2): # Will print or count 0,2,4,6,8,10 up to 98
    print (x)

# Arrays in C are called Lists in Python
# Lists are not fixed and function more like linked lists, allowing 
# you to add and remove dynamically and splice things in and out easily
# Declaration
nums = []
nums = [1,2,3,4] # Explicitly created list
# List Comprehension
nums = [x for x in range(500)] # Generates list for me 0 up to 499
# Instead of [] i can use list finction declaration
nums = list()
nums = [1, 2, 3, 4]
nums.append(5) # Attach 5 to the back of the list
nums.insert(4,5) # Inserts 5 at position 4 
nums[len(nums):] = [5, 6, 7] # Splice list 5, 6, 7 onto nums 


# Tuple data type is almost like a struct in C, but not for changing
# Tuples are ordered, immutable sets of data; great for associating
# collections of data thats unlikely to change, but the order matters.
# Fast to navigate
# List of 4 iterable tuples
presidents = [
    ("George Washington", 1789),
    ("John Adams", 1797),
    ("Thomas Jefferson", 1801),
    ("James Madison", 1809)
]
# Iterate over the tuples
for prez, year in presidents:
    print("In {1}, {0} took office".format(prez,year)) # .format function
    # allows swaping values for printing


# Dictionaries allow you to specify list indices with words or phrases (keys),
# instead of just integers in C
# Dictionary examples and actions
pizzas = {
    "cheese": 9,
    "pepperoni": 10,
    "vegetable": 11,
    "buffalo chicken": 12
}
pizzas["cheese"] = 8 # change the values by reference
if pizzas["vegetables"] < 12:
    # do something using boolian expressions
    pizzas["bacon"] = 14 # add new keys and values

# Using the flexibility of python for loops
for pie in pizzas: # pie gets the value of each key as it loops through
    print(pie) # prints out the keys not in particular order 

for pie, price in pizzas.items(): # .items method transforms dict into list
    print(price) # prints out key values (note list are random) 

for pie, price in pizzas.items(): # to print out key and value
    print("A whole {} pizza costs ${}".format(pie, price)) 
    # or this will do  the same, but price must be converted to str
    print("A whole " + pie + " pizza costs $" + str(price)) 
    # avoid deprecated ways like
    print("A whole %s pizza costs $%2d" % (pie, price)) 
    
    

