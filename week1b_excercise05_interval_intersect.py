# Write a Python function 𝚒𝚗𝚝𝚎𝚛𝚟𝚊𝚕_𝚒𝚗𝚝𝚎𝚛𝚜𝚎𝚌𝚝 that takes
# parameters 𝚊, 𝚋, 𝚌, and 𝚍 and returns 𝚃𝚛𝚞𝚎 if the
# intervals [a,b] and [c,d] intersect and 𝙵𝚊𝚕𝚜𝚎 otherwise.
# While this test may seem tricky, the solution is actually
# very simple and consists of one line of Python code.
# (You may assume that a≤b and c≤d.)

def interval_intersect(a,b,c,d):
    return  b>=c and d>=a #this must be 'and'!! not 'or' !!


def test(a,b,c,d):
    if interval_intersect(a,b,c,d):
        print(a,b,c,d, ' do intersect')
    else:
        print (a,b,c,d, ' do not intersect')

test (2,3,5,6)
test (2,4,3,5)
test (1,4,5,8)
test (1,5,2,12)
test(1,4,4,6)
