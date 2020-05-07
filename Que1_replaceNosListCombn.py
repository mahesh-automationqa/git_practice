'''
There are two numbers 3358 & 2583, 3 can be replaced by 8,
and 8 can be replaced by 3. List out all combinations of interchangeable numbers and
display maximum, minimum and average of number
'''
for number in [2583]:
    startnum = list(str(number))
    threes_and_eights = [z for z in range(len(startnum)) if startnum[z] in "38"]
    binary_switches = [list(f'{i:#016b}'[-len(threes_and_eights):]) for i in range(2 ** len(threes_and_eights))]
    num_list = []
    for i in binary_switches:
        for ix, j in enumerate(i):
            if j == '0':
                startnum[threes_and_eights[ix]] = '3'
            else:
                startnum[threes_and_eights[ix]] = '8'
        num_list.append(int(''.join(startnum)))
print(f"\nNumber: {number}. \ninterchangeable Variants: {num_list}")
print(f"Minimum: {min(num_list)},  Maximum: {max(num_list)}, Average: {sum(num_list) / len(num_list)}")
print(f'After Replace 2583 the Replaced Number is: {num_list[1]}')

for number in [3358]:
    startnum = list(str(number))
    threes_and_eights = [z for z in range(len(startnum)) if startnum[z] in "38"]
    binary_switches = [list(f'{i:#016b}'[-len(threes_and_eights):]) for i in range(2 ** len(threes_and_eights))]
    num_list = []
    for i in binary_switches:
        for ix, j in enumerate(i):
            if j == '0':
                startnum[threes_and_eights[ix]] = '3'
            else:
                startnum[threes_and_eights[ix]] = '8'
        num_list.append(int(''.join(startnum)))
print(f"\nNumber: {number}. \ninterchangeable Variants: {num_list}")
print(f"Minimum: {min(num_list)},  Maximum: {max(num_list)}, Average: {sum(num_list) / len(num_list)}")
print(f'After Replace 3358 the Replaced Number is: {num_list[6]}')



'''
Help
from itertools import product
replacements = [seq for seq in product("38", repeat=2)]
print(replacements)


for number in [3358]:
    startnum = list(str(number))
    threes_and_eights = [z for z in range(len(startnum)) if startnum[z] in "38"]
    print(startnum)
    print(threes_and_eights)
'''