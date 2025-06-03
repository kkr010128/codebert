def func(N):
  strN = str(N)
  sum = 0
  for s in strN:
    sum += int(s)
  return "Yes" if sum % 9 == 0 else "No"

if __name__ == "__main__":
  N = str(input())
  print(func(N))