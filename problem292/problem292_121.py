N = int(input())
*d, = map(int, input().split())
sum = 0
for i in range(len(d)):
    for j in range(i+1, len(d)):
        sum+=d[i]*d[j]
print(sum)