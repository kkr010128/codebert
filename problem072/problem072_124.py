n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
#print(l[0][0])
#print(l[0][1])
ans = n-2
ans1 = 0

for m in range(ans):
  if l[m][0]  == l[m][1] and l[m+1][0] == l[m+1][1] and l[m+2][0] == l[m+2][1]:
    ans1 += 1
 
    
    
if ans1 >= 1:
  print("Yes")
else:
  print("No")