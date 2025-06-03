def main():
  name = list(map(str,input().split()))
  num = list(map(int,input().split()))
  n = input()
  if n==name[0]:
    print(num[0]-1,num[1])
  else:
    print(num[0],num[1]-1)

main()