s=input()
r=input()
n=len(s)
c=0
for i in range(n):
    if(s[i]!=r[i]):
        c=c+1
print(c)
