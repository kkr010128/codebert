a, b, c = list(map(int, input().split()))
k = int(input())

for i in range(k+1) :
  if a >= b :
    b *= 2
  elif b >= c :
    c *= 2
  else :
    print("Yes")
    exit()
    
print("No")
