import sys
import math
import functools

def resolve(in_):
    N = int(next(in_))
    A = tuple(map(int, next(in_).split()))

    max_a = max(A)
    temp = [0] * (max_a + 1)
    temp[1] = 1

    for i in range(2, max_a + 1):
        if temp[i]:
            continue

        j = i
        while j < max_a + 1:
            if not temp[j]:
                temp[j] = i
            j += i

    B = set()
    for a in A:
        s = set()
        while a > 1:
            s.add(temp[a])
            a = a // temp[a]
        for v in s:
            if v in B:
                if functools.reduce(math.gcd, A) == 1:
                    return 'setwise coprime'
                else:
                    return 'not coprime'
            B.add(v)
    
    return 'pairwise coprime'
    

def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
