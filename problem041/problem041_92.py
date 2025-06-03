(W, H, x, y, r) = [int(i) for i in input().rstrip().split()]

if x + r <= W and x - r >= 0 and y + r <= H and y - r >= 0:
 print('Yes')
else:
 print('No')