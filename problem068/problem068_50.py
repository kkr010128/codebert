str = [w for w in input()]
q = int(input())
for i in range(q):
    command = [w for w in input().split()]
    command[1] = int(command[1])
    command[2] = int(command[2])
    if command[0] == "print":
        for i in range(command[1], command[2]+1):
            print(str[i], end="")
        print()
    if command[0] == "replace":
        j = command[1]
        for i in range(len(command[3])):
            str[j] = command[3][i]
            j += 1
    if command[0] == "reverse":
        r = []
        for i in range(command[2], command[1]-1, -1):
            r.append(str[i])
        i = command[1]
        for w in r:
            str[i] = w
            i += 1