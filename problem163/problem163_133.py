import sys
def main():
  s,w = list(map(int,(input().split())))
  if s<=w:
    print('unsafe')
    sys.exit()
  else:
    print('safe')
    sys.exit()

if __name__ == '__main__':
  main()



