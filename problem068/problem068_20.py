t = input()
n = int(input())
for i in range(n):
    orders = input().split()
    order = orders[0]
    a = int(orders[1])
    b = int(orders[2])

    if order == "replace":
        word = orders[3]
        t = t[:a] + word + t[b+1:]
    if order == "print":
        print(t[a:b+1])
    if order == "reverse":
        t = t[:a] + t[a:b+1][::-1]+ t[b+1:]
