h, w = map(int, input().split())
s = []
score = [[0] * w for i in range(h)]
for i in range(h):
  s.append(list(input()))
  for j in range(w):
    if i == 0:
      if j == 0:
        score[0][0] = 1 if s[0][0] == '#' else 0
      else:
        score[0][j] = score[0][j-1]
        if s[0][j] == '#' and s[0][j-1] != '#':
          score[0][j] += 1
    else:
      if j == 0:
        score[i][0] = score[i-1][0]
        if s[i][0] == '#' and s[i-1][0] != '#':
          score[i][0] += 1
      else:
        r = score[i][j-1]
        if s[i][j] == '#' and s[i][j-1] != '#':
          r += 1
        d = score[i-1][j]
        if s[i][j] == '#' and s[i-1][j] != '#':
          d += 1
        score[i][j] += min(r, d)
print(score[-1][-1])