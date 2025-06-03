n,m = map(int, input().split())
height_list = list(map(int, input().split()))

heightest_list = [0] * n
for _ in range(m):
  a,b = map(int, input().split())
  heightest_list[a-1] = max(heightest_list[a-1], height_list[b-1])
  heightest_list[b-1] = max(heightest_list[b-1], height_list[a-1])

result = 0
for i in range(n):
  if height_list[i] > heightest_list[i]:
    result += 1

print(result)