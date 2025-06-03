K=int(input())
num=7
ans=-1
for n in range(pow(10,7)):
    if num%K==0:
        ans=n+1
        break
    shou=num//K
    num-=K*shou
    num=int(str(num)+'7')
print(ans)
