# Write a Python function 𝚗𝚊𝚖𝚎_𝚊𝚗𝚍_𝚊𝚐𝚎 that take as input the
# parameters 𝚗𝚊𝚖𝚎 (a string) and 𝚊𝚐𝚎 (a number) and returns a
# string of the form "% 𝚒𝚜 % 𝚢𝚎𝚊𝚛𝚜 𝚘𝚕𝚍." where the percents are
# the string forms of 𝚗𝚊𝚖𝚎 and 𝚊𝚐𝚎. The function should include
# an error check for the case when 𝚊𝚐𝚎 is less than zero. In this
# case, the function should return the string "𝙴𝚛𝚛𝚘𝚛: 𝙸𝚗𝚟𝚊𝚕𝚒𝚍 𝚊𝚐𝚎".

def name_and_age (name, age):
    return age >= 0

def test(name, age):
    if name_and_age (name, age):
        print (name ,'is', age, 'years old')
    else:
        print('Error: Invalid age')

test ('Harry Marry', 24)
test ('Larry Take', 55)
test ('Loise', -3)
