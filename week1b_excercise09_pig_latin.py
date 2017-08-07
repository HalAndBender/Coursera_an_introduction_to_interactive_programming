# Pig Latin is a language game that involves altering words via a simple set of rules.
# Write a Python function 𝚙𝚒𝚐_𝚕𝚊𝚝𝚒𝚗 that takes a string 𝚠𝚘𝚛𝚍 and applies the following rules
# to generate a new word in Pig Latin. If the first letter in 𝚠𝚘𝚛𝚍 is a consonant, append
# the consonant plus "𝚊𝚢" to the end of the remainder of the word. For example, 𝚙𝚒𝚐_𝚕𝚊𝚝𝚒𝚗("𝚙𝚒𝚐")
# would return "𝚒𝚐𝚙𝚊𝚢". If the first letter in 𝚠𝚘𝚛𝚍 is a vowel, append "𝚠𝚊𝚢" to the end of the word.
# For example, 𝚙𝚒𝚐_𝚕𝚊𝚝𝚒𝚗("𝚘𝚠𝚕") returns "𝚘𝚠𝚕𝚠𝚊𝚢". You can assume that 𝚠𝚘𝚛𝚍 is in lower case.
# The provided template includes code to extract the first letter and the rest of 𝚠𝚘𝚛𝚍 in Python.
# Note that, in full Pig Latin, the leading consonant cluster is moved to the end of the word.
# However, we don't know enough Python to implement full Pig Latin just yet.

# Compute a (simplified) Pig Latin version of a word.

###################################################
# Pig Latin formula
def pig_latin(word):
    """Returns the (simplified) Pig Latin version of the word."""

    first_letter = word[0]
    rest_of_word = word[1:]


    if first_letter == 'a' or first_letter == 'o' or first_letter == 'e' or first_letter == 'i' or first_letter == 'u' :
        print (first_letter + rest_of_word + 'way')
    else:
        print (rest_of_word + first_letter + 'ay')



###################################################
# Tests
# Student should not change this code.

def test(word):
    """Tests the pig_latin function."""

    print
    pig_latin(word)


test("pig")
test("owl")
test("python")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# igpay
# owlway
# ythonpay
