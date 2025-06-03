# -*- coding: utf-8 -*-

def main():
  Num = input().split()
  area = int(Num[0]) * int(Num[1])
  sur = 2 * (int(Num[0])+int(Num[1]))

  print(area, sur)
 
if __name__ == '__main__':
  main()