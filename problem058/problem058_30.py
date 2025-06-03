from itertools import combinations

def f(s):
    n, x = list(map(int, s.split()))
    return len(tuple(filter(lambda it: sum(it) == x,
                            combinations(range(1, n+1), 3))))

while True:
    s = input()
    if s == "0 0":
        break
    print(f(s))