#!/usr/bin/env python3

# Objects in Python and any other OOP language are almost like C structures
# but besides the fields(properties), objects contain functions(methods)

"""Object properties work similar to C
struct car
{
    int year;
    char *model;
}
properties can not stand on their own, needing the .notation name
struct car herbie;
herbie.year = 1963;
herbie.model = "Beetle"; 
So this is the similarity of object properties to C structure fields"""

""" OBJECTS have PROPERTIES but also METHODS that are inherent to it's OBJECT,
and mean nothing outside of it. You define the METHODS inside the object also.
Thus PROPERTIES and METHODS don't ever stand on their own, that where the term
OBJECT ORIENTED Programming comes from. OBJECTS are most important. """

# We don't pass an object into a function, function(object);
# but rather call METHODS on OBJECTS.
# object.method()

""" We define a custom type of OBJECT using the CLASS keyword in Python
CLASSES require an initialization function a.k.a. a CONSTRUCTOR,
which SETS the START values of the PROPERTIES of the OBJECT.
In defining each METHOD of an OBJECT, 'self' should be it's 1st parameter, 
which stipulates on what OBJECT is CALLED"""

# OBJECT example

class Student(): # Just like structs, 'Student' is used to create new OBJECTS

    def __init__(self, name, id): # Constructor will configure initial values
        self.name = name # will pass whatever is in 'name' into self.name
        self.id = id # will pass whatever is in 'name' into self.id

    def changeID(self, id): # to change just the id 
        self.id = id

    def print(self): # only taking in 'self' and printing what's inside
        print("{} - {}".format(self.name, self.id))

jayne = Student("Jayne", 10)
jayne.print()
jayne.changeID(11)
jayne.print()
        
# Python relies on style and requires propper indentation to work

# Including files, instead of '#include <cs50.h>' we now have the following:
# 'import cs50' will include the whole MODULE or 'from cs50 import get_int'
# for a parial import

""" Besides python program.py files, we can write and test short python snippets
using the python interpreter from the command line. 
This only requires the Python interpreter installed on the system
Just type python in terminal """

""" To make python programs run like C by typing './filename' we add a shebang
to the top of you python files ' #!/usr/bin/env python3 '
, which finds and executes the interpreter automatically. Doing this requires 
changing permissions on your file & using Linux command 
'chmod a+x filename.py ' after saving the file programs"""


