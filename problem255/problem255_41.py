n=int(input())
s=input().split()
a=s[0]
b=s[1]
ans=''
for i in range(len(a)):
  ans+=a[i]
  ans+=b[i]
print (ans)