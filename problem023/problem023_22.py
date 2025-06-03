n = int(input())
d = {}

for i in range(n):
    line = input().split()
    if line[0] == "insert":
        d[line[1]] = 1
    elif line[0] == "find":
        if line[1] in d:
            print("yes")
        else:
            print("no")