# "rock paper scissors lizard spock" game:
# Allows the player to choose one of the 5 options and let him play against the computer.

# rock beats scissors and lizard
# scissors beats lizard and paper
# lizard beats paper and Spock
# paper beats spock and rock
# Spock beats rock and scissors

# If both choose the same, its a tie

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


#Test of name_to_number function:
# name_to_number('rock')
# name_to_number('paper')
# name_to_number('scissors')
# name_to_number('lizard')
# name_to_number('Spock')
# name_to_number('else')

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

#Test of number_to_name function:
#
# number_to_name (0)
# number_to_name (1)
# number_to_name (2)
# number_to_name (3)
# number_to_name (4)
# number_to_name (5)



def game (player_choice):

    number = random.randrange(5)
    print (' ')
    print ('You have chosen: ')
    print number_to_name(number)
    print (' ')

    comp_number = random.randrange(5)
    print ("Computer chose: ")
    print number_to_name(comp_number)
    print (' ')

    decideWinner(number, comp_number)
    # print ('The computer chooses: ')
    # print (comp_number)
    # print (' ')
    # print('The resulting number is:')
    # result = number - comp_number
    # print (result)

def decideWinner (user_num, cpu_num):

    if user_num == cpu_num:
        print ("It's a tie")
        return
    elif user_num > cpu_num:
        first = user_num
        second = cpu_num
    else:
        first = cpu_num
        second = user_num

    mod = (first - second) % 5

    if mod == 1 or mod == 2:
        winner = number_to_name(first)
    else:
        winner = number_to_name(second)

    print ("Winner is: ")
    print (winner)

#Test of rpsls

game ('')