N, K = map(int, input().split())
W = []
for _ in range(N):
  W.append(int(input()))
    
def carriable(p):
  if p < max(W):
    return False
  
  k_count = 0
  current_weight = 0
  for w in W:
    if current_weight + w <= p:
      current_weight += w
    else:
      if k_count + 1 < K:
        k_count += 1
        current_weight = w
      else:
        return False
      
  return True

def solve():
  min_p = 0
  max_p = sum(W)
  current_p = (max_p + min_p) // 2
  
  while True:    
    if min_p == current_p:
      return max_p
    
    if carriable(current_p):
      max_p = current_p
    else:
      min_p = current_p
    current_p = (max_p + min_p) // 2
    
print(solve())
