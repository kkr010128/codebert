import sys
k = int(input())
a = dict()
cnt = 0
base = 0
while True:
    cnt += 1
    base = (base*10+7)%k
    if base == 0:
        break
    if base in a:
        cnt = -1
        break
    else:
        a[base] = 1
print(cnt)