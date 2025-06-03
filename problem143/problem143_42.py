#168b
#値を受け取る
K = int(input())
S = str(input())

#Kになるまで文字を取り、K以降の文字列は'…'で表す
def answer(K: int, S: str) -> str:
    if len(S) <= K:
        return S
    else:
        return S[:K] + '...'


print(answer(K, S))