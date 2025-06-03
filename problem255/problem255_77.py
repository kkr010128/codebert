n=int(input())
s,t=input().split()

ans=''

for i in range(2*n):
    ans=ans+(s[i//2] if i%2==0 else t[(i-1)//2])

print(ans)
