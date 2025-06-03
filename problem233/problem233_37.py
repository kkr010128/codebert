n = int(input())
l = list(map(int, input().split()))

cnt = 0
minimun = max(l)
for i in range(n):
    if l[i] <= minimun:
        cnt += 1
        minimun = l[i]
print(cnt)



