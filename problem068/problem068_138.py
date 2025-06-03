string = input()
num = int(input())
orders = [input().split() for _ in range(num)]

for order in orders:
    start = int(order[1])
    end = int(order[2]) + 1
    if order[0] == "reverse":
        string = string[:start] + string[start:end][::-1] + string[end:]
    elif order[0] == "replace":
        string = string[:start] + order[3] + string[end:]
    elif order[0] == "print":
        print(string[start:end])

