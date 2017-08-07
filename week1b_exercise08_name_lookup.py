# Write a Python function 𝚗𝚊𝚖𝚎_𝚕𝚘𝚘𝚔𝚞𝚙 that takes a string 𝚏𝚒𝚛𝚜𝚝_𝚗𝚊𝚖𝚎 that corresponds
# to one of ("𝙹𝚘𝚎", "𝚂𝚌𝚘𝚝𝚝", "𝙹𝚘𝚑𝚗" or "𝚂𝚝𝚎𝚙𝚑𝚎𝚗") and then returns their
# corresponding last name ("𝚆𝚊𝚛𝚛𝚎𝚗", "𝚁𝚒𝚡𝚗𝚎𝚛", "𝙶𝚛𝚎𝚒𝚗𝚎𝚛" or "𝚆𝚘𝚗𝚐"). If 𝚏𝚒𝚛𝚜𝚝_𝚗𝚊𝚖𝚎
# doesn't match any of those strings, return the string "𝙴𝚛𝚛𝚘𝚛: 𝙽𝚘𝚝 𝚊𝚗 𝚒𝚗𝚜𝚝𝚛𝚞𝚌𝚝𝚘𝚛".

def name_lookup (first_name):
    if first_name == 'Joe':
        print (" Joe's last name is Warren")
    elif first_name == 'Scott':
        print (" Scott's last name is Rixner")
    elif first_name == 'John':
        print (" John's last name is Greiner")
    elif first_name == 'Stephen':
        print (" Stephen's last name is Wong")
    else:
        print ('Error: Not an instructor')

name_lookup ('Joe')
name_lookup ('Scott')
name_lookup('John')
name_lookup('Stephen')
name_lookup('Harry')

#Solution:
# def name_lookup(first_name):
#
#
#     if first_name == "Joe":
#         return "Warren"
#     elif first_name == "Scott":
#         return "Rixner"
#     elif first_name == "John":
#         return "Greiner"
#     elif first_name == "Stephen":
#         return "Wong"
#     else:
#         return "Error: Not an instructor"
#
# def test(first_name):
#
#
#     print
#     name_lookup(first_name)
#
#
# test("Joe")
# test("Scott")
# test("John")
# test("Stephen")
# test("Mary")