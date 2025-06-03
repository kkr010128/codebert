# coding: UTF-8
from collections import deque
operators = {'+','*','-'}

def operate(L,R,C):
  if C == '+':
    return L + R
  elif C == '*':
    return L * R
  else: #<=>if C == '-'
    return L - R

raw = input().split()
stack = deque()
for C in raw:
  if C in operators:
    R = stack.pop()
    L = stack.pop()
    stack.append(operate(L,R,C))
  else:
    stack.append(int(C))
print(stack.pop())

