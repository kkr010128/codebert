n=int(input())
s=input()
r=s.count('R')
g=s.count('G')
b=s.count('B')
ans=r*g*b
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]!=s[j]:
            k=j+j-i
            if k>=len(s):
                break
            else:
                if s[i]!=s[k] and s[j]!=s[k]:
                    ans-=1
print(ans) 
