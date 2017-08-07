import random

# Helper function converting names to numbers:
def name_to_number (name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    return False


#helper function converting number to names:
def number_to_name (number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    return False

# computers choosing
def game (player_choice):

    number = random.randrange(5)
    print (' ')
    print ('Hal has chosen: ')
    print number_to_name(number)
    print (' ')

    comp_number = random.randrange(5)
    print ("Bender has chose: ")
    print number_to_name(comp_number)
    print (' ')

#The magic happens here:
    mod = (number - comp_number) % 5

    if mod == 1 or mod == 2:
        print 'Hal wins'
    elif mod == 3 or mod == 4:
        print 'Bender wins'
    else:
        print "It's is a tie"

#Test of rpsls

game ('')