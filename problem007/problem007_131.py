n = int(input())


def memoize(f):
    memo = [1, 1] + [0] * max(0, n - 1)

    def main(i):
        if memo[i]:
            return memo[i]
        result = memo[i] = f(i)
        return result

    return main


@memoize
def fibonacci(i):
    return fibonacci(i - 1) + fibonacci(i - 2)


print(fibonacci(n))