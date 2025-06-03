import sys
def input(): return sys.stdin.readline().rstrip()

S = input()
T = input()

size = len(S)

if S == T[:size]:
    print("Yes")
else:
    print("No")