names = ["Carter", "David", "John"]

name = input("Name: ")

for n in names: # This will loop through the list
    if name == n:
        print("Found")
        break # Lets you get out of any for or while loop
else: # Yes python has an else that will run if nothing broke out
    print("Not found")