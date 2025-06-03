#!/usr/bin/env python3

from collections import Counter


def solve(N: int, A: "List[int]", Q: int, BC: "List[(int,int)]"):
    A = Counter(A)
    answers = []
    ans = ans = sum((i * n for i, n in A.items()))
    for b, c in BC:
        if b != c:
            ans += (c - b) * A[b]
            A[c] += A[b]
            del A[b]
        answers.append(ans)
    return answers


def main():
    N = int(input())  # type: int
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [tuple(map(int, input().split())) for _ in range(Q)]
    answer = solve(N, A, Q, BC)
    for ans in answer:
        print(ans)


if __name__ == "__main__":
    main()
