from math import ceil
n=int(input())
lst=list(map(int, input().split()))
cut=ceil(n/2)
lst=sorted(lst,reverse=True)
arr=lst[:cut]
f=arr[0]
if n%2==0:
    for i in range(1,len(arr)):
        f+=2*arr[i]
else:
    for i in range(1,len(arr)):
        if i==len(arr)-1:
            f+=arr[i]
        else:
            f+=2*arr[i]
print(f)