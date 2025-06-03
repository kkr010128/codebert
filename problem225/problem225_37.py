H,A = map(int,input().split())
 
answer = 0
if H %A != 0:
  answer = H//A + 1
else:
  answer = H / A
  
print(int(answer))
