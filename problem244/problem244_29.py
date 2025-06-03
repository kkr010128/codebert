def main():
  num = list(map(int,input().split()))
  if num[0]*500>=num[1]:
    print("Yes")
  else:
    print("No")

main()