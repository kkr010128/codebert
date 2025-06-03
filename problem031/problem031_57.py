import math
while True:
    n = int(input())
    if n == 0:
        break
    
    s = list(map(int, input().split()))
    m = sum(s)/n
    v = 0
    for i in s:
        v += (i - m) ** 2
    ans = math.sqrt(v/n)
    print("{:.5f}".format(ans))
        

