N=int(input())

if N&0b1:
    ans=N//2+1
else:
    ans=N//2

print(ans)