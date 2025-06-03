in_str = input().split(" ")

a = int(in_str[0])
b = int(in_str[1])
c = int(in_str[2])

if a < b:
    if b < c:
        print("Yes")
    else:
        print("No")
else:
    print("No")