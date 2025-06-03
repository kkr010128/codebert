H=int(input())
ans = 0
count = 0
while H>0:
    H=int(H/2)
    ans+=2**count
    count+=1
print(ans)