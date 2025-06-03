num = int(input())

if num%2 == 0:
  ans = float(1/2)
  
else:
  ans = float((num//2 + 1)/num)

print(ans)