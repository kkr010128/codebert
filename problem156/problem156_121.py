X = int(input())
import sys
for a in range(-118, 120, 1):
    for b in range(-119, 119, 1):
        if X == pow(a,5) - pow(b,5):
            print(a, b)
            sys.exit()