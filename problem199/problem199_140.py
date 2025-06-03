#!/usr/bin/env python3
# -*- coding: utf-8 -*-

c = {"hi", "hihi", "hihihi", "hihihihi", "hihihihihi"}

def main():
    s = input().strip()
    ans = s in c
    print("Yes" if ans else "No")


if __name__ == '__main__':
    main()
