def func(N):
  result = 0

  for A in range(1,N):
    result += (N-1)//A

  return result

if __name__ == "__main__":
    N = int(input())
    print(func(N))