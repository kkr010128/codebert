import sys
input_str = sys.stdin.read()
table = [0]*26
letters = "abcdefghijklmnopqrstuvwxyz"
for A in input_str:
    index = 0
    for B in letters:
        if A == B or A == B.upper():
            table[index] += 1
            break
        index += 1
for i in range(len(letters)):
    print("{} : {}".format(letters[i],table[i]))

