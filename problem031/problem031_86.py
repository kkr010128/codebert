from math import sqrt
while True:
    n = int(input())
    if n == 0:
        break
    scores = list(map(int,input().split()))
    m = sum(scores)/len(scores)
    print(sqrt(sum((sc -m)**2 for sc in scores)/len(scores)))