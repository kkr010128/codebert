import sys
input = sys.stdin.readline
from string import ascii_uppercase

letters = ascii_uppercase + ascii_uppercase
shift = int(input())
s = input()[:-1]
for char in s: print(letters[letters.index(char) + shift], end = '')
print()