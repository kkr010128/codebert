# C - Traveling Salesman around Lake

k,n = map(int,input().split())
a = list(map(int,input().split()))
bet = [a[0]+k-a[n-1]]

for i in range(n-1):
    bet.append(a[i+1]-a[i])

print(k-max(bet))
