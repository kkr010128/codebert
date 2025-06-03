import math
n = int(raw_input())
while(n):
    score = map(int, (raw_input()).split(" "))
    m = sum(score)*1.0/n
    dev = [(s-m)*(s-m) for s in score]
    print math.sqrt(sum(dev)*1.0/n)
    n = int(raw_input())