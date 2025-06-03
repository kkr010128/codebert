n, k = map(int, input().split())
lst = [0] + list(map(int, input().split()))
dic = {1:0}
loc = 1
for i in range(1, k + 1):
  loc = lst[loc]
  if loc not in dic:
    dic[loc] = i
  else:
    span = i - dic[loc]
    initial = dic[loc]
    z = (k - initial) % span
    for j in range(z):
      loc = lst[loc]
    print(loc)
    exit()
print(loc)