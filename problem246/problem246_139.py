import itertools

def main():
    N = int(input())
    P = tuple(map(int, input().split()))
    Q = tuple(map(int, input().split()))

    l = [i for i in range(1, N+1)]
    p = list(itertools.permutations(l, N))

    print(abs(p.index(P) - p.index(Q)))

if __name__ == '__main__':
    main()