K = int(input())
S = input()

def answer(K: int, S: str) -> str:
    if len(S) <= K:
        return S
    else:
        return S[:K]+ '...'

print(answer(K, S))