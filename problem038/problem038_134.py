data = input().split(' ')
a = int(data[0])
b = int(data[1])

if a > b:
    print("a > b")
else:
    if a < b:
        print("a < b")
    else:
        print("a == b")