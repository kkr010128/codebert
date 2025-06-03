from math import *
while True:
    n = input()
    if n==0:
        break
    score_li = map(int,raw_input().split())
    score_sum = sum(score_li)
    ave = score_sum/float(n)
    variance = 0
    for i in xrange(n):
        variance += (score_li[i]-ave)**2
    variance /=float(n)
    sd = sqrt(variance) #sd:standard deviation
    print sd