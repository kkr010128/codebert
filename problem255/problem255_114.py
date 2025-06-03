n=int(input())
s,t=input().split()
ans=""
for i,j in zip(list(s),list(t)):ans+=i+j
print(ans)