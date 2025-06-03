n=int(input())
s=input()
ans=""
for i in range(len(s)):
    a=(ord(s[i])+n-65)%26
    ans=ans+chr(a+65)
print(ans)