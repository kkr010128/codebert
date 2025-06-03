# Aizu Problem ALDS_1_4_C: Dictionary
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


D = set()
N = int(input())
for _ in range(N):
    cmd, string = input().split()
    if cmd == "insert":
        D.add(string)
    elif cmd == "find":
        print("yes" if string in D else "no")