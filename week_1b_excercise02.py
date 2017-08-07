# Compute whether a person is cool.

###################################################
# Is cool formula
# Student should enter function on the next lines.



###################################################
# Tests
# Student should not change this code.

def is_cool(name):
    """Tests the is_cool function."""

    if name == "Joe":
        print
        (str(name) + " is cool.")

    elif name == "John":
        print (str(name) + " is cool.")

    elif name == "Stephen":
        print (str(name) + " is cool.")
        
    else:
        print (str(name) + " is not cool.")


is_cool("Joe")
is_cool("John")
is_cool("Stephen")
is_cool("Scott")

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Joe is cool.
# John is cool.
# Stephen is cool.
# Scott is not cool.