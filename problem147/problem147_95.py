def main():
  s = input()
  t = input()
  if s == t[0:len(t) - 1]:
      print('Yes')
  else:
      print('No')

main()