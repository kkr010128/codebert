s=input()
n=0
m=0
for i in range(len(s)):
    if s[i]=='S':
        n=0
    else:
        n+=1
        m=n
print(m)