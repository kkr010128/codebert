n = int(input())

a = list(map(int,input().split()))

ap = {}
am = {}


for i in range(1,n+1):
    j = i - 1

    if (i + a[j]) in ap:
        ap[i+a[j]] = ap[i+a[j]] + 1
    else:
        ap[i+a[j]] = 1
    
    if (i - a[j]) in am:
        am[i-a[j]] = am[i-a[j]] + 1
    else:
        am[i-a[j]] = 1

ans = 0
for i in ap.keys():
    if i in am:
        ans += am[i] * ap[i]
print(ans)