import sys

n = int(sys.stdin.readline())

dict = {}

for _ in range(n):
    op, key = input().split()

    if op == "insert":
        dict[key] = "insert"
        continue

    if op == "find":
        print("yes") if key in dict.keys() else print("no")
