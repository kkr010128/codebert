s=str(input())
c=len(s)//2
e=0
for i in range(0,c):
    if(s[i]!=s[len(s)-1-i]):
        e=e+1
print(e)