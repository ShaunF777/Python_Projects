# Using Libraries and Modules to load in all the books i have in a list
# https://docs.python.org/3/library/csv.html
import csv # import csv library

books = [] # blank list of books

# Add books to shelf by reading from books.csv
with open("books.csv") as tmpfile: # call that file "tmpfile" 
# Using the open function, puts data into tmpfile for me to access
    text = tmpfile.read() # text receives all lines in tmpfile
    print(text) # all lines are printed
print("---------------------------------------")

# Convert csv file into list of dictionaries
with open("books.csv") as tmpfile: # 'with' closes the file automatically
    # csv.DictReader helps us make dicts of eavery row in the file
    reader = csv.DictReader(tmpfile) 
    for row in reader:
        books.append(row) # Add rows as dictionaries to my list of books


# print books
for book in books:
    print(books)