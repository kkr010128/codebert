from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


class Fibonacci(object):
    memo = [1, 1]

    def get_nth(self, n):
        if n < len(Fibonacci.memo):
            return Fibonacci.memo[n]
        # print('fib({0}) not found'.format(n))
        for i in range(len(Fibonacci.memo), n+1):
            result = Fibonacci.memo[i-1] + Fibonacci.memo[i-2]
            Fibonacci.memo.append(result)
            # print('fib({0})={1} append'.format(i, result))
        return Fibonacci.memo[n]


if __name__ == '__main__':
    # ??????????????\???
    num = int(input())

    # ?????£??????????????°????¨????
    #f = Fibonacci()
    #result = f.get_nth(num)
    result = fib(num+1)

    # ???????????????
    print('{0}'.format(result))