string = input()
q = int(input())
for _ in range(q):
    line = input().split()
    a = int(line[1])
    b = int(line[2])
    if line[0] == "print":
        print(string[a:b+1])
    elif line[0] == "reverse":
        tmp = string[a:b+1]
        tmp = tmp[::-1]
        new_s = string[:a] + tmp + string[b+1:]
        string = new_s
    else:
        new_s = string[:a] + line[3] + string[b+1:]
        string = new_s

