X,Y = map(int, input().split()) 

ans = "No"

for turtle in range(X+1):
  crain = X - turtle
  if 2 * crain + 4 * turtle == Y:
    ans = "Yes"

print(ans)