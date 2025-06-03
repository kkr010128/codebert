import math
N, K = map(int,input().split())
logs = list(map(int,input().split()))
a = 0
b = max(logs)
b_memo = set()
count=0
flg =0
while math.ceil(a) != math.ceil(b):
    c = (a+b)/2
    times = []
    for i in logs:
        times.append(math.floor(i/c))
    if sum(times) > K:
        a = c
    else:
        b = c
    if b - a < 0.001:
        count +=1
    if count >20:
        flg+=1
        break
if flg == 0:         
    print(math.ceil(b))
else:
    a = math.ceil(a)
    times = []
    for j in logs:
        times.append(math.floor(i/a))
    if sum(times) > K:
        print(math.ceil(b))   
    else:
        print(math.ceil(a)) 