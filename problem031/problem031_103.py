from math import *
while True:
    n = 0
    n = int(input())
    if n == 0:
        break
    else :
        sco = map(int,raw_input().split())
        for i in range(n):
            ave=0.0
            for i in sco:
                ave += i
            ave /= n
            dev = 0.0
            for i in sco:
                dev += (i-ave)*(i-ave)
            dev /= n
        print sqrt(dev)