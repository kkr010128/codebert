from statistics import mean
import math

while True:
    ans = 0
    n = int(input())
    if n == 0:
        break
    scores = list(map(int, input().split()))
    m = mean(scores)
    for s in scores:
        ans += (s - m)**2
    print(math.sqrt(ans/n))
