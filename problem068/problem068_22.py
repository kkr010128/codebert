s = input()
q = int(input())

for i in range(q):
    inp = input().split()
    com = inp[0]
    a = int(inp[1])
    b = int(inp[2])+1
    if com =="print":
        print(s[a:b])
    elif com =="reverse":
        s_rev = s[a:b]
        s = s[:a] + s_rev[::-1] + s[b:]
    elif com =="replace":
        s = s[:a] + inp[3] + s[b:]