K = int(input())
S = str(input())


def result(K: int, S: str) -> str:
    if len(S) <= K:
        return S
    else:
        answer = S[:K]
        return answer + '...'

print(result(K, S))
