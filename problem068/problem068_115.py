s = raw_input()
n = int(raw_input())

for i in range(n):
    message = raw_input().split(" ")
    a, b = int(message[1]), int(message[2])

    if message[0] == "print":
        print(s[a:b+1])
    elif message[0] == "reverse":
        s = s[:a] + s[a:b+1][::-1] + s[b+1:]
    elif message[0] == "replace":
        s = s[:a] + message[3] + s[b+1:]