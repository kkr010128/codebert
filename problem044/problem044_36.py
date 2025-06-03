from itertools import repeat
print(sum((lambda a, b, c: map(lambda r, n: n % r == 0,
                               range(a, b+1), repeat(c))
           )(*map(int, input().split()))))