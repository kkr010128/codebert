import math
N, K = map(int,input().split())
logs = list(map(int,input().split()))
a = 0
b = max(logs)
b_memo = set()
count=0
flg =0
while b-a > 1:
    c = (a+b)//2
    times = []
    for i in logs:
        times.append(math.ceil(i/c)-1)
    if sum(times) > K:
        a = c
    else:
        b = c

print(b)