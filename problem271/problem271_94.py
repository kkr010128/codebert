#!/usr/bin/env python3
n = int(input())
s = input()
print(*[chr((ord(i) + n - 65) % 26 + 65)for i in s], sep="")
