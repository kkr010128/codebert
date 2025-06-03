N, M = map(int, input().split())
countlis = [0] * (N+1)
penalty = 0
clear = 0
checkset = set()
for i in range(1,M+1):
    p,s = input().split()
    p = int(p)
    if p in checkset:
        continue
    if s == "WA":
        countlis[p] += 1
    elif s == "AC":
        penalty += countlis[p]
        clear += 1
        checkset.add(p)

print("{0} {1}".format(clear, penalty))