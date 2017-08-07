def greet(friend, money):
    if friend and (money > 20):
        print ('Hi, I know you, I am giving you money!')
        money = money - 20
    elif friend:
        print ('Hello! I know you, but I dont have any money')
    else:
        print ('Ha ha. I am mugging you, Give me 10 money!')
        money = money + 10
    return money

money = 15

money = greet(True, money)
print ('Money in pocket: ' + str(money))
print (' ')

money = greet(False, money)
print ('Money in pocket: ' + str(money))
print (' ')

money = greet(True, money)
print ('Money in pocket: ' + str(money))
print (' ')