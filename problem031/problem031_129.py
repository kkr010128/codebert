import math
while True:
    n=int(input())
    if n==0:
        break
    else:
        score=list(map(int,input().split()))
        dev=math.sqrt(sum((x-sum(score)/len(score))**2 for x in score)/len(score))
        print("{:.8f}".format(dev))

