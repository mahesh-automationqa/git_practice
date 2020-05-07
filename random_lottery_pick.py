'''Question 2: Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
The lottery number must be 5 digits long.
All 100 ticket number must be unique.
'''

import random

lottery_tickets_list = []
print("Creating 100 random lottery tickets")
# to get 100 ticket
for i in range(100):
    # ticket number must be 5 digit (10000, 99999)
    lottery_tickets_list.append(random.randrange(10000, 99999))
# pick 2 luck tickets
winners = random.sample(lottery_tickets_list, 2)
print("Lucky 2 lottery tickets are: ", winners)