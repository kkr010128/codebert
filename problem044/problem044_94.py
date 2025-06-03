nums=[]
nums=input().split()
a=int(nums[0])
b=int(nums[1])
c=int(nums[2])
ans=0
for i in range(a,b+1):
    if c%i==0:
        ans+=1
print(ans)