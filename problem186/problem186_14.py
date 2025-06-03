k,n = map(int,(input().split()))
a = list(map(int,input().split()))
maxDis = 0

for i in range(len(a)-1):
    if i == 0:
        maxDis = a[i]+k-a[i-1]
    elif abs(a[i]-a[i-1]) > maxDis:
        maxDis = abs(a[i]-a[i-1])
    if abs(a[i]-a[i+1]) > maxDis:
        maxDis = abs(a[i]-a[i+1])

print(k-maxDis)
