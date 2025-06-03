n = int(input())

t = [0]*(n+1)
for i in range(1,n+1):
    for j in range(i,n+1,i):
        t[j] += j
print(sum(t))
