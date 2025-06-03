def func(A):
  result = 0
  min = 0
  for a in A:
    if a < min:
      result += min - a
    else:
      min = a
  return result

if __name__ == "__main__":
    N = int(input())
    A = list(map(int,input().split()))
    print(func(A))