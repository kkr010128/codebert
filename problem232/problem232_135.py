a, b = input().split(" ")

a_str = ""
b_str = ""

for i in range(int(b)):
    a_str = a_str + a
for i in range(int(a)):
    b_str = b_str + b

if a_str < b_str:
    print(a_str)
else:
    print(b_str)