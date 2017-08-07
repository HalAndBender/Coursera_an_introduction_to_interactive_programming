# solution given by website:

def is_leap_year (year):
    return ((year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0))


def test(year):
	"""Tests the is_leapyear function."""
	if is_leap_year(year):
		print (year, "is a leap year.")
	else:
		print (year, "is not a leap year.")

test(2000)
test(1996)
test(1800)
test(2013)

# print(is_leap_year)


# Wikipedia instructions:
    # if (year is not divisible by 4) then (it is a common year)
    # else if (year is not divisible by 100) then (it is a leap year)
    # else if (year is not divisible by 400) then (it is a common year)
    # else (it is a leap year)