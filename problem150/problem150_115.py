from sys import stdin
n,k = map(int,stdin.readline().split())
a = list(map(int,stdin.readline().split()))
for i in range(n):
    a[i] -= 1
d = {}
d[0] = 0
cur = 0
step = 0
while step < k:
    cur = a[cur]
    step += 1
    if cur in d:
        looplen = step - d[cur]
        step += looplen * ((k-step)//looplen)
    else:
        d[cur] = step
print(cur + 1)
