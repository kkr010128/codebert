N = int(input())
flag = 0
ans = "No"
for i in range(N):
  A,B = input().split()
  if A == B:    
    flag += 1
  else:
    flag = 0
  if flag == 3:
    ans = "Yes"
    break
    
print(ans)