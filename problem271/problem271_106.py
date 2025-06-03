n = int(input())
s = input()
ans=[]

for i in s:
  a = chr(ord('A')+(ord(i)-ord('A')+n)%26)
  ans.append(a)

print(('').join(ans))