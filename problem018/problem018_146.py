# Aizu Problem ALDS_1_3_A: Stack
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


stack = []
for x in input().split():
    if x == '+':
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)
    elif x == '-':
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)
    elif x == '*':
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)
    else:
        stack.append(int(x))

print(stack[0])