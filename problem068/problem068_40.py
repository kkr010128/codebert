S = raw_input()
n = int(raw_input())

for i in range(n):
    command = (raw_input()).split(" ")
    if command[0] == "print":
        a = int(command[1])
        b = int(command[2])
        print S[a:b+1]
    elif command[0] == "reverse":
        a = int(command[1])
        b = int(command[2])
        T = S[a:b+1]
        S = S[0:a] + T[::-1] + S[b+1:]
    else:
        a = int(command[1])
        b = int(command[2])
        S = S[0:a] + command[3] + S[b+1:]