import sys
line = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
for i in range(n):
    v = sys.stdin.readline().split()
    op = v[0]
    a = int(v[1])
    b = int(v[2])
    if op == "print":
        print(line[a: b + 1])
    elif op == "reverse":
        line = line[:a] + line[a: b + 1][::-1] + line[b + 1:]
    elif op == "replace":
        p = v[3]
        line = line[:a] + p + line[b + 1:]