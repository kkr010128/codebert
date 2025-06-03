#! /usr/lib/python3
import fractions
while True:
    try:
        a, b=map(int, input().split())
        s=fractions.gcd(a,b)
        print("{0} {1:.0f}".format(s,a*b/s))
    except:
        break