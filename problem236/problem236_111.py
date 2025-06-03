H=int(input())
W=int(input())
N=int(input())

if H<=W: big=W
else: big=H
if N%big==0: ans=N//big
else: ans=N//big+1
print(ans)