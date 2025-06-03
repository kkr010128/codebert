def main():
  num = list(map(int,input().split()))
  if num[0]>2*num[1]:
    print(num[0]-2*num[1])
  else:
      print(0)
main()