from sys import stdin


n = int(stdin.readline().strip())
a_lst = [int(x) for x in stdin.readline().strip().split()]

pos = len(a_lst) // 2
min_diff = 10000000000000000000

while(True):
  left = sum(a_lst[:pos])
  right = sum(a_lst[pos:])
  diff = right - left
  
  if min_diff > abs(diff): min_diff = abs(diff)
  else: break
  
  if diff > 0: pos += 1
  elif diff < 0: pos -= 1
    
print(min_diff)