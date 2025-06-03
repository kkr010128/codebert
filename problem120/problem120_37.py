n,k=[int(i) for i in input().strip().split(" ")]
arr=[int(i) for i in input().strip().split(" ")] 
ans=0
arr=sorted(arr)
for i in range(k):
    ans+=arr[i]
print(ans)