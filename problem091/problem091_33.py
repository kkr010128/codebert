from itertools import combinations
def triangle(l_tuple):
  if len(set(l_tuple)) == 3:
    if l_tuple[0] + l_tuple[1] > l_tuple[2] and l_tuple[1] + l_tuple[2] > l_tuple[0] and l_tuple[2] + l_tuple[0] > l_tuple[1]:
      return True
  return False
n = int(input())
l = list(map(int, input().split()))
l_comb = list(combinations(l, 3))
cnt = 0
for i in l_comb:
  if triangle(i):
    cnt += 1
print(cnt)