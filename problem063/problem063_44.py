#coding: UTF-8
import sys

table = [0]*26

letters = [chr(i) for i in range(97, 97+26)]
input_str = sys.stdin.read()

for A in input_str:
    index = 0
    for B in letters:
        if A == B or A == B.upper():
            table[index] += 1
            break
        index += 1

for i in range(len(letters)):
    print("%s : %d"%(letters[i], table[i]))

