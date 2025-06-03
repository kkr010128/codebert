n,k=map(int,input().split())
h=list(map(int,input().split()))
sum=0
h.sort()
h=h[:n-k]

if n <= k:
    print(0)
    exit()
else:
    for i in h:
        sum += i
print(sum)