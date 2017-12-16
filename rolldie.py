import random

four_dice = [1,2,3,4]
six_dice = [1,2,3,4,5,6]
eight_dice = [1,2,3,4,5,6,7,8]
ten_dice = [1,2,3,4,5,6,7,8,9,10]
twelve_dice = [1,2,3,4,5,6,7,8,9,10,11,12]
twenty_dice = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


	
def roll():
        what_die = int(input("How many sides on your dice? 4,6,8,10,12,or 20? \n"))
        if what_die == 4:
                return "You rolled a {}.".format(random.choice(four_dice))
        elif what_die == 6:
                return "You rolled a {}.".format(random.choice(six_dice))
        elif what_die == 8:
                return "You rolled a {}.".format(random.choice(eight_dice))
        elif what_die == 10:
                return "You rolled a {}.".format(random.choice(ten_dice))
        elif what_die == 12:
                return "You rolled a {}.".format(random.choice(twelve_dice))
        elif what_die == 20:
                return "You rolled a {}.".format(random.choice(twenty_dice))
        else:
                return "Invalid input."

print(roll())
