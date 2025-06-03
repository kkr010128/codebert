def f(s):
    return sum(map(int, s))

while True:
    s = input()
    if s == "0":
        break

    print(f(s))