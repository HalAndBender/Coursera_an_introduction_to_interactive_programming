# Write a Python function 𝚙𝚛𝚒𝚗𝚝_𝚍𝚒𝚐𝚒𝚝𝚜 that takes an integer 𝚗𝚞𝚖𝚋𝚎𝚛 in
# the range [0,100) and prints the message "𝚃𝚑𝚎 𝚝𝚎𝚗𝚜 𝚍𝚒𝚐𝚒𝚝 𝚒𝚜 %, 𝚊𝚗𝚍 𝚝𝚑𝚎 𝚘𝚗𝚎𝚜 𝚍𝚒𝚐𝚒𝚝 𝚒𝚜 %." where
# the percents should be replaced with the appropriate values. The function should
# include an error check for the case when 𝚗𝚞𝚖𝚋𝚎𝚛 is negative or greater than or equal to 100.
# In those cases, the function should instead print "𝙴𝚛𝚛𝚘𝚛: 𝙸𝚗𝚙𝚞𝚝 𝚒𝚜 𝚗𝚘𝚝 𝚊 𝚝𝚠𝚘-𝚍𝚒𝚐𝚒𝚝 𝚗𝚞𝚖𝚋𝚎𝚛."

def print_digits (integer):
    if integer >=0 and integer <= 100:
        print ('The tens digit is', integer // 10, 'and the ones digit is', integer % 10 )
    else:
        print ('Error: Input is not a two-digit number.')

print_digits(12)
print_digits(100)
print_digits(46)
print_digits(103)
print_digits(-4)