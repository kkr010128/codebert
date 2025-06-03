ans = []

while True:
    tmp = input().split()

    a, b = map(int, [tmp[0], tmp[2]])
    op = tmp[1]

    if op == "?":
        break
    if op == "+":
        ans.append(a + b)
    if op == "-":
        ans.append(a - b)
    if op == "*":
        ans.append(a * b)
    if op == "/":
        ans.append(a // b)

print("\n".join(map(str, ans)))
