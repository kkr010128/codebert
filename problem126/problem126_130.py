def main():
  nums = list(map(int,input().split()))
  for i,n in enumerate(nums):
    if n == 0:
      return i + 1

if __name__ == '__main__':
  print(main())