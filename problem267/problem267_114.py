N = int(input())
S = list(map(int, input()))
ans = 0
first = [0] * 10
a = 0
for i in range(N):
  if first[S[i]] == 0:
    first[S[i]] = 1
    a += 1
    second = [0] * 10
    b = 0
    for j in range(i+1, N):
      if second[S[j]] == 0:
        second[S[j]] = 1
        b += 1
        third = [0] * 10
        c = 0
        for k in range(j+1, N):
          if third[S[k]] == 0:
            third[S[k]] = 1
            ans += 1
            c += 1
            if c == 10:
              break
        if b == 10:
          break
    if a == 10:
      break
print(ans)