#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def main():
  numbers = input().split(' ')
  height = int(numbers[0]) 
  width = int(numbers[1])
  print(height * width ,height * 2 + width * 2)
  return

if __name__ == '__main__':
  main()