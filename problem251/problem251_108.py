from collections import Counter
N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
result = []
for i in range(K):
    result.append(T[i])
for j in range(K, N):
    if result[j-K] == T[j]:
        result.append("d")
    else:
        result.append(T[j])

result = Counter(result)
print(result["r"]*P+result["s"]*R+result["p"]*S)
