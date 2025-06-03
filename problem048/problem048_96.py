n = int(input())
l = list(map(int,input().split()))

mini = min(l)
maxi = max(l)
sums = 0

for i in range(0,n):
    sums = sums + int(l[i])
    
print(f"{mini} {maxi} {sums}")
