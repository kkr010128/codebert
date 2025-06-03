import math

def takoyaki(n, x, t)-> int :
  itr = math.ceil(n / x)
  return itr * t

if __name__ == "__main__":
  input = list(map(int, input().split()))
  print(takoyaki(input[0], input[1], input[2]))
