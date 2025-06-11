# Using Dictionary for a book
book = dict()
book["title"] = "Corduroy" # key is "title" , value is "Corduroy"
book["author"] = "Don Freeman"
print(book["title"]) # will print "Corduroy"
print("------------------------------------")
# dict only allows 1 value for each key, but the value could be a list
# or any other object
# print(book["Corduroy"]) would give me KeyError: 'Corduroy'
# struct in c were fixed in size & shape
# dict are more dynamic, and can be added onto

# Using lists, we could add dictionaries inside, giving us a list of books
books = []

#Add three books to shelf
for i in range(3): # each time add, create a dict with title & author
    book = dict()
    book["author"] = input("Enter and author: ")
    book["title"] = input("Enter a title: ")
    books.append(book) # Adding it to the list or book shelf
print("------------------------------------")
    

# Print list of books
print(books)
print("------------------------------------")

# Print keys of dict
print(book.keys())
print("------------------------------------")
for book in books: # Normal conventional, single iterating through a plural
    print(book)
print("------------------------------------")

for book in books: 
    if book["author"] == "GGG": #search throuhg authors
        print(book)
print("------------------------------------")

# Print dicts as sentences 
for book in books: 
    #print(f"Author wrote book.")
    print(f"{book['author']} wrote {book['title']}.")
print("------------------------------------")


