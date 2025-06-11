# If all we're storing are names and numbers, simplify code:
people = { # Only 1 key connected to only 1 value
    "Shaun": "+2783-426-9884",
    "Thersia": "+2771-678-4733",
    "Terri": "+2772-144-2924",
    "Keira": "+2782-474-7125",
} # people is now a single dictionary

# prompt user for a name to lookup
name = input("Names: ")

# Python allows looking for name through a dict as if it was a list
if name in people: # Looks through the dict people for name
    number = people[name] # Index dict for the name and assign number
    print(f"Found {number}") # Print number
else:
    print("Not Found") # Or not

# docs.python.org/3/library/stdtypes.html#mapping-types-dict