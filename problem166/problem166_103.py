from collections import Counter
s=input()[::-1]
DP=[0]

num,point=0,1
for i in s:
    num +=int(i)*point
    num %=2019
    DP.append(num)
    point *=10
    point %=2019

ans=0
DP=Counter(DP)
for v,m in DP.items():
    if m>=2:
        ans +=m*(m-1)//2
print(ans)