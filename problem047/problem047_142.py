def solve(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a // b
    return None

if __name__ == '__main__':
    while True:
        a, op, b = input().split()
        if op == '?': break
        print(solve(int(a), op, int(b)))