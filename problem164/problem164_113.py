A, B, C, D = map(int, input().split())
while True:
  # 高橋
  C -= B
  if C <= 0:
    print('Yes')
    break
  # 青木
  A -= D
  if A <= 0:
    print('No')
    break