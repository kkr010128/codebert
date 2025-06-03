n,k,s = map(int,input().split(" "))
ar = []
for i in range(k):
    ar.append(s)
for i in range(n-k):
    if s == 10 ** 9:
        ar.append(1)
    else:
        ar.append(s + 1)
for i in range(n-1):
    print(ar[i],end=" ")
print(ar[n-1])