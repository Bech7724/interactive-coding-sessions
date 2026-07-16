# Let's first re-create a variable or two
my_integer = 10
my_str = "Hello world"
# He told us before that you can always see the type of a vatiable using type()
type(my_integer)
type(my_str)

# What is stored inside of these objects?
my_str.upper # Upper is a METHOD that is attached to all the objects of class string
# A method is like a function, so it needs to be CALLED. Jpw dp we call a function again?
# We put () after it
my_str.upper() # Returning the upper, capitalized verstion of the string.
my_str.upper() # What does it mean to return a copy?
# It means the original string is unchanged:
my_str
# Let's try another one:
my_str.lower()
# What else is in there?
my_str.endswith('!') #Does not end with an "!"
my_str.endswith('orld') # Returns true!
# Methods are a way of pairing functions to specific types of objects. 

# Some objects have other things than methods: Properties.
# Properties are information about the object that was created.
my_integer.denominator # White wrenches are properties of the object
my_integer.numerator # Do we put parentesis? No.
# Properties are only meant to be read. They don't do anything. They just exist
# If something does not require any calclation to be given to you,
# and does not do anything, it is probably a property
# But to be sure: look at the icon