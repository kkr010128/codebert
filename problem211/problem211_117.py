tmp = input().split(" ")
 
N = int(tmp[0])
R = int(tmp[1])
 
if N >= 10:
  print(R)
else:
  ans = R + 100 * (10 - N)
  print(int(ans))