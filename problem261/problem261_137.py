s=input()
t=s[::-1]
num=0
for i in range(len(s)):
    if s[i]!=t[i]:
        num+=1
print(num//2)
