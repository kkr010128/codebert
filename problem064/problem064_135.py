s=input()
p=input()
result="No"
for i in range(len(s)):
    r=s[i:]+s[:i]
    if r[0:len(p)]==p:
        result="Yes"
        break
print(result)