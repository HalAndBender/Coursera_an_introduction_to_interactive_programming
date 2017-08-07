
def is_lunchtime (hour, is_am):
    if (hour == 11 and is_am == 'am') or (hour == 12 and is_am == 'pm' ):
        return True
    else:
        return False

print('11am', is_lunchtime(11,'am'))
print(is_lunchtime(12,'pm'))
print(is_lunchtime(11,'pm'))