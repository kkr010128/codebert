import math
while True:
    n = int(input())
    if n == 0: break
    s = list(map(int, input().split()))
    ave = sum(s) / n
    S = []
    for i in range(n):
        key = ave - s[i]
        S.append(key * key)
    print('{:.5f}'.format(math.sqrt(sum(S) / n)))

