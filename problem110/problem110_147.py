H,W,K = map(int,input().split())
array = [ list(input()) for k in range(H)]
ans = 0
for bit_row in range(2**H):
  for bit_line in range(2**W):
    count = 0
    for i in range(H):
      for j in range(W):
        if ( bit_row >> i ) & 1 == 0 and ( bit_line >> j ) & 1 == 0:
          if array[i][j] == '#':
            count += 1
    if count == K:
      ans += 1
print( ans )