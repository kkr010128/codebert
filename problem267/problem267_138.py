N = int(input())
S =list(map(int,input()))

ans = 0

for x in [0,1,2,3,4,5,6,7,8,9]:
  if x in S:
    x_index = S.index(x)
    for y in [0,1,2,3,4,5,6,7,8,9]:
      if y in S[x_index+1:]:
        y_index = S[x_index+1:].index(y)
        for z in [0,1,2,3,4,5,6,7,8,9]:
          if z in S[x_index + 1 + y_index+1:]:
            ans += 1
print(ans)