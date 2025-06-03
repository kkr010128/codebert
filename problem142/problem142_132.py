def solve():
  N = input()[-1]
  if N in '3':
    return 'bon'
  if N in '0168':
    return 'pon'
  return 'hon'
print(solve())
