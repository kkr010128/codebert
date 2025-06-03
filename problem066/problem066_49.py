string = []
while 1:
    s = input()
    if s == "-":
        break
    try:
        n = int(s)
        for i in range(n):
            m = int(input())
            string = string[m:] + string[:m]
        output = "".join(string)
        print(output)
    except ValueError:
        string = list(s)
        continue