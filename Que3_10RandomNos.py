''' Problem:
Generate 10 random numbers, add them to a list and print the list.
If the program is ran 2 times, different set of numbers should be printed.
Additional difficulty, the numbers should be less than 100.
'''

import random
my_list = list(range(1, 100, 10)) # Shows 10 Random numbers between 1 to 100
random.shuffle(my_list)
print(my_list)
