s = input()
d = input()

c=0
for i in range(len(s)):
    if s[i]!=d[i]:
        c+=1
print(c)