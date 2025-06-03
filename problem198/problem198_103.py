
N = int(input())


def func(x):
    if len(x) == N:
        print("".join(x))
        return

    last = ord(max(x)) - ord("a") + 1 if x else 0
    for i in range(min(26, last) + 1):
        x.append(chr(ord("a") + i))
        func(x)
        x.pop()


func([])
