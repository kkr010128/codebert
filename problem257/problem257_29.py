N = int(input())
a = list(map(int,input().split()))
num = 1
for i in range(N):
    if a[i] == num:
        num += 1
if num == 1:
    print(-1)
    exit()
print(N - num + 1)