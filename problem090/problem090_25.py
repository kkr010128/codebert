# rainy season

def rainy(S):
  if 'RRR' in S:
    return 3
  if 'RR' in S:
    return 2
  if 'R' in S:
    return 1
  return 0

if __name__ == "__main__":
  input = list(input().split())
  print(rainy(input[0]))
