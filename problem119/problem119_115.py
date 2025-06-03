from sys import stdin
input = stdin.readline
 
a = input().rstrip()
 
if a.isupper():
  print("A")
else:
  print("a")