N = int(input())
As = list(map(int,input().split()))
max = 0
sum = 0
for i in range(N):
    if max < As[i]:
        max = As[i]
    else:
        sum += (max-As[i])

print(sum)
