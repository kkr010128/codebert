from math import *
PI = 3.1415926535898
while True:
    try:
        t = input()
        ans = ""
        ans += str(t/(60*60))
        t %= 60*60
        ans += ":"
        ans += str(t/60)
        t %= 60
        ans += ":"
        ans += str(t)
        print ans
    except EOFError:
        break