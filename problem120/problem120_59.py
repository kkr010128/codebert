[n, k] = map(int, input().split())
p_list = input().split()
p_list = [int(x) for x in p_list]

p_list.sort()

ans = 0

for i in range(k):
  ans += p_list[i]
  
print(ans)