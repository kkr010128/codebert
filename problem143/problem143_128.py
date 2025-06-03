S_list = [input() for i in range(2)]
K = int(S_list[0])
S = S_list[1]
n = len(S)
if n <= K:
    result = S
else:
    S = S[:K] + "..."
    result = S
print(result)