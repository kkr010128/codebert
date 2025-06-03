def resolve():
  N = int(input())
  count = 0

  for A in range(1, N):
    count += ((N-1)//A)
  print(count)

if __name__ == "__main__":
  resolve()