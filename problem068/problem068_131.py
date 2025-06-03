string = list(input())
times = int(input())
for i in range(times):
    order = input().split()
    if order[0] == "print":
        print("".join(string[int(order[1]):int(order[2]) + 1]))
    elif order[0] == "replace":
        string[int(order[1]):int(order[2]) + 1] = order[3]
    else:
        string[int(order[1]):int(order[2]) + 1] = list(reversed(string[int(order[1]):int(order[2]) + 1]))