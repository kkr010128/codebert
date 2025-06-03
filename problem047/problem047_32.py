#!/usr/bin/python

n = []

while True:
  (a, b, c) = (i for i in input().split())
  if b == '?':
    break
  else:
    n.append((int(a),b,int(c)))

for i in range(len(n)):
  if n[i][1] == '+':
    print(n[i][0] + n[i][2])
  elif n[i][1] == '-':
    print(n[i][0] - n[i][2])
  elif n[i][1] == '*':
    print(n[i][0] * n[i][2])
  elif n[i][1] == '/':
    print(int(n[i][0] / n[i][2]))