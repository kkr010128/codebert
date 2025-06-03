
while True:
    entry = map(str, raw_input().split())
    a  = int(entry[0])
    op = entry[1]
    b  = int(entry[2])
    if op == "?":
        break
    elif op == "+":
        ans = a + b
    elif op == "-":
        ans = a - b
    elif op == "*":
        ans = a * b
    elif op == "/":
        ans = a / b
    print(ans)