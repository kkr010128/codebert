import sys


table = [0]*26

letters = "abcdefghijklmnopqrstuvwxyz"
input_str = sys.stdin.read()

for A in input_str:
    ind = 0
    for B in letters:
        if A == B or A == B.upper():
            table[ind] += 1
            break
        ind += 1

for i in range(len(letters)):
    print("%s : %d"%(letters[i],table[i]))
