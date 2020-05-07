''' Problem:
Accept a string as input. Reverse the order of words in a string.
e.g. if string input is "Today is Wednesday"
the output should be "Wednesday is Today"
'''
'''
#SOLUTION 1
accept = input(str("Please enter a String: "))
reverse_str = accept.split() # First Split the entered list
reverse_str.reverse()
result = " ".join(reverse_str)
print(result)
'''


# SOLUTION2
def reverse_string_words(accept):
    while True:
        accept = input(str("Please enter a String: ")).strip()
        for accept in accept.split('\n'):
            if accept == '':
                print("Please enter a string input seems you did't enter any input")
                continue
            elif (accept >= 'a' and accept <= 'z') or (accept >= 'A' and accept <= 'Z'):
                pass
            else:
                print("Please enter String inputs only.. ")
                continue

            return ' '.join(accept.split()[::-1])


print(reverse_string_words(""))

