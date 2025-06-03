def main():
  n = int(input())
  h = tuple(map(int, input().split()))
  ans = [0]*n
  for i in range(n):
    ans[h[i]-1] = i+1
  print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()