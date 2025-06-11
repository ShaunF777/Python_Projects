# text input string methods
# text = input("   In the great green room      ")
# text = text.strip() # Removes whitespaces before and after
# text = text.lower()
# text = text.capitalize() # Correct sentence starting with capital letter
# https://docs.python.org/3/library/stdtypes.html

text = ("IN THE GREAT GREEN ROOM")
text = text.capitalize()
print(text)
print("------------------------------------")
# In python str is an object having its own set of .notation functions
# These are called methods(data + funtions)

# When looking at a struct in C, OOP allows functions aswell
# OOP allows data types to have structured data and functions
# In short, its like a preset program, ready made with different 
# functions to perform ON the input you give it

# c is assigned the value as iterated through the list of characters
for c in text: 
    print(c)
print("------------------------------------")
# _ is created for this loop only, going through linked list of words
words = text.split()
print(words)
for _ in words:
    print(_)
print("------------------------------------")
# Thus Python's for/in syntax helps you iterate through components on an"iterable"
# while refering to each character(string) or element(list) in that structure 

for word in text.split():
    print(word)
print("------------------------------------")
for word in text.split():
    for c in word:
        print(c, end="")
print()
print("------------------------------------")

for word in text.split():
    if "g" in word: # Linear search through words 
        print(word)
print("------------------------------------")

words = text.split()
print(words[1:]) # only print from word 1 in the list 
print(words[1:4]) # only includes words 1 to 3
print("------------------------------------")
