from math import ceil, floor

def resolve():
  N = int(input())
  tax = 0.08

  if floor(ceil(N/(1+tax))*(1+tax)) == N:
    print(ceil(N/(1+tax)))
  else:
    print(":(")

if __name__ == "__main__":
  resolve()