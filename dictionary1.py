people = [ # name and number are the index headings, with names in the key field
    {"name": "Shaun", "number": "+2783-426-9884"}, # dictionay 1
    {"name": "Thersia", "number": "+2771-678-4733"}, # dictionary 2
    {"name": "Terri", "number": "+2772-144-2924"},
    {"name": "Keira", "number": "+2782-474-7125"},
] # people is now a list of dictionaries

# prompt user for a name to lookup
name = input("Names: ")
# for loop assignes person to each dict, as it goes down the list
for person in people: # Loop though people dictionaries
    if person["name"] == name: # Dict lets us index into it like an array in c
# number = person["number"] line can be removed
# print(f"Found {number}") instead of this use:
        print(f"Found {person['number']}") 
# single 'number' so we dont confuse python 
        break
else:
    print("Not Found")