def resolve():
    N = int(input())
    S = [input() for _ in range(N)]
    import collections
    counter = collections.Counter(S)
    answers = []
    maxcnt = 0
    for k, v in counter.items():
        if maxcnt < v:
            maxcnt = v
            answers = [k]
        elif maxcnt == v:
            answers.append(k)
    [print(s) for s in sorted(answers)]

if '__main__' == __name__:
    resolve()