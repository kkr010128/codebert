def main():
  num = list(map(int,input().split()))
  if num[0]<10 and num[1]<10:
    print(num[0]*num[1])
  else:
      print(-1)
main()