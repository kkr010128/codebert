import sys
import string

C = input()

if C == 'z' : sys.exit()

pos = string.ascii_lowercase.index(C)+1
print(string.ascii_lowercase[pos])