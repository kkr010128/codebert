s = input()
line = int(input())

for i in range(line):
    param = input().split(" ")

    if len(param) == 4: ope, a, b, p = param
    else: ope, a, b = param

    a,b = int(a), int(b)

    if ope == "print":
        print(s[a:b+1])
    elif ope == "reverse":
        rev = s[a:b+1][::-1]
        s = (s[:a] + rev + s[b+1:])
    elif ope == "replace":
        s = (s[:a] + p + s[b+1:])