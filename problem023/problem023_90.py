n = int(input())
l = {}
for _ in range(n):
    ss = input().split()
    order, string = ss[0], ss[1]
    if order == "insert":
        l[string] = 1
    else:
        print('yes' if string in l else 'no')