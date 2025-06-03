#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def main():
	nums = input().split(" ")
	fst , snd ,trd = int(nums[0]),int(nums[1]),int(nums[2])
	if fst < snd < trd :
		return "Yes"
	else:
		return "No"
	
if __name__ == '__main__':
  print(main())