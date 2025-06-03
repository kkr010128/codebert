n, k = map(int, input().split())

okashi = set()
for _ in range(k):
  d = int(input())
  lst = [int(i) for i in input().split()]
  for i in range(d):
    if lst[i] not in okashi:
      okashi.add(lst[i])
count = 0
for i in range(n):
  if i + 1 not in okashi:
    count += 1
print(count)