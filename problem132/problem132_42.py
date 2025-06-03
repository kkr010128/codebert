def count_num_light(a):
  ret = [0 for _ in range(len(a))]
  n = len(a)
  for i in range(n):
    start = max(0, i-a[i])
    end = min(n-1, i+a[i])
    ret[start] += 1
    if end+1 < n:
      ret[end+1] -= 1
  for i in range(1,n):
    ret[i] += ret[i-1]
  
  return ret
                  
n, k = map(int, input().split())
a = list(map(int, input().split()))
num_light = count_num_light(a)
 
for i in range(k-1):
  num_light = count_num_light(num_light)
  if sum(num_light) == n**2:
    break
    
print(*num_light)
