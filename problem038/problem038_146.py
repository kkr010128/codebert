input_line = input()
a,b = input_line.strip().split(' ')
a = int(a)
b = int(b)

if a < b:
    print("a < b")
elif a > b:
    print("a > b")
elif a == b:
    print("a == b")