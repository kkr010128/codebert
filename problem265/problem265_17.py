n=int(input())
ans=0
for i in range(1,50000+1):
    z=i*1.08
    if n<=z<(n+1):
        ans=i
        break
if ans==0:
    print(":(")
else:
    print(ans)

