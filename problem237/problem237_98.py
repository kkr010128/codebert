n = int(input())
arm = []
for _ in range(n):
    x, l = map(int,input().split())
    arm.append([x-l, x+l])
arm.sort(key=lambda x: x[1])
cnt = 0
pr = -float('inf')
for a in arm:
    if pr <= a[0]:
        cnt += 1
        pr = a[1]
print(cnt)
