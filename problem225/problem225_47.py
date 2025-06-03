def main():
  num = list(map(int,input().split()))
  if num[0]%num[1]==0:
    print(int(num[0]/num[1]))
  else:
    print(int(num[0]/num[1])+1)

main()