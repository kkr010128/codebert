import sys

INF = 1001001001

def resolve():
  k, x = map(int, input().split())
  if 500 * k >= x:
    print("Yes")
  else:
    print("No")

  return

if __name__ == "__main__":
    resolve()
