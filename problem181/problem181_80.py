import sys
sys.setrecursionlimit(10**9)
S = []
def add(a):
    if a > 3234566667:
        return
    x = a % 10
    if x != 0:
        S.append(a * 10 + x - 1)
        add(a * 10 + x - 1)
    S.append(a * 10 + x)
    add(a * 10 + x)
    if x != 9:
        S.append(a * 10 + x + 1)
        add(a * 10 + x + 1)
for i in range(9):
    S.append(i+1)
    add(i+1)
S.sort()
print(S[int(input())-1])
