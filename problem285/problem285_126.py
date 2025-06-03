s=input()
n=len(s)+1
mountain=[0,0]
count=[0,0]
sum=0
for i in range(n-1):
    if s[i]=="<":
        mountain[1]+=1
    else:
        if mountain[1]>0:
            sum+=(mountain[0]*(mountain[0]-1)+mountain[1]*(mountain[1]+1))//2+max([0,mountain[0]-count[1]])
            count=mountain
            mountain=[1,0]
        else:
            mountain[0]+=1

sum+=(mountain[0]*(mountain[0]-1)+mountain[1]*(mountain[1]+1))//2+max([0,mountain[0]-count[1]])

print(sum)
