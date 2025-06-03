n,k,s = map(int,input().split())

a = [s] * n
for i in range(k,n):
    a[i] +=1-(s==10**9)*s
print(*a)

