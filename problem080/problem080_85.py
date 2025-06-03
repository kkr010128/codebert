n = int(input())
x = [None]*n
y = [None]*n

for i in range(n):
    x[i],y[i] = map(int,input().split())


#y=x+k1 <=> x-y=-k1
k1 = [0]*n
#y=-x+k2 <=> x+y=k2
k2 = [0]*n
for i in range(n):
    k1[i] = -(x[i]-y[i])
    k2[i] = x[i]+y[i]

print(max(max(k1)-min(k1),max(k2)-min(k2)))