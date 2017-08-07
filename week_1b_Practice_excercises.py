# Compute whether an integer is even.

###################################################
# Is even formula
# Student should enter function on the next lines.



###################################################
# Tests
# Student should not change this code.

def is_even(number):
	"""Tests the is_even function."""
	if number % 2 == 0:
		print (str(number), "is even.")
	else:
		print (str(number), "is odd.")

is_even(8)
is_even(3)
is_even(12)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#8 is even.
#3 is odd.
#12 is even.

