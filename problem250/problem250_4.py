from math import sqrt as r
from math import floor as f
X = int(input())
going = True

def judge(X):
    for i in range(3, f(r(X)) + 1, 2):
        if X % i == 0:
            return False
    return True

if X == 2 or X == 3:
    print(X)
    going = False
elif X % 2 == 0:
    X += 1

while going:
    if judge(X):
        print(X)
        break
    X += 2
