def dist (s1,s2):
    x1=s1[0]
    y1=s1[1]
    x2=s2[0]
    y2=s2[1]
    a=(x1-x2)**2+(y1-y2)**2
    return pow(a,0.5)
arr=[]
n=int(input())
for _ in range(n):
    inp=list(map(int,input().split()))
    arr.append((inp[0],inp[1]))
ans=0
for i in range(len(arr)):
    for j in range(len(arr)):
        ans+=dist(arr[i],arr[j])
print (ans/n)