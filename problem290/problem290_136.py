import sys

def main():
  input = sys.stdin.readline
  n, k = map(int, input().split())
  a = [int(x) for x in input().split()]
  f = [int(x) for x in input().split()]
  a.sort(reverse=True)
  f.sort()
  
  l, r = -1, pow(10, 12)+1
  while r-l > 1:
    judge = (r+l)//2
    sub = 0
    for i in range(n):
      if a[i]*f[i] <= judge:
        continue
      sub += a[i]-judge//f[i]
    if sub <= k:
      r = judge
    else:
      l = judge
  
  print(r)
  
if __name__ == "__main__":
  main()