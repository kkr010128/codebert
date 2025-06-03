s=input()
k=int(input())
s0=s[0]
s1=s[-1]
cs=[]
p=s[0]
c=1
for i in range(1,len(s)):
      if p==s[i]:
            c+=1
      else:
            cs.append(c)
            p=s[i]
            c=1
cs.append(c)
if len(cs)==1:
      print((cs[0]*k)//2)
      exit()
ans=0
if s0!=s1:
      for csi in cs:
            ans+=csi//2
      ans*=k
      print(ans)
      exit()
else:
      for i in range(1,len(cs)-1):
            ans+=cs[i]//2
      ans*=k
      ans+=cs[0]//2+cs[-1]//2
      ans+=((cs[0]+cs[-1])//2)*(k-1)
      print(ans)


