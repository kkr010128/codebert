n, k, c = map(int, input().split())
S = input()

# 要素の値は何回目の働く日か(0は働いていない状態)
by_left = [0] * n
by_right = [0] * n

# 左から貪欲
rest = 0
cnt = 1
for itr, s in enumerate(S):
  rest -= 1
  if rest <= 0 and s == "o":
    by_left[itr] = cnt
    cnt += 1
    rest = c + 1
    
# 右から貪欲
rest = 0
cnt = k
for itr, s in enumerate(S[::-1]):
  rest -= 1
  if rest <= 0 and s == "o":
    by_right[n - itr- 1] = cnt
    cnt -= 1
    rest = c + 1

# 左右からの貪欲で、どちらでも同じ働く回数の値が入っている日が必ず働く日
ans = [itr + 1 for itr, (i, j) in enumerate(zip(by_left, by_right)) if i != 0 and i == j]

for a in ans:
  print(a)