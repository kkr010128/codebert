string = raw_input()
n = input()

for i in range(n):
    tmp = map(str, raw_input().split())
    if tmp[0] == "print":
        print string[int(tmp[1]): int(tmp[2]) + 1]
    elif tmp[0] == "reverse":
        s = ""
        for i in range(int(tmp[1])):
            s += string[i]
        for i in range(int(tmp[2]) - int(tmp[1]) + 1):
            s += string[int(tmp[2]) - i]
        for i in range (len(string) - int(tmp[2]) - 1):
            s += string[i + int(tmp[2]) + 1]
        string = s
    elif tmp[0] == "replace":
        s = string[:int(tmp[1])] + tmp[3] + string[int(tmp[2]) + 1:]
        string = s