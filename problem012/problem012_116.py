import sys
readline = sys.stdin.readline
prime = set([2])
for i in range(3, 10000, 2):
    for j in prime:
        if i % j == 0:
            break
    else:
        prime.add(i)
n = int(input())
cnt = 0
for i in (int(readline()) for _ in range(n)):
    if i in prime:
        cnt += 1
        continue
    for j in prime:
        if i % j == 0:
            break
    else:
        cnt += 1
print(cnt)

