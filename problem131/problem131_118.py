a_index, a_v = map(int, input().split())
b_index, b_v = map(int, input().split())
t = int(input())
 
d = abs(b_index - a_index)
d_v = a_v - b_v
 
if d == 0 :
  print("YES")
elif d_v > 0 and d / d_v <= t :
  print("YES")
else :
  print("NO")