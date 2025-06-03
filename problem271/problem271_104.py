n=int(input())
al='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans=[]
s=input()
for i in range(len(s)):
  ans.append(al[(ord(s[i])-65+n)%26])
print(''.join(ans))