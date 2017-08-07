# Challenge: Given numbers a, b, and c, the quadratic equation ax^2+bx+c=0 can have zero,
# one or two real solutions (i.e; values for x that satisfy the equation).
# The quadratic formula x = (−b±sqrt(b^2−4ac))/(2a) can be used to compute these solutions.
# The expression b^2−4ac is the discriminant associated with the equation.
# If the discriminant is positive, the equation has two solutions. If the discriminant is zero,
# the equation has one solution. Finally, if the discriminant is negative, the equation has
# no solutions. Write a Python function 𝚜𝚖𝚊𝚕𝚕𝚎𝚛_𝚛𝚘𝚘𝚝 that takes an input the numbers 𝚊, 𝚋 and 𝚌 and
# returns the smaller solution to this equation if one exists. If the equation has no real
# solution, print the message "𝙴𝚛𝚛𝚘𝚛: 𝙽𝚘 𝚛𝚎𝚊𝚕 𝚜𝚘𝚕𝚞𝚝𝚒𝚘𝚗𝚜" and simply return. Note that, in this case,
# the function will actually return the special Python value 𝙽𝚘𝚗𝚎.

def smaller_root (a,b,c):
    if ((b**2) - (4 * a * c) ) < 0 :
        print ('Error: No real solutions')
    elif ((b ** 2) - (4 * a * c)) == 0:
        print('Equation has only one solution')
    else:
        print('Equation has two solutions, of which the smaller is: ', (-b -  (   (b**2)-4*a*c)**(1/2)   )/(2*a))

#small_solution = (-b -  (   (b**2)-4*a*c)**(1/2)   )/(2*a)

smaller_root(1,2,3)
smaller_root(2, 0, -10)
smaller_root(6, -3, 5)




def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    future = present_value * (1 + rate_per_period)**periods
    return future


print ("$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3))
print (future_value(500,0.04,10,10))

