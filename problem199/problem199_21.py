s=list(input())
f=1
for i in range(len(s)):
    if i%2 and s[i]!="i":
        f=0
    elif i%2==0 and s[i]!="h":
        f=0
    elif s[0]!="h" or s[-1]!="i":
        f=0
print("Yes" if f else "No")
