names = ["Carter", "David", "John"]

name = input("Name: ")

if name in names: # Python loops through the list doing linear search
    print("Found")  
else: # Yes python has an else that will run if nothing broke out
    print("Not found")