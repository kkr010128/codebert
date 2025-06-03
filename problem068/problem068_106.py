# Pythonのスライスは最後が開区間だから癖がある
t = input()
for i in range(int(input())):
    cmd = list(input().split())
    cmd[1] = int(cmd[1])
    cmd[2] = int(cmd[2])
    if cmd[0] == "print":
        print(t[cmd[1] : cmd[2]] + t[cmd[2]])
    elif cmd[0] == "reverse":
        tmp = t[cmd[1] : cmd[2]] + t[cmd[2]]
        tmp = tmp[::-1]
        t = t[:cmd[1]] + tmp + t[cmd[2]+1:]
    elif cmd[0] == "replace":
        t = t[:cmd[1]] + cmd[3] + t[cmd[2]+1:]
