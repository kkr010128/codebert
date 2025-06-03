import sys
import string
N = int(input())
S = input()
s = list(S)
array = string.ascii_uppercase

if not ( 0 <= N <= 26 ): sys.exit()
if not ( 1 <= len(s) <= 10**4 ): sys.exit()
if not S.isupper(): sys.exit()

for I in s:
    if array.index(I) + N <= 25:
        print(array[array.index(I) + N],end='')
    else:
        print(array[(array.index(I) + N) - 26],end='')