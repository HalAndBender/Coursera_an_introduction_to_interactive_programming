# Conditionals Examples

#Return True if year is a leap year, false otherwise

def is_leap_year(year):
    '''a documentation string
    should generally be placed
    right after the def function header'''
    if (year % 400) == 0:
        return True
    elif (year % 100) == 0:
        return False
    elif (year % 4) == 0:
        return True
    else:
        return False

year = 2000 #input a year to check here!

leap_year = is_leap_year(year)

if leap_year:
    print (str(year) +
           '  is a leap year')
else:
    print (str(year) + #lines can be broken to make code more readable
           '  is not a leap year')

'''triple quotes can be used as a documentation string'''
"""triple double quotes as well...."""