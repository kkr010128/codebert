N, K, C = map(int, input().split())
S = input()
left = []
right = []
i, j = 0, N-1
while len(left) <= K-1:
    if S[i] == "o":
        left.append(i)
        i += C+1
    else:
        i += 1
while len(right) <= K-1:
    if S[j] == "o":
        right.append(j)
        j -= C+1
    else:
        j -= 1
right.sort()
for n in range(K):
    if left[n] == right[n]:
        print(left[n] + 1)