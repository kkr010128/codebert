import sys
readline = sys.stdin.readline
SET = set()
for _ in range(int(readline())):
    c, s = readline().split()
    if c == "insert":
        SET.add(s)
    elif c == "find":
        print("yes" if s in SET else "no")

