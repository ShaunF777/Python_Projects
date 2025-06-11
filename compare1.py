# Without the cs50 library for numbers
x = input("What's x? ")
y = input("What's y? ")
x = int(x) #instead of cast, py uses conversion
y = int(y)

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
