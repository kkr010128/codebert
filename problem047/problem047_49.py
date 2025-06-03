from sys import stdin

operate = {
    '+': lambda lhs, rhs: lhs + rhs,
    '-': lambda lhs, rhs: lhs - rhs,
    '*': lambda lhs, rhs: lhs * rhs,
    '/': lambda lhs, rhs: lhs // rhs,
}

while True:
    arr = (stdin.readline().rstrip().split())
    a, op, b = int(arr[0]), arr[1], int(arr[2])

    if op == '?':
        break

    answer = operate[op](a, b)

    print(answer)

