in_str = input().split(" ")

a = int(in_str[0])
b = int(in_str[1])

if a > b:
    print("a > b")
elif a < b:
    print("a < b")
else:
    print("a == b")