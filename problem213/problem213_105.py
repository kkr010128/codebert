n = int(input())
l = list(map(int,input().split()))
min_sum = 10**9
for i in range(min(l),max(l)+1):
    min_sum = min(min_sum,sum([(j-i)**2 for j in l]))

print(min_sum)