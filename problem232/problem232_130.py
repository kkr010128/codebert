#!/usr/bin/env python3

def solve(a,b):
  str1 = str(a)*b
  str2 = str(b)*a
  if str1 < str2:
    return str1
  else:
    return str2



def main():
  a,b = map(int,input().split())
  print(solve(a,b))
  return

if __name__ == '__main__':
  main()
