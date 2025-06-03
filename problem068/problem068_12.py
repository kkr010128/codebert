line = input()
q = int(input())
for _ in range(q):
    cmd = input().split()
    a = int(cmd[1])
    b = int(cmd[2])
    if cmd[0] == "print":
        print(line[a:b + 1])
    elif cmd[0] == "replace":
        line = line[:a] + cmd[3] + line[b + 1:]
    else:
        line = line[:a] + line[a:b + 1][::-1] + line[b + 1:]