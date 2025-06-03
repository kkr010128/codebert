def main():
  num = list(map(int,input().split()))
  if num[0]+num[1]+num[2]<22:
    print('win')
  else:
      print('bust')
main()