N = int(input())
S = ""
Num = 0
Ans = []

for i in range(15):
  if not N:
    break
    
  r = (N-1) % 26 +1
  #print("r=", r)
  N = (N-1) // 26
  S += chr(ord("a")+r-1)
  
print(S[::-1])