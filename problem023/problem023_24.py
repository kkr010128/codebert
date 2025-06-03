n = int(input())
d = {}
for i in range(n):
    cmd, s = input().split()
    if cmd == "insert":
        d.update([(s, 0)])
    else:
        if s in d:
            print("yes")
        else:
            print("no")