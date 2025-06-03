n=int(input())
s=input()
ans=''
for i in s:
    if ord(i)+n>ord('Z'):
        ans+=chr(ord(i)+n-26)
    else:
        ans+=chr(ord(i)+n)
print(ans)