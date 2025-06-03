from sys import stdin
def ip(): return [int(i) for i in stdin.readline().split()]
def sp(): return [str(i) for i in stdin.readline().split()]

s = str(input())
c = 0
for i in s:
    c += int(i)
if (c % 9) == 0: print("Yes")
else: print("No")
