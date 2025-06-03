n = int(input())
s = [int(i) for i in input().split()]
s.sort()
flag = False
for i in range (0,n-1):
  if s[i] == s[i+1]:
    flag = True
    break
if flag == True:
  print("NO")
else: print("YES")