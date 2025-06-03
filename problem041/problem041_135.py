#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def main():
	nums = input().split(" ") 
	width, height, x, y, r =[int(i) for i in nums]
	if 0 <= x - r and x + r <= width and 0 <= y - r and y + r <= height:
		return "Yes"
	else:
		return "No"
if __name__ == '__main__':
  print(main())