dic = set()
n = int(input())
for i in range(n):
    cmd, val = input().split()
    if cmd == "insert":
        dic.add(val)
    elif cmd == "find":
        print("yes" if val in dic else "no")
    else:
        print("wrong command")
