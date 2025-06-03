str = input()
q = int(input())

for i in range(q):
    args = input().split()
    order = args[0]
    a = int(args[1])
    b = int(args[2])
    if order == "print":
        print(str[a : b + 1])
    elif order == "reverse":
        str = str[: a] + str[a : b + 1][: : -1] + str[b + 1 :]
    elif order == "replace":
        str = str[: a] + args[3] + str[b + 1 :]

    
