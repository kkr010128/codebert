import bisect
n=int(input())
a=list(map(int,input().split()))
suma=[]
sumans=0
for i in range(n):
	sumans += a[i]
	suma.append(sumans)
u=bisect.bisect_right(suma, sumans//2)
print(min(abs(2*suma[u-1]-sumans), abs(2*suma[u]-sumans)))