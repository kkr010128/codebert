from itertools import tee
print(
    ' '.join(
        map(str,
            map(lambda f, ns: f(ns),
                (min, max, sum),
                (lambda m: tee(m, 3))(
                    map(int,
                        (lambda _, line: line.split())(
                            input(), input())))))))