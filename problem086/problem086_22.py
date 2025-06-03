def func(N,X,T):
  result = -(-N // X) * T
  return result

if __name__ == "__main__":
  N,X,T = map(int,input().split())
  print(func(N,X,T))