#D - Brick Break
N = int(input())
a = list(map(int,input().split()))

num = 1
count = 0
for i in range(N):
    if a[i] == num:
        num += 1
    else:
        count += 1
result = count
if result == N:
    result = '-1'
print(result)