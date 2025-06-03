import sys

n = int(input())
dic = set()

for i in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "insert":
        dic.add(cmd[1])
    else:
        print("yes" if cmd[1] in dic else "no")